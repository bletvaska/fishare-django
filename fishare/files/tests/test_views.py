import pytest
from django.urls import reverse


def test_view(client):
    url = reverse('files:homepage')
    response = client.get(url)
    assert response.status_code == 200, "Homepage should return 200."


@pytest.mark.django_db
def test_404(client):
    slug = 'jano'
    url = reverse('files:download_file', args=[slug])
    response = client.get(url)
    assert response.status_code == 404, f"File with slug {slug} doesn't exist."
