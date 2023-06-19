from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status

from .models import Proposal
from .serializers import ProposalSerializer


class ProposalModelTest(TestCase):
    def setUp(self):
        self.proposal = Proposal.objects.create(
            full_name="John Doe",
            cpf=12345678901,  # CPF deve ser um número inteiro
            address="123 Street, City, State, Country",
            loan_value=10000.0,
        )

    def test_proposal_creation(self):
        self.assertEqual(self.proposal.full_name, "John Doe")
        self.assertEqual(self.proposal.cpf, 12345678901)  # CPF é um número inteiro
        self.assertEqual(self.proposal.address, "123 Street, City, State, Country")
        self.assertEqual(self.proposal.loan_value, 10000.0)


class ProposalAPITest(APITestCase):
    def setUp(self):
        self.proposal = Proposal.objects.create(
            full_name="John Doe",
            cpf=12345678901,  # CPF deve ser um número inteiro
            address="123 Street, City, State, Country",
            loan_value=10000.0,
        )

    def test_get_proposal(self):
        response = self.client.get(
            reverse("proposals:proposal-detail", kwargs={"pk": self.proposal.id})
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, ProposalSerializer(self.proposal).data)

    def test_create_proposal(self):
        proposal_data = {
            "full_name": "Jane Doe",
            "cpf": 12345678902,  # CPF deve ser um número inteiro
            "address": "124 Street, City, State, Country",
            "loan_value": 5000.0,
        }
        response = self.client.post(reverse("proposals:proposal-list"), proposal_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(
            response.data,
            ProposalSerializer(Proposal.objects.get(pk=response.data["id"])).data,
        )
