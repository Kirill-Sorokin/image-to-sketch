# *image-to-sketch*
Using a combination of 'OpenCV', 'NumPy', and 'PyQt5', to build a program that creates a sketch based on real images/photos.

# Launching the Application
To start the application, double-click on the main.py file or run it from your terminal or command prompt:
sh: python main.py

# Converting Images to Sketches
Selecting an Image:

Drag-and-Drop: Simply drag an image file from your computer and drop it onto the designated area within the application window.
File Selection: Alternatively, double-click inside the application window to open a file dialog. Navigate to the image you wish to convert, select it, and click 'Open'.
Converting the Image:

Once an image is loaded, click the "Convert to Sketch" button. The application will process the image and display the resulting sketch in a new window.
Viewing the Sketch:

The sketch will appear in a separate window. You can view and compare it with the original image.

# Using the Webcam Feature
If you wish to capture an image using your computer’s webcam to convert it into a sketch:

Click the "Open Camera" button on the main application window.
A live video feed will appear. Position yourself or an object in front of the camera as desired.
To capture the image, press the 'c' key on your keyboard. The application will then convert this image into a sketch and display it as described above.
If you wish to close the webcam feed without capturing an image, press the 'q' key.

# Saving Your Sketch
After your image has been converted into a sketch and displayed:

To save the sketch, press the 's' key while the sketch window is active. The application will save the sketch to a predetermined folder on your computer.
You will receive a confirmation in the application window with the saved file path.

# Additional Tips
Ensure that the application window is active (selected) when pressing the 'c', 'q', or 's' keys for their respective actions.
The application accepts most common image formats, including .jpg, .png, and .bmp.

# Troubleshooting
If the webcam does not activate or the application does not respond to the 'Open Camera' button, ensure no other program is using the webcam and check your system’s privacy settings to allow camera access.

If the drag-and-drop feature does not work, try running the application with administrative privileges or checking your system’s settings to allow drag-and-drop operations for the application.
