class India:

    def capital(self):
        print("New Dehli is the capital of India")
    def main_language(self):
        print("The main language in India is Hindi")
    def type(self):
        print("India is a democratic country")

class Australia:

    def capital(self):
        print("The capital of Australia is Canberra")
    def main_language(self):
        print("The main language in Australia is English")
    def type(self):
        print("Australia is a democratic country")

obj_India = India()
obj_Aus = Australia()

for i in (obj_India, obj_Aus):
    i.capital()
    i.main_language()
    i.type()