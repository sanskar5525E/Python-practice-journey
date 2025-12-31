def massage_format(name,product,tracking_no=None):
    if tracking_no:
        msg = f"Hey {name}, your order {product} has been shipped and your tracking no. is {tracking_no}. "
    else :
        msg = f"Hey {name}, your order {product} has been shipped and your tracking no. is updated soon!"
    return msg 
print(massage_format("Sanskar","t-shirt",))  
print(massage_format("Rahul","pant","QR365"))  

