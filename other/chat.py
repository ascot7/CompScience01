'''
Chat Program  v.1
Lawrence Nelson
April 2013

Simulates a Chat with user.  
Computer learns how to hold a simple conversation.

'''


from __future__ import print_function

import random
import time

# ********************************************
def clean(string):
  for letter in string:
    if letter.isalpha()== False:
      string = string.replace(letter, "")
      
  return string


# ********************************************
def scrollprint (stuffToPrint):
  
  
  
  time.sleep(0.7)

  for i in range (len(stuffToPrint)):
    letter = stuffToPrint[i]
    print(letter, end = '')
    if letter == " ":
      time.sleep (0.01)
    elif letter == ".":
      time.sleep (0.1)
    else:
      time.sleep (0.08)                        
    
  print (' ')
  return

# ********************************************

# Main Program Starts Here

  


affirmative = {"yes", "yep", "yeah", "ya"}

done = False					  
abuseCount = 0


questionFile = open("question.txt", 'r')
answerFile = open("answer.txt", 'r')

i = 0
question = "start"
questionList = {}
while question != "":
  i = i + 1
  question = questionFile.readline()
  answer = answerFile.readline()
  question = question.strip()
  answer = answer.strip()
  questionList[question] = answer
  
questionFile.close()
answerFile.close()

numberofquestions = i

userQuestion = str(input("WRITE SOMETHING: (suggestion: start with hello!)\n"))
question = clean(userQuestion)

quitt = {"bye", "goodbye", "byebye", "later", "ltr", "ciao", "culater", "cya", "seeyoulater", "peace", "peaceout"}

while question.lower() not in quitt:
  
  question = question.upper()
  if question in questionList:
    scrollprint (questionList[question])
  else:
    
      
      r = int(random.random() * 6)
      if r == 0: scrollprint ("I DON'T UNDERSTAND. HOW DO YOU ANSWER THAT?")
      elif r == 1:  scrollprint ("I DON'T KNOW THE ANSWER.  WHAT DO YOU THINK?")
      elif r == 2:  scrollprint ("NOT SURE.  WHAT IS THE ANSWER?")
      elif r == 3:  scrollprint ("I COULDN'T SAY.  WHAT DO YOU THINK?")
      elif r == 4:  scrollprint ("Wut?")
      elif r == 5:  scrollprint ("Um, is that a question?")
      elif r == 6:  scrollprint ("Hm...")      
      
      
      userAnswer = str(input())
      
      userQuestion = clean(userQuestion.upper())
      userAnswer = userAnswer.upper()
      
      numberofquestions = numberofquestions + 1
      questionList[userQuestion] = userAnswer
              
      questionFile = open("question.txt", 'a')
      answerFile = open("answer.txt", 'a')
      questionFile.write(userQuestion+'\n')
      answerFile.write(userAnswer+'\n')
  
      questionFile.close()
      answerFile.close()
  
      scrollprint ("OKAY, THANKS. NOW ASK ME ANOTHER QUESTION")
  
  userQuestion = str(input())
  question = clean(userQuestion)

r = int(random.random() * 3)
if r == 0: scrollprint ("LATER SKATER.")
if r == 1:  scrollprint ("PEACE OUT.")
if r == 2:  scrollprint ("THANKS FOR THE TALK")
if r == 3: scrollprint ("BYE!")








