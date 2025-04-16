from django.contrib import admin
from .models import Post, tag

admin.site.register(Post)
admin.site.register(tag)

# Register your models here.
