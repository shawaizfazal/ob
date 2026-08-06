class parrot:
    species ="bird"
    def __init__(self,name,age):
        self.name=name
        self.age=age
blu=parrot("blu",10)
woo=parrot("woo",15)
print("blu is a {}".format(blu.species))
print("woo is a {}".format(woo.species))


        