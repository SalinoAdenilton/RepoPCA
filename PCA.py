class Question:
     def __init__(self, prompt, answer):
          self.prompt = prompt
          self.answer = answer
question_prompts = [
     "É possível compartilhar objetos sem transmitir Covid-19?\n(a) Verdadeiro\n(b) Falso\nResposta: ",'\n'
     "Uma pessoa pode estar infectada mesmo 14 dias antes de apresentar os sintomas?\n(a) Verdadeiro\n(b) Falso\nResposta: ",'\n'
    "É possível contaminar outras pessoas mesmo sem sintomas?\n (a) Sim\n (b) Não\nResposta: ", '\n'
    "Quando foi relatado o primeiro caso de Covid-19 no mundo?\n (a) 13/11/2019\n (b) 21/01/2020\n (c) 01/12/2019\n (d) Nenhuma das alternativas\nResposta: ", '\n'
    "A cidade onde ocorreu o primeiro caso de Covid-19 foi Beijing, China!\n (a) Verdadeiro\n (b) Falso\nResposta: ", '\n'
]
print('-------------------------')
print('-------------------------')
print('      QUIZ DO COVID')
print('-------------------------')
print('-------------------------')
name = input("Por favor, diga seu nome: ").title()
questions = [
     Question(question_prompts[0], "b"),
     Question(question_prompts[1], "a"),
    Question(question_prompts[2], "a"),
    Question(question_prompts[3], "c"),
    Question(question_prompts[4], "b")
              ]
def run_quiz(questions):
     score = 0
     for question in questions:
          answer = input(question.prompt)
          if answer == question.answer:
               score += 1
     print("\n{0}, Você acertou {1} das {2} perguntas.".format(name, score, len(questions)))
run_quiz(questions)
input("Aperte Enter para sair do jogo!")