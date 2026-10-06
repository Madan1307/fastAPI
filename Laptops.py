from fastapi import FastAPI,Path,HTTPException,Query

app=FastAPI()

data={
    "L001": {
        "name": "Dell Inspiron",
        "processor": "Intel i5",
        "ram": "8GB",
        "storage": "512GB SSD",
        "screen": "15.6 inch",
        "os": "Windows 11"
    },

    "L002": {
        "name": "HP Pavilion",
        "processor": "Intel i7",
        "ram": "16GB",
        "storage": "1TB SSD",
        "screen": "15.6 inch",
        "os": "Windows 11"
    },

    "L003": {
        "name": "Lenovo IdeaPad",
        "processor": "AMD Ryzen 5",
        "ram": "8GB",
        "storage": "512GB SSD",
        "screen": "15.6 inch",
        "os": "Windows 11"
    },

    "L004": {
        "name": "ASUS VivoBook",
        "processor": "Intel i5",
        "ram": "16GB",
        "storage": "512GB SSD",
        "screen": "14 inch",
        "os": "Windows 11"
    },

    "L005": {
        "name": "Acer Aspire",
        "processor": "AMD Ryzen 7",
        "ram": "16GB",
        "storage": "1TB SSD",
        "screen": "15.6 inch",
        "os": "Windows 11"
    },

    "L006": {
        "name": "MacBook Air",
        "processor": "Apple M2",
        "ram": "8GB",
        "storage": "256GB SSD",
        "screen": "13.6 inch",
        "os": "macOS"
    },

    "L007": {
        "name": "Dell XPS",
        "processor": "Intel i7",
        "ram": "16GB",
        "storage": "1TB SSD",
        "screen": "13.4 inch",
        "os": "Windows 11"
    },

    "L008": {
        "name": "HP Envy",
        "processor": "AMD Ryzen 5",
        "ram": "16GB",
        "storage": "512GB SSD",
        "screen": "15.6 inch",
        "os": "Windows 11"
    },

    "L009": {
        "name": "Lenovo ThinkPad",
        "processor": "Intel i5",
        "ram": "8GB",
        "storage": "512GB SSD",
        "screen": "14 inch",
        "os": "Windows 11"
    },

    "L010": {
        "name": "ASUS ROG",
        "processor": "Intel i7",
        "ram": "16GB",
        "storage": "1TB SSD",
        "screen": "15.6 inch",
        "os": "Windows 11"
    }
}


@app.get("/show")
def show_data():
    return data

@app.get("/show/{input_parameter}")
def show_user(input_parameter :str = Path(...,description="provide the laptop_id in the database",example="L001")):
    if(input_parameter in data):
        return data[input_parameter]
    raise HTTPException(status_code=404,detail="patient not found")


@app.get("/sort")
def sort(sort_by:str = Query(...,description="Sorting the recores based on provided input"),order:str=Query('asc',description="order for sorting asc or desc")):
   if(sort_by not in ["name","os"]):
        raise HTTPException(status_code=400,detail="sort by should be name or os")
   
   if(order not in ["asc","desc"]):
        raise HTTPException(status_code=400,detail="sort by should be asc or desc")
    
    
   req_ord= True if order == "desc" else False
   
   sorted_ans = sorted(data.values(),key= lambda x:x.get(sort_by),reverse=req_ord)
   return sorted_ans