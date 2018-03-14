import requests
class User:
    def badges(id):
        url = "https://www.roblox.com/badges/roblox?userId=" + str(id)
        r = requests.get(url)
        res = r.json()['RobloxBadges']
        return res
    def is_online(username):
        url = "https://api.roblox.com/users/get-by-username?username=" + username
        r = requests.get(url)
        res = r.json()['IsOnline']
        return res
    def id(username):
        url = "https://api.roblox.com/users/get-by-username?username=" + username
        r = requests.get(url)
        res = r.json()['Id']
        return res
    def does_user_exist(username):
        url = "https://api.roblox.com/users/get-by-username?username=" + username
        r = requests.get(url)
        res = r.json()['success']
        return res
class Group:
    def description(id):
        url = "https://api.roblox.com/groups/" + str(id)
        r = requests.get(url)
        return(r.json())['Description']
    def name(id):
        url = "https://api.roblox.com/groups/" + str(id)
        r = requests.get(url)
        return(r.json()['Name'])
    def owner(id):
        url = "https://api.roblox.com/groups/" + str(id)
        r = requests.get(url)
        res = r.json()['Owner']['Name']
        return res
    def owner_id(id):
        url = "https://api.roblox.com/groups/" + str(id)
        r = requests.get(url)
        res = r.json()['Owner']['Id']
        return res
class Asset:
    def asset_id(id):
        url = "https://api.roblox.com/Marketplace/ProductInfo?assetId=" + str(id)
        r = requests.get(url)
        res = r.json()['AssetId']
        return res
    def creator(id):
        url = "https://api.roblox.com/Marketplace/ProductInfo?assetId=" + str(id)
        r = requests.get(url)
        res = r.json()['Creator']['Name']
        return res
    def product_id(id):
        url = "https://api.roblox.com/Marketplace/ProductInfo?assetId=" + str(id)
        r = requests.get(url)
        res = r.json()['ProductId']
        return res
    def name(id):
        url = "https://api.roblox.com/Marketplace/ProductInfo?assetId=" + str(id)
        r = requests.get(url)
        res = r.json()['Name']
        return res
    def description(id):
        url = "https://api.roblox.com/Marketplace/ProductInfo?assetId=" + str(id)
        r = requests.get(url)
        res = r.json()['Description']
        return res
    def asset_type_id(id):
        url = "https://api.roblox.com/Marketplace/ProductInfo?assetId=" + str(id)
        r = requests.get(url)
        res = r.json()['AssetTypeId']
        return res
    def created_at(id):
        url = "https://api.roblox.com/Marketplace/ProductInfo?assetId=" + str(id)
        r = requests.get(url)
        res = r.json()['Created']
        return res
    def last_updated(id):
        url = "https://api.roblox.com/Marketplace/ProductInfo?assetId=" + str(id)
        r = requests.get(url)
        res = r.json()['Updated']
        return res
    def price_in_robux(id):
        url = "https://api.roblox.com/Marketplace/ProductInfo?assetId=" + str(id)
        r = requests.get(url)
        res = r.json()['PriceInRobux']
        return res
    def price_in_tickets(id):
        url = "https://api.roblox.com/Marketplace/ProductInfo?assetId=" + str(id)
        r = requests.get(url)
        res = r.json()['PriceInTickets']
        return res
    def sales(id):
        url = "https://api.roblox.com/Marketplace/ProductInfo?assetId=" + str(id)
        r = requests.get(url)
        res = r.json()['Sales']
        return res
    def is_new(id):
        url = "https://api.roblox.com/Marketplace/ProductInfo?assetId=" + str(id)
        r = requests.get(url)
        res = r.json()['IsNew']
        return res
    def is_for_sale(id):
        url = "https://api.roblox.com/Marketplace/ProductInfo?assetId=" + str(id)
        r = requests.get(url)
        res = r.json()['IsForSale']
        return res
    def is_limited(id):
        url = "https://api.roblox.com/Marketplace/ProductInfo?assetId=" + str(id)
        r = requests.get(url)
        res = r.json()['IsLimited']
        return res
    def remaining(id):
        url = "https://api.roblox.com/Marketplace/ProductInfo?assetId=" + str(id)
        r = requests.get(url)
        res = r.json()['Remaining']
        return res

