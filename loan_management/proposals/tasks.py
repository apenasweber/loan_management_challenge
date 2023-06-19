from celery import shared_task
from .models import Proposal
from .services import evaluate_proposal


@shared_task
def evaluate_proposal_task(proposal_id: int):
    proposal = Proposal.objects.get(id=proposal_id)
    evaluate_proposal(proposal)
