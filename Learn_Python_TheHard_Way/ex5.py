my_name = 'Allen Song'
my_age = 22 # not a lie
my_height = 175 # cm
my_weight = 60 # kg
my_eyes = 'black'
my_teeth = 'white'
my_hair = 'black'
height_inch = my_height * 0.394 # inches
weight_lb = my_weight * 2.20 # lbs

print(f"Let's talk about {my_name}.")
print(f"He's {my_height} cm tall. He's {height_inch} inches tall.")
print(f"He's {my_weight} kg heavy. He's {weight_lb} pounds heavy.")
print("Actually that's not too heavy.")
print(f"He's got {my_eyes} eyes and {my_hair} hair.")
print(f"His teeth are usually {my_teeth} depending on the coffee.")

# this line is triky, try to get it exactly right
total = my_age + my_weight + my_height
print(f"If I add {my_age}, {my_height}, and {my_weight} I get {total}.")
