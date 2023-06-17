from django.conf import settings
from captus_shopi.settings.base import CARRO_SESSION_ID


class Car:
    def __init__(self,request):
        self.request = request
        self.session = request.session
        car = self.session.get(settings.CARRO_SESSION_ID)
        if not car:
            car = self.session[settings.CARRO_SESSION_ID]={}
        self.car=car
        
        
    def add(self,request, plant):
        if str(plant.id) not in self.carro.keys():
            self.car[plant.id] = {
                "plant_id":plant.id,
                "plant_name":plant.name,
                "quantity": 1,
                "cost": plant.cost * self.car[plant.id]["quantity"],
                "image":plant.image.url,
            }
        else:
            for key, value in self.car.items():
                if key == str(plant.id):
                    value["quantity"] = value["quantity"]+1
                    break
        self.save()
        
        
        
    def save(self):
        self.session["car"] = self.car
        self.session.modified = True
        
        
    def remove(self,plant):
        plant_id = str(plant.id)
        if plant_id in self.car:
            del self.car[plant_id]
            self.save()
            
    def decrement(self,plant):
        for key, value in self.car.items():
            if key == str(plant.id):
                value["quantity"] = value["quantity"]-1
                if value["quantity"] < 1:
                    self.remove(plant)
                else:
                    self.save()
                break
            else:
                print('El producto no existe en el carrito')
        
    def clear(self):
        self.session[settings.CARRO_SESSION_ID]={}
        self.session.modified=True
        
        
        
        