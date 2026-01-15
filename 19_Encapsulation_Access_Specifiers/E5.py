# Product Price Protection (Protected + Private)
# Requirements
# Class Product
# Protected variable:
# _category
# Private variable:
# __price
# Provide setters/getters
# Ensure price > 0
# Display product info using a method.

class Product:

    def __init__(self):
        self._category = 'Pen'
        self.__price = 2

    def get_category(self):
        return self._category
    
    def get_price(self):
        return self.__price
    
    def set_category(self):
        category_name = input("Enter Category Name: ")
        self._category = category_name

    def set_price(self):
        price = float(input("Enter Product real price: "))
        if price > 0:
            self.__price = price
            print(f"\nProduct price is {self.__price} Rupees.")
        else:
            print("\nInvalid Price! Price must be greater than 0.")


    def info(self):
        print("\n--- Product Details ---")
        print(f"Category : {self._category}")
        print(f"Price    : {self.__price} Rupees")

p1 = Product()
p1.set_category()
p1.set_price()
p1.info()
# OP:
# Enter Category Name: light
# Enter Product real price: 20

# Product price is 20.0 Rupees.

# --- Product Details ---
# Category : light
# Price    : 20.0 Rupees