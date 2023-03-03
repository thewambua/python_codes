class Temperature():
    def __init__(self,t):
        self.temperature=t
    def fahrenheit(self):
       print(self.temperature*32)
    def celsius(self):
        print(self.temperature/32)
Newtemperature=Temperature(50)
Newtemperature.fahrenheit()
Newtemperature.celsius()

     