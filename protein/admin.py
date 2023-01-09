from django.contrib import admin
from .models import *

# Register your models here.
class OrganismAdmin(admin.ModelAdmin): 
    list_display = ('taxa_id', 'clade', 'genus', 'species')

admin.site.register(Organisms, OrganismAdmin)

class ProteinAdmin(admin.ModelAdmin): 
    list_display = ('protein_id', 'sequence', 'length', 'taxa_id')

admin.site.register(Proteins, ProteinAdmin)

class DomainAdmin(admin.ModelAdmin): 
    list_display = ('description', 'start', 'stop', 'pfam_id', 'protein_id')

admin.site.register(Domains, DomainAdmin)

class PfamAdmin(admin.ModelAdmin):
    list_display = ('domain_id', 'domain_description')

admin.site.register(Pfam, PfamAdmin)

class ProteinDomainAdmin(admin.ModelAdmin):
    list_display = ('proteins_id', 'domains_id')

admin.site.register(ProteinDomain, ProteinDomainAdmin)




