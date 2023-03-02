import random

# Define initial population and resources
initial_pop = 10000
initial_food = 5000
initial_wood = 5000
initial_stone = 5000

# Define rates of change for population, food, wood, and stone
pop_growth_rate = 1.02
food_growth_rate = 1.03
wood_growth_rate = 1.02
stone_growth_rate = 1.02

# Define initial demographic factors
birth_rate = 0.05
death_rate = 0.03
migration_rate = 0.005

# Define initial technological and cultural factors
initial_tech_level = 1
initial_culture_level = 1
tech_growth_rate = 1.05
culture_growth_rate = 1.03

# Define initial happiness and education levels
initial_happiness_level = 0.6
initial_education_level = 0.3

# Define factors influencing happiness and education
food_happiness_factor = 0.1
education_tech_factor = 0.2

# Define variables to track years passed and resources available
years_passed = 0
food_available = initial_food
wood_available = initial_wood
stone_available = initial_stone

# Start simulation loop
while True:
    # Update population, food, wood, and stone
    population = int(initial_pop * pop_growth_rate ** years_passed)
    food_available = int(initial_food * food_growth_rate ** years_passed)
    wood_available = int(initial_wood * wood_growth_rate ** years_passed)
    stone_available = int(initial_stone * stone_growth_rate ** years_passed)

    # Calculate demographic changes
    births = int(population * birth_rate)
    deaths = int(population * death_rate)
    migrations = int(population * migration_rate)
    population = population + births - deaths + migrations
    
    # Update technological and cultural factors
    tech_level = initial_tech_level + int(years_passed * tech_growth_rate)
    culture_level = initial_culture_level + int(years_passed * culture_growth_rate)
    
    # Update happiness and education levels
    food_happiness = min(food_available / population, 1.0) * food_happiness_factor
    education_tech = tech_level / 100 * education_tech_factor
    happiness_level = initial_happiness_level + food_happiness
    education_level = initial_education_level + education_tech
    
    # Check if Golden Age conditions are met
    if population >= 100000 and food_available >= 100000 and wood_available >= 50000 and stone_available >= 50000 and happiness_level >= 0.8 and education_level >= 0.6:
        print(f"A Golden Age has been reached after {years_passed} years!")
        break
    
    # Increment years passed
    years_passed += 1
