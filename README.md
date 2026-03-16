# Scam Detector Web App

A simple machine learning web application that detects whether a message is **Spam** or **Not Spam**.

## Features

* Spam detection using a trained **Naive Bayes** model
* Confidence score for predictions
* Web interface built with Django
* Text vectorization using CountVectorizer

## Tech Stack

* Python
* Django
* Scikit-learn
* Pandas

## Machine Learning Model

The spam classifier uses **Multinomial Naive Bayes** from scikit-learn.
Messages are converted into numerical features using **CountVectorizer** before classification.

Pipeline:

Message → Vectorization → Naive Bayes Model → Spam / Not Spam

## Project Structure

```
scam-detector/
│
├── app/
├── templates/
├── bayes_model.pkl
├── manage.py
├── requirements.txt
├── README.md
└── .gitignore
```

## How to Run

1. Clone the repository

git clone https://github.com/Shreyas-180/scam-detector.git

2. Install dependencies

pip install -r requirements.txt

3. Run the server

python manage.py runserver

4. Open in browser

http://127.0.0.1:8000/

## Example

Input:
"Congratulations! You won a free gift card."

Output:
Spam (Confidence: 92%)

## Future Improvements

* Improve phishing detection with more training data
* Better UI styling
* Deploy the application online
