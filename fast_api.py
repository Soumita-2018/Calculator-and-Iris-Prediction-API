from fastapi import FastAPI
from pydantic import BaseModel
from calculator import calculate

class User_input(BaseModel): #inherit from BaseModel class
    operation:str
    x:float
    y:float
    
app = FastAPI() #Object create

@app.post('/calculate')
def operate(input:User_input):
    result = calculate(input.operation, input.x, input.y)
    return result 

