import random

def check_hunger(cats):
    hunger = False
    for cat in cats:
        if cat.hunger > 50:
            print(f"¡{cat.name} tiene hambre!")
            hunger = True
    if hunger:
        return True

class Cat():
    species = "gato"
    sound = "miau"
    def __init__(self, name, gender, color, age):
        self.name = name.title()
        self.gender = gender.lower()
        self.color = color.lower()
        self.age = age
        self.hunger = 0

    def talk(self):
        print(f"{self.name} dice: ¡{(self.sound).capitalize()}!")

    def introduce(self):
        print(f"Mi nombre es {self.name}, soy un {self.species} {self.gender} {self.color} y tengo {self.age} meses")

    def increase_hunger(self):
        cat.hunger += random.randint(5, 11)
        cat.talk()

#Inicializar gatos
zeus = Cat("Zeus", "macho", "blanco con rayas grises", 12)
rayas = Cat("Rayas", "hembra", "rol de canela", 45)
dali = Cat("Dalí", "macho", "blanco con rayas grises", 30)
leo = Cat("Leo", "macho", "naranjoso", 18)
lince = Cat("Lince", "macho", "gris rayado", 38)

#Se agrupan
cats = set((zeus, rayas, dali, leo, lince))

#Gatos maullan
for cat in cats:
    cat.talk()

#Gatos se presentan:
for cat in cats:
    cat.introduce()

#Incrementa el hambre de los gatos
while True:
    cats = list(cats)
    num = random.randint(0,len(cats)-1)
    selected_cat = cats[num]
    print(num)
    selected_cat.increase_hunger()
    cats_hungry = check_hunger(cats)
    if cats_hungry:
        break