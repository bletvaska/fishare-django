import pytest
from django.contrib.auth.models import User
from django.db import IntegrityError
from faker import Faker


@pytest.fixture()
def fake():
    yield Faker()


@pytest.mark.django_db
def test_when_email_is_entered_then_it_should_be_in_email_field(fake):
    # arrange
    email = fake.email()
    username = fake.user_name()
    password = fake.password()

    # act
    user = User.objects.create(username=username, email=email, password=password)

    # assert
    assert user.email == email, "The email used during creation is not the same."


@pytest.mark.django_db
def test_when_two_users_with_same_username_are_created_then_raise_exception(fake):
    # arrange
    email = fake.email()
    username = fake.user_name()
    password = fake.password()

    # act
    User.objects.create(username=username, email=email, password=password)

    with pytest.raises(IntegrityError):
        User.objects.create(username=username, email=email, password=password)
