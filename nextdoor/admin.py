from django.contrib import admin
from .models import Neighborhood,Profile,Alert,Hospital,Business

admin.site.register(Neighborhood)
admin.site.register(Alert)
admin.site.register(Profile)
admin.site.register(Business)
admin.site.register(Hospital)

