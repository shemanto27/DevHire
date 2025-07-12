from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

# Create your models here.

class CustomUserManager(BaseUserManager):
    def create_user(self, email, full_name, role, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        if not full_name:
            raise ValueError('Users must have a full name')
        if not role:
            raise ValueError('Users must have a role')

        email = self.normalize_email(email)
        user = self.model(email=email, full_name=full_name, role=role)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, full_name, role='admin', password=None):
        user = self.create_user(email, full_name, role, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):

    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('developer', 'Developer'),
        ('company', 'Company'),
    )

    email = models.EmailField(unique=True)
    full_name = models.CharField(max_length=30, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)

    date_joined = models.DateField(auto_now_add=True)
    date_updated = models.DateField(auto_now=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['full_name']

    def __str__(self):
        return f'{self.full_name} ({self.email})'

class DeveloperProfileModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='developer_profile')
    skills = models.JSONField(default=dict)
    experiences = models.JSONField(default=dict)
    bio = models.TextField(blank=True, null=True)
    cv = models.FileField(upload_to='cv/', blank=True, null=True)

    def __str__(self):
        return f'{self.user.full_name} (Developer)'

class CompanyProfileModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='company_profile')
    company_name = models.CharField(max_length=100)
    company_description = models.TextField(blank=True, null=True)
    website = models.URLField(blank=True, null=True)

    def __str__(self):
        return f'{self.company_name} (Company)'