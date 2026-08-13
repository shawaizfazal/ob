class myclass:
    __private=21
    def __privMeth(self):
        print("i`m inside the classroom")
    def hello (self):
        print("private variable",myclass.__private)
foo=myclass()
foo.hello()

