#get and format data

#import mini_data
import csv

#Episode Class definition
class Episode:
  def __init__(self, round_number, air_date):
    self.round_number = round_number
    self.air_date = air_date
    self.single_jeopardy = Round("Single Jeopardy")
    self.double_jeopardy = Round("Double Jeopardy")
    self.final_jeopardy = Round("FinalJeopardy")

class Round:
  def __init__(self, name):
    self.name = name
    self.categories = []

class Category:
  def __init__(self, name):
    self.name = name 
    self.questions = []

class Question:
  def __init__(self, clue_value, daily_double_value, answer, question):
    self.clue_value = clue_value
    self.daily_double_value = daily_double_value
    self.answer = answer
    self.question = question


#Method to gather information
episodes = []

#read the file
with open('mini_data.tsv', 'r', encoding='utf-8') as tsvfile:
  reader = csv.DictReader(tsvfile, delimiter='\t')

  current_episode = None

  for row in reader:
    round_number = int(row['round'])
    clue_value = int(row['clue_value'])
    daily_double_value = int(row['daily_double_value'])
    category_name = row['category']
    answer = row['answer']
    question = row['question']
    air_date = row['air_date']

    if current_episode is None or current_episode.air_date != air_date:
      current_episode = Episode(round_number, air_date)
      episodes.append(current_episode)

    # Find the round within the episode based on the round number
    if round_number == 1:
      current_round = current_episode.single_jeopardy
    elif round_number == 2:
      current_round = current_episode.double_jeopardy
    elif round_number == 3:
      current_round = current_episode.final_jeopardy

    # Find the category within the round based on the category name
    current_category = None
    for category in current_round.categories:
      if category.name == category_name:
        current_category = category
        break
    
    # If the category does not exist, create a new one and add it to the round
    if current_category is None:
      current_category = Category(category_name)
      current_round.categories.append(current_category)
    
    # Create an instance of the Question class and add it to the category
    current_question = Question(clue_value, daily_double_value, answer, question)
    current_category.questions.append(current_question)

# Print the information from the created instances
for episode in episodes:
  print("Air Date:", episode.air_date)
  print("Single Jeopardy Categories:")
  for category in episode.single_jeopardy.categories:
    print("- Category:", category.name)
  print("Double Jeopardy Categories:")
  for category in episode.double_jeopardy.categories:
    print("- Category:", category.name)
    '''for question in category.questions:
      print("-- Clue Value:", question.clue_value)
      print("-- Daily Double Value:", question.daily_double_value)
      print("-- Answer:", question.answer)
      print("-- Question:", question.question)
  print("Double Jeopardy Categories:")
  for category in episode.double_jeopardy.categories:
    print("- Category:", category.name)
    for question in category.questions:
      print("-- Clue Value:", question.clue_value)
      print("-- Daily Double Value:", question.daily_double_value)
      print("-- Answer:", question.answer)
      print("-- Question:", question.question)'''
  print()