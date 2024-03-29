from pydantic import BaseModel

class Test(BaseModel):
    name: str 
    result: bool 

class Vehicle(BaseModel):
    type: str 
    tuition: str 
    color: str 
    brand: str 
    kilometric: int 
    tests: list[Test]  