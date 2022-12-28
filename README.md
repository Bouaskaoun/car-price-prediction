# Car Price Prediction

This project uses Linear Regression to predict the price of a car based on its features. The model is served using FastAPI and a web application is built using Streamlit to allow users to easily interact with the model and make predictions.

## Requirements

To run this project, you will need to have the following dependencies installed:

- Python 3.7 or higher
- FastAPI
- Streamlit
- Scikit-learn
- Numpy

You can install these dependencies using `pip`. For example:

```bash
pip install fastapi streamlit scikit-learn numpy
```

## Usage

To start the API and the frontend, run the following commands:

```bash
# Start the API
uvicorn main:app --reload

# Start the frontend
streamlit run app.py
```

The frontend will be available at **http://localhost:8501** and the API will be available at **http://localhost:8000**.

## Data

The data used to train the model is a dataset of used car prices from [Kaggle](https://www.kaggle.com/). The data has been cleaned and preprocessed for use in training the model.

## Model

The model was trained using Linear Regression from the scikit-learn library. The training process involved splitting the data into training and validation sets, fitting the model on the training data, and evaluating the model on the validation data. 

## API

The API allows you to classify images of Arabic handwritten characters by sending a POST request to the `/predict` endpoint. The request should include a JSON payload in the request body, containing the data for which the prediction should be made. The data is expected to have the following fields:

- name: the name of the car
- year: the year the car was manufactured
- kms_driven: the number of kilometers the car has been driven
- fuel_type: the type of fuel the car uses
- Company: the manufacturer of the car

The endpoint first converts the data into a pandas DataFrame, with the columns specified in the pd.DataFrame constructor. The data is then passed to the predict method of the model object.

The API will return a JSON object with the following fields:

- `prediction`: The predicted price of the car (float)

## Frontend

The frontend is a simple web app built using Streamlit, that allows users to input the features of a car and make a prediction of its price. The frontend displays the
prediction returned by the API.

