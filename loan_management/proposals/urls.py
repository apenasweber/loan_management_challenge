from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProposalViewSet, proposal_form_view

router = DefaultRouter()
router.register(r"proposta", ProposalViewSet, basename="proposal")

app_name = "proposals"

urlpatterns = [
    path("", proposal_form_view, name="proposal_form"),
    path("api/", include(router.urls)),
]
