from pyscript import display #This imports the pyscript module, specifically the display function

# ==========
# Variables
# ==========

# 1. String
restaurant_name = "Kain Tayo"

# 2. String
owner_name = "Allen Daradal"

# 3. Integer
year_established = 2015

# 4. Float
popular_item_price = 120.50

# 5. Boolean
has_delivery = True

# 6. List
product_names = ["Burger Meal", "Spaghetti", "Halo-Halo"]

# 7. Dictionary
business_hours = {
    "open": "08:00 AM",
    "close": "09:00 PM"
}

# 8.Dictionary
menu_prices = {
    "Burger Meal": 120.50,
    "Spaghetti": 95.00,
    "Halo-Halo": 75.00,
    "Chicken Adobo": 150.00,
    "Sinigang na Baboy": 180.00,
    "Fried Rice": 50.00
}

# 9.List
common_allergens = ["Peanuts", "Seafood", "Dairy"]

# 10. Float
tax_rate = 0.08


# ==========
# Displaying values
# ==========

display(restaurant_name, target="restaurant_name")
display(owner_name, target="owner_name")
display(year_established, target="year_established")

display(f"Delivery Services Available?:{has_delivery}", target="delivery_status")

display(f"{business_hours['open']} - {business_hours['close']}", target="business_hours")

display(tax_rate, target="tax_rate")


# Display items using loops to save time.

for x in common_allergens:
    display(x, target="allergens_list")

for x in menu_prices:
    display(f"{x}", target="menu_items")
    display(f"{menu_prices[x]}", target="menu_prices")