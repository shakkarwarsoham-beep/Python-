moon_gravity = 1.62

def calculate_weight(mass):
    weight = mass * MOON_GRAVITY
    return weight

mass = float(input("Enter mass in kg: "))
print("Weight on Moon =", calculate_weight(mass), "N")