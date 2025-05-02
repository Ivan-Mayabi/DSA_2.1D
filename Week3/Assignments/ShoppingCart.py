""""
Author: Mayabi Muigai Ivan 180954

Description: I altered the class code written to generate the final printing statements
so that I did not only depend on copying functions. The resulted returned is still the same.
"""


class ShoppingCart:
#     #This method is doing.........
#     PI: float = 3.14
#
#     def __init__(self):
#         pass
#
#     def area(self,radius) -> float:
#         return 3.14 * (radius*radius)
#
# obj1: ShoppingCart = ShoppingCart()
# obj2: ShoppingCart = ShoppingCart()
#
# print(obj1.area(7))
# print(obj2.area(7.7))
    item_name: str
    qty: int
    items: list
    unit_price: float

    def __init__(self):
        self.items = []


    def add_item(self, item_name: str, qty:int, unit_price:float):
        self.item_name = item_name
        self.qty = qty
        self.unit_price = unit_price
        self.items.append((item_name,qty, unit_price))

    def remove_item(self,item_name: str):
        i: int = 0
        for items in self.items:
            if items[0] == item_name:
                self.items.pop(i)
                # self.items.remove(items)
                break
            i += 1

    """""Check what this thing does"""
    def calculate_total(self) -> float:
        total = 0
        for name, qty, price in self.items:
            total+= qty * price
        return total

    def summary(self) -> None:
        print("Cart Content")
        for name, qty, price in self.items:
            print(f"{name} : {qty} @ Ksh {price:.3f}")
        print(f"Total: Ksh {self.calculate_total():.3f}")

class DiscountedCart(ShoppingCart):
    def __init__(self, discount_rate:float):
        super().__init__()
        self.discount_rate = discount_rate

    def calculate_total(self) -> float:
        initial_total : float = super().calculate_total()
        discount: float =  initial_total * self.discount_rate
        return initial_total - discount

class TaxedCart(ShoppingCart):
    def __init__(self,tax_rate:float):
        super().__init__()
        self.tax_rate: float= tax_rate

    def calculate_total(self) -> float:
        initial_total:float = super().calculate_total()
        tax:float = initial_total * self.tax_rate
        return initial_total+tax


# obj: ShoppingCart = ShoppingCart("Papaya",9)
# obj2: ShoppingCart = ShoppingCart("Guava",17)
#
# print(obj.item_name)
# print(obj2.item_name)

if __name__ == "__main__":
    #1) Print an ordinary cart
    cart: ShoppingCart = ShoppingCart()

    cart.add_item("Kiwi",69,30.7)
    cart.add_item("Papaya",70,50.2)
    cart.add_item("Apple",69,31.7)
    # cart.remove_item("Apple")

    print(">>>>>>Ordinary Cart<<<<<<")
    print(cart.summary())

    #2) Print the discounted Cart
    disc_cart: DiscountedCart = DiscountedCart(0.15)
    disc_cart.add_item("Papaya", 76, 6.20)
    disc_cart.add_item("Orange", 96, 11.50)
    disc_cart.add_item("Kiwi", 85, 9.60)
    print(">>> Applying a 15% Discount <<<")
    print(disc_cart.summary())

    # 3) Applying Tax
    taxed_cart = TaxedCart(0.07)
    taxed_cart.add_item("Papaya", 5, 2.00)
    taxed_cart.add_item("Orange", 96, 11.50)
    taxed_cart.add_item("Kiwi", 3, 1.50)
    print(">>> Applying a 12% Tax  <<<")
    print(taxed_cart.summary())

