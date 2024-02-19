cart = {'apple': 10, 'plums': 15, 'bananas': 5}

shop_K = {'apple': 1.2, 'plums': 4, 'bananas': 5.5}
shop_P = {'apple': 1.3, 'plums': 3, 'bananas': 8}
shop_L = {'apple': 1.4, 'plums': 2, 'bananas': 10}

shops = {'pro': shop_P, 'lil': shop_L, 'kau': shop_K}

result = {}

for cart_product, cart_quantity in cart.items():
    # print(cart_product, cart_quantity)
    for shop_name, shop_products in shops.items():
        # print(shop_name, shop_products[cart_product] * cart_quantity)
        result[shop_name] = result.get(shop_name, 0) + shop_products[cart_product] * cart_quantity

print(result)

min_price = None
shop_name = ''
for name, price in result.items():
    if min_price is None or price < min_price:
        min_price = price
        shop_name = name

print(shop_name)




