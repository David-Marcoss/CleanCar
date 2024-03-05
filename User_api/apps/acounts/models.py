from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager


class CustomUserManager(BaseUserManager):
    
    def create_user(self, email,password=None, **extra_fields):
        if not email:
            raise ValueError('The Email is required')
        
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)

        user.save()
    
        return user

    def create_superuser(self, email,password=None ,**extra_fields):
        user = self.create_user(email, password, is_staff=True, is_superuser=True, **extra_fields)
        user.save()

        return user


class User(AbstractUser):
    name = models.CharField('Nome', max_length=255)
    email = models.EmailField('Email', unique=True)
    phone = models.CharField('Telefone', max_length=15,null=True, blank=True)
    date_birth = models.DateField('Data de Nascimento', null=True, blank=True)

    cretaed_at = models.DateTimeField('Criado em', auto_now_add=True)
    updated_at = models.DateTimeField('Atualizado em', auto_now=True)

    username = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'phone', 'date_birth']

    objects = CustomUserManager()

