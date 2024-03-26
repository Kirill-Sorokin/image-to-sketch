# Sticking to the PEP 8—Python's style guide.
import cv2
import numpy
import time
import traceback

def webcam():
    stname = 'K.D. Sorokin Image-to-Sketch'
    video_capture = cv2.VideoCapture(0)
    while True:
        ret, frame = video_capture.read(0)
        cv2.putText(frame, "Image-to-Sketch by: {}".format(stname), (430, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.3, (0, 0, 255), 1)
        cv2.imshow("Webcam", frame)
        if cv2.waitKey(1) == ord('q'):
            break
        elif cv2.waitKey(1) == ord('c'):
            print('Sketching')
            print(type(frame))
            Sketcher(frame=frame)
    video_capture.release()
    # cv2.destroyAllWindows()

def Sketcher(img=None, frame=None):
    try:
        if img:
            print('Sketching from img')
            image = cv2.imread(img)
            # Correcting the typo in the color conversion
            grey_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            invert = cv2.bitwise_not(grey_img)
            blur = cv2.GaussianBlur(invert, (61, 61), 0)
            invertedblur = cv2.bitwise_not(blur)
            sketch = cv2.divide(grey_img, invertedblur, scale=256.0)
            cv2.imshow("Sketch", sketch)
            while True:
                if cv2.waitKey(1) == ord('q'):
                    cv2.destroyAllWindows()
                    break
                elif cv2.waitKey(1) == ord('s'):
                    img_path = './Sketches/'+'sketch-'+time.strftime('%d-%m-%y-%H-%M-%S')+'.png'
                    cv2.imwrite(img_path, sketch)
                    print('Image Saved as: ', img_path)
                    cv2.destroyAllWindows()
                    break
        elif type(frame) == numpy.ndarray:
            print('Sketching from Webcam')
            grey_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # Correctly applying color conversion
            invert = cv2.bitwise_not(grey_img)
            blur = cv2.GaussianBlur(invert, (61, 61), 0)
            invertedblur = cv2.bitwise_not(blur)
            sketch = cv2.divide(grey_img, invertedblur, scale=256.0)
            cv2.imshow("Sketch", sketch)
            while True:
                if cv2.waitKey(1) == ord('q'):
                    cv2.destroyAllWindows()
                    break
                elif cv2.waitKey(1) == ord('s'):
                    img_path = './Sketches/'+'sketch-'+time.strftime('%d-%m-%y-%H-%M-%S')+'.png'
                    cv2.imwrite(img_path, sketch)
                    print('Image Saved as: ', img_path)
                    cv2.destroyAllWindows()
                    break
        else:
            print('Wrong / Invalid Image Selected')
    except Exception as ex:
        print('Error in Sketching...', traceback.format_exc(), ex)

if __name__ == "__main__":
    print()
    webcam()
