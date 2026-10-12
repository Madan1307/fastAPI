
from fastapi import FastAPI
from pydantic import BaseModel, Field
import numpy as np
import pickle
import pandas as pd
app = FastAPI(title="Iris Prediction API")

with open("grid_search_logistic_model.pkl", "rb") as file:
    model = pickle.load(file)

# Iris input schema
class IrisInput(BaseModel):
    sepal_length: float = Field(gt=0)
    sepal_width: float = Field(gt=0)
    petal_length: float = Field(gt=0)
    petal_width: float = Field(gt=0)

# Species mapping
species = {
    0: "setosa",
    1: "versicolor",
    2: "virginica"
}

@app.post("/predict")
def predict(data: IrisInput):

    # Convert input JSON into a 2D NumPy array
    features = pd.DataFrame([data.model_dump()])

    # Predict using the trained model
    prediction = int(model.predict(features)[0])

    # Return JSON response
    return {
        "predicted_class": prediction,
        "predicted_species": species[prediction]
    }
