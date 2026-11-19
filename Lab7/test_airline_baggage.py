"""Property-based and fuzz tests for the airline baggage module."""

import math
import string

import pytest
from hypothesis import given, strategies as st

from airline_baggage import parse_booking, total_weight, tag_label


# Fuzz tests: arbitrary strings and None should either be handled
# or rejected cleanly with ValueError.

@given(st.text() | st.none())
def test_parse_booking_no_crash(value):
    try:
        result = parse_booking(value)
    except ValueError:
        return

    assert isinstance(result, tuple)
    assert len(result) == 3
    assert isinstance(result[0], str)
    assert isinstance(result[1], int)
    assert isinstance(result[2], str)
    assert len(result[2]) == 1


@given(st.text() | st.none())
def test_total_weight_no_crash(value):
    try:
        result = total_weight(value)
    except ValueError:
        return

    assert isinstance(result, float)
    assert math.isfinite(result)
    assert result >= 0


@given(st.text() | st.none())
def test_tag_label_no_crash(value):
    try:
        result = tag_label(value)
    except ValueError:
        return

    assert isinstance(result, str)
    assert len(result) >= 4
    assert result[1:3] == ". "


# Valid-input properties: generated inputs must preserve the function rules.

@given(
    airline=st.text(
        alphabet=string.ascii_letters,
        min_size=1,
        max_size=3
    ),
    flight=st.integers(min_value=0, max_value=99999),
    row=st.integers(min_value=1, max_value=99),
    seat_letter=st.sampled_from(list(string.ascii_letters)),
)
def test_parse_booking_valid_codes(
    airline, flight, row, seat_letter
):
    code = f"{airline}-{flight}-{row}{seat_letter}"

    assert parse_booking(code) == (
        airline.upper(),
        flight,
        seat_letter.upper()
    )


@given(
    weights=st.lists(
        st.floats(
            min_value=0,
            max_value=1000,
            allow_nan=False,
            allow_infinity=False
        ),
        min_size=1,
        max_size=15
    )
)
def test_total_weight_adds_valid_weights(weights):
    csv_value = ",".join(str(weight) for weight in weights)

    assert total_weight(csv_value) == pytest.approx(sum(weights))


@given(
    first=st.text(
        alphabet=string.ascii_letters,
        min_size=1,
        max_size=15
    ),
    last=st.text(
        alphabet=string.ascii_letters,
        min_size=1,
        max_size=15
    ),
)
def test_tag_label_uses_first_initial_and_second_name(first, last):
    assert tag_label(f"{first} {last}") == (
        f"{first[0].upper()}. {last.upper()}"
    )


# Known invalid inputs should be rejected consistently.

@pytest.mark.parametrize(
    "value",
    [
        None,
        "",
        "AI-ABC-12A",
        "AI-203",
        "AI-203-",
        "AI-203-12A-extra"
    ]
)
def test_parse_booking_rejects_invalid_values(value):
    with pytest.raises(ValueError):
        parse_booking(value)


@pytest.mark.parametrize(
    "value",
    [
        None,
        "",
        "1,,2",
        "abc",
        "nan",
        "inf",
        "-1"
    ]
)
def test_total_weight_rejects_invalid_values(value):
    with pytest.raises(ValueError):
        total_weight(value)


@pytest.mark.parametrize(
    "value",
    [
        None,
        "",
        "SingleName",
        "   "
    ]
)
def test_tag_label_rejects_invalid_values(value):
    with pytest.raises(ValueError):
        tag_label(value)


# Basic sample tests.

def test_sample_booking():
    assert parse_booking("AI-203-12A") == (
        "AI", 203, "A"
    )


def test_sample_total_weight():
    assert total_weight("12.5,7,23") == pytest.approx(42.5)


def test_sample_tag_label():
    assert tag_label("John Doe") == "J. DOE"