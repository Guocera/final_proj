from random import randint, choice
from .models import *

def get_meals(label):
  meals = []
  labels = MealLabel.objects.filter(label=label)

  for label in labels:
    meals.append(label.recipe)

  return meals

def generate_plan_meeting_nutrition(meals, nutrition):
  tries = 0
  while True:
    tries += 1
    for i, meal in enumerate(meals):
      meals[i] = choice(meals[i])
    # if nutrition_met(meals, nutrition):
    #   break
    # if tries == 5000:
    #   print("No meal plans can be generated for nutrional requirements.")
    #   break
    break
  return meals

def nutrition_met(meals, nutrition):
  pass