import time
from AlphabetTrainer import AlphabetTrainer

def runGame(option: str) -> None:
   """Executa o jogo."""
   game = AlphabetTrainer(option)
   game.loadAlphabet()

   start_time = time.time()

   while game.alphabet:
      game.displayProgress()
      game.answer()

   end_time = time.time()
   elapsed_time = end_time - start_time

   game.displayProgress()

   if len(game.correctList) == 71:
      print("Extraordinário! você acertou todas as letras!")

      if elapsed_time <= 240: 
         print(f"Você concluiu em {elapsed_time:.2f} segundos. Você está muito rápido!")

      elif elapsed_time <= 420:
         print(f"Você concluiu em {elapsed_time:.2f} segundos. Continue praticando!")

      else:  
         print(f"Você concluiu em {elapsed_time:.2f} segundos. Com mais treino, você ficará mais rápido!")
      
      print(f"Acertos: {len(game.correctList)}")
      print(f"Erros: {len(game.wrongList)}")

   if len(game.correctList) > len(game.wrongList):
      print(f"Parabéns! você acertou a maior parte das letras!")

      if elapsed_time <= 240: 
         print(f"Você concluiu em {elapsed_time:.2f} segundos. Você está muito rápido!")

      elif elapsed_time <= 420:
         print(f"Você concluiu em {elapsed_time:.2f} segundos. Continue praticando!")

      else:  
         print(f"Você concluiu em {elapsed_time:.2f} segundos. Com mais treino, você ficará mais rápido!")
      
      print(f"Acertos: {len(game.correctList)}")
      print(f"Erros: {len(game.wrongList)}")

   else:
      print(f"Não foi dessa vez, mas com prática você vai dominar isso! Continue tentando! 💪")
      print(f"Você concluiu em  {elapsed_time:.2f} segundos.")
      print(f"Acertos: {len(game.correctList)}")
      print(f"Erros: {len(game.wrongList)}")
