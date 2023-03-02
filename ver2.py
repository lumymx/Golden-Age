import random

# Define variables for population, resources, technology, and culture
population = 10000
resources = 100000
technology = 0
culture = 0

# Define variables for rate of change for each variable
pop_growth_rate = 1.03
res_growth_rate = 1.02
tech_growth_rate = 1.1
culture_growth_rate = 1.05

# Define variables for events that can occur during Golden Age
great_discovery_chance = 0.05
artistic_flourishing_chance = 0.1
prosperity_decline_chance = 0.1

# Define variable to track number of years that have passed
years_passed = 0

# Start simulation loop
while True:
    # Update population, resources, technology, and culture
    population = int(population * pop_growth_rate)
    resources = int(resources * res_growth_rate)
    technology = int(technology * tech_growth_rate)
    culture = int(culture * culture_growth_rate)
    years_passed += 1
    
    # Check for events that can occur during Golden Age
    if random.random() < great_discovery_chance:
        technology *= 2
        print(f"A great discovery has been made in year {years_passed}!")
    
    if random.random() < artistic_flourishing_chance:
        culture *= 2
        print(f"Artistic expression is flourishing in year {years_passed}!")
    
    if random.random() < prosperity_decline_chance:
        resources = int(resources * 0.5)
        print(f"The society is experiencing a decline in prosperity in year {years_passed}!")
    
    # Check if Golden Age conditions are met
    if population >= 100000 and resources >= 1000000 and technology >= 10000 and culture >= 5000:
        print(f"A Golden Age has been reached after {years_passed} years!")
        break
