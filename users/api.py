from django.contrib.auth import authenticate
from jwt import encode
from ninja import Router

from ctrlreview_backend.settings import JWT_SECRET_KEY

from .models import User
from .schemas import LoginSchema, RegisterSchema, UserSchema

router = Router()


@router.post("/login", auth=None)
def login(request, credentials: LoginSchema):
    user = authenticate(
        request, username=credentials.username, password=credentials.password
    )
    if user is not None:
        user_response = UserSchema.from_orm(user)
        token = encode(dict(user_response), JWT_SECRET_KEY, algorithm="HS256")
        return {"message": "Login successful", "user": user_response, "token": token}
    else:
        return {"message": "Invalid credentials"}


@router.post("/register", auth=None)
def register(request, body: RegisterSchema):
    user = User.objects.create_user(
        email=body.email, username=body.username, password=body.password
    )
    if user is not None:
        user_response = UserSchema.from_orm(user)
        token = encode(dict(user_response), JWT_SECRET_KEY, algorithm="HS256")
        return {"message": "Register successful", "user": user_response, "token": token}
    else:
        return {"message": "Invalid credentials"}
