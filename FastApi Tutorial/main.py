from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app= FastAPI() # Create a app

class Tea(BaseModel):
    id : int
    name : str
    origin : str
    
teas: List[Tea]= []

@app.get("/")
def read_root():
    return {"message":"Welcome to tea house"}


@app.get("/teas")
def get_teas():
    return teas    

@app.post("/teas")
def add_tea(tea:Tea):
    teas.append(tea)
    return tea

@app.put("/teas?{tea_id}")
def update_tea(tea_id: int,updated_tea:Tea):
    for index ,tea in enumerate (teas):
        if tea.id ==tea.id:
            teas[index]= update_tea
            return update_tea
    return {"error":"Tea not Found"}

@app.delete("/teas/{tea_id}")
def delete_tea(tea_id : int):
    for index ,tea in enumerate (teas):
          if tea.id ==tea.id:
              deleted = tea.pop(index)
              return deleted
    return {"error":"Tea not found"}