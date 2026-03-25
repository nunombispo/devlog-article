# entries/tests.py
import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Entry


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def sample_entry(db):
    return Entry.objects.create(
        title="First deployment",
        body="Shipped the initial version of DevLog."
    )


@pytest.mark.django_db
def test_list_entries_empty(api_client):
    url = reverse("entry-list")
    response = api_client.get(url)

    assert response.status_code == status.HTTP_200_OK
    assert response.data["results"] == []


@pytest.mark.django_db
def test_list_entries_returns_existing(api_client, sample_entry):
    url = reverse("entry-list")
    response = api_client.get(url)

    assert response.status_code == status.HTTP_200_OK
    assert response.data["results"][0]["title"] == "First deployment"


@pytest.mark.django_db
def test_create_entry(api_client):
    url = reverse("entry-list")
    payload = {
        "title": "Second deployment",
        "body": "Added pagination to the entries endpoint."
    }
    response = api_client.post(url, payload, format="json")

    assert response.status_code == status.HTTP_201_CREATED
    assert Entry.objects.count() == 1
    assert response.data["title"] == "Second deployment"