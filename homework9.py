class account :
    def __init__ (self , owner , pin) :
        self . owner = owner
        self . __pin = pin
    def show_pin_status (self) :
        print ( "account owner:" , self . owner)
        print ("pin is safely stored inside the class")
    def set_pin (self , new_pin) :
        if len (new_pin) == 4 and new_pin . isdigit () :
            self . __pin = new_pin
            print ("updated")
        else :
            print ("incorrect it should be 4 digits")
    def check_pin ( self , entered_pin ) :
        if entered_pin == self . __pin :
            print ("accepted")
        else :
            print ("denied")
    def __str__ ( self ) :
        return "account holder: " + self . owner
my_account = account ("shawaiz" , "1405")
print ( my_account )
my_account.how_pin_status ( )
my_account . __pin = "9999"
print ("trying changing pin")
my_account.check_pin ("7623")
my_account.check_pin ("2244")
my_account.set_pin ("0986")
my_account.check_pin ("6754")