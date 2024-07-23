class TeisyokuBaseClass:
    def __init__(self):
        self.main = ""
        self.sub = "白ごはん"
        self.soup = "味噌汁"
    
    def show(self):
        print(self.main)
        print(self.sub)
        print(self.soup)
        print("")

    def clone(self):
        teisyoku_base = TeisyokuBaseClass()
        teisyoku_base.main = self.main
        teisyoku_base.sub = self.sub
        teisyoku_base.soup = self.soup
        return teisyoku_base

teisyoku_base = TeisyokuBaseClass()

karaage_teisyoku = teisyoku_base.clone()
karaage_teisyoku.main = "唐揚げ"

sukiyaki_teisyoku = teisyoku_base.clone()
sukiyaki_teisyoku.main = "すき焼き"

karaage_teisyoku.show()
sukiyaki_teisyoku.show()
