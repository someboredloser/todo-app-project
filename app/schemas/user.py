from pydantic import BaseModel, ConfigDict


class UserSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    
    id: str
    email: str
    
class CreateUserSchema(BaseModel):
    email: str
    password:str