def calculate_ticket_price(number_of_tickets, price_per_ticket=150):
    """Return the total price for a positive number of tickets."""
    if number_of_tickets <= 0:
        raise ValueError("Number of tickets must be greater than zero.")
    if price_per_ticket < 0:
        raise ValueError("Ticket price cannot be negative.")
    return number_of_tickets * price_per_ticket


def lock_seats(seats_available, requested_seats):
    """Temporarily reserve seats if all requested seats are available."""
    if not requested_seats:
        raise ValueError("Select at least one seat.")
    if len(set(requested_seats)) != len(requested_seats):
        raise ValueError("Duplicate seats are not allowed.")
    if any(seat not in seats_available for seat in requested_seats):
        return False
    for seat in requested_seats:
        seats_available.remove(seat)
    return True
