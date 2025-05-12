from bus import Bus
from user import Admin, Passenger

class BusSystem:
    def __init__(self):
        self.buses = []
        self.passengers = []
        self.admin = Admin("admin", "1234")

    def add_bus(self, number, route, seats):
        for bus in self.buses:
            if bus.number == number:
                print(f"Bus with number {number} already exists.")
                return
        new_bus = Bus(number, route, seats)
        self.buses.append(new_bus)
        print(f"Bus no: {number} for route {route} with {seats} added successfully.")

    def show_buses(self):
        if not self.buses:
            print("No buses available.")
        else:
            print("\n{:<12} {:<25} {:<12} {:<15}".format("Bus Number", "Route", "Total Seats", "Available Seats"))
            print("-" * 70)
            for bus in self.buses:
                print(bus)

    def find_bus(self, number):
        for bus in self.buses:
            if bus.number == number:
                return bus
        return None

    def book_ticket(self, bus_number, name, phone):
        bus = self.find_bus(bus_number)
        if bus:
            if bus.book_seat():
                passenger = Passenger(name, phone, bus)
                self.passengers.append(passenger)
                print("Ticket booked successfully!")
                print(f"Passenger: {name}, Phone: {phone}, Fare: 500 Taka")
            else:
                print("Sorry, no seats available on this bus.")
        else:
            print("Bus not found.")