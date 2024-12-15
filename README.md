# faceRecognition
Face Recognition-Based Door Lock System

For more information you can visit our website -->  https://mefaceguard.com/  or check out our youtube video -->  [...]

This project aims to create a secure door lock system based on face recognition using Raspberry Pi and OpenCV. The system will unlock the door when an authorized user’s face is recognized by controlling a servo motor. The system allows the creation of a face database for recognition and ensures security by identifying known faces.

Requirements;

*Raspberry Pi (or similar device)

*Servo motor (to control the door lock)

*Webcam (for capturing the user's face)

*Python 3.x

*OpenCV (for face recognition)

*GPIOZero (for controlling the servo motor via GPIO pins)

*NumPy (for handling image data)

*Pickle (for saving trained models and labels)

Getting Started

->1. Creating the Face Database
  
The first step is to capture and store facial images for each user. These images will be used for training the      recognition model.
  
  Run capture_faces.py to capture the user’s facial images. This script will ask for the user’s name,           
  create a folder in the dataset directory, and capture 30 images of the user’s face from various angles.
    
  Run the script with the following command:
    
     capture_faces.py
  
  Once the user looks at the camera, the script will begin capturing and saving the images in the respective folder.

->2. Training the Model
  
After capturing the faces, the next step is to train a face recognition model using the captured dataset. This is   done by running the train_model.py script.
  
  The train_model.py script trains the face recognition model using OpenCV's LBPH (Local Binary Patterns    Histogram) face recognizer.
    
  Once trained, the model is saved as trainer.yml, and the labels (user names) are saved in labels.pkl.
    
  Run the script with:
    
     train_model.py
  
->3. Face Recognition and Unlocking the Door

  Now, you can start the face recognition process. The main.py script will capture frames from the webcam,         
  recognize faces, and unlock the door if a recognized person is detected.
  
  If the system detects a known face, it will unlock the door by controlling the servo motor.
    
   For unrecognized faces, no action is taken.
  
   Run the script with:
  
     main.py

->4. Requirements

  Make sure you have installed the necessary Python libraries for this project:
  
  OpenCV (for face detection and recognition)
  
  NumPy (for array handling)
  
  GPIOZero (for controlling the servo motor)
  
  Pickle (for saving and loading the trained model)
  
  To install these libraries, run:
  
    pip install opencv-python opencv-python-headless numpy gpiozero

->5. Exiting the System
  
  Once the system is up and running, it will recognize faces and control the door lock accordingly. You can stop      the system at any time by pressing 'q'. If an error occurs, an error message will be displayed in the terminal.   
  
  
