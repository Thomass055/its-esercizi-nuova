class Restaurant:
    def __init__(self,Restaurant_name:str,cuisine_type:str):
        self.Restaurant_name= Restaurant_name 
        self.cuisine_type= cuisine_type

    def describe_restaurant(self):
        print(f"Nome Ristorante: {self.Restaurant_name}")
        print(f"Tipo Cucina: {self.cuisine_type}")

    def open_restaurant(self):
        print(f"{self.Restaurant_name} è ora aperto")
        
restaurant = Restaurant("Da Thomas", "Italiano")
restaurant2 = Restaurant("La Fraschetta", "Carne,Pesce")
restaurant3 = Restaurant("La Marinella", "Pesce")

print(restaurant.Restaurant_name)
print(restaurant.cuisine_type)

restaurant.describe_restaurant()
restaurant.open_restaurant()

restaurant2.describe_restaurant()
restaurant2.open_restaurant()

restaurant3.describe_restaurant()
restaurant3.open_restaurant()

