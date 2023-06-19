from rest_framework import serializers
from .models import Proposal


class ProposalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proposal
        fields = ["id", "full_name", "cpf", "address", "loan_value", "status"]
