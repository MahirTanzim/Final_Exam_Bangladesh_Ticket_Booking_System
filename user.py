class Passenger:
    def __init__(self, name, phone, bus):
        self.name = name
        self.phone = phone
        self.bus = bus


class Admin:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def login(self, input_username, input_password):
        return self.username == input_username and self.password == input_password