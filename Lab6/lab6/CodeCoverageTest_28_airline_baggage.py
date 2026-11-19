
"""Code coverage tests for airline_baggage.py."""

import pytest

from airline_baggage import baggage_fee, carry_on_ok, check_in_status


# -------------------- BAGGAGE FEE TESTS --------------------

def test_baggage_fee_rejects_unknown_cabin():
    with pytest.raises(ValueError, match="unknown cabin"):
        baggage_fee("first", 10, "domestic", False)


def test_baggage_fee_rejects_negative_weight():
    with pytest.raises(ValueError, match="invalid weight"):
        baggage_fee("economy", -1, "domestic", False)


def test_baggage_fee_within_free_allowance():
    assert baggage_fee("economy", 10, "domestic", False) == 0


def test_member_gets_extra_allowance_in_economy():
    assert baggage_fee("economy", 25, "domestic", True) == 0


def test_business_member_does_not_get_extra_allowance():
    assert baggage_fee("business", 45, "domestic", True) == 100


def test_domestic_excess_uses_domestic_rate():
    assert baggage_fee("economy", 20, "domestic", False) == 100


def test_non_domestic_excess_uses_other_route_rate():
    assert baggage_fee("premium", 30, "international", False) == 225


def test_large_domestic_excess_doubles_rate():
    assert baggage_fee("economy", 40, "domestic", False) == 1000


def test_large_international_excess_adds_surcharge():
    assert baggage_fee("economy", 40, "international", False) == 2500


def test_large_other_route_excess_without_international_surcharge():
    assert baggage_fee("economy", 40, "charter", False) == 2250


# -------------------- CARRY-ON TESTS --------------------

def test_infant_can_carry_two_items():
    assert carry_on_ok(12, 2, True) is True


def test_infant_cannot_carry_more_than_two_items():
    assert carry_on_ok(12, 3, True) is False


def test_non_infant_cannot_exceed_seven_kg():
    assert carry_on_ok(7.1, 1, False) is False


def test_non_infant_can_carry_one_item_within_limit():
    assert carry_on_ok(7, 1, False) is True


def test_non_infant_cannot_carry_more_than_one_item():
    assert carry_on_ok(5, 2, False) is False


# -------------------- CHECK-IN STATUS TESTS --------------------

def test_check_in_open_with_checked_baggage():
    assert check_in_status(60, True, False) == "open"


def test_check_in_open_without_checked_baggage():
    assert check_in_status(45, False, False) == "open"


def test_check_in_open_for_international_flight():
    assert check_in_status(120, False, True) == "open"


def test_check_in_late_with_checked_baggage():
    assert check_in_status(50, True, False) == "late"


def test_check_in_late_without_checked_baggage():
    assert check_in_status(40, False, False) == "late"


def test_check_in_late_for_international_flight():
    assert check_in_status(100, False, True) == "late"


def test_check_in_closed_with_checked_baggage():
    assert check_in_status(44, True, False) == "closed"


def test_check_in_closed_without_checked_baggage():
    assert check_in_status(29, False, False) == "closed"


def test_check_in_closed_for_international_flight():
    assert check_in_status(89, False, True) == "closed"
