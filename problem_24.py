def massage_format(name,product,price):
    massage = f"Hello {name}, Thanks for buying {product} and the price is {price}."
    return massage

msg = massage_format ("Sanskar","Sneakers","$45")
print(msg)