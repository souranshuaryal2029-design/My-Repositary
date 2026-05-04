class dinosaurs:


    species = "Giganotasaurus"


    def __init__(self, name, age):
        self.name = name
        self.age = age


fatpig = dinosaurs("fatpig", 21)
skinnypig = dinosaurs("skinnypig", 30)


print("Fatpig is a {}".format(fatpig.species))
print("Skinnypig is also a {}".format(skinnypig.species))


print("{} is {} years old".format(fatpig.name, fatpig.age))
print("{} is {} years old".format(skinnypig.name, skinnypig.age))