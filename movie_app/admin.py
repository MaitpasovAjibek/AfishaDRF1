from django.contrib import admin
from .models import Movie,Director,Rewiew

# Register your models here.
@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('id','title','description','duration','director')



admin.site.register(Director)
admin.site.register(Rewiew)