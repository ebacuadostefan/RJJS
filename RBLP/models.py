from django.db import models

# Create your models here.

class Gender(models.Model):
    gender_id = models.BigAutoField(primary_key=True, blank=False) # BIGINT NOT NULL AUTO_INCREMENT PRIMARY KEY
    gender = models.CharField(max_length=55, blank=False) # VARCHAR(55) NOT NULL
    date_created = models.DateTimeField(auto_now_add=True) # TIMESTAMP DEFUALT CURRENT_TIMESTAMP
    date_updated = models.DateTimeField(auto_now=True) # TIMESTAMP DEFUALT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
    
    class Meta:
        db_table = 'genders'
          
    def __str__(self):
        return self.gender
        
class User(models.Model):
    user_id = models.BigAutoField(primary_key=True, blank=False) #BIGINT NOT NULL AUTO_INCREMENT PRIMARY KEY
    first_name = models.CharField(max_length=55, blank=False) #VARCHAR(55) NOT NULL
    middle_name = models.CharField(max_length=55, blank=False) #VARCHAR(55) DEFAULT NULL
    last_name = models.CharField(max_length=55, blank=False) #VARCHAR(55) NOT NULL
    address = models.CharField(max_length=55, blank=False)
    age = models.IntegerField(blank=False) #INT NOT NULL
    birth_date = models.DateField(blank=False) #DATE NOT NULL
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE) 
    username =models.CharField(max_length=55, blank=False) 
    password = models.CharField(max_length=255, blank=False) 
    date_created =models.DateTimeField(auto_now_add=True) #TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    date_updated  = models.DateTimeField(auto_now=True) #TIMESTAMP DEFUALT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
    
    class Meta:
        db_table = 'users'
        