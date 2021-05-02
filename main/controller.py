from .ENUMS import COFFEE, TEA, JUICE, HOT_WATER, COLD_WATER, SODA, CAPPUCCINO, BIG, MEDIUM, SMALL


# TODO refactor to get prices and modifiers from the database
def set_price_before_vat(drink: str, size: str) -> float:
    modifier = 0
    # setting size modifier
    if size == BIG:
        modifier = 1.15
    elif size == MEDIUM:
        modifier = 1.1
    elif size == SMALL:
        modifier = 1.0
    # setting final price
    if drink == COFFEE:
        return 10 * modifier
    elif drink == TEA:
        return 11 * modifier
    elif drink == JUICE:
        return 12 * modifier
    elif drink == HOT_WATER:
        return 13 * modifier
    elif drink == COLD_WATER:
        return 14 * modifier
    elif drink == SODA:
        return 15 * modifier
    elif drink == CAPPUCCINO:
        return 16 * modifier
