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

with open(data_file_pfam, 'r') as csvfile:
    reader = csv.reader(csvfile)
    # Iterate over the rows of the CSV file
    for row in reader:
        # Create a Pfam object with the data from the row
        pfam = Pfam(domain_id=row[0], domain_description=row[1])
        # Save the object to the database
        pfam.save()

with open(data_file_domain, 'r') as csvfile:
    reader = csv.reader(csvfile)
    # Iterate over the rows of the CSV file
    for row in reader:
        # Split the species name into genus and species
        if "." in row[3]:
            genus, species = row[3].split(".", 1)
        else:
            genus, species = row[3].split(' ',1)
                
        # Create the Domains object with the data from the row and the foreign key objects
        organism = Organisms(taxa_id=row[1], clade=row[2], genus=genus, species=species)

        # Save the object to the database
        organism.save()

with open(data_file_protein, 'r') as csvfile:
    reader = csv.reader(csvfile)
    # Iterate over the rows of the CSV file
    for row in reader:
        # Create a Protein object with the data from the row
        proteins = Proteins(protein_id=row[0], sequence=row[1])
        # Save the object to the database
        proteins.save()

# proteins = set()

# with open(data_file_protein, 'r') as csvfile:
#     reader = csv.reader(csvfile)
#     # Iterate over the rows of the CSV file
#     for row in reader:
#         proteins.add((row[0], row[1]))



with open(data_file_domain, 'r') as csvfile:
    reader = csv.reader(csvfile)
    # Iterate over the rows of the CSV file
    for row in reader:
        
        # Retrieve the Pfam and Proteins objects from the database
        pfam = Pfam.objects.get(pk=row[5])
        protein = Proteins.objects.get(pk=row[0])
        
        # Create the Domains object with the data from the row and the foreign key objects
        domain = Domains(protein_id=protein, description=row[4], start=row[6], stop=row[7], pfam_id=pfam)
        proteins = Proteins(length=row[8])

        # Save the object to the database
        domain.save()
        proteins.save()

