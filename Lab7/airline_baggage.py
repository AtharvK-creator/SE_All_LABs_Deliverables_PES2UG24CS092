"""Airline baggage helper functions used for Lab 7 fuzz testing."""

import math


def parse_booking(code):
    """Parse a booking code in AIRLINE-FLIGHT-SEAT format.

    Example: AI-203-12A -> ("AI", 203, "A")
    Invalid input raises ValueError with a readable message.
    """
    if not isinstance(code, str):
        raise ValueError("Booking code must be a string.")

    parts = code.split("-")
    if len(parts) != 3:
        raise ValueError(
            "Booking code must contain exactly three parts separated by '-'."
        )

    airline, flight, seat = (part.strip() for part in parts)

    if not airline or not flight or not seat:
        raise ValueError(
            "Airline, flight number and seat must not be empty."
        )

    try:
        flight_number = int(flight)
    except ValueError as exc:
        raise ValueError("Flight number must be an integer.") from exc

    return airline.upper(), flight_number, seat[-1].upper()


def total_weight(weights_csv):
    """Return the sum of comma-separated baggage weights in kilograms."""

    if not isinstance(weights_csv, str):
        raise ValueError(
            "Baggage weights must be supplied as a CSV string."
        )

    fields = weights_csv.split(",")

    if not fields or any(not field.strip() for field in fields):
        raise ValueError("Enter one or more comma-separated weights.")

    try:
        weights = [float(field.strip()) for field in fields]
    except ValueError as exc:
        raise ValueError(
            "Every baggage weight must be numeric."
        ) from exc

    if any(not math.isfinite(weight) or weight < 0 for weight in weights):
        raise ValueError(
            "Weights must be finite, non-negative numbers."
        )

    return sum(weights)


def tag_label(name):
    """Create a baggage tag using the first initial and second name."""

    if not isinstance(name, str):
        raise ValueError("Passenger name must be a string.")

    parts = name.split()

    if len(parts) < 2:
        raise ValueError(
            "Enter at least a first name and a last name."
        )

    return parts[0][0].upper() + ". " + parts[1].upper()


def main():
    print("==== Running parse_booking ====")

    user_input = input(
        "Enter a booking code (e.g. AI-203-12A): "
    )

    try:
        result = parse_booking(user_input)
        print("Airline, Flight and Seat Letter:", result)
    except ValueError as error:
        print("Invalid booking code:", error)

    print("\n==== Running total_weight ====")

    user_input = input(
        "Enter bag weights in kg as CSV (e.g. 12.5,7,23): "
    )

    try:
        result = total_weight(user_input)
        print("Total Weight:", result)
    except ValueError as error:
        print("Invalid baggage weights:", error)

    print("\n==== Running tag_label ====")

    user_input = input(
        "Enter a passenger name (first and last): "
    )

    try:
        result = tag_label(user_input)
        print("Tag Label:", result)
    except ValueError as error:
        print("Invalid passenger name:", error)


if __name__ == "__main__":
    main()