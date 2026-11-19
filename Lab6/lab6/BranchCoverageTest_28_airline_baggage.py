
"""Branch coverage tests for airline_baggage.py."""

import pytest

from airline_baggage import baggage_fee, carry_on_ok, check_in_status


# ==========================================================
# 1. BAGGAGE FEE - BRANCH COVERAGE
# ==========================================================

def test_unknown_cabin():
    with pytest.raises(ValueError, match="unknown cabin"):
        baggage_fee("first", 10, "domestic", False)


def test_negative_weight():
    with pytest.raises(ValueError, match="invalid weight"):
        baggage_fee("economy", -1, "domestic", False)


def test_weight_within_free_allowance():
    assert baggage_fee("economy", 10, "domestic", False) == 0


def test_member_extra_allowance():
    assert baggage_fee("economy", 25, "domestic", True) == 0


def test_non_member_without_extra_allowance():
    assert baggage_fee("economy", 20, "domestic", False) == 100


def test_business_member_without_extra_allowance():
    assert baggage_fee("business", 45, "domestic", True) == 100


def test_domestic_normal_excess_fee():
    assert baggage_fee("economy", 20, "domestic", False) == 100


def test_international_normal_excess_fee():
    assert baggage_fee("premium", 30, "international", False) == 225


def test_large_domestic_excess():
    assert baggage_fee("economy", 40, "domestic", False) == 1000


def test_large_international_excess():
    assert baggage_fee("economy", 40, "international", False) == 2500


def test_large_non_international_excess():
    assert baggage_fee("economy", 40, "charter", False) == 2250


# ==========================================================
# 2. CARRY-ON - BRANCH COVERAGE
# ==========================================================

def test_infant_with_two_items():
    assert carry_on_ok(12, 2, True) is True


def test_infant_with_more_than_two_items():
    assert carry_on_ok(12, 3, True) is False


def test_non_infant_weight_above_limit():
    assert carry_on_ok(8, 1, False) is False


def test_non_infant_within_weight_and_item_limit():
    assert carry_on_ok(7, 1, False) is True


def test_non_infant_with_multiple_items():
    assert carry_on_ok(5, 2, False) is False


# ==========================================================
# 3. CHECK-IN STATUS - BRANCH COVERAGE
# ==========================================================

def test_domestic_checkin_open_with_baggage():
    assert check_in_status(60, True, False) == "open"


def test_domestic_checkin_open_without_baggage():
    assert check_in_status(45, False, False) == "open"


def test_domestic_checkin_late_with_baggage():
    assert check_in_status(50, True, False) == "late"


def test_domestic_checkin_late_without_baggage():
    assert check_in_status(40, False, False) == "late"


def test_domestic_checkin_closed_with_baggage():
    assert check_in_status(44, True, False) == "closed"


def test_domestic_checkin_closed_without_baggage():
    assert check_in_status(29, False, False) == "closed"


def test_international_checkin_open():
    assert check_in_status(120, False, True) == "open"


def test_international_checkin_late():
    assert check_in_status(100, False, True) == "late"


def test_international_checkin_closed():
    assert check_in_status(89, False, True) == "closed"
