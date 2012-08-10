from django.contrib import admin
from core.models import News,Tag

class TagInline(admin.StackedInline):
	model = Tag
	extras = 2

class NewsAdmin(admin.ModelAdmin):
	list_display = ('title','user')
	list_filter = ('timestamp',)
	search_fields = ('story','title')
	inlines = [TagInline]
	fieldsets = [
			(None, {'fields':['user']}),
			('News Particulars',{'fields':['title','story','is_active']}),
			('Date Information',{'fields':['timestamp'],'classes':['collapse']})
		]

class TagAdmin(admin.ModelAdmin):
	list_display = ('title','user')
	search_fields = ('title',)
	fieldsets = [
		(None,{'fields':['user']}),
		('Tag Title',{'fields':['title']}),
		('Date Information',{'fields':['timestamp'],'classes':['collapse']})
	]

admin.site.register(News,NewsAdmin)
admin.site.register(Tag,TagAdmin)