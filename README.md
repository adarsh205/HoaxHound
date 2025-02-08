# HoaxHound
A fake news detection web application using a machine learning model.

Welcome to the Fake News Detector GitHub project! This project is a simple web-based application that allows you to 
detect fake news articles using Natural Language Processing (NLP) techniques. It uses a machine 
learning model to classify news articles as either "Real" or "Fake" based on their content.

## How It Works
1. **Submit an article**: Enter an article you want to check.
2. **Get Answers**: The system processes the article using NLP to check its authenticity.


## Installation

### Prerequisites
- Python 3.x
- Flask

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/adarsh205/HoaxHound.git
   ```
   
2. Navigate to the project directory:
   ```bash 
   cd project-name
   ```
   
3. Install the dependencies from `requirements.txt`:
   ```bash 
   pip install -r requirements.txt
   ```
   
4. Run the Flask server:
   ```bash 
   flask run
   ```
   
The server will start on `http://127.0.0.1:5000/` by default.

### Requirements
Make sure the `requirements.txt` file includes:
```plaintext
joblib
scikit-learn
Bootstrap_Flask==2.2.0
Flask_WTF==1.2.1
WTForms==3.0.1
Flask==2.3.2
```


## Limitations

This fake news detector app is using a machine learning model that is trained using an old dataset.

Language, slang, and contextual meanings change over time. A model trained on older data may not fully 
understand the nuances of contemporary language or cultural references, leading to false positives or negatives.

Fake news detection benefits from real-time data and continuous updates to adapt to evolving tactics. A static dataset
from five years ago cannot incorporate ongoing developments and new trends in misinformation.


   
## Contact

For questions or feedback, please contact us at `adarshg205205@gmail.com`.





