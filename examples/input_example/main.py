import robloxpy
id = input("Please type an Asset ID: ")
print("Sales: "+ robloxpy.Asset.sales(id))
print("Price in tickets: "+ robloxpy.Asset.price_in_tickets(id))
print("Price in robux: "+ robloxpy.Asset.price_in_robux(id))
print("Creator: " + robloxpy.Asset.creator(id))
