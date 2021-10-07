class Road:
    def attribute (self, lenght, wigth):
        self._lenght = lenght
        self._wigth = wight
    def full_profit (self,weight=25, thickness = 5):
        return f"{self._lenght} * {self._wigth} * {wigth} * {thickness} = " 
             f"{(self._lenght * self._wigth * wigth * thickness)/1000}"
    road_one = Road (5000, 20)
    print (road_one.full_profit)