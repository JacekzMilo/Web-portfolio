from django.contrib import admin
from .models import *
from django.utils.html import format_html

class GalleryAdmin(admin.ModelAdmin):
    def image_tag(self, obj):
        return format_html('<img src="{}" width="auto" height="200px" />'.format(obj.Project_img.url))

    image_tag.short_description = 'Image Preview'
    # list_display = ['image_tag'] #-> This will show image in your dashboard instead of First Image, Second Image and Third Image
    readonly_fields = ['image_tag']

    # class landingpageAdmin(admin.ModelAdmin):
    list_display = ('Project_name', 'Project_desc', "Project_img", "Skills", "Project_no")




admin.site.register(Project, GalleryAdmin)
