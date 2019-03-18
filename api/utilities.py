import os
import random
import re
import pprint
import requests
from decimal import Decimal
from datetime import time
from os.path import join

from cafeterias.models import Cafeteria
from schedules.models import Schedule
from categories.models import Category
from food.models import FoodItem, FoodProps


# Machine-learned neural network that defines macroelements proportions
def macros():
	ft = round((random.random()*100) % 80, 1)
	ch = round((random.random()*100) % (100-ft), 1)
	return [ft, ch, round(100-ft-ch,1)]

# Function that african children haven't created yet
def get_food():
	''' This function reads file and returns data structure,
		containing all meal properties '''
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


def db_loader():
	c1 = Cafeteria.objects.create(name="Ключ на старт!")
	c2 = Cafeteria.objects.create(name="Бауманская столовка")
	c3 = Cafeteria.objects.create(name="ИмпВысТех Столовка")

	cafe_list = [c1, c2, c3]

	all_schedules = get_food()

	known_names = []

	times = [
	    (time(9,0), time(20,0)),
	    (time(9,30), time(19,30)),
	    (time(8,0), time(20,30))
	    ]

	for day in range(5):
		for cafei in range(3):
			sch = Schedule.objects.create(
			    week_day=day, cafe=cafe_list[cafei], open_time=times[cafei][0],
			    close_time=times[cafei][1]
				)
			day_menu = all_schedules[(day + cafei*2) % 6]
			for cat in list(day_menu.keys()):
				cat_obj = Category.objects.create(name=cat, sched=sch)
				for props in day_menu[cat]:
					if props[1] not in known_names:
						fp = FoodProps(
							weight		=props[0],
							name		=props[1],
							price		=Decimal(float(props[2])),
							cal			=props[3],
							fat			=Decimal(float(props[4])),
							carbohydrats=Decimal(float(props[5])),
							proteins	=Decimal(float(props[6])),
							)
						fp.save()
						FoodItem.objects.create(cat=cat_obj, props=fp)
						known_names.append(props[1])
					else:
						fpx = FoodProps.objects.get(name=props[1])
						FoodItem.objects.create(cat=cat_obj, props=fpx)


	sch = Schedule.objects.create(
	    week_day=5 , cafe=c1, open_time=time(10, 0),
	    close_time=time(16, 0)
	    )
	day_menu = all_schedules[5]
	for cat in list(day_menu.keys()):
		cat_obj = Category.objects.create(name=cat, sched=sch)
		for props in day_menu[cat]:
			if props[1] not in known_names:
				fp = FoodProps.objects.create(
					weight		=props[0],
					name		=props[1],
					price		=Decimal(float(props[2])),
					cal			=props[3],
					fat			=Decimal(float(props[4])),
					carbohydrats=Decimal(float(props[5])),
					proteins	=Decimal(float(props[6])),
					)
				FoodItem.objects.create(cat=cat_obj, props=fp)
				known_names.append(props[1])
			else:
				fpx = FoodProps.objects.get(name=props[1])
				FoodItem.objects.create(cat=cat_obj, props=fpx)

	sch = Schedule.objects.create(
	    week_day=5, cafe=c2, open_time=time(9, 30),
	    close_time=time(19, 30)
	    )
	day_menu = all_schedules[1]
	for cat in list(day_menu.keys()):
		cat_obj = Category.objects.create(name=cat, sched=sch)
		for props in day_menu[cat]:
			if props[0] not in known_names:
				fp = FoodProps.objects.create(
					weight		=props[0],
					name		=props[1],
					price		=Decimal(float(props[2])),
					cal			=props[3],
					fat			=Decimal(float(props[4])),
					carbohydrats=Decimal(float(props[5])),
					proteins	=Decimal(float(props[6])),
					)
				FoodItem.objects.create(cat=cat_obj, props=fp)
				known_names.append(props[1])
			else:
				fpx = FoodProps.objects.get(name=props[1])
				FoodItem.objects.create(cat=cat_obj, props=fpx)


def image_url(query):
	print(query)
	r = requests.get("https://api.qwant.com/api/search/images",
	    params={
	        'count': 1,
	        'q': query,
	        't': 'images',
	        'uiv': 4
	    },
	    headers={
	        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
	    }
	)

	response = r.json().get('data').get('result').get('items')

	if not response:
		print(query)
		return 0
	return response[0].get('media')


# Searches and downloads images of food
# This function is unstable, because during requests may errors occur
# and you need to restart function
def image_downloader():
	start_pk = 0
	path = "/home/bunt/Desktop/djangoproject/mobileapi/static/"
	for meal in FoodProps.objects.all()[start_pk:]:
		url = image_url(meal.name)
		if not url:
			continue
		# Leave only filename with extension
		filename = url.split('/')[-1].split('?')[0]
		ext = filename.split('.')[1]
		img_data = requests.get(url).content
		meal.image = str(meal.pk) + '.' + ext
		meal.save()
		with open(path + meal.image, 'wb') as handler:
		    handler.write(img_data)
