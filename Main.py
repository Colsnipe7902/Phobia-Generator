
welcome_banner = """ Welcome to the Phobia Generator. The theme is animals. Type 4 animals. """
print(welcome_banner)

animals = []
for i in range(4):
    animal = input(f"Enter animal {i + 1}: ")
    animals.append(animal)

phobia_list = [animal + "ophobia" for animal in animals]

print("\nList of animals:")
for animal in animals:
    print(animal)

print("\nList with phobias:")
for phobia in phobia_list:
    print(phobia)
