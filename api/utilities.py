import os
import pprint
import re
import random

# Machine-learned neural network that defines macroelements proportions
def macros():
	ft = round((random.random()*100) % 80, 1)
	ch = round((random.random()*100) % (100-ft), 1)
	return [ft, ch, round(100-ft-ch,1)]

# Function that african children haven't created yet
def get_food():
	root = os.path.dirname(os.path.abspath(__file__))
	files = os.listdir(root + '/menus')

	# Consists of category:meals_list
	all_menus = []

	for file_name in files:
		with open(root + "/menus/" + file_name) as f:
			data = f.read()

		lines = [i for i in data.split('\n') if i and i.split()[0]]

		# Consists of categories and meals, appropriete for these ones
		cats = {}

		for i in lines:
			# Always first line is category, so next won't crash
			if i.upper() == i:
				category = i.replace('\t\t', '')
				cats[category] = []
			else:
				# group - meal properties list. Consists of:
				# 	weight, name, price, calories, fats, carbohydrats, proteins
				group = i.split('\t')
				# Smart weigher
				weight = max([int(i) for i in re.findall(r"\d+", group[0])])
				group[0] = weight
				# AI recognizing meal calories
				group.append(random.randint(100,400))
				group += macros()

				cats[category].append(group)

		all_menus.append(cats)

	return all_menus
