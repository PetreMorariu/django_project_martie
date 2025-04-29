from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    page_count = models.IntegerField()
    created_by = models.ForeignKey(User, on_delete= models.CASCADE, related_name='books')



    def __str__(self):
        return "{} by {}, {} pages.".format(self.title, self.author, self.page_count)


class Pizza(models.Model):
    name = models.CharField(max_length=255)
    pizza_type = models.CharField(max_length=255)
    weight = models.IntegerField()
    size = models.IntegerField()

    def __str__(self):
        return "{} {} {} {}".format(self.name,self.pizza_type,self.weight,self.size)

class BookDetail(models.Model):
    summary = models.TextField(blank=True)
    published_date = models.DateField(null=True)
    isbn = models.CharField(max_length=13)
    book = models.OneToOneField(Book,on_delete=models.CASCADE,related_name='detail')

    def __str__(self):
        return "{} {} {} {}".format(self.summary,self.published_date,self.isbn,self.book)