
class PayrollDeduction:

    def __init__(self, de, da, ch, ei):
        
        self.__description = de
        self.__date = da
        self.__charge = ch
        self.__empid = ei 
        self.__total = 0

    def get_description(self):
        return self.__description

    def get_date(self):
        return self.__date

    def get_charge(self):
        return self.__charge

    def get_empid(self):
        return self.__empid

    def get_total_charge(self, charge2, charge4, charge5):
        self.__total = charge2 + charge4 + charge5
        return self.__total