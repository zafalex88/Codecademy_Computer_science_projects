#Solution of Sal's Shipping project
#Codecademy - Computer Science Path

def ground_shipping(weight):
      if weight <= 2:
    return (weight * 1.5) + 20.00
  elif weight > 2 and weight <= 6:
    return (weight * 3) + 20.00
  elif weight > 6 and weight <= 10:
    return (weight * 4) + 20.00
  else:
    return (weight * 4.75) + 20.00
print(ground_shipping(8.4))

premium_ground_shipping = 125

def drone_shipping(weight):
  if weight <= 2:
    return (weight * 4.5)
  elif weight > 2 and weight <= 6:
    return (weight * 9)
  elif weight > 6 and weight <= 10:
    return (weight * 12)
  else:
    return (weight * 14.25)
  
print(drone_shipping(1.5))

def cheapest_shipping(weight):
  if ground_shipping(weight) < drone_shipping(weight) and ground_shipping(weight) < premium_ground_shipping:
    return "The cheapest shipping method is Ground Shipping and it costs " + str(ground_shipping(weight))
  elif drone_shipping(weight) < ground_shipping(weight) and drone_shipping(weight) < premium_ground_shipping:
    return "The cheapest shipping method is Drone Shipping and it costs " + str(drone_shipping(weight))
  else:
    return "The cheapest shipping method is Premium Ground Shipping and it costs " + str(premium_ground_shipping)
  
print(cheapest_shipping(4.8))
print(cheapest_shipping(41.5))