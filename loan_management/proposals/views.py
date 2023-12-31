from rest_framework import viewsets
from .models import Proposal
from .serializers import ProposalSerializer
from .tasks import evaluate_proposal_task
from .services import evaluate_proposal

from django.shortcuts import render


def proposal_form_view(request):
    return render(request, "proposal_form.html")


class ProposalViewSet(viewsets.ModelViewSet):
    queryset = Proposal.objects.all()
    serializer_class = ProposalSerializer

    def perform_create(self, serializer):
        proposal = serializer.save()
        evaluate_proposal(proposal)
        evaluate_proposal_task.delay(proposal.id)
