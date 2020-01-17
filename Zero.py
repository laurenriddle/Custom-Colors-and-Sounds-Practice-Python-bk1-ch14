from vehicle import Vehicle
# Electric car

class Zero(Vehicle):
    def __init__(self):
        self.battery_kwh = 0
    def drive(self):
        print("Zoooooooooooom!")