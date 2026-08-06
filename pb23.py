"""
-oop project : data analyst
"""

class data_analyst:
    def __init__(self,datas):
        self.datas=datas

    def show_datas(self):
        print(f"datas: {self.datas}")

    def total(self):
        total= sum(self.datas)
        print(f"sum:{total} ")

    def average(self):
        average = sum(self.datas)/len(self.datas)
        print(f"average: {average}")

    def minimum(self):
        self.minimum=min(self.datas)
        print(f"min: {self.minimum}")

    def maximum(self):
        self.maximum=max(self.datas)
        print(f"max: {self.maximum}")


analys=data_analyst([4,5,6,7,8,9,12,23])
analys.show_datas()
analys.total()
analys.average()
analys.minimum()
analys.maximum()


    
        
