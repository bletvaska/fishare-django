import pytest
from django.urls import reverse


@pytest.fixture
def api_client():
    from rest_framework.test import APIClient
    yield APIClient()


@pytest.fixture()
def response(api_client):
    url = reverse('files:api-collection')
    response = api_client.get(url)
    yield response


@pytest.mark.django_db
def test_when_files_list_is_retrieved_then_status_is_200(response):
    assert response.status_code == 200, "Should be 200 on HTTP GET."


@pytest.mark.django_db
def test_when_response_is_returned_then_type_of_response_is_json(response):
    assert response.headers.get('content-type') == 'application/json', "Response type should be JSON."


@pytest.mark.django_db
@pytest.mark.parametrize("key", ['count', 'next', 'previous', 'results'])
def test_when_response_is_returned_then_specific_keys_should_be_specific(key, response):
    assert key in response.json()
