from django.contrib import admin
from repo_scrapper.core import models as core_models


class RepositoryAdmin(admin.ModelAdmin):
    pass


class UserAdmin(admin.ModelAdmin):
    pass


admin.site.register(core_models.User, UserAdmin)
admin.site.register(core_models.Repository, RepositoryAdmin)
