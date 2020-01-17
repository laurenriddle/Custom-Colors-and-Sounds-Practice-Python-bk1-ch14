from vehicle import Vehicle
# Electric car

class Tesla(Vehicle):
    def __init__(self, main_color, maximum_occupancy):
        super().__init__(main_color, maximum_occupancy)
        self.battery_kwh = 0
    def drive(self):
        print(f"The {self.main_color} Tesla drives past.")