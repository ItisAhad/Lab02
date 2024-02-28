#---------------------------------------
#  Question Bank
#    Student B
#---------------------------------------

import random

# Simplified example with one category. Expand as needed.
questions = {
    "Science": [
        ("What is the chemical symbol for water?", "H2O"),
        ("What is the most common gas in our atmosphere?","Nitrogen")
        ("How many elements are there in a periodic table?","118")
    ],
    "History":[
        ("When was Pakistan made","1947")
        ("Who is Pakistan current Prime Minister?","Imran Khan")
        ("What is Pakistans National Sport","Hockey")
        ("Who started World War 2?","Hitler")
    ],
    "Maths":[
        ("What is the square of 2?","4")
        ("What is the inverse of cos?","sec")
        ("Find out area of the square?","a^2")
    ]
}

hints = {
    "Science": [
        ("It is made up by the gas that we breath in")
        ("It is not oxygen ")
        ("It is less than 120")
    ],
    "History":[
        ("India also has the same date")
        ("He is a world winning captain of pakistan team")
        ("It is not cricket")
        ("He had German Nationality")
    ],
    "Maths":[
        ("It is less than 5")
        ("It starts with the letter S")
        ("All sides of square are the same")
    ]
    # Repeat for other categories as needed.
}

#---------------------------------------

def select_random_question(category):
    """
    Selects a random question from the specified category.

    Parameters:
    - category (str): The category from which to select a question.

    Returns:
    - tuple: A tuple containing the selected question (str) and its corresponding answer (str).
    """
    #------------------------
   questions_list=("Maths","Science","History")
   random_questions=select_random_questions(questions_list)

   def select_random_questions(questions)
      if not questions
        print("No questions")
        return None
      
      random_question=random.choice(questions)
      return random_question

      if random_question:
        print("Random Question:",random.question)
    #------------------------
    raise NotImplementedError("This function is not implemented yet.")
    #------------------------

#---------------------------------------

def check_answer(player_answer, correct_answer):
    """
    Checks if the player's answer matches the correct answer.

    Parameters:
    - player_answer (str): The answer provided by the player.
    - correct_answer (str): The correct answer to the question.

    Returns:
    - bool: True if the answers match, False otherwise.
    """
    #------------------------
    if player_answer== correct_answer:
      return True
    else
      return False
    #------------------------
    raise NotImplementedError("This function is not implemented yet.")
    #------------------------

#---------------------------------------

def remove_question(category, question):
    """
    Removes a question from the list once it has been asked.

    Parameters:
    - category (str): The category from which to remove the question.
    - question (str): The question to be removed.

    Returns:
    - None
    """
    #------------------------
    # Add your code here
    #------------------------
    raise NotImplementedError("This function is not implemented yet.")
    #------------------------

#---------------------------------------

def display_question_and_accept_answer(question):
    """
    Displays a question to the player and accepts their answer via input.

    Parameters:
    - question (str): The question to be displayed.

    Returns:
    - str: The player's answer to the question.
    """
    #------------------------
  answers=input("Enter your answer:")
  print("Questions:",question)
  return answers
    #------------------------
    raise NotImplementedError("This function is not implemented yet.")
    #------------------------

#---------------------------------------

def provide_hint(category, question):
    """
    Provides a hint for the given question based on its category.

    Parameters:
    - category (str): The category of the question.
    - question (str): The question for which to provide a hint.

    Returns:
    - str: The hint for the given question.
    """
    #------------------------
    # Add your code here
    #------------------------
    raise NotImplementedError("This function is not implemented yet.")
    #------------------------

#---------------------------------------

def display_correct_answer(correct_answer):
    """
    Displays the correct answer if the player's answer is incorrect.

    Parameters:
    - correct_answer (str): The correct answer to the question.

    Returns:
    - None
    """
    #------------------------
   if not(answer_check(player_answer,correct_answer))
     print(correct_answer)
    #------------------------
    raise NotImplementedError("This function is not implemented yet.")
    #------------------------

#---------------------------------------

remove_question("Science","How many elements are there in a periodic table?")
print(question)


