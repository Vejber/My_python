# Нужно написать программу - Тест с выбором ответов. 
# Каждый вопрос в тесте должен содержать 4 варианта ответов, количество вопросов >= 5. 
# Программа должна подсчитывать количество правильных и неправильных ответов, и в конце выдавать результат. 
# Если результат теста неудовлетворительный, то программа должна предложить пользователю пройти тест повторно.

def problem(rigth_answer: int, student_answer: str):
    student_answer = int(student_answer)
    if rigth_answer == student_answer:
        return 1
    else:
        return 0

import random

def test_cycle():
    i = 1
    count = 0
    while i <= 5:
       number1 = random.randint(1, 10)
       number2 = random.randint(1, 10)
       sum = number1 + number2
       print("{} + {} = ?". format(number1, number2))
       answer = str(input("Enter your answer > "))
       test1 = problem(sum, answer)
       if test1 == 1:
         count = count + 1
       i = i + 1
    print("Your score is {}.". format(count))
    if count < 4:
      print("Try again.")
      test_cycle()

test_cycle()



