from django.test import TestCase
from ..models import Role

# Create your tests here.
class RoleTest(TestCase):
    """ Test module for Role """

    def setUp(self):
        Role.objects.create(name="Customer", role_alias="customer")
        Role.objects.create(name="Sales Person", role_alias="sales_person")

    def test_role_alias(self):
        customer = Role.objects.get(role_alias="customer")
        salesperson = Role.objects.get(role_alias="sales_person")

        self.assertEqual(customer.get_alias(), "customer")
        self.assertEqual(salesperson.get_alias(), "sales_person")
