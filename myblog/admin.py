from django.contrib import admin
from .models import Article, Category, Author,Feedback


admin.site.register(Article)
admin.site.register(Category)
admin.site.register(Author)
admin.site.register(Feedback)

