from application.models import *
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

class ProfileAdmin(admin.ModelAdmin):
	fieldsets = [
		(None, {'fields': ['puser']}),
		('Physical Characteristics', {'fields': ['pheight', 'pweight'], 'classes': ['collapse']}),
	]
	inlines = [SessionInline]

admin.site.register(Profile, ProfileAdmin)
admin.site.register(Session, SessionAdmin)
