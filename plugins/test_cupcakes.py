#!/usr/bin/env python3
from unittest import TestCase

from beancount import loader
from beancount.core.amount import Amount
from beancount.core.number import Decimal


class TestCupcakesPlugin(TestCase):
    def setUp(self):
        self.example_beancount_file = """
option "title" "Example Beancount file"
option "operating_currency" "USD"

plugin "beancount.plugins.auto_accounts"
plugin "plugins.cupcakes" "Assets:Cash,Expenses:Food:Groceries,1"


1792-01-01 commodity USD
  export: "CASH"
  name: "US Dollar"


2019-03-02 * "Opening cash balance"
    Equity:Opening-Balances                         -100.00 USD
    Assets:Cash
""".strip()
        entries, errors, options = loader.load_string(self.example_beancount_file)
        self.entries = entries
        self.errors = errors
        self.options = options

    def test_add_cupcake_purchase_adds_transaction_to_entries(self):
        self.assertEqual(5, len(self.entries))

    def test_add_cupcake_purchase_transaction_has_two_postings(self):
        cupcake_transaction = self.entries[4]

        self.assertEqual(2, len(cupcake_transaction.postings))

    def test_add_cupcake_purchase_transaction_first_posting_subtracts_from_first_account(self):
        cupcake_transaction = self.entries[4]
        first_posting = cupcake_transaction.postings[0]

        self.assertEqual("Assets:Cash", first_posting.account)
        self.assertEqual(first_posting.units, Amount(number=Decimal(-1), currency="USD"))

    def test_add_cupcake_purchase_transaction_second_posting_adds_to_second_account(self):
        cupcake_transaction = self.entries[4]
        second_posting = cupcake_transaction.postings[1]

        self.assertEqual("Expenses:Food:Groceries", second_posting.account)
        self.assertEqual(second_posting.units, Amount(number=Decimal(1), currency="USD"))
