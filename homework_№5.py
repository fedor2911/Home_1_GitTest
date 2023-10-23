class KgToPounds:
    def __init__(self, kg):
        self.__kg = kg

    @property
    def to_pounds (self):
        return self.__kg * 2.205

    # def set_kg(self, new_kg):
    #     if isinstance (new_kg, (int, float)):
    #         self.__kg = new_kg
    #     else:
    #         print('Килограммы задаются только числами')


    # def get_kg(self):
    #     return self.__kg


    def display_info(self):
        print(f"Имя: {self.__kg}")

