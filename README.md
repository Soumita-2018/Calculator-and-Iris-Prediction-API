


# Projects Overview

This repository contains two projects implemented using FastAPI and Streamlit. The first project is a simple calculator API, while the second project involves predicting the species of iris flowers using a machine learning model.

## Project 1: Calculator API

This project creates a calculator module as a backend service using FastAPI and exposes REST API endpoints. A simple Streamlit application is integrated to interact with the calculator API.

### Features
- Perform basic arithmetic operations: addition, subtraction, multiplication, and division.
- User-friendly interface built with Streamlit.
- REST API documentation available via Swagger UI.

### Implementation

1. **Calculator Module**: The `Calculator.py` file contains the FastAPI app, which has a single endpoint for calculations.
2. **Streamlit App**: A basic Streamlit app allows users to select operations and input numbers using sliders.

### Setup

To run the Calculator API:
```bash
uvicorn Calculator:app --reload --host 0.0.0.0 --port 8000
```

To run the Streamlit app:
```bash
streamlit run app.py
```

### Screenshots

--![Screenshot 2024-11-03 215551](https://github.com/user-attachments/assets/2e261723-a690-4e5f-9446-07bf687ef035)


![Screenshot 2024-11-03 215635](https://github.com/user-attachments/assets/1e54429b-3d42-44c7-91da-06fbd18b7fc5)


-

## Project 2: Iris Species Prediction

This project uses a machine learning model to predict the species of iris flowers based on input features. FastAPI serves as the backend to handle requests and return predictions.

### Features
- Load and preprocess the iris dataset.
- Train a Random Forest model and save it using Joblib.
- REST API endpoint for predicting iris species based on input features.
- Simple Streamlit application for user input.

### Implementation

1. **Model Training**: A script trains a Random Forest model on the Iris dataset and saves it as `soumita.joblib`.
2. **FastAPI App**: The FastAPI app contains endpoints to welcome users and make predictions.
3. **Streamlit App**: Users can input feature values, which are sent to the FastAPI endpoint for predictions.

### Setup

To run the Iris Prediction API:
```bash
uvicorn iris_model:app --reload --host 0.0.0.0 --port 8001
```

To run the Streamlit app:
```bash
streamlit run iris_app.py
```

### Screenshots


---![Screenshot 2024-11-03 214937](https://github.com/user-attachments/assets/839bbd43-1ed5-455a-93c6-5fbfa1477aa8)
![Screenshot 2024-11-03 215006](https://github.com/user-attachments/assets/d65ae53f-b879-4085-998b-72adfcb1307c)



## Requirements

- Python 3.8 or higher
- FastAPI
- Uvicorn
- Streamlit
- Scikit-learn
- Joblib

### Installation

You can install the required libraries using pip:

```bash
pip install fastapi uvicorn streamlit scikit-learn joblib
```

## License

This project is licensed under the MIT License. See the LICENSE file for more information.

## Author

Soumita Sahu


