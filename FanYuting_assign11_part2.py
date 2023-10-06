class Smartphone:
    # construct a new Smartphone
    # smartphones need to keep track of how much space they have left (integer)
    # they also need to keep track of their name (string)
    # smartphones will need some kind of internal system to keep track of all of 
    # the apps that are installed, along with their size. a list or a dictionary
    # would be useful here.
    # when a phone is constructed the 'report' method should be called (see below)
    # this method returns nothing and simply prints the desired output to the user
    def __init__(self, capacity, name):
        self.capacity = capacity
        self.appnames = []
        self.appsizes = []
        self.name = name
        pass

    # add a new app to the smartphone given an appname (string) and an appsize (integer)
    # if any of the following conditions are detected the method should reject the input
    # and print out a message as to why the app cannot be installed:
    # (1) the app is already installed
    # (2) the phone cannot hold any additional apps because the capacity has been reached
    # (3) the app size is negative
    # this method returns nothing and simply prints the desired output to the user
    def add_app(self, appname, appsize):
        if self.has_app(appname):
            print("Cannot add app: already installed\n")
        if appsize < 0:
            print("Cannot add app: size cannot be negative\n")
            return
        elif self.get_available_space() < appsize:
            print("Cannot add app: not enough available space\n")
            return
        self.appnames.append(appname)
        self.appsizes.append(appsize)
        for i in range(len(self.appnames)):
            for j in range(i+1, len(self.appnames)):
                if self.appsizes[i] > self.appsizes[j]:
                    self.appnames[i], self.appnames[j] = self.appnames[j], self.appnames[i]
                    self.appsizes[i], self.appsizes[j] = self.appsizes[j], self.appsizes[i]

        print("App %s was added successfully\n"%appname)
    # removes an app from the phone based on appname (string)
    # if the app is not installed, reject it and print out an error message
    # this method returns nothing and simply prints the desired output to the user
    
    def remove_app(self, appname):
        if not self.has_app(appname):
            print("Cannot remove app: app not currently installed\n")
            return
        for i in range(len(self.appnames)):
            if self.appnames[i] == appname:
                self.appnames.pop(i)
                self.appsizes.pop(i)
                print("App %s was removed successfully\n"%appname)
                return
        
    # resets the phone (removes all apps, gives the phone a name of "Untitled")
    # print out a confirmation message
    
    def reset(self):
        self.appnames = []
        self.appsizes = []
        print("Phone has been reset\n")

    # renames the phone
    # print out a confirmation message
    def rename(self, new_name):
        self.name = new_name
        print("Phone has been renamed\n")

    # checks to see if an app is installed based on appname (string)
    # returns True if the app is installed, False if it is not
    def has_app(self, appname):
        if appname in self.appnames:
            return True
        else:
            return False
    # returns the current space available on the phone (integer)
    def get_available_space(self):
        return self.capacity - sum(self.appsizes)
    # prints a detailed report that describes the following:
    # Name of phone
    # Storage capacity of phone
    # Used space
    # Available space
    # # of apps installed
    # a listing of all apps installed, in alphabetical order, with their sizes
    # this method returns nothing and simply prints the desired output to the user
    def report(self):
        print("Name:", self.name)
        print("Storage capacity: %d GB"%self.capacity)
        print("Used space: %d GB"%sum(self.appsizes))
        print("Available space: %d GB"%self.get_available_space())
        print("Apps installed: %d"%len(self.appnames))
        for i in range(len(self.appnames)):
            print("*", self.appnames[i], "(%d GB)"%self.appsizes[i])
        print("")


if __name__ == "__main__":
    while True:
        capacity = input("Size of your new smartphone (32, 64 or 128 GB): ")
        if not capacity.isdigit():
            print("Invalid size, try again")
        elif int(capacity) not in [32, 64, 128]:
            print("Invalid size, try again")
        else:
            name = input("Smartphone name: ")
            phone = Smartphone(int(capacity), name)
            print("Smartphone name:")
            phone.report()
            break
    while True:
        choice = input("(r)eport, (a)dd app, r(e)move app, re(s)et, re(n)ame or (q)uit: ")
        choice = choice.lower()
        if choice == 'q':
            print("Goodbye!")
            break
        elif choice == 'r':
            phone.report()
        elif choice == 's':
            phone.reset()
        elif choice == 'n':
            name = input("Enter a new name for your phone: ")
            phone.rename(name)
        elif choice == 'e':
            name = input("App name to remove: ")
            phone.remove_app(name)
        elif choice == 'a':
            name = input("App name to add: ")
            size = int(input("App size in GB: "))
            phone.add_app(name, size)