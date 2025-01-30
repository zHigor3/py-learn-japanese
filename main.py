import inquirer
from runGame import runGame

def main() -> None:
   """Ponto de entrada do programa."""
   options = ["hiragana", "katakana", "todos", "sair"]
   question = [
      inquirer.List(
         "escolha",
         message="Selecione qual alfabeto deseja treinar:",
         choices=options,
      )
   ]

   answer = inquirer.prompt(question)

   if answer and answer["escolha"] != "sair":
      runGame(answer["escolha"])
   else:
      print("Treinamento encerrado. Até a próxima!")


if __name__ == "__main__":
   main()
