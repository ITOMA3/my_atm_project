# Create your tests here.
import pytest
from django.test import TestCase
from atm.models import Account

class AccountModelTest(TestCase):
    def test_account_creation(self):
        account = Account.objects.create(account_number="1234567890",balance=100000)
        self.assertEqual(account.account_number,"1234567890")
        self.assertEqual(account.balance, 100000)