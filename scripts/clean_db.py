import os
import sys
import django
import csv
from collections import defaultdict

sys.path.append("/Users/pierinasalinas/Downloads/proteinapi-main")
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'web_project.settings')
django.setup()

from protein.models import * 

ProteinDomain.objects.all().delete()

# Delete Domain objects
Domains.objects.all().delete()

# Delete Protein objects
Proteins.objects.all().delete()

# Delete Pfam objects
Pfam.objects.all().delete()

# Delete Organism objects
Organisms.objects.all().delete()

