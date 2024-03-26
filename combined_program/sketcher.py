# python3 -m pip install opencv-python opencv-python-headless
import cv2, numpy, time, traceback

def webcam():
    stname = 'K.D. Sorokin Image-to-Sketch'
    video_capture = cv2.VideoCapture(0)
    while True:
        ret, frame = video_capture.read(0)
        cv2.putText(frame, "Image-to-Sketch by: {}".format(stname), (430, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.3, (0,0,255), 1)
        cv2.imshow("Webcam", frame)
        if cv2.waitKey(1)==ord('q'):
            break
        elif cv2.waitKey(1)==ord('c'):
            print('Sketching')
            print(type(frame))
            Sketcher(frame=frame)
    video_capture.release()
    # cv2.destroyAllWindows()

def Sketcher(img = None, frame = None):
    try:
        if img:
            print('Sketching from img')
            image = cv2.imread(img)
            grey_img = cv2.cvtColor(image, cv2.COLOR_BAYER_BG2GRAY)
            invert = cv2.bitwise_not(grey_img)
            blur = cv2.GaussianBlur(invert, (61, 61), 0)
            invertedblur = cv2.bitwise_not(blur)
            sketch = cv2.divide(grey_img, invertedblur, scale = 256.0)
            cv2.imshow("Sketch", sketch)
            while True:
                # Press 'q' to 'Quit'.
                if cv2.waitKey(1) == ord('q'):
                    cv2.destroyAllWindows()
                    break
                # Press 's' to 'Save'.
                elif cv2.waitKey(1) == ord('s'):
                    img = './Sketches/'+'sketch-'+time.strftime('%d-%m-%y-%H-%M-%S')+'.png'
                    cv2.imwrite(img, sketch)
                    print('Image Saved as: ', img)
                    cv2.destroyAllWindows()
                    break
        elif type(frame) == numpy.ndarray:
            print('Sketching from Webcam')
            image = frame
            grey_img = cv2.bitwise_not(grey_img)
            invert = cv2.bitwise_not(grey_img)
            blur = cv2.GaussianBlur(invert, (61, 61), 0)
            invertedblur = cv2.bitwise_not(blur)
            sketch = cv2.divide(grey_img, invertedblur, scale = 256.0)
            cv2.imshow("Sketch", sketch)
            while True:
                if cv2.waitKey(1) == ord('q'):
                    cv2.destroyAllWindows()
                    break
                elif cv2.waitKey(1) == ord('s'):
                    img = './Sketches/'+'sketch-'+time.strftime('%d-%m-%y-%H-%M-%S')+'.png'
                    cv2.imwrite(img,sketch)
                    print('Image Saved as: ',img)
                    cv2.destroyAllWindows()
                    break
        else:
            print('Wrong / Invalid Image Selected')
    except Exception as ex:
        print('Error in Sketching...', traceback.format_exc(), ex)

if __name__ == "__main__":
    print()
    webcam()

