import cv2
import mediapipe as mp
import numpy as np
import serial
import time

# ---------------- CONFIGURATION ----------------
EAR_THRESHOLD = 0.20
DROWSY_TIME = 1.5
SERIAL_PORT = "COM3"  # Change this to your Arduino's port in Device Manager
BAUD_RATE = 9600

# MediaPipe Face Mesh eye landmark indices
LEFT_EYE = [33, 160, 158, 133, 153, 144]
RIGHT_EYE = [362, 385, 387, 263, 373, 380]


def calculate_ear(landmarks, eye_indices, width, height):
    """Calculate the Eye Aspect Ratio (EAR) for six eye landmarks."""
    points = []
    for index in eye_indices:
        landmark = landmarks[index]
        points.append((int(landmark.x * width), int(landmark.y * height)))

    points = np.array(points)
    vertical_1 = np.linalg.norm(points[1] - points[5])
    vertical_2 = np.linalg.norm(points[2] - points[4])
    horizontal = np.linalg.norm(points[0] - points[3])

    if horizontal == 0:
        return 0.0, points

    ear = (vertical_1 + vertical_2) / (2.0 * horizontal)
    return ear, points


def main():
    arduino = None
    camera = None
    last_command = None
    closed_start = None

    try:
        try:
            arduino = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)
            time.sleep(2)  # Allow Arduino to reset after serial connection
            print(f"Arduino connected on {SERIAL_PORT}")
        except serial.SerialException as error:
            print(f"Arduino unavailable: {error}")
            print("Continuing in webcam-only mode.")

        camera = cv2.VideoCapture(0)
        if not camera.isOpened():
            raise RuntimeError("Could not open webcam. Check camera permissions or index.")

        mp_face_mesh = mp.solutions.face_mesh

        with mp_face_mesh.FaceMesh(
            max_num_faces=1,
            refine_landmarks=True,
            min_detection_confidence=0.5,
            min_tracking_confidence=0.5,
        ) as face_mesh:
            while camera.isOpened():
                success, frame = camera.read()
                if not success:
                    print("Unable to read a frame from the webcam.")
                    break

                height, width = frame.shape[:2]
                rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                results = face_mesh.process(rgb_frame)
                is_drowsy = False
                elapsed = 0.0

                if results.multi_face_landmarks:
                    landmarks = results.multi_face_landmarks[0].landmark
                    left_ear, left_points = calculate_ear(
                        landmarks, LEFT_EYE, width, height
                    )
                    right_ear, right_points = calculate_ear(
                        landmarks, RIGHT_EYE, width, height
                    )
                    ear = (left_ear + right_ear) / 2.0

                    for point in np.vstack((left_points, right_points)):
                        cv2.circle(frame, tuple(point), 2, (255, 255, 0), -1)

                    if ear < EAR_THRESHOLD:
                        if closed_start is None:
                            closed_start = time.time()
                        elapsed = time.time() - closed_start
                        is_drowsy = elapsed >= DROWSY_TIME
                    else:
                        closed_start = None

                    status = "DROWSY!" if is_drowsy else "ALERT"
                    color = (0, 0, 255) if is_drowsy else (0, 255, 0)
                    cv2.putText(
                        frame, f"EAR: {ear:.2f}", (20, 35),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, color, 2
                    )
                    cv2.putText(
                        frame, status, (20, 75),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2
                    )
                    if closed_start is not None:
                        cv2.putText(
                            frame, f"Closed: {elapsed:.1f}s", (20, 110),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.65, color, 2
                        )
                else:
                    # Reset the timer if no face is detected.
                    closed_start = None
                    cv2.putText(
                        frame, "Face not detected", (20, 35),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 165, 255), 2
                    )

                if is_drowsy != last_command:
                    if arduino is not None and arduino.is_open:
                        try:
                            arduino.write(b"1" if is_drowsy else b"0")
                        except serial.SerialException as error:
                            print(f"Serial communication error: {error}")
                    last_command = is_drowsy

                cv2.imshow("DriveSafe-AI | Drowsiness Detection", frame)
                if cv2.waitKey(1) & 0xFF == ord("q"):
                    break

    except (RuntimeError, cv2.error) as error:
        print(f"Application error: {error}")
    finally:
        if arduino is not None and arduino.is_open:
            try:
                arduino.write(b"0")
            except serial.SerialException:
                pass
            arduino.close()
        if camera is not None:
            camera.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
