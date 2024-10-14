from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.title

class Book(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='book_image/', null=True, blank=True)
    author = models.CharField(max_length=200)
    publication_date = models.DateField()
    publisher = models.CharField(max_length=200)
    category = models.ManyToManyField(Category,blank=True)
    about = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    url = models.URLField(null=True, blank=True)
    is_published = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.title