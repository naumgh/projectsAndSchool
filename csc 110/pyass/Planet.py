class Planet:
    def __init__(self, name, place, moons, temp, state):
        self.name = name
        self.place = place
        self.moons = moons
        self.temp = temp
        self.state = state

    def __str__(self):
        return self.name +', planet number #' + str(self.place)

    def __repr__(self):
        return self.name

    def __eq__(self):
        if (self.name == other.get_name()):
            return True
        else:
            return False

    def get_name(self):
        return self.name

    def get_place(self):
        return self.place

    def get_moons(self):
        return self.moons

    def get_temp(self):
        return self.temp

    def get_state(self):
        return self.state

    def inner_planet(self):
        if (self.state == "solid"):
            return True
        else:
            return False
