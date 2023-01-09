import os
import sys
import django
import csv
from collections import defaultdict

sys.path.append("/Users/pierinasalinas/Downloads/proteinapi-main")
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'web_project.settings')
django.setup()

from protein.models import * 

data_file_protein = '/Users/pierinasalinas/Downloads/proteinapi-main/scripts/assignment_data_sequences.csv'


with open(data_file_protein, 'r') as csvfile:
    reader = csv.reader(csvfile)
    # Iterate over the rows of the CSV file
    for row in reader:
        protein = Proteins.objects.get(pk=row[0])
        # Create a Protein object with the data from the row
        proteins = Proteins(protein_id=protein, sequence=row[1])
        # Save the object to the database
        proteins.save()