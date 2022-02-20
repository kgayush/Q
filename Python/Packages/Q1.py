import random
class Dice:
    def roll(self):
        first = random.randint(1,6)
        second = random.randint(1,6)

        return first, second

def rand_choice(choice_list):
    print(random.choice(choice_list))

def rand_seed(seed):
    random.seed(seed)
    print(random.random())

dice = Dice()
print(dice.roll()) 

choice_list = [1, 2, 3, 4, 5, 6]
rand_choice(choice_list)

seed = 5
rand_seed(seed)

