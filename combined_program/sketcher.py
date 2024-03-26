# python3 -m pip install opencv-python opencv-python-headless
import cv2
import numpy
import time
import traceback
import os

def webcam():
    stname = 'K.D. Sorokin Image-to-Sketch'
    video_capture = cv2.VideoCapture(0)
    
    while True:
        ret, frame = video_capture.read()
        if not ret:
            print("Failed to grab frame")
            break

        cv2.putText(frame, "Image-to-Sketch by: {}".format(stname), (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        cv2.imshow("Webcam", frame)
        
        # Capture image on 'c' key press
        if cv2.waitKey(1) == ord('c'):
            Sketcher(frame=frame)
        
        # Exit on 'q' key press
        elif cv2.waitKey(1) == ord('q'):
            break

    video_capture.release()
    cv2.destroyAllWindows()

def Sketcher(img=None, frame=None):
    sketch = None
    try:
        if img is not None:
            image = cv2.imread(img)
            grey_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        elif frame is not None:
            grey_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        else:
            print('No image data to process.')
            return

        # Image processing to create a sketch effect
        invert = cv2.bitwise_not(grey_img)
        blur = cv2.GaussianBlur(invert, (21, 21), 0)
        invertedblur = cv2.bitwise_not(blur)
        sketch = cv2.divide(grey_img, invertedblur, scale=256.0)

        # Show the sketch
        cv2.imshow("Sketch", sketch)

        # Wait for 's' to save the sketch
        while True:
            k = cv2.waitKey(1)
            if k == ord('s'):
                # Save the sketch
                sketches_dir = 'Sketches'
                if not os.path.isdir(sketches_dir):
                    os.makedirs(sketches_dir)
                filename = 'sketch-{}.png'.format(time.strftime('%Y%m%d-%H%M%S'))
                cv2.imwrite(os.path.join(sketches_dir, filename), sketch)
                print('Saved as: {}'.format(filename))
                break
            elif k == ord('q'):
                break

    except Exception as ex:
        print('Error in Sketching...', traceback.format_exc(), ex)
    finally:
        if sketch is not None:
            cv2.destroyAllWindows()

if __name__ == "__main__":
    webcam()
