
# Speech-Translation-with-Python

This is simple speech translation web application mainly built with python along with streamlit for frontend UI designs. Its my first complete web application program with graphical user interface.


## How it works
This web application is a real-time speech translation tool using Streamlit. Here's how it works:

**Initialization**:
   - Imports necessary libraries.
   - Initializes `pygame` for playing audio.
   - Sets up language mappings with `googletrans`.

**Functions**:
   - Converts language names to codes.
   - Translates text between languages.
   - Converts text to speech and plays it.
   - Handles continuous speech recognition, translation, and audio playback.

**UI and Styling**:
   - Custom CSS styles for better appearance.
   - Dropdowns for selecting source and target languages.
   - "Start" and "Stop" buttons to control translation.
   - Placeholder for status messages.

**Event Handling**:
   - On clicking "Start", the app listens to speech, translates it, and plays the translated speech.
   - Displays status updates like "Listening", "Processing", and "Translating".
   - On clicking "Stop", the translation process halts.

In summary, the user selects languages, starts the translation, speaks, and hears the translated speech in real-time.
## Screenshots

Here are some screenshots of this web application is provided for better understandings:


![App Screenshot](https://github.com/Monstub/Speech-Translation-with-Python/blob/main/Project-Imgs/Screenshot%202024-07-06%20160049.png)
![App Screenshot](https://github.com/Monstub/Speech-Translation-with-Python/blob/main/Project-Imgs/Screenshot%202024-07-06%20160123.png)
![App Screenshot](https://github.com/Monstub/Speech-Translation-with-Python/blob/main/Project-Imgs/Screenshot%202024-07-06%20160136.png)


## Run Locally

To deploy this project, first clone this repository in your computer and perform follow the following steps:

1. Create a python virtual environment (Python virtual environments allow you to install Python packages)
```bash
  python -m venv <directory>
```
For example:
```
  python -m venv venv
```

2. Now activate the virtual environment and install the required packages from `requirements.txt` as given below:
```
# For cmd.exe
venv\Scripts\activate.bat

# For PowerShell
venv\Scripts\Activate.ps1

# To install required packages
pip install -r requirements.txt
```
3. Now you are all set, change the current dirtectory to `App` folder and run the program with following command:
```
# To change directory
cd App

# Run the program
streamlit run main.python
```


## Feedback

Thats all for this project, If you have any feedback or queries, please reach out to me anytime at monstub7@gmail.com

