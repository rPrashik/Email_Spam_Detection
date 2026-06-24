# Email Spam Detection System

## Overview

An end-to-end Email Spam Detection System built using Machine Learning and NLP techniques. The project processes raw email data, performs text preprocessing and TF-IDF feature extraction, trains classification models, and exposes a FastAPI-based API for real-time spam prediction.

## Datasets

### Enron Email Dataset

https://www.kaggle.com/datasets/wcukierski/enron-email-dataset

### Apache SpamAssassin Public Corpus

https://spamassassin.apache.org/old/publiccorpus/

## Tech Stack

* Python
* Pandas
* Scikit-Learn
* TF-IDF Vectorizer
* Logistic Regression
* Multinomial Naive Bayes
* FastAPI
* Joblib

## Workflow

1. Email Parsing and Extraction
2. Text Cleaning and Preprocessing
3. TF-IDF Feature Engineering
4. Model Training and Evaluation
5. Model Serialization
6. FastAPI Deployment
7. Real-Time Spam Prediction

## Results

| Model                   | Accuracy |
| ----------------------- | -------- |
| Logistic Regression     | 98%      |
| Multinomial Naive Bayes | 100%     |

## API Usage

### Start Server

```bash
uvicorn app:app
```

### Swagger Documentation

```text
http://127.0.0.1:8000/docs
```

### Sample Request

```json
{
  "email": "Congratulations! You have won a free iPhone. Click now!"
}
```

### Sample Response

```json
{
  "prediction": "Spam"
}
```

## Features

* Email Parsing
* Text Preprocessing
* TF-IDF Vectorization
* Spam Classification
* REST API Deployment
* Real-Time Prediction
