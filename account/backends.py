from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend

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
        


    
            
        
        
        
    