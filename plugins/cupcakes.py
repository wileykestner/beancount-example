from datetime import date
from typing import Dict, Any, Optional, Collection

from beancount.core import flags

__plugins__ = ("cupcakes",)

from beancount.core.amount import Amount
from beancount.core.data import Account, Posting, Currency, Transaction
from beancount.core.number import Decimal


def cupcakes(entries, option_map, configuration_string):
    errors = tuple()

    first_account, second_account, amount_string = configuration_string.strip().split(",")

    assets_leg = _get_posting(account=first_account, units="-{}".format(amount_string), currency="USD")
    expenses_leg = _get_posting(account=second_account, units=amount_string, currency="USD")
    postings = (assets_leg, expenses_leg)
    transaction = _get_transaction(transaction_date=date.today(), postings=postings, narration="Bought a cupcake")
    updated_entries = entries + [transaction]

    return updated_entries, errors


def _get_transaction(transaction_date: date,
                     postings: Collection[Posting],
                     narration: str,
                     lineno: Optional[int] = -1,
                     meta: Optional[Dict[str, Any]] = None) -> Transaction:
    meta = meta if meta else {}
    if not meta.get("lineno", None):
        meta["lineno"] = lineno

    return Transaction(date=transaction_date,
                       meta=meta,
                       postings=postings,
                       flag=flags.FLAG_OKAY,
                       payee=None,
                       narration=narration,
                       tags=frozenset(),
                       links=frozenset())


def _get_posting(account: str, units: str, currency: str, meta: Optional[Dict[str, Any]] = None):
    meta = meta if meta else {}

    return Posting(account=Account(account),
                   units=Amount(number=Decimal(units), currency=Currency(currency)),
                   cost=None,
                   price=None,
                   flag=None,
                   meta=meta)
