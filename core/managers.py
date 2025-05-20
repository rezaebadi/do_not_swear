from django.contrib.auth.models import BaseUserManager
import uuid

class UserManager(BaseUserManager):
    def generate_user_code(self):
        return str(uuid.uuid4())
    
    def create_user(self, email,first_name, last_name, user_code, password=None):
        if not first_name:
            raise ValueError('Users must have a first name')
        if not last_name:
            raise ValueError('Users must have a last name')
        if not user_code:
            raise ValueError('Users must have a user code')
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            first_name=first_name,
            last_name=last_name,
            user_code=user_code
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, first_name, last_name, password=None):
        user = self.create_user(
            first_name,
            last_name,
            user_code=self.generate_user_code(),
            password=password
        )
        user.is_admin = True
        user.is_active = True
        user.save(using=self._db)
        return user