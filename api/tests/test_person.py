from django.test import TestCase
from ..models import Person, Role
from faker import Factory

faker = Factory.create()

# Create your tests here.
class PersonTest(TestCase):
    """ Test module for Person """

    def setUp(self):
        role = Role.objects.create(name="Customer", role_alias="customer")

        Person.objects.create(
            name="chriscupas",
            role=role,
            email="chriscupas@outlook.com",
            address="test address",
            status=1,
        )

    def test_person_email(self):
        person = Person.objects.get(email="chriscupas@outlook.com")

        self.assertEqual(person.get_email(), "chriscupas@outlook.com")

    def test_list_persons(self):
        response = self.client.get("http://127.0.0.1:8000/Persons/")
        self.assertEqual(response.status_code, 200)

    def test_create_person(self):
        role = Role.objects.create(name=faker.name(), role_alias=faker.name())

        person = Person.objects.create(
            name=faker.name(),
            role=role,
            email=faker.email(),
            address=faker.street_address(),
            status=1,
        )

        self.assertEqual(person.id, 2)
