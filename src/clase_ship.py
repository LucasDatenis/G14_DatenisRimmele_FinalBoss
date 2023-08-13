class Ship(object):
    cant_ship = 0
    def __init__(self, draft, crew):
        self.draft = draft
        self.crew = crew
        Ship.cant_ship = Ship.cant_ship+1
        print("Se creo el barco")

    def is_worth_it(self):
        worthit = self.draft - self.crew * 1.5
        return worthit
