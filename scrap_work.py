import random
test = {'Ring of Three Wishes': '150,000 gp',
 'Ring of Warmth': '350 gp',
 'Ring of Water Walking': '450 gp',
 'Ring of X-Ray Vision': '3,000 gp',
 'Rod of Ressurection': '50,000 gp',
 'Rod of Rulership': '4,500 gp',
 'Rope of Climbing': '350 gp',
 'Sending Stones': '200 gp',
 'Slippers of Spider Climbing': '500 gp',
 'Talisman of the Sphere': '20,000 gp',
 'Trident of Fish Command': '400 gp',}

# print (random.choice(test))

entry_list = random.choice(list(test.items()))
print (entry_list)
print (entry_list[0])