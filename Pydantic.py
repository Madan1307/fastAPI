
from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()


# 1. Define the Pydantic validation model
class Laptop(BaseModel):
    name: str
    price: float = Field(gt=0)
    ram: int = Field(gt=0)


# 2. Create an API endpoint
@app.post("/laptops")
def create_laptop(laptop: Laptop):

    # 3. Display the validated object
    print(laptop)
    print(type(laptop))

    return {
        "message": "Laptop received successfully",
        "name": laptop.name,
        "price": laptop.price,
        "ram": laptop.ram
    }
