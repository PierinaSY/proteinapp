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
        taxa = Organisms.objects.get(pk=row[1])
        
        # Create the Domains object with the data from the row and the foreign key objects
        proteins = Proteins(protein_id=row[0], taxa_id=taxa, length=row[8], sequence='0')

        # Save the object to the database
        proteins.save()