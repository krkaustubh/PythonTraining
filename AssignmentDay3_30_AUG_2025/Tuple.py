# Create a tuple named product containing the following items: "Laptop", 50000, Black ,'Samsung' and "Electronics". Print the tuple
product = ("Laptop", 50000, "Black", "Samsung", "Electronics")
print(product)

#Access and print the second element of the tuple product.
secondElement = product[1]
print("Second eleent from product tupple: ", secondElement)

#Slice and print the last two elements of the product tuple.
lastTwo = product[-2:0]
print("last two elements after Slicing: ", lastTwo)

#Check whether "Electronics" is present in the product tuple and print a message.
if "Electronics" in product:
    print("Yes, 'Electronics' is present in product Tuple")
else:
    print("No, 'Electronics' is not present in product Tuple")
    
#Create a tuple of 5 product prices: (1000, 1500, 1200, 1100, 900). Count how many times 1000 appears.
prices = (1000, 1500, 1200, 1000, 900)
countOneThousand = prices.count(1000)
print("1000 appears in prices: ", countOneThousand,"times")


#Find and print the maximum and minimum price from the prices tuple.
maxPrice = max(prices)
minPrice = min(prices)
print(f"Maximum price: {maxPrice}")
print(f"Minimun price: {minPrice}")

#Use a loop to print each item from the product tuple on a new line.
print("Items in product Tuple:-")
for item in product:
    print(item)

#Convert the product tuple to a list. Change the price to 55000, then convert it back to a tuple. Print the updated tuple.
productList = list(product)
productList[1] = 55000
updatedProduct = tuple(productList)
print("Updated Tuple: ", updatedProduct)

#Add a new item "In Stock" to the product tuple (simulate adding by concatenation).
product_with_stock = product + ("In Stock",)
print("New Item added, and updated tuple is: ", product_with_stock)

#Remove "Electronics" from the product tuple (by converting to list, removing, and converting back).
product_list_to_remove = list(product)#converted to list
product_list_to_remove.remove("Electronics")#remove an Item
productRemoved = tuple(product_list_to_remove)
print("removed product ", productRemoved)


#Unpack the tuple product into three variables and print each variable.
#item, price, color, brand, category = product
#print("Item: ",item)
#print("Price: ", price)
#print("color: ", color)
#print("brand: ", brand)
#print("category: ", category)

name, price, color, *rest = product
print("name = ", name, " price = ", price, " color = ", color)

 
#Create a nested tuple that contains three product tuples inside it. Access and print the name of the second product in the nested tuple.
nested_tuple = (("Laptop", 50000, "Black"),
                ("Tablet", 10000, "Silver"),
                ("Desktop", 30000, "Blue"))
print("Name of second product is : ", nested_tuple[1][0])






