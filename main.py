from ride import Ride,RideRequest,RideMatching , Ridesharing
from users import Driver,Rider
from vehicle import Car,Bike


Sharing_is_caring = Ridesharing("Sharing is Caring")

provati = Rider("Provati", "provati@example.com", 1000 , "Munshiganj" , 1000)
Sharing_is_caring.add_rider(provati)
tanusree = Driver("Tanusree" ,"tanusree@example.com", 1500 , "Bikrampur")
Sharing_is_caring.add_driver(tanusree)

#ride request kori ektA

provati.request_ride(Sharing_is_caring , "Dhaka" , "car")
tanusree.reach_destination(provati.current_ride)  
provati.show_current_ride()

#print(Sharing_is_caring)
