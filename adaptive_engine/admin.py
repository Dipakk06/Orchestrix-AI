from django.contrib import admin
from .models import ConceptDependency, ConceptMastery, ConceptNode

admin.site.register(ConceptNode)
admin.site.register(ConceptDependency)
admin.site.register(ConceptMastery)
