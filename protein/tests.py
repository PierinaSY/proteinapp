from django.test import TestCase
from django.urls import reverse

from .factories import *
from .serializers import *

class CoverageViewTest(TestCase):
    def setUp(self):
        # Create some test data using factory boy and factories
        self.domain1 = Domains(protein_id='Protein1')
        self.domain2 = Domains(protein_id='Protein1')
        self.domain3 = Domains(protein_id='Protein2')

    def test_get_request(self):
        # Send a GET request to the CoverageView API with the protein_id parameter
        response = self.client.get(reverse('coverage', kwargs={'protein_id': 'Protein1'}))

        # Verify that the response has the expected status code
        self.assertEqual(response.status_code, 200)

        # Verify that the response contains the expected data
        self.assertEqual(response.data[0]['id'], self.domain1.id)
        self.assertEqual(response.data[1]['id'], self.domain2.id)
        self.assertEqual(len(response.data), 2)