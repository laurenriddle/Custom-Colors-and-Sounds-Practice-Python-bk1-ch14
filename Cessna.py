from vehicle import Vehicle
# Electric car


class Cessna(Vehicle):
    def __init__(self, main_color, maximum_occupancy):
        super().__init__(main_color, maximum_occupancy)
        self.battery_kwh = 0
    def drive(self):
        print(f"The {self.main_color} Cessna drives past.")
    def stop(self):
        print("The white Cessna rolls to a stop after rolling a mile down the runway.")
    def turn(self, direction):
        print("Turn upward!")
