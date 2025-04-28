import random

friends=["Sasha", "Alex","Miguel","Shamil", "Pablo", "Yumi", "Dave", "Qiao"]
#option 1
print(random.choice(friends))

#2 option

random_index = random.randint(0 ,6)
print(friends[random_index])

