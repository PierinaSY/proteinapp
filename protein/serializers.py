from django.db.models import Sum
from rest_framework import serializers
from rest_framework.serializers import SerializerMethodField
from .models import *

class OrganismSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Organisms
        fields = ['taxa_id', 'clade', 'genus', 'species']

class ProteinSerializer(serializers.ModelSerializer):
    taxa_id = OrganismSerializer()
    class Meta: 
        model = Proteins
        fields = ['protein_id', 'sequence', 'taxa_id', 'length']

    def create(self, validated_data):
        taxa_id_data = self.initial_data.get('taxa_id')
        protein = Proteins(**{**validated_data,
                    'taxa_id' : Organisms.objects.get(pk=taxa_id_data['id'])
                    })
        protein.save()
        return protein

class PfamSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Pfam
        fields = ['domain_id', 'domain_description']

class DomainSerializer(serializers.ModelSerializer):
    pfam_id =  PfamSerializer()
    class Meta: 
        model = Domains
        fields = ['pfam_id','description', 'start', 'stop']

    def create(self, validated_data):
        pfam_id_data = self.initial_data.get('pfam_id')
        domain = Domains(**{**validated_data,
                 'pfam_id' : Pfam.objects.get(pk=pfam_id_data['id'])
                 })
        domain.save()
        return domain

class ProteinDomainSerializer(serializers.ModelSerializer):
    proteins_id = ProteinSerializer()
    domains_id = DomainSerializer()

    class Meta:
        model = ProteinDomain
        fields =  ['proteins_id', 'domains_id'] #'protein_id']

    def create(self, validated_data):
        proteins_id_data = self.initial_data.get('proteins_id')
        domains_id_data = self.initial_data.get('domains_id')
        proteindomain = ProteinDomain(**{**validated_data,
                 'proteins_id' : Proteins.objects.get(pk=proteins_id_data['id']),
                 'domains_id' : Domains.objects.get(pk=domains_id_data['id'])
                 })
        proteindomain.save()
        return proteindomain


#Taxa, Proteins and Domain 
class DomainIdSerializer(serializers.ModelSerializer):
    protein_id = serializers.SerializerMethodField()

    class Meta: 
        model = Domains
        fields = ['id', 'protein_id']
        depth = 1

    def get_protein_id(self, obj):
        return obj.protein_id.protein_id


#Taxa, Pfam and Domain 
class PfamDomainIdSerializer(serializers.ModelSerializer):
    pfam_id =  PfamSerializer()
    class Meta: 
        model = Domains
        fields = ['id', 'pfam_id']

    def create(self, validated_data):
        pfam_id_data = self.initial_data.get('pfam_id')
        domain = Domains(**{**validated_data,
                 'pfam_id' : Pfam.objects.get(pk=pfam_id_data['id']), 
                 })
        domain.save()
        return domain

#Coverage Serializer
class CoverageSerializer(serializers.ModelSerializer):
    coverage = serializers.SerializerMethodField()

    class Meta:
        model = Domains
        fields = ['coverage']
        depth = 1

    def get_coverage(self, obj):
        # return (obj.start + obj.stop) / obj.protein_id.length
        
        # Calculate the sum of all the start values
        start_sum = Domains.objects.all().aggregate(Sum('start'))['start__sum']
        
        # Calculate the sum of all the stop values
        stop_sum = Domains.objects.all().aggregate(Sum('stop'))['stop__sum']
        
        # Calculate the coverage
        coverage = (start_sum + stop_sum) / obj.protein_id.length
        return coverage
