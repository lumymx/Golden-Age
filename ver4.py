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

# Define crafting system
crafting_system = {
    'tools': {'wood': 5, 'stone': 5},
    'houses': {'wood': 20, 'stone': 10},
    'walls': {'wood': 10, 'stone': 20},
}

# Define events that can change growth rates
events = {
    'drought': {'food': 0.8},
    'flood': {'food': 1.2},
    'plague': {'pop': 0.9},
    'immigration': {'pop': 1.1},
}

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
    
    # Check for events that change growth rates
    event = random.choice(list(events.keys()))
    if event == 'drought':
        food_growth_rate *= events[event]['food']
    elif event == 'flood':
        food_growth_rate *= events[event]['food']
    elif event == 'plague':
        pop_growth_rate *= events[event]['pop']
    elif event == 'immigration':
        pop_growth_rate *= events[event]['pop']
    
    # Craft items if enough resources are available
    for item in crafting_system:
        can_craft = True
            for resource, amount in crafting_system[item].items():
        if resource == 'food' and food_available < amount * population:
            can_craft = False
            break
        elif resource == 'wood' and wood_available < amount * population:
            can_craft = False
            break
        elif resource == 'stone' and stone_available < amount * population:
            can_craft = False
            break
    if can_craft:
        print(f"Crafting {item}...")
        food_available -= crafting_system[item]['food'] * population
        wood_available -= crafting_system[item]['wood'] * population
        stone_available -= crafting_system[item]['stone'] * population

# Check if Golden Age has been reached
if happiness_level >= 0.9 and education_level >= 0.8 and tech_level >= 50:
    print("Golden Age reached!")
    break

# Increment years passed and print current state of simulation
years_passed += 1
print(f"Year {years_passed}: Population={population}, Food={food_available}, Wood={wood_available}, Stone={stone_available}, Happiness={happiness_level}, Education={education_level}, Tech={tech_level}")
