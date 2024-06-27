from ninja import Router
from jwt import encode
from django.contrib.auth import authenticate
from ctrlreview_backend.settings import JWT_SECRET_KEY
from .schemas import LoginSchema, UserSchema


router = Router()

@router.post('/login', auth=None)
def register(request, credentials: LoginSchema):
  user = authenticate(request, username=credentials.username, password=credentials.password)
  if user is not None:
    user_response = UserSchema.from_orm(user)
    token = encode(dict(user_response), JWT_SECRET_KEY, algorithm="HS256")
    return {"message": "Login successful", "user": user_response, "token": token}
  else:
    return {"message": "Invalid credentials"}

