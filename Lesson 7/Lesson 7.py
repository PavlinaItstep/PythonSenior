class Human:
    def __init__(self,name):
        self.name = name

class Auto:
    def __init__(self,brand):
        self.brand = brand
        self.passengers = []
    
    def add_passenger(self,human):
        self.passengers.append(human)

    def print_passengers(self):
        if self.passengers != []:
            print(f"Name of {self.brand} passengers:")
            for i in self.passengers:
                print(i.name)
        else:
            print(f"There are no passenger in {self.brand}")

nick = Human("Nick")
kate = Human("Kate")

car = Auto("Mercedes")
car.add_passenger(nick)
car.add_passenger(kate)
car.print_passengers()



