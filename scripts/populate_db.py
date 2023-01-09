import os
import sys
import django
import csv
from collections import defaultdict

sys.path.append("/Users/pierinasalinas/Documents/UOL/AWD/Midterm/protein_app")
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'web_project.settings')
django.setup()

from protein.models import * 

data_file_pfam = '/Users/pierinasalinas/Documents/UOL/AWD/Midterm/protein_app/scripts/pfam_descriptions.csv'

data_file_protein = '/Users/pierinasalinas/Documents/UOL/AWD/Midterm/protein_app/scripts/assignment_data_sequences.csv'

data_file_domain = '/Users/pierinasalinas/Documents/UOL/AWD/Midterm/protein_app/scripts/assignment_data_set.csv'


# pfam_descriptions
with open(data_file_pfam, 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        domain_id = row[0]
        domain_description = row[1]
        pfam, created = Pfam.objects.get_or_create(
            domain_id=domain_id,
            defaults={'domain_description': domain_description}
        )
        if not created:
            pfam.domain_description = domain_description
            pfam.save()

# assignment_data_sequences
with open(data_file_protein, 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        protein_id = row[0]
        sequence = row[1]
        organism, created = Organisms.objects.get_or_create(
            taxa_id=taxa_id,
            defaults={'clade': clade, 'genus': genus, 'species': species}
        )
        taxa_id = organism.taxa_id
        try:
            protein = Proteins.objects.get(protein_id=protein_id)
            protein.sequence = sequence
            if protein.taxa_id is None:
                protein.taxa_id = taxa_id
            protein.save()
        except Proteins.DoesNotExist:
            protein = Proteins(protein_id=protein_id, sequence=sequence, taxa_id=taxa_id)
            protein.save()

taxa_id = organism.taxa_id
with open(data_file_protein, 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        protein_id = row[0]
        sequence = row[1]
        try:
            protein = Proteins.objects.get(protein_id=protein_id)
            protein.sequence = sequence
            if protein.taxa_id is None:
                protein.taxa_id = taxa_id
            protein.save()
        except Proteins.DoesNotExist:
            protein = Proteins(protein_id=protein_id, sequence=sequence, taxa_id=taxa_id)
            protein.save()


# assignment_data_sequences
with open(data_file_protein, 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        protein_id = row[0]
        sequence = row[1]
        try:
            protein = Proteins.objects.get(protein_id=protein_id)
            protein.sequence = sequence
            if protein.taxa_id is None:
                protein.taxa_id = taxa_id
            protein.save()
        except Proteins.DoesNotExist:
            protein = Proteins(protein_id=protein_id, sequence=sequence, taxa_id=taxa_id)
            protein.save()

# assignment_data_set
with open(data_file_domain, 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        if "." in row[3]:
            genus, species = row[3].split(".", 1)
        else:
            genus, species = row[3].split(' ',1)
        protein_id = row[0]
        taxa_id = row[1]
        clade = row[2]
        description = row[4]
        domain_id = row[5]
        start = row[6]
        stop = row[7]
        length = row[8]

        try:
            protein = Proteins.objects.get(protein_id=protein_id)
        except Proteins.DoesNotExist:
            protein = Proteins(protein_id=protein_id, sequence=sequence)
            protein.save()
        
        organism, created = Organisms.objects.get_or_create(
            taxa_id=taxa_id,
            defaults={'clade': clade, 'genus': genus, 'species': species}
        )
        if not created:
            organism.clade = clade
            organism.genus = genus
            organism.species = species
            organism.save()
        taxa_id = organism.taxa_id
        protein.taxa_id = taxa_id
        protein.save()


        pfam = Pfam.objects.get(domain_id=domain_id)
        domain, created = Domains.objects.get_or_create(
            description=description,
            start=start,
            stop=stop,
            pfam_id=pfam,
            protein_id=protein
        )
        if not created:
            domain.description = description
            domain.start = start
            domain.stop = stop
            domain.save()
