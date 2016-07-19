from django.contrib import admin

# Register your models here.
from kdm.models import User, Blog, Project
# class BlogAdmin(admin.ModelAdmin):
#     exclude = ['posted']
#     prepopulated_fields = {'slug': ('title',)}

# class CategoryAdmin(admin.ModelAdmin):
#     prepopulated_fields = {'slug': ('title',)}

# admin.site.register(Blog)
# admin.site.register(Category)
from django.contrib import admin

# Register your models here.

from .forms import SignUpForm
from .models import SignUp

class BlogModelAdmin(admin.ModelAdmin):
	list_display = ["__unicode__", "posted"]
	search_fields = ["title", "body"]
	class Meta:
		model=Blog

class SignUpAdmin(admin.ModelAdmin):
	list_display = ["__unicode__", "timestamp", "updated"]
	form = SignUpForm
	# class Meta:
	# 	model = SignUp

class ProjectModelAdmin(admin.ModelAdmin):
	list_display = ["__unicode__", "publish"]
	search_fields = ["title", "content"]
	class Meta:
		model=Project


admin.site.register(Blog, BlogModelAdmin)
admin.site.register(Project, ProjectModelAdmin)

