from django.contrib import admin
from web.models import Subscription, Clients, Feature

admin.site.register(Subscription)

admin.site.register(Clients)

class FeatureAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "description"]

admin.site.register(Feature)