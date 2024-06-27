from ninja import Schema

class LoginSchema(Schema):
  username: str
  password: str

class UserSchema(Schema):
  id: int
  username: str
  email: str

class RegisterSchema(Schema):
  username: str
  email: str
  password: str
