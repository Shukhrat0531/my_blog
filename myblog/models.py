from django.db import models
from django.utils.safestring import mark_safe



class Author(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name        

class Article(models.Model):
    avtor = models.ForeignKey(Author,on_delete=models.CASCADE)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    heading = models.CharField(max_length=150)
    text = models.TextField()
    image1 = models.ImageField(upload_to ='upload', blank= True,null =True)
    text2 = models.TextField(blank=True)
    image2 = models.ImageField(upload_to ='upload', blank= True,null =True)
    text3 = models.TextField(blank=True)
    image3 = models.ImageField(upload_to ='upload', blank= True,null =True)
    like = models.BooleanField(default=False)
    data = models.CharField(max_length=10)


    def __str__(self):
        return self.heading 
        

class Feedback(models.Model):
    emaail = models.CharField(max_length=150)