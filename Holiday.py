#want to write a progrom for a holiday
#the program will have three inputs 
#asking user to inter a city, number of nights staying and if they want rent a car
#bellow are the inputs
city_flight = input("choose city; Paris,Rome,Tokyo,Harare : ")
num_nights = int(input("how many nights you staying : "))
rental_days = int(input("how many days you renting a car : "))

def hotel_cost(num_nights): #def function and argument for hotel cost 
    y = num_nights*150 #calculation for hotel cost
    return y

def plane_cost(city_flight) : #def function and argument for plane cost
    cities ={"Paris": 200, "Rome":400 , "Tokyo":800 ,"Harare":800,} # a dict with a list of cities
    return cities.get(city_flight,0) #gives the value 0 if no city selected

def car_rental(rental_days) : #def function and argument for car rental
    t = rental_days*70 #caculation for csr rental
    return t

def holiday_cost( a,b,c,): # a def function and three arguments
    total  = a,b,c, #giving defination to argument
    return total
sum = hotel_cost(num_nights)+plane_cost(city_flight)+car_rental(rental_days) #function calculation
print("the holiday total cost: £"+str(sum)) #prints holiday price
holiday_cost( num_nights,city_flight,rental_days) #calling functions   