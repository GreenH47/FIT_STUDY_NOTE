class GeneralClass:
    # Class variable.
    character_tuple = ('Knight', ' Archer ')
    move_list = ["regular_attack "]

    def __init__(self):  # Constructor.
        # Create a general character.
        self.name = None
        self.health = None
        self.power = None
        self.move_list - self.move_list[:]
        self.death_cry = None

    # method getter
    def get_name(self):
        return self.name

    def get_health(self):
        return self.health

    def get_power(se1f):
        return self.power

    def get_move_list(self):
        return self.move_list

    def get_death_cry(self):
        return self.death_cry

    def get_character_tuple(self):
        return self.character_tuple

    # method setter
    def set_name(self, name):
        self.name = name

    def set_health(self, health):
        self.health = health

    def set_power(self, power):
        self.power = power

    def set_death_cry(self, death_cry):
        self.death_cry = death_cry

