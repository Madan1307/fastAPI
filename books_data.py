from fastapi import FastAPI,HTTPException
from pydantic import BaseModel,Field
from typing import Annotated,Optional
import json
from fastapi.responses import JSONResponse

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

class update_books(BaseModel):
    book_name:Annotated[Optional[str],Field(default=None)]
    author:Annotated[Optional[str],Field(default=None)]
    publish_year:Annotated[Optional[int],Field(gt=1000,lt=2026,default=None)]
    country:Annotated[Optional[str],Field(default=None)]


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


@app.put("/update/{book_id}")
def update_books(book_id:str,updated_book:update_books):
    data=load_data()
    if book_id not in data:
        raise HTTPException(status_code=400,detail="Book not Exist")

    existing_record = data[book_id]
    updating_record=updated_book.model_dump(exclude_unset=True)

    for key,value in updating_record.items():
        existing_record[key]=value

    existing_record['id']=book_id
    updating_record_pydantic=books(**existing_record)
    existing_record=updating_record_pydantic.model_dump(exclude='id')
    data[book_id]=existing_record

    add_data(data)
    return JSONResponse(
    status_code=201,
    content={"message": "Book added successfully"}
)

