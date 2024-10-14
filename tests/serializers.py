from rest_framework.serializers import ModelSerializer
from . import models


class CategorySerializers(ModelSerializer):
    class Meta:
        model = models.Category
        fields = '__all__'

class BookListSerializers(ModelSerializer):

    class Meta:
        model = models.Book
        fields = ['id', 'title', 'author', 'image', 'category']


class BookDetailSerializers(ModelSerializer):
    category = CategorySerializers(many = True, read_only = True)


    class Meta:
        model = models.Book
        fields = '__all__'

