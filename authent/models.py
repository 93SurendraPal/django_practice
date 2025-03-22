from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
#class Student(models.Model):

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        print("extra_fields")
        if not email:
            raise ValueError("Email is required")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

class Student(AbstractBaseUser, PermissionsMixin):
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='student_groups',  # Change this to avoid conflict
        blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='student_permissions',  # Change this to avoid conflict
        blank=True
    )

    name = models.CharField(max_length=100,null=True)
    age = models.IntegerField(default=18)
    father_name = models.CharField(max_length=100,null=True)
    class_name = models.CharField(max_length=100,null=True)
    email = models.CharField(max_length=100,null=True,unique=True)
    password = models.CharField(max_length=300,null=True)
    
    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def __str__(self):
        #return self.email
        return str(vars(self))
    class Meta:
        db_table="students"


class ClassName(models.Model):
    name = models.CharField(max_length=100,null=True)
    fees = models.IntegerField(default=2000)
    numberOfSubject = models.IntegerField(default=6)
    class Meta:
        db_table="classname"
class Book(models.Model):
    book_title = models.CharField(max_length=100,null=True)
    auther = models.CharField(max_length=100)
    #auther = models.ForeignKey(Category, on_delete=models.CASCADE)
    class Meta:
        db_table="book"