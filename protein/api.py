from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt

from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework import mixins

from .models import *
from .serializers import *

#GET method for All Proteins 
class AllElementsList(generics.ListAPIView):
    queryset = Proteins.objects.all()
    serializer_class = ProteinSerializer


# POST for ProteinDomain 
class NewProteinDomainDetails(mixins.CreateModelMixin, 
                     mixins.RetrieveModelMixin,
                     mixins.UpdateModelMixin, 
                     mixins.DestroyModelMixin, 
                     generics.GenericAPIView): 
    queryset = ProteinDomain.objects.all()
    serializer_class = ProteinDomainSerializer
    # lookup_field = 'protein_id'

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


#GET for ProteinDomain 
class ProteinDomainDetails(mixins.CreateModelMixin, 
                     mixins.RetrieveModelMixin,
                     mixins.UpdateModelMixin, 
                     mixins.DestroyModelMixin, 
                     generics.GenericAPIView): 
    queryset = ProteinDomain.objects.all()
    serializer_class = ProteinDomainSerializer
    lookup_field = 'protein_id'

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    

    def get(self, request, protein_id):
        proteins = ProteinDomain.objects.filter(proteins_id__protein_id=protein_id)
        serializer = ProteinDomainSerializer(proteins, many=True)
        return Response(serializer.data)
    
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)



#GET method for Pfam 
class PfamList(generics.ListAPIView): 
    queryset = Pfam.objects.all()
    serializer_class= PfamSerializer

class PfamDetails(mixins.CreateModelMixin, 
                     mixins.RetrieveModelMixin,
                     mixins.UpdateModelMixin, 
                     mixins.DestroyModelMixin, 
                     generics.GenericAPIView): 
    queryset = Pfam.objects.all()
    serializer_class = PfamSerializer
    lookup_field = 'domain_id'

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


# Proteins filter by TaxaID 
class ProteinsTaxaID(mixins.CreateModelMixin, 
                     mixins.RetrieveModelMixin,
                     mixins.UpdateModelMixin, 
                     mixins.DestroyModelMixin, 
                     generics.GenericAPIView): 
    queryset = Domains.objects.all()
    serializer_class = DomainIdSerializer
    lookup_field = 'taxa_id'

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
    def get(self, request, taxa_id):
        proteins = Domains.objects.filter(protein_id__taxa_id=taxa_id)
        serializer = DomainIdSerializer(proteins, many=True)
        return Response(serializer.data)

    
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

# Pfam filter by TaxaID 
class PfamsTaxaID(mixins.CreateModelMixin, 
                     mixins.RetrieveModelMixin,
                     mixins.UpdateModelMixin, 
                     mixins.DestroyModelMixin, 
                     generics.GenericAPIView): 
    queryset = Domains.objects.all()
    serializer_class = PfamDomainIdSerializer
    lookup_field = 'taxa_id'

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
    def get(self, request, taxa_id):
        proteins = Domains.objects.filter(protein_id__taxa_id=taxa_id)
        serializer = PfamDomainIdSerializer(proteins, many=True)
        return Response(serializer.data)
    
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

#Coverage 
class CoverageView(mixins.CreateModelMixin,
                mixins.RetrieveModelMixin,
                mixins.UpdateModelMixin,
                mixins.DestroyModelMixin,
                generics.GenericAPIView):
    queryset = Domains.objects.all()
    serializer_class = CoverageSerializer
    lookup_field = "protein_id"

    def get(self, request, protein_id):
        proteins = Domains.objects.filter(protein_id__protein_id=protein_id)
        serializer = CoverageSerializer(proteins, many=True)
        return Response(serializer.data)

