import requests
# These are all GET requests from the Roblox Web API
# API: http://wiki.roblox.com/index.php?title=Web_APIs
# API Wrapper made by Cameron
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
    def friend_count(id):
        url = "https://www.roblox.com/friends/json?userId=" + str(id) + "&currentPage=0&pageSize=20&imgWidth=110&imgHeight=110&imgFormat=jpeg&friendsType=BestFriends"
        r = requests.get(url)
        res = r.json()['TotalFriends']
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
    def is_public(id):
        url = "https://api.roblox.com/Marketplace/ProductInfo?assetId=" + str(id)
        r = requests.get(url)
        res = r.json()['PublicDomain']
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
class Image:
    '''Get an image of a torso, head,, outfit, or asset'''
    def get_torso_thumbnail(id):
        url = "https://www.roblox.com/bust-thumbnail/json?userId=" + str(id) + "&height=180&width=180"
        r = requests.get(url)
        res = r.json()['Url']
        return res
    def get_head_thumbnail(id):
        url = "https://www.roblox.com/headshot-thumbnail/json?userId=" + str(id) + "&height=180&width=180"
        r = requests.get(url)
        res = r.json()['Url']
        return res
    def get_outfit_thumbnail(id):
        url = "https://www.roblox.com/outfit-thumbnail/json?userId=" + str(id) + "&height=180&width=180"
        r = requests.get(url)
        res = r.json()['Url']
        return res
    def get_asset_thumbnail(id):
        url = "https://www.roblox.com/Thumbs/Asset.ashx?width=110&height=110&assetId=" + str(id)
        r = requests.get(url)
        res = r.json()['Url']
        return res
class Friends:
    def are_user_friendship(id1, id2):
        print("not done yet")
    def are_users_best_friends(id1, id2):
        print("not done yet")
