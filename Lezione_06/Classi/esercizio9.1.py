class Restaurant:
    def __init__(self,Restaurant_name:str,cuisine_type:str):
        self.Restaurant_name= Restaurant_name 
        self.cuisine_type= cuisine_type

    def describe_restaurant(self):
        print(f"Nome Ristorante: {self.Restaurant_name}")
        print(f"Tipo Cucina: {self.cuisine_type}")

    def open_restaurant(self):
        print(f"{self.Restaurant_name} è ora aperto")
        
Restaurant = Restaurant("La Fraschetta", "Italiano")

print(Restaurant.Restaurant_name)
print(Restaurant.cuisine_type)

Restaurant.describe_restaurant()
Restaurant.open_restaurant()

