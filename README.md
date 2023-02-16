# Voice-Biometrics
This project was made with a vision to improve biometric security in our laptops
Although it isn't implemented that way, the project was for research and development purpose of the machine learning modelling used for recognizing the speaker

To run the project:

1.  first make sure that you create your own dataset( dataset details are given below).
2.  main.py is the first file that gets executed.
3.  main.py uses speaker_identifier() function from model.py script.
4.  speaker_identifier() function takes user's voice input, extracts the voice features and runs the model(read more about the models in model.py file itself) to predict the user and returns the output as 0(unauthorized) or 1(authorized person). 


read the comments in the python scripts to know more about the functions and execution of script.
