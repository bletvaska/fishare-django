import pytest
from django.contrib.auth.models import User
from django.db import IntegrityError
from faker import Faker


@pytest.fixture()
def fake():
    yield Faker()


@pytest.fixture()
def user(fake):
    email = fake.email()
    username = fake.user_name()
    password = fake.password()

    yield username, email, password


@pytest.mark.django_db
def test_when_email_is_entered_then_it_should_be_in_email_field(user):
    # act
    u = User.objects.create(username=user[0], email=user[1], password=user[2])

    # assert
    assert u.email == user[1], "The email used during creation is not the same."


@pytest.mark.django_db
def test_when_two_users_with_same_username_are_created_then_raise_exception(user):
    # act
    User.objects.create(username=user[0], email=user[1], password=user[2])

    # assert
    with pytest.raises(IntegrityError):
        User.objects.create(username=user[0], email=user[1], password=user[2])


@pytest.mark.django_db
def test_when_username_is_none_then_raise_integrityerror_exception(user):
    with pytest.raises(IntegrityError):
        User.objects.create(username=None)
