class Item:
    def __init__(self, name : str, price : float):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name}: {self.price} Kč"

class Pizza(Item):
    def __init__(self, name : str, price : float, ingredients : dict):
        super().__init__(name, price)
        self.ingredients = ingredients
        ingredients = {}

    def add_extra(self, ingredient, quantity, price_per_ingredient):
        self.ingredients[ingredient] = quantity
        self.price += quantity * price_per_ingredient

    def __str__(self):
        ingredient_list = ", ".join([f"{ingredient}: {quantity}g" for ingredient, quantity in self.ingredients.items()])
        return f"Pizza {self.name} obsahuje {ingredient_list} a stojí {self.price} Kč"

class Drink(Item):
    def __init__(self, name : str, price : float, volume : int):
        super().__init__(name, price)
        self.volume = volume

    def __str__(self):
        return f"Nápoj {self.name}, objem {self.volume} ml, cena {self.price} Kč"


class Order:
    def __init__(self, customer_name : str, delivery_address : str, items : list):
        self.customer_name = customer_name
        self.delivery_address = delivery_address
        self.items = items
        self.status = "Nová"

    def mark_delivered(self):
          self.status = "Doručeno"

    
    def __str__(self):
         item_list = "\n".join([str(item) for item in self.items])
         return f"Objednávka od: {self.customer_name}\nAdresa doručení: {self.delivery_address}\nPoložky:\n{item_list}\nStav objednávky: {self.status}"
          
class DeliveryPerson:
    def __init__(self, name : str, phone_number : str):
        self.name = name
        self.phone_number = phone_number
        self.available = True
        self.current_order = None

    def assign_order(self, order):
        if self.available:
            self.current_order = order
            order.status = "Na cestě"
            self.available = False

    def complete_delivery(self):
        if self.current_order:
            self.current_order.mark_delivered()
            self.available = True
            self.current_order = None

    def __str__(self):
        availability = "Dostupný" if self.available else "Nedostupný"
        return f"Doručovatel: {self.name}, Kontakt: {self.phone_number}, Stav: {availability}"

    
margarita = Pizza("Margarita", 200, {"sýr": 100, "rajčata": 150})
margarita.add_extra("olivy", 50, 10)

cola = Drink("Cola", 45, 500)

order = Order("Jan Novák", "Pražská 123", [margarita, cola])
print(order)

delivery_person = DeliveryPerson("Petr Novotný", "777 888 999")
delivery_person.assign_order(order)
print(delivery_person)

delivery_person.complete_delivery()
print(delivery_person)

print(order)









    

