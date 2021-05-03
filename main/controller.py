from .ENUMS import COFFEE, TEA, JUICE, HOT_WATER, COLD_WATER, SODA, CAPPUCCINO, BIG, MEDIUM, SMALL


# TODO refactor to get prices and modifiers from the database
def get_price_with_vat(price: float, vat: float):
    return price * (1 + (vat / 100))
