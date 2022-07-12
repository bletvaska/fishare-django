import pytest
from django.urls import reverse


def test_when_homepage_is_requested_then_status_is_200(client):
    url = reverse('files:homepage')
    response = client.get(url)
    assert response.status_code == 200, "Homepage should return 200."


@pytest.mark.django_db
def test_when_file_with_given_slug_is_not_found_then_raise_404(client):
    # arrange
    slug = 'jano'
    url = reverse('files:download_file', args=[slug])

    # act
    response = client.get(url)

    # assert
    assert response.status_code == 404, f"File with slug {slug} doesn't exist."


@pytest.mark.parametrize("word",
                         ['hello', 'World', '123', ''])
def test_when_not_uppercase_word_is_given_then_false(word):
    assert word.isupper() is False
