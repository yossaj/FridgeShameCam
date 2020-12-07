
import cv2
import time


def run_webcam_capture(image_count):
    print("Package imported")
    cap = cv2.VideoCapture(0)
    cap.set(3, 640)
    cap.set(4, 480)
    #
    image_file_count = image_count
    image_name = f"test{str(image_count)}.jpg"
    image_path = '/home/pi/Desktop/'
    start = time.time()

    while cap.isOpened():
        start_time = time.time()
        ret, frame = cap.read()
        if ret == True:
            cv2.imshow("frame", frame)
            if time.time() - start > 5:
                start = time.time()
                image_file_count += 1
                print(image_file_count)
                cv2.imwrite(  image_path + image_name , frame, [cv2.IMWRITE_JPEG_QUALITY, 50])
                print(f"Saved to {image_path}{image_name}")
                cap.release()
                cv2.destroyAllWindows()
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break
        else:
            break
    cap.release()
    cv2.destroyAllWindows()


#
# while True:
#     success, img = cap.read()
#     cv2.imshow("Image", img)
#     if cv2.waitKey(1) & 0xFF == ord('s'):
#         cv2.imwrite('/Users/kenneth.stewart/Desktop/test1.jpg', img, [cv2.IMWRITE_JPEG_QUALITY, 50])
#         print("Saved to desktop")
#         break

# t_end = time.time() + 100
# while True:
#     success, img = cap.read()
#     cv2.imshow("Video", img)
#     if time.time() < t_end:
#         print("Picture Taken")
#         cv2.imwrite('/Users/kenneth.stewart/Desktop/test1.jpg', img, [cv2.IMWRITE_JPEG_QUALITY, 50])
#         print("Saved to desktop")
#     break



# image = cv2.imread('/Users/kenneth.stewart/Desktop/test1.jpg')
# image = "/Users/kenneth.stewart/Desktop/test1.jpg"

