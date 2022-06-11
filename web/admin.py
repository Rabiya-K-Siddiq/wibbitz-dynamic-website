from django.contrib import admin
from web.models import Subscription, Clients, Feature, Contact

admin.site.register(Subscription)

admin.site.register(Clients)

class FeatureAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "description"]

admin.site.register(Feature)


class ContactAdmin(admin.ModelAdmin):
    list_display = ["id", "first_name", "company", "jobe_role"]

admin.site.register(Contact)