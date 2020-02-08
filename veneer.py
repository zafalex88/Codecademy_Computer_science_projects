#Solution of Veneer project
#Codecademy - Computer Science Path

class Art:
  def __init__(self, artist, title, medium, year, owner):
    self.artist = artist
    self.title = title
    self.medium = medium
    self.year = year
    self.owner = owner
    
  def __repr__(self):
    return "{0}, '{1}'. {2}, {3}. {4}, {5}.".format(self.artist, self.title, self.year, self.medium, self.owner.name, self.owner.location)
  
class Marketplace:
  def __init__(self):
    self.listings = []
    
  def add_listing(self, new_listing):
    self.listings.append(new_listing)
    
  def remove_listing(self, expired_listing):
    self.listings.remove(expired_listing)
    
  def show_listings(self):
    for listing in self.listings:
      print(listing)
      
class Client:
  def __init__(self, name, location, is_museum):
    self.name = name
    self.is_museum = is_museum
    if is_museum == True:
      self.location = location
    else:
      self.location = "Private Collection"
      
      
  def sell_artwork(self, artwork, price):
    if artwork.owner == self:
      new_listing = Listing(artwork, price, self)
      veneer.add_listing(new_listing)
      
class Listing:
  def __init__(self, art, price, seller):
    self.art = art
    self.price = price
    self.seller = seller

  def __repr__(self):
    return "{0}, {1}.".format(self.art.title, self.price)

edytta = Client("Edytta Halpirt", None, False)
moma = Client("The MOMA", "New York", True)

girl_with_mandolin = Art("Picasso, Pablo", "Girl with a Mandolin (Fanny Tellier)", 1910, "oil on canvas", edytta)
print(girl_with_mandolin)

veneer = Marketplace()
edytta.sell_artwork(girl_with_mandolin, "$6M (USD)")
print(veneer.show_listings()) 