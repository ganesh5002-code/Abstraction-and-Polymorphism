class BMW:

    def fuel_type(self):
        print("The fuel type of a BMW is premium petrol")
    
    def max_speed(self):
        print("The max_speed of a BMW is 305km/h")

class Ferrari:

    def fuel_type(self):
        print("The fuel type of a Ferrari is premium unleaded gasoline")
    
    def max_speed(self):
        print("The max speed of a Ferrari is 351km/h")

obj_Bmw = BMW()
obj_Ferrari = Ferrari()

for six_seven in (obj_Bmw, obj_Ferrari):
    six_seven.fuel_type()
    six_seven.max_speed()
