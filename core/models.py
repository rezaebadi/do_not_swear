from django.db import models
from django.contrib.auth.models import PermissionsMixin,AbstractBaseUser
from .managers import UserManager
# Create your models here.

class CustomUser(AbstractBaseUser,PermissionsMixin):
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='id')
    email=models.EmailField(max_length=255,unique=True,null=False,blank=False)
    first_name=models.CharField(max_length=50,null=False,blank=False)
    last_name=models.CharField(max_length=50,null=False,blank=False)
    user_code=models.CharField(max_length=50,null=False,blank=False)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name','last_name','user_code']

    objects = UserManager()

    @property
    def is_staff(self):
        return self.is_admin
    

    class Meta:
        db_table = 'user'
        verbose_name = 'user'
        verbose_name_plural = 'users'

class Role(models.Model):
    name = models.CharField(max_length=50,null=False,blank=False)
    description = models.TextField(null=True,blank=True)

    class Meta:
        db_table = 'role'
        verbose_name = 'role'
        verbose_name_plural = 'roles'

class Group(models.Model):
    name = models.CharField(max_length=50,null=False,blank=False)
    group_code = models.CharField(max_length=50,null=False,blank=False)
    description = models.TextField(null=True,blank=True)
    group_code=models.CharField(max_length=50,null=False,blank=False)
    class Meta:
        db_table = 'group'
        verbose_name = 'group'
        verbose_name_plural = 'groups'

class UserGroup(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'user_group'
        verbose_name = 'user group'
        verbose_name_plural = 'user groups'
 

class Board(models.Model):
    name = models.CharField(max_length=50,null=False,blank=False)
    description = models.TextField(null=True,blank=True)
    group=models.ForeignKey(Group, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'board'
        verbose_name = 'board'
        verbose_name_plural = 'boards'

class column(models.Model):
    name = models.CharField(max_length=50,null=False,blank=False)
    description = models.TextField(null=True,blank=True)
    board=models.ForeignKey(Board, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'column'
        verbose_name = 'column'
        verbose_name_plural = 'columns'

class UserBoard(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    value=models.CharField(max_length=50,null=False,blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'user_board'
        verbose_name = 'user board'
        verbose_name_plural = 'user boards'

