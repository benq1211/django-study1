from django.contrib import admin
from .models import Author, Book, Publisher

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    fields = ['name','title']
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    pass
@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    pass
# Register your models here.
