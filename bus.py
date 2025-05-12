class Bus:
    def __init__(self, number, route, total_seats):
        self.number = number
        self.route = route
        self.total_seats = total_seats
        self.booked_seats = 0
        

    def available_seats(self):
        self.unbooked_seats = self.total_seats - self.booked_seats
        return self.unbooked_seats

    def book_seat(self):
        if self.available_seats() > 0:
            self.booked_seats += 1
            return True
        else:
            return False

    def __repr__ (self):
        return f"{self.number:<12} {self.route:<25} {self.total_seats:<12} {self.available_seats():<15}"
