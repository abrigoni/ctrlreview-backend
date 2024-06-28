from jwt import PyJWTError, decode
from ninja.security import HttpBearer

from ctrlreview_backend.settings import JWT_SECRET_KEY

from .models import User


class AuthBearer(HttpBearer):
    def authenticate(self, request, token):
        try:
            payload = decode(token, JWT_SECRET_KEY, algorithms=["HS256"])
            user_id = payload.get("id")
            if user_id is None:
                return None
            # Get the user
            user = User.objects.get(id=user_id)

            # Add the user to the request
            request.user = user
            return user
        except PyJWTError:
            return None
        except User.DoesNotExist:
            return None
