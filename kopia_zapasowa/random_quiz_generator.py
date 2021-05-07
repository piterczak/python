#! python3
 # randomQuizGenerator.py - Creates quizzes with questions and answers in
# random order, along with the answer key.
import random
# The quiz data. Keys are states and values are their capitals.
capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
   'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
   'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
   'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
   'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
   'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
   'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
   'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
   'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
   'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New Mexico': 'Santa Fe', 'New York': 'Albany',
   'North Carolina': 'Raleigh', 'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
   'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
   'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
   'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
   'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

   # Generate 35 quiz files.
for quizNum in range(35):
   #create the quiz and answer key files.
   quizFile = open(f'capitalsquiz{quizNum+1}.txt', 'w')
   answerKeyFile = open(f'capitalsquiz_answers{quizNum+1}.txt','w')
   #header for quiz
   quizFile.write('Name:\n\nDate:\n\nPeriod:\n\n')
   quizFile.write((''*20)+f'State Capitals Quiz (Form{quizNum+1})')
   quizFile.write('\n\n')
   
   states=list(capitals.keys())
   #shuffling the list States, that involve capitals.keys 
   random.shuffle(states)

   for i in range(50):
      #looping through 50 states to write questions in file 
      #get right and wrong answers
      correct_answer = capitals[states[i]]
      wrong_answers = list(capitals.values())
      del wrong_answers[wrong_answers.index(correct_answer)]
      wrong_answers = random.sample(wrong_answers, 3)
      answer_options = wrong_answers + [correct_answer]
      random.shuffle(answer_options)



      quizFile.write(f'{i+1}. What is the capital of the State  {states[i]}\n')
      for j in range(4):
         quizFile.write(f" {'ABCD'[j]}.{answer_options[j]} \n")


      #write answers to the key file
      answerKeyFile.write(f"{i+1}.")
      answerKeyFile.write(f"{'ABCD'[answer_options.index(correct_answer)]} \n")

   quizFile.write('Thank you for taking part in the test. Scores will be stated on my website')
   quizFile.close()
   answerKeyFile.close()
