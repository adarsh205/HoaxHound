# HoaxHound
A fake news detection web application using a machine learning model.

Welcome to the Fake News Detector GitHub project! This project is a simple web-based application that allows you to 
detect fake news articles using Natural Language Processing (NLP) techniques. It uses a pre-trained machine 
learning model to classify news articles as either "Real" or "Fake" based on their content.


# Installation

To run the Fake News Detector locally, follow these steps:

Clone this GitHub repository to your local machine

Create a virtual environment (optional but recommended):

Install the required dependencies:


# Usage

To run the Fake News Detector using Streamlit, follow these steps:

Make sure you have activated your virtual environment if you created one (see step 2 in the installation section).

In your terminal, navigate to the project directory (if you're not already there):

Run the Streamlit app:

Once the app is running, a new tab or browser window will open automatically, displaying the Fake News Detector interface.

You can input news articles by pasting the article text.

Click the "Predict" button, and the app will classify the article as "Real" or "Fake."


# Working 

A machine learning model named as hoaxhoundmodel is trained, tested and then downloaded (to be used in app.py) in google colab notebook.
The code for the google colab notebook can be seen in the file HoaxHound.ipynb in our repository.

The application's interface is coded in the app.py file.

In app.py, the model (hoaxhoundmodel) is loaded. The input is processed and output is predicted 
using this model. 

Procfile is a configuration file used in the web application deployment environment, (it is used particularly with platforms like Heroku). 
It specifies the commands that should be executed by the hosting environment to run the application. The name "Procfile" is short for 
"process file."

In the setup.sh file the script creates a Streamlit configuration file with these settings in the user's home directory,
ensuring that Streamlit runs in headless mode, listens on the specified port, and has CORS disabled.


# Limitations

This fake news detector app is using a machine learning model that is trained using a 5 year old dataset.

Language, slang, and contextual meanings change over time. A model trained on older data may not fully 
understand the nuances of contemporary language or cultural references, leading to false positives or negatives.

Fake news detection benefits from real-time data and continuous updates to adapt to evolving tactics. A static dataset
from five years ago cannot incorporate ongoing developments and new trends in misinformation.






