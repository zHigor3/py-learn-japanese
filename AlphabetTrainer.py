import json
import random
import os

class AlphabetTrainer():
   def __init__(self, option: str):
      self.option = option
      self.alphabet = []
      self.wrongList = []
      self.correctList = []

   # Carrega o alfabeto escolhido
   def loadAlphabet(self):
      try:
         with open(f'./assets/{self.option}.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
            self.alphabet = data

      except Exception as e:
         print('Error --> ', e)

   # Seleciona uma letra aleatória e pergunta qual o som dela
   def answer(self):
      question = random.choice(self.alphabet)
      response = input(f"Qual o som dessa letra? {question['latter']}: ")

      if str(question['sound']).lower() == str(response).lower():
         self.correctAnswer(question)

      else:
         self.wrongAnswer(question)

   # Quando question for errado, remove letra do alfabeto e adiciona a lista de errados
   def wrongAnswer(self, question):
      self.wrongList.append(question)
      self.alphabet.remove(question)

   # Quando question for correto, remove letra do alfabeto e adiciona a lista de corretos
   def correctAnswer(self, question):
      self.correctList.append(question)
      self.alphabet.remove(question)
   
   # Display de progresso do treinamento
   def displayProgress(self):
      os.system('cls' if os.name == 'nt' else 'clear')

      print(f"Restam {len(self.alphabet)} letras para treinar.")
      print("Total acertado: ")
      correctStr = ', '.join(f"{i['latter']} - {i['sound']}" for i in self.correctList)
      print(correctStr if correctStr else "Nenhuma resposta correta até agora.")

      print("\nTotal de erros: ")
      wrongStr = ', '.join(f"{i['latter']} - {i['sound']}" for i in self.wrongList)
      print(wrongStr if wrongStr else "Nenhum erro até agora.")
      print()
