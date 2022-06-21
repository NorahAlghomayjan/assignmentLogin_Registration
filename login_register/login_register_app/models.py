import email
from django.db import models
import re
import bcrypt
# Create your models here.

class UserManager (models.Manager):
    def validRegister(self,post):
        errors = {}
        #checking first name & last name:
        if len(post['first']) < 2:
            errors['first_name'] = "First Name should be at least 2 characters"
            
        if len(post['last']) < 2:
            errors['last_name'] = "First Name should be at least 2 characters"
        
        #checking first password:
        if len(post['pw']) < 8:
            errors['pw'] = "Password should be at least 8 characters"
        if post['pw'] != post['pw2']:
            errors['pw_match'] = "Passwords don't match "
        
        #checking email:
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(post['email']):
            errors['email'] = "Invalid email address!"
        elif (User.objects.filter(email=post['email'])):
            errors['identical']= 'Email already exist..' 
        return errors

    def validLogin(self,post):
        errors = {}
        #fetching for the email in db.
        user = User.objects.filter(email=post['email'])

        #checking email (if user=none -> error , if user exist -> else)
        if not(user):
            errors ['email'] = 'Email is not correct'
        elif not(bcrypt.checkpw(post['pw'].encode(), user[0].password.encode())):
            errors ['pw'] = 'Not correct password'
        return errors


class User (models.Model):
    first_name = models.CharField(max_length=50,blank=False,null=False)
    last_name = models.CharField(max_length=50,blank=False,null=False)
    email = models.EmailField(blank=False,null=False)
    password = models.CharField(max_length=50,blank=False,null=False)
    objects = UserManager()