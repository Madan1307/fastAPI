from fastapi import FastAPI,HTTPException
from pydantic import BaseModel,Field
from typing import Annotated
import json

def load_data():
    with open('books_data.json','r') as f:
        data = json.load(f)
    
    return data

def add_data(data):
    with open('books_data.json', 'w') as f:
        json.dump(data,f)

class books(BaseModel):
    id: Annotated[str,Field(...,description="Enter the book ID",examples=["B001"])]
    book_name: Annotated[str,Field(...,description="Enter the name of the book",examples=["Wings of Fire"])]
    author: Annotated[str,Field(...,description="Enter the Author for that book",examples=["A P J Abdul Kalam"])]
    publish_year: int = Field(gt=1000,lt=2026)
    country:Annotated[str,Field(...,description="Enter the country of origin",examples=["Inida"])]

app = FastAPI()

@app.post("/add_books")
def add_books(book:books):
    #load data
    data=load_data()

    #if book already present
    if book.id in data:
        raise HTTPException(status_code=400,detail="Book already exists")

    #add the book with key as id and other as values in the form of dictonary
    data[book.id]= book.model_dump(exclude=["id"])

    #store the data bacl to the dictonary
    add_data(data)

