import random

# Define variables for resources, happiness, and technological advancement
resources = 1000
happiness = 100
tech_level = 1

# Start simulation loop for 100 years
for year in range(1, 101):
    # Increase resources and happiness each year
    resources += random.randint(50, 100)
    happiness += random.randint(1, 5)
    
    # Increase tech_level every 10 years
    if year % 10 == 0:
        tech_level += 1
    
    # If resources and happiness are high and tech_level is 3 or higher, print Golden Age message
    if resources > 15000 and happiness > 500 and tech_level >= 3:
        print(f"The year is {year}. This is a Golden Age!")
        break
