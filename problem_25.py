def shipped_massage(name,product,tracking_no):
   msg= f"Hi {name}, your order {product} has been shipped. Tracking code: {tracking_no}."
   return msg
massage = shipped_massage("sanskar","shoes","QR345")   
print(massage)
