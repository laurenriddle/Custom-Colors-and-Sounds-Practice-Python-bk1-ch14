from Zero import Zero
from Tesla import Tesla
from Cessna import Cessna
from Jeep import Jeep
from Versa import Versa
'''
    1. Define 5 of your favorite vehicles
    2. Move all common properties in your vehicles to a new Vehicle class.
    3. Create an instance of each vehicle.
    4. Define a different value for each vehicle's properties.
    5. Create a drive() method in the Vehicle class.
    6. Override the drive() method in all the other vehicle classes. Include the vehicle's color in the message (i.e. "The blue Ram drives past. RRrrrrrummbbble!").
    7. Create a turn(self, direction) method, and a stop(self) method on Vehicle. Define a basic implementation of each.
    8. Override all three of those methods on some of the vehicles. For example, the stop() method for a plane would be to output the message "The white Cessna rolls to a stop after rolling a mile down the runway."
    9. Make your vehicle instances perform all three behaviors.
'''

fxs = Zero("black", "9")
modelS = Tesla("black", "9")
mx410 = Cessna("black", "9")
V2012 = Versa("black", "9")
jeep = Jeep("black", "9")


fxs.battery_kwh = 9
fxs.main_color = "Black"
fxs.maximum_occupancy = 20
modelS.battery_kwh = 9
modelS.main_color = "Purple"
modelS.maximum_occupancy = 2
mx410.battery_kwh = 9
mx410.main_color = "Blue"
mx410.maximum_occupancy = 4
V2012.battery_kwh = 9
V2012.main_color = "Yellow"
V2012.maximum_occupancy = 5
jeep.battery_kwh = 9
jeep.main_color = "Red"
jeep.maximum_occupancy = 6

fxs.drive()
modelS.drive()
mx410.drive()
V2012.drive()
jeep.drive()

fxs.turn("Right")
modelS.turn("Left")
mx410.turn("Right")
V2012.turn("Left")
jeep.turn("Right")

fxs.stop()
modelS.stop()
mx410.stop()
V2012.stop()
jeep.stop()



