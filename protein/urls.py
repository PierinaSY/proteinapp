from django.urls import path
from protein import views
from . import api

urlpatterns = [
    path("", views.home, name="home"),
    path("api/all", api.AllElementsList.as_view()),
    path("api/protein/", api.NewProteinDomainDetails.as_view()),
    path("api/protein/<str:protein_id>", api.ProteinDomainDetails.as_view()),
    path("api/pfam/<str:domain_id>", api.PfamDetails.as_view()),
    path("api/proteins/<str:taxa_id>", api.ProteinsTaxaID.as_view()),
    path("api/pfams/<str:taxa_id>", api.PfamsTaxaID.as_view()),
    path("api/coverage/<str:protein_id>", api.CoverageView.as_view()),
]