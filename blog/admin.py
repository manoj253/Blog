from django.contrib import admin
from .models import Post

# Register your models here.
class PostAdmin(admin.ModelAdmin):
	list_display = ('title','slug','author','publish','status')
	search_fields = ('title','body')
	list_filter = ('status','created','author','publish')
	prepopulated_fields = {'slug':('title',)}
	raw_id_fields = ('author',)
	date_hierarchy = 'publish'
	ordering = ['status','publish']

admin.site.register(Post,PostAdmin)
