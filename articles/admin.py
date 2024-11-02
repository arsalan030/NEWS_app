from django.contrib import admin
# articles/admin.py
from django.contrib import admin
from .models import Article,Comment

class CommentInline(admin.StackedInline):
    model = Comment
    extra = 0 
class ArticleAdmin(admin.ModelAdmin):
# new
# newinlines = [
    
    inlines = [
    CommentInline,
    ]
    







# Register your models here.
admin.site.register(Article,ArticleAdmin)
admin.site.register(Comment)
# new
#