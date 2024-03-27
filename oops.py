# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 08:56:23 2024

@author: VishalRajak
"""

class Car:
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
    
    def display_info(self):
        return f'{self.year} {self.model} {self.year}'
car1 = Car('Toyota','Camry','2022')
print(car1.display_info(),'\n')


#inheritance
class ElectricCar(Car):
    def __init__(self,make,model,year,battery_cap):
        super().__init__(make,model,year)
        self.battery_cap = battery_cap
    #polymorphism, method overriding
    def display_info(self):
        return f'{self.year} {self.make} {self.model} with {self.battery_cap} kWh battery'

electric_car = ElectricCar('Nissan', 'Leaf', 2023, 30)
print(electric_car.display_info())        