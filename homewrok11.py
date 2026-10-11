class vehicle:
    def __init__(self, company, max_speed):
        self.brand = company
        self.max_speed = max_speed
    def show_details(self):
        print("company:", self.company)
        print("max speed:", self.max_speed,"km/h")
class car(vehicle):
    def __init__(self, model, seats,company, max_speed):
        self.model = model
        self.seats = seats
        super().__init__(company, max_speed)
    def show_details(self):
        print("Model:", self.model)
        print("Seats:", self.seats)
        super().show_details()
    def fuel_type(self, fuel):
        print(self.model, "uses", fuel)
my_car = car("santa fe", 7, "hyundai", 350)
my_car.show_details()
my_car.fuel_type("petrol")
print("is the car a subclass of vehicle?", issubclass(car, vehicle))