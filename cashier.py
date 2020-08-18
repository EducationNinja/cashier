def main():
	cart = []

	item = input("Item (Type \"done\" to exit: ")

	while item != "done":
		price = input("Price: ")
		qty = input("Qty: ")

		cart.append({"name": item, "price": float(price), "quantity": int(qty)})
		item = input("Item (Type \"done\" to exit: ")

	print("\n")
	print("-"*40)
	print("Fatoura")
	print("-"*40)

	total = 0
	for item in cart:
		print(f"{item['quantity']} - {item['name']} - {item['quantity'] * item['price']}")
		total += item['quantity'] * item['price']

	print("-"*40)

	print(f"Total: ${total}")

if __name__ == '__main__':
	main()