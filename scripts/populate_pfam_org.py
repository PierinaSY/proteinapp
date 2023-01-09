import os
import sys
import django
import csv
from collections import defaultdict

sys.path.append("/Users/pierinasalinas/Downloads/proteinapi-main")
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'web_project.settings')
django.setup()

from protein.models import * 

data_file_pfam = '/Users/pierinasalinas/Downloads/proteinapi-main/scripts/pfam_descriptions.csv'
data_file_domain = '/Users/pierinasalinas/Downloads/proteinapi-main/scripts/assignment_data_set.csv'


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
            genus, species = row[3].split(' ', 1)
                
        # Create the Domains object with the data from the row and the foreign key objects
        organism = Organisms(taxa_id=row[1], clade=row[2], genus=genus, species=species)

        # Save the object to the database
        organism.save()