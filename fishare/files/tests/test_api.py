import pytest
from django.urls import reverse


@pytest.fixture
def api_client():
    from rest_framework.test import APIClient
    yield APIClient()


@pytest.mark.django_db
def test_when_files_list_is_retrieved_then_status_is_200(api_client):
    url = reverse('files:api-collection')
    response = api_client.get(url)
    assert response.status_code == 200, "Should be 200 on HTTP GET."


@pytest.mark.django_db
def test_when_response_is_returned_then_type_of_response_is_json(api_client):
    url = reverse('files:api-collection')
    response = api_client.get(url)
    assert response.headers.get('content-type') == 'application/json', "Response type should be JSON."

