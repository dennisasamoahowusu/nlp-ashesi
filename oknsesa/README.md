# capstone-final

This Capstone Final Project is a Natural Language Processing (NLP) System called OkNsesa, that uses voice features and commands to allow users to accumulate change amounts electronically. Users are recognized and verified to access their account based on their voice features. Accordingly, they can now use voice commands such as “Update my account with GHC 2”, to update their respective change accounts and use the accumulated money for other purchases.

## Installation

Clone the Repository and install all depencies in python 3 or above.

### Predependicies 

Python 3 and above: https://www.python.org/downloads/

PyAudio: https://pypi.org/project/PyAudio/

Python Speech Recognition: https://pypi.org/project/SpeechRecognition/

### Install OkNsesa

Clone the Project from this repository

## Run the Application

The application is run currently with shell commands in either a terminal. The file to be run is the main.py file in from the cloned repository and application takes charge from there. The main.py file is in the Speaker Recognition/Cognitive-SpeakerRecognition-Python/ Directory.

### Commands to use

1.  Please add to my account please
2.  Please remove from my account please
3. Verification phrase: my voice is my passport verify me

### Run with Existing User

After running the main.py file, there are a couple of steps to follow.

1. The user is asked to say a command, One can mention any of the commands stated above (User has about 8 seconds)
2. The system would identify the user based on features
3. The System would ask the user to verify by saying the phrase above (User has about 5 seconds)
4. System verifies user and updates his database account with said amount

### Launch Web Interface

This can be displayed by running the index.py file in the interface folder. To display the change update on a web interface

### Run with New User

This involves pre-enrolling all users and processing the audio to perform the desired task. The pre-enrollment is done at the backend level manually.
It involves the 

1.  Identification Enrollment
2.  Verification Enrollment
3.  Database Insertion
4.  Add Users to dictionairies in main.py file

The process requires uses of subscription keys from microsoft which cannot be published online thus, to perform this process the creator of this project has to be contacted




