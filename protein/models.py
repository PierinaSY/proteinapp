from django.db import models

# Create your models here.
class Organisms(models.Model):
    taxa_id =  models.IntegerField(primary_key=True)
    clade = models.CharField(max_length=10)
    genus = models.CharField(max_length=100)
    species = models.CharField(max_length=100)

class Pfam(models.Model):
    id = models.AutoField(primary_key=True)
    domain_id = models.CharField(max_length=100)
    domain_description = models.TextField()

class Proteins(models.Model):
    id = models.AutoField(primary_key=True)
    protein_id = models.CharField(max_length=100)
    sequence = models.TextField()
    length = models.IntegerField()
    taxa_id =  models.ForeignKey(Organisms, on_delete=models.CASCADE)
    
class Domains(models.Model):    
    id = models.AutoField(primary_key=True)
    description = models.TextField()
    start = models.IntegerField()
    stop = models.IntegerField()
    pfam_id = models.ForeignKey(Pfam, on_delete=models.CASCADE)
    protein_id = models.ForeignKey(Proteins, on_delete=models.CASCADE)

class ProteinDomain(models.Model): 
    id = models.AutoField(primary_key=True)
    proteins_id = models.ForeignKey(Proteins, on_delete=models.CASCADE)
    domains_id = models.ForeignKey(Domains, on_delete=models.CASCADE)
    