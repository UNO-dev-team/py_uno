from pydantic import BaseModel, Field, EmailStr


class DbModel():
    def do_something(self):
        print("I'm doing something")

class User(BaseModel):
    email: str = EmailStr()
    username: str = Field(...)
    password: str = Field(..., regex='((?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[\W]).{8,64})|(password)')

    def do_something(self):
        db_model = DbModel()
        db_model.do_something()
