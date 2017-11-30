from django.contrib import admin
from main.models import Post

# Register your models here.
class PostAdmin(admin.ModelAdmin):
	search_fields = ['id', 'title', 'content', 'posted_at', 'edited_at', ]
	list_display = ('id', 'title', 'content', )
	readonly_fields = ('posted_at', 'edited_at', )

admin.site.register(Post, PostAdmin)