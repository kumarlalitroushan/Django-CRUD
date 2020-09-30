from django.contrib import admin
from home.models import Books
# Register your models here.

@admin.register(Books)
class BookAdmin(admin.ModelAdmin):
    list_display=('sno','title','author','publisher','stock')