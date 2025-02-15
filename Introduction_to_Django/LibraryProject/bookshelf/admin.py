from django.contrib import admin
from bookshelf.models import Book

# Register your models here.
class BookAdmin(admin.ModelAdmin):
    list_filter = "title","author", "publication_year"
    search_field = "title","author", "publication_year"
    list_display = "title","author", "publication_year"

admin.site.register(Book,BookAdmin)
