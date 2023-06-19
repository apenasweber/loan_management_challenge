from .models import Proposal


def evaluate_proposal(proposal: Proposal):
    # Assign status based on the ID of the proposal
    proposal.status = "A" if proposal.id % 2 == 0 else "R"
    proposal.save()
