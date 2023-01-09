import os
import sys
import django
import csv
from collections import defaultdict

sys.path.append("/Users/pierinasalinas/Downloads/proteinapi-main")
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'web_project.settings')
django.setup()

from protein.models import * 

data_file_domain = '/Users/pierinasalinas/Downloads/proteinapi-main/scripts/assignment_data_set.csv'

with open(data_file_domain, 'r') as csvfile:
    reader = csv.reader(csvfile)
    # Iterate over the rows of the CSV file
    for row in reader:
        
        # Retrieve the Pfam and Proteins objects from the database
        pfam = Pfam.objects.get(pk=row[5])
        protein = Proteins.objects.get(pk=row[0])
        
        # Create the Domains object with the data from the row and the foreign key objects
        domain = Domains(protein_id=protein, description=row[4], start=row[6], stop=row[7], pfam_id=pfam)

        # Save the object to the database
        domain.save()
