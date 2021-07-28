from django.db import models

class Student(models.Model):
  name = models.CharField(max_length=200)
  location = models.CharField(max_length=200)
  qualification = models.CharField(max_length=200)
  college = models.ForeignKey('College', on_delete=models.CASCADE)
  
  def __str__(self):
    return self.name  
  
class College(models.Model):
  name = models.CharField(max_length=200)
  
  def __str__(self):
    return self.name