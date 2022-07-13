from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
import re
import pandas as pd
import os

class EmailBackend(ModelBackend):
    
    def authenticate(email=None, password=None, **kwargs):
        UserModel = get_user_model()
        
        try:
            #Make sure E-Mail is lowercase
            email = email.lower()
            
            #Try to get User Query with E-Mail
            user = UserModel.objects.get(email=email)
            if user.check_password(password):
                return user #Return user if password matches
        except UserModel.DoesNotExist:
            return None
        
    def password_validator(email=None, password=None):
        password = str(password)
        commonPasswords = pd.read_csv('account/static/account/commonpasswords.csv')["password"]
        symbolSet = '[@_!#$%^&*()<>?/\|}{~:]'
        characterSet = r"[A-Z]+"
        
        #Control Functions
        def likeString(firstString, secondString):
            if firstString in secondString:
                return True
            
        def containsNumber(string):
            return any(s.isdigit() for s in string)
        
        #Password Validation
        if len(password) < 8:
            return "Password has to contain atleast eight characters."
        elif not containsNumber(password):
            return "Password has to contain atleast one Number (0-9)"
        elif not re.search(symbolSet, password):
            return "Password has to contain atleast one Symbol ([@_!#$%^&*()<>?/\|}{~:])"
        elif not re.search(characterSet, password):
            return "Password has to contain atleast one Capital Letter (A-Z)"
        elif password in commonPasswords:
            return "Too easily guessed Password"
        elif likeString(email, password):
            return "Password is similar to E-Mail"
        else:
            return password
                
        


    
            

        
        
    