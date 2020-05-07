class Character:
    def __init__(self, name, **kwargs):
        self.name = name

        for key, value in kwargs.items():
            setattr(self, key, value)

class Assassin(Character):
    sneaky = True

    def __init__(self, name, sneaky = True, **kwargs):
        super().__init__(name, **kwargs)
        self.sneaky = sneaky


    # sneaky=True means that if a value for sneaky is not provided as an argument, then this will be the default value. (True)
    #self refers to the instance of the class. so self.name = name is assigning that the variable 'name' to the instance's 'name' characteristic
    # def __init__(self, name, sneaky=True, **kwargs):
    #     self.name = name
    #     self.sneaky = sneaky
#^^^ having this innitialized strcuture for methods allowed it to be more flexible, you're not limited to a certain # of arguments.
        # for key, value in kwargs.items():
        #     setattr(self, key, value)

    def murder(self):
        return self.sneaky and str("Let's Kill.")

    def hide(self, light_level):
        return self.sneaky and light_level < 10