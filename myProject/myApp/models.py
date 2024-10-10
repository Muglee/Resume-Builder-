from django.db import models
from django.contrib.auth.models import AbstractUser


class custom_user(AbstractUser):
    
    USER=[
        ('admin','Admin'),
        ('viewer','Viewer'),
    ]

    user_type=models.CharField(choices=USER,max_length=10)
    
    
class resumeModel(models.Model):
    
    GENDER=[
        ('male','Male'),
        ('female','Female'),
        ('others','Others'),
    ]
    
    linkedin_url=models.URLField(null=True,max_length=100)
    github_url=models.URLField(null=True,max_length=100)
    codepen_url=models.URLField(null=True,max_length=100)
    yoursite_url=models.URLField(null=True,max_length=100)
    
    user=models.OneToOneField(custom_user,max_length=100,on_delete=models.CASCADE,null=True)
    profile_pic=models.ImageField(upload_to='Media/Pro_pic',null=True)
    contact_no=models.CharField(max_length=100,null=True)
    gender=models.CharField(choices=GENDER,max_length=100,null=True)
    experience=models.CharField(max_length=100,null=True)
    designation=models.CharField(max_length=100,null=True)
    skills_title=models.CharField(max_length=100,null=True)
    education=models.CharField(max_length=100,null=True)
    awards=models.CharField(max_length=100,null=True)
    language=models.CharField(max_length=100,null=True)
    Interest=models.CharField(max_length=100,null=True)
    age=models.CharField(max_length=100,null=True)
    career_summery=models.TextField(max_length=100,null=True)
    
    def __str__(self):
        return f"{self.user.username}-{self.designation}"
    
    
class skillModel(models.Model):
    
    skill_LEVEL=[
        ('high','High'),
        ('low','Low'),
        ('medium','Medium'),
    ]
    user=models.ForeignKey(custom_user,null=True,on_delete=models.CASCADE)
    skill_name=models.CharField(max_length=10,null=True)   
    proficiency_level=models.CharField(choices=skill_LEVEL,max_length=10,null=True) 
    
    
    class Meta:
        unique_together=['user','skill_name']
        
    def __str__(self) :
        return f"{self.skill_name}-{self.proficiency_level}"  
    

class intermediate_skillModel(models.Model):
    my_skill_name=models.CharField(max_length=10,null=True)   
    
    def __str__(self) :
        return f"{self.my_skill_name}" 
    
    
    
class LanguageModel(models.Model):
    
    Language_LEVEL=[
        ('high','High'),
        ('low','Low'),
        ('medium','Medium'),
    ]
    user=models.ForeignKey(custom_user,null=True,on_delete=models.CASCADE)
    Language_name=models.CharField(max_length=10,null=True)   
    proficiency_level=models.CharField(choices=Language_LEVEL,max_length=10,null=True) 
    
    
    class Meta:
        unique_together=['user','Language_name']
        
    def __str__(self) :
        return f"{self.Language_name}-{self.proficiency_level}"  
    

class intermediate_LanguageModel(models.Model):
    my_Language_name=models.CharField(max_length=10,null=True)   
    
    def __str__(self) :
        return f"{self.my_Language_name}"
    
    
    
class experienceModel(models.Model):
    
    experience_LEVEL=[
        ('high','High'),
        ('low','Low'),
        ('medium','Medium'),
    ]
    user=models.ForeignKey(custom_user,null=True,on_delete=models.CASCADE)
    experience_name=models.CharField(max_length=10,null=True)   
    proficiency_level=models.CharField(choices=experience_LEVEL,max_length=10,null=True) 
    
    
    class Meta:
        unique_together=['user','experience_name']
        
    def __str__(self) :
        return f"{self.experience_name}-{self.proficiency_level}"  
    

class intermediate_experienceModel(models.Model):
    my_experience_name=models.CharField(max_length=10,null=True)   
    
    def __str__(self) :
        return f"{self.my_experience_name}" 
    
    
    
class educationModel(models.Model):
    
    education_LEVEL=[
        ('high','High'),
        ('low','Low'),
        ('medium','Medium'),
    ]
    user=models.ForeignKey(custom_user,null=True,on_delete=models.CASCADE)
    education_name=models.CharField(max_length=10,null=True)   
    proficiency_level=models.CharField(choices=education_LEVEL,max_length=10,null=True) 
    
    
    class Meta:
        unique_together=['user','education_name']
        
    def __str__(self) :
        return f"{self.education_name}-{self.proficiency_level}"  
    

class intermediate_educationModel(models.Model):
    my_education_name=models.CharField(max_length=10,null=True)   
    
    def __str__(self) :
        return f"{self.my_education_name}" 
    
    
    
class interestModel(models.Model):
    
    interest_LEVEL=[
        ('high','High'),
        ('low','Low'),
        ('medium','Medium'),
    ]
    user=models.ForeignKey(custom_user,null=True,on_delete=models.CASCADE)
    interest_name=models.CharField(max_length=10,null=True)   
    proficiency_level=models.CharField(choices=interest_LEVEL,max_length=10,null=True) 
    
    
    class Meta:
        unique_together=['user','interest_name']
        
    def __str__(self) :
        return f"{self.interest_name}-{self.proficiency_level}"  
    

class intermediate_interestModel(models.Model):
    my_interest_name=models.CharField(max_length=10,null=True)   
    
    def __str__(self) :
        return f"{self.my_interest_name}" 