import unittest

from booking import calculate_ticket_price, lock_seats


class TestMovieTicketBooking(unittest.TestCase):
    def test_calculate_ticket_price(self):
        self.assertEqual(calculate_ticket_price(2, 150), 300)

    def test_zero_tickets_raise_error(self):
        with self.assertRaises(ValueError):
            calculate_ticket_price(0)

    def test_lock_available_seats(self):
        available = ["A1", "A2", "A3"]
        self.assertTrue(lock_seats(available, ["A1", "A2"]))
        self.assertEqual(available, ["A3"])

    def test_unavailable_seat_is_not_locked(self):
        available = ["A1", "A2"]
        self.assertFalse(lock_seats(available, ["A3"]))
        self.assertEqual(available, ["A1", "A2"])


if __name__ == "__main__":
    unittest.main()
