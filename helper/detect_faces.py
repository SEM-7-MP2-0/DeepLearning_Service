from mtcnn import MTCNN
import cv2


def detect_faces(original_images, img):
    detector = MTCNN()
    detections = detector.detect_faces(img)
    img_with_dets = original_images.copy()
    min_conf = 0.9
    person_count = 0
    for det in detections:
        if det["confidence"] >= min_conf:
            person_count += 1
            x, y, width, height = det["box"]
            keypoints = det["keypoints"]
            cv2.rectangle(
                img_with_dets, (x, y), (x + width, y + height), (0, 155, 255), 2
            )
            cv2.circle(img_with_dets, (keypoints["left_eye"]), 2, (0, 155, 255), 2)
            cv2.circle(img_with_dets, (keypoints["right_eye"]), 2, (0, 155, 255), 2)
            cv2.circle(img_with_dets, (keypoints["nose"]), 2, (0, 155, 255), 2)
            cv2.circle(img_with_dets, (keypoints["mouth_left"]), 2, (0, 155, 255), 2)
            cv2.circle(img_with_dets, (keypoints["mouth_right"]), 2, (0, 155, 255), 2)

    return img_with_dets, person_count
