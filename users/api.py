from ninja import Router
from .models import User
from .schemas import LoginSchema
from django.contrib.auth import authenticate, login

router = Router()

@router.post('/login')
def register(request, credentials: LoginSchema):
  user = authenticate(request, username=credentials.username, password=credentials.password)
  if user is not None:
    login(request, user)
    return {"message": "Login successful"}
  else:
    return {"message": "Invalid credentials"}

