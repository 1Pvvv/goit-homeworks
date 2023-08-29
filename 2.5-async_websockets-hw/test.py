from typing import List
from enum import Enum


class Currency(Enum):
    USD: "USD"
    EUR: "EUR"
    CHF: "CHF"
    GBP: "GBP"
    PLZ: "PLZ"
    SEK: "SEK"
    XAU: "XAU"
    CAD: "CAD"

def parse_currency(currency: List[Currency]):

    print(currency)

l = 1, 2, 3, 4

parse_currency(l)
