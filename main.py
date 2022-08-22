class People:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name.lower()

class Man(People):
    def __init__(self, name):
        super().__init__(name)
        self.sex = "m"
    def get_sex(self):
        return self.sex

class Woman(People):
    def get_sex(self):
        return "w"

man = Man("Zaza")
print(man.get_name(), man.get_sex())
