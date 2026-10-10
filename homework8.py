from abc import abc, abstractmethod
class smartdevice (abc):
    def show_device ( self, name):
        print ( "Device Name:", name)
    @abstractmethod
    def turn_on (self):
        pass
class smartlight (smartdevice):
    def turn_on (self):
        print ("smart light is on")
class smartfan ( smartdevice ):
    def turn_on ( self ):
        print ("fan is on")
class smartspeaker (smartdevice):
    def turn_on (self):
        print ("speaker is on")
light = smartlight ()
fan = smartfan ()
speaker = smartspeaker ()
light.show_device ("light")
light.turn_on ()
fan.show_device ("fan")
fan.turn_on ()
speaker.show_device ("speaker")
speaker.turn_on ()
class securitycamera :
    def check_status (self ):
        print ("camera is recording")
class doorlock :
    def check_status (self):
        print ("lock is secure")
devices = [ securitycamera (), doorlock () ]
print ("")
print ("smart device")
for device in devices:
print("")