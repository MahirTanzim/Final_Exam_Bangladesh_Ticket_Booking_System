from bus import Bus
from bussystem import BusSystem
from user import Admin, Passenger


def admin_menu(bdticket):
    while True:
        print("\n--- Admin Menu ---")
        print("1. Add Bus")
        print("2. View All Buses")
        print("3. Logout")

        choice = input("Enter your choice: ")
        if choice == '1':
            number = input("Enter bus number: ")
            route = input("Enter bus route: ")
            seats = int(input("Enter total seats: "))
            bdticket.add_bus(number, route, seats)
        
        elif choice == '2':
            bdticket.show_buses()
        elif choice == '3':
            print("Logged out from admin.")
            break
        else:
            print("Invalid choice. Try again.")

def user_menu(bdticket):
    while True:
        print("\n===== Bangladesh Bus Ticket Booking System =====")
        print("1. Admin Login")
        print("2. Book Ticket")
        print("3. View Buses")
        print("4. Exit")

        choice = input("Enter your choice: ")
        if choice == '1':
            username = input("Enter username: ")
            password = input("Enter password: ")
            if bdticket.admin.login(username, password):
                print("Admin login successful.")
                admin_menu(bdticket)
            else:
                print("Invalid Username or passward. Please Try again...")
        elif choice == '2':
            bus_number = input("Enter bus number: ")
            name = input("Enter your name: ")
            phone = input("Enter your phone number: ")
            bdticket.book_ticket(bus_number, name, phone)
        elif choice == '3':
            bdticket.show_buses()
        elif choice == '4':
            print("Exiting the system. Thank you!")
            break
        else:
            print("Invalid choice. Please try again.")

bdticket = BusSystem()
user_menu(bdticket)