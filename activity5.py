class familymember():
    def __init__(self,eyecolour,height_cm):
        self.eyecolour=eyecolour
        self.height_cm=height_cm
    def show_traits(self):
        print("eyecolour",self.eyecolour)
        print("height_cm",self.height_cm)
class kid (familymember):
    def __init__(self, name, age, height_cm, eyeseight):
        super().__init__(height_cm, eyeseight)
        self.name=name
        self.age=age
    def show_traits(self):
        print("name",self.name)
        print("age",self.age) 
        return super().show_traits()
    def favourite_hobby(self,hobby):
            self.hobby=hobby
            print(self.name,"loves",hobby)
child=kid("maya",10,"brown",140)
child.show_traits()
child.favourite_hobby("painting")
print("is kid subclass of familymember?",issubclass(kid,familymember))
            
        
        