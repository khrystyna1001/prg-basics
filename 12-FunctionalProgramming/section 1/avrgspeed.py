avrg_speed = lambda distance, hours, minutes: round((distance/(minutes/60 + hours)), 2)

distance = int(input("Enter the distance in km: "))
hours = int(input("Enter the time in hours: "))
minutes = int(input("Enter the time in minutes: "))

print(f"The average speed is: {avrg_speed(distance, hours, minutes)} km/h")
