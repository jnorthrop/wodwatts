from application.models import Definition, User, Session, Exercise
from django.contrib import admin

admin.site.register(Definition)

class ExerciseInline(admin.TabularInline):
	model = Exercise
	extra = 3

class SessionInline(admin.TabularInline):
	model = Session
	extra = 3
	
class SessionAdmin(admin.ModelAdmin):
	fieldsets = [
		(None, {'fields': ['sdate', 'slength']}),
	]
	inlines = [ExerciseInline]
	list_display = ('sdate',)
	list_filter = ['sdate']
	date_hierarchy = 'sdate'

class UserAdmin(admin.ModelAdmin):
	fieldsets = [
		(None, {'fields': ['uuser']}),
		('Physical Characteristics', {'fields': ['uheight', 'uweight'], 'classes': ['collapse']}),
	]
	inlines = [SessionInline]

admin.site.register(User, UserAdmin)
admin.site.register(Session, SessionAdmin)
