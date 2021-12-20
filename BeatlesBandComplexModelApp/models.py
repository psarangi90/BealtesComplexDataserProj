from django.db import models

# Create your models here.
class Person(models.Model):
    name=models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Group(models.Model):
    name=models.CharField(max_length=100)
    person=models.ManyToManyField(Person,through='Intermidiate')
    
    def __str__(self):
        return self.name

class Intermidiate(models.Model):
    person=models.ForeignKey(Person, on_delete=models.CASCADE,)
    group=models.ForeignKey(Group, on_delete=models.CASCADE)
    date_joined=models.DateTimeField(auto_now_add=True)
    reason=models.CharField(max_length=100)
    
    def __str__(self):
        return self.person.name
    
    # def __str__(self):
    #     return self.reason
    
    
    