from Person_Thing import Person

name = "Jack"

height = "Five foot six"

weight = int("225")

hair_color = "Black"

my_person = Person(name, height, weight, hair_color)
my_person.description()
my_person.change_hair_color("Green")
my_person.weight_update(25)
my_person.description()
