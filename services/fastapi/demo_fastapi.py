from fastapi import FastAPI, HTTPException, Response
from typing import Optional
from pydantic import BaseModel


app = FastAPI()

class Contact(BaseModel):
    contact_id:int
    first_name:str
    last_name:str
    user_name:str
    password:str

class ContactOut(BaseModel):
    contact_id:int
    first_name:str
    last_name:str
    user_name:str

class Config:
        schema_extra = {
            "example": {
                "contact_id": 1,
                "first_name": "Jhon",
                "last_name": "Doe",
                "user_name": "jhon_123",
            }
        }


@app.get("/")
def home():
    return {"Hello": "FastAPI"}

@app.get("/contact/{contact_id}")
def contact_details(contact_id: int, page: Optional[int] = 1):
    if page:
        return {'contact_id': contact_id, 'page': page}
    return {'contact_id': contact_id}


@app.get("/contact/{id}", response_model=Contact, response_model_exclude={"password"}, description="Fetch a single contact")
async def contact_details(id: int, response: Response):
    response.headers["X-LOL"] = "1"
    if id < 1:
        raise HTTPException(status_code=404, detail="The required contact details not found")
    contact = Contact(contact_id=id, 
                        first_name='Adnan',
                        last_name='Siddiqi',
                        user_name='adnan1',
                        password='adn34')
    return contact