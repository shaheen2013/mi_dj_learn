from django.contrib import admin
from posts.models import Post, Category


# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    fields = ('title',)
    list_display = ('title', 'slug',)


admin.site.register(Post)
admin.site.register(Category, CategoryAdmin)
