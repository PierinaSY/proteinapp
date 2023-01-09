import factory
import random

from .models import *

class OrganismsFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Organisms

    taxa_id = random.randint(1, 10000)
    clade = factory.Faker('word')
    genus = factory.Faker('word')
    species = factory.Faker('word')

class PfamFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Pfam

    domain_id = factory.Faker('word')
    domain_description = factory.Faker('text')

class ProteinsFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Proteins

    protein_id = factory.Faker('word')
    sequence = factory.Faker('text')
    length = random.randint(1, 10000)
    taxa_id = factory.SubFactory(OrganismsFactory)

class DomainsFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Domains

    description = factory.Faker('text')
    start = random.randint(1, 10000)
    stop = random.randint(1, 10000)
    pfam_id = factory.SubFactory(PfamFactory)
    protein_id = factory.SubFactory(ProteinsFactory)

class ProteinDomainFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ProteinDomain

    proteins_id = factory.SubFactory(ProteinsFactory)
    domains_id = factory.SubFactory(DomainsFactory)
