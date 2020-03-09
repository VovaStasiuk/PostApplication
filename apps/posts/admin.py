from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):
    fields = ("title", "content", "total_like",)
    readonly_fields = ('total_like',)
    list_display = ("title", "total_like", )

    def total_like(self, obj):
        return obj.total_likes


admin.site.register(Post, PostAdmin)