products = ["Mouse", "Keyboard", "Monitor", "USB", "Webcam"]

print("Original inventory: ",products)

new=input("Please enter a new product: ")
products.append(new)

dell=input("Please enter a name to delet: ")
if products.count(dell) != 0:
    products.remove(dell)
    print("Removed successfully")
else:
    print("Error")

products.insert(2,"Laptop")
ser=input("Search: ")
if products.index(ser) !=ValueError:
    print("Products found at ",products.index(ser))
else:
    print("Product not found")
products.sort(key=str.lower)
print("Inventory ater sorting: \n",products)

print("Remove last item: ",products.pop())

print("current inventory: ")
print(products)

print("Backup inventory: ")
print(products.reverse())

