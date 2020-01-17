class Vehicle:
    def __init__(self, main_color, maximum_occupancy):
        self.main_color = ""
        self.maximum_occupancy = ""

    def drive(self):
        print("Vroooom!")

    def turn(self, direction):
        print(f"Turn {direction}!")
    def stop(self):
        print(f"STOP!")