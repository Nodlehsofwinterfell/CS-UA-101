import random
class Gumball_Machine:
    def __init__(self, capacity = 0):
        self.capacity = capacity
        self.money = 0
        self.gumballs = []
        gumball_types = ['red', 'green', 'blue']
        self.gumballs = [gumball_types[random.randint(0,2)] for _ in range(self.capacity)]
        print("Gumball Machine created with %d random gumballs\n"%self.capacity)
        pass
    def report(self):
        print("Gumball Machine Report:")
        print("* Gumballs in machine:", self.capacity)
        print("* Money in machine: $%.2f\n"%self.money)
    def dispense(self, coin):
        if coin != 0.25:
            print("Invalid coin, no gumball will be dispensed\n")
        elif self.capacity == 0:
            print("Machine is empty, no gumball will be dispensed\n")
        else:
            self.money += coin
            self.capacity -= 1
            print("Accepting 0.25; Dispensing a %s gumball\n"%(self.gumballs[0]))
            self.gumballs.pop(0)

        pass
    def count_gumballs_by_type(self, type):
        num = sum([1 if self.gumballs[i] == type else 0 for i in range(self.capacity)])
        print("There are %d gumballs of type %s in the machine\n"%(num, type))



# TESTER CODE
machine = Gumball_Machine(5)
machine.report()
machine.count_gumballs_by_type("red")
machine.count_gumballs_by_type("green")
machine.count_gumballs_by_type("blue")
machine.dispense(0.10)
machine.dispense(0.50)
machine.dispense(0.01)
machine.report()
machine.count_gumballs_by_type("red")
machine.count_gumballs_by_type("green")
machine.count_gumballs_by_type("blue")
machine.dispense(0.25)
machine.dispense(0.25)
machine.dispense(0.25)
machine.report()
machine.count_gumballs_by_type("red")
machine.count_gumballs_by_type("green")
machine.count_gumballs_by_type("blue")
machine.dispense(0.25)
machine.dispense(0.25)
machine.dispense(0.25)
machine.report()
machine.count_gumballs_by_type("red")
machine.count_gumballs_by_type("green")
machine.count_gumballs_by_type("blue")