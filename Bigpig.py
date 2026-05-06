class Animals:

    species = "Pig"

    def __init__(self, name, weight,):
        self.name = name
        self.weight = weight
    
    def eat(self, eat):
        return "{} eats {}".format(self.name, eat)
    
    def scream(self):
        return "{} is now screaming".format(self.name)


bigpig = Animals("bigpig", 100000)
smallpig = Animals("smallpig", 0.1)

print(bigpig.eat("Fried chicken"))
print(smallpig.scream())


print("Bigpig is a {}".format(bigpig.species))
print("Smallpig is also a {}".format(smallpig.species))


print("{} is {} kgs".format(bigpig.name, bigpig.weight))
print("{} is {} kgs".format(smallpig.name, smallpig.weight))