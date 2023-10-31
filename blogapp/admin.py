from django.contrib import admin

from .models import Post_data

# Register your models here.
#admin.site.register(Post_data)
@admin.register(Post_data)
class post_dataadmin(admin.ModelAdmin):
    list_display = ['id','title','desc']
