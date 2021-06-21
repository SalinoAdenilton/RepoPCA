from random import randint

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
     "Para prevenir o contágio, é aconselhado que se use uma máscara PFF2, também chamada de N92?\n (a) Verdadeiro\n (b) Falso\n Resposta: ", '\n'
     "Qual das alternativas abaixo é um dos sintomas claros da Covid-19?\n (a) Febre\n (b) Coceira\n (c) Desmaio\n (d) Perda de cabelo\n Resposta: ", '\n'
     "Pessoas com idade avançada ou com doenças pulmonares são mais propensas a terem casos mais graves?\n (a) Verdadeiro\n (b) Falso\n Resposta: ", '\n'
     "Estar em locais com um número considerável de pessoas trará mais chances de contaminação?\n (a) Verdadeiro\n (b) Falso\n Resposta: ", '\n'
     "A vacina para gripe também é eficaz contra o vírus da Covid-19?\n (a) Verdadeiro\n (b) Falso\n Resposta: ", '\n'
     "Álcool isopropílico é o mais recomendado para se prevenir de ser contaminado?\n (a) Verdadeiro\n (b) Falso\n Resposta: ", '\n'
     "O coronavírus pode ser transmitido através de quais situações?\n (a) Ao inalar fumaça\n (b) Pelo ar\n (c) Superfícies contaminadas\n (d) Ao ingerir alimentos à base de soja\n Resposta: ", '\n'
     "Caso se agrave muito, o coronavírus pode causar a morte?\n (a) Verdadeiro\n (b) Falso\n Resposta: ", '\n'
     "O que fazer, caso sinta algum dos sintomas relacionados?\n (a) Correr ao ar livre\n (b) Procurar ajuda médica imediata\n (c) Manter contato apenas com pessoas próximas\n (d) Nenhuma das alternativas\n Resposta: ", '\n'
     "Atualmente, existem métodos 100'%' eficazes contra o coronavírus?\n (a) Verdadeiro\n (b) Falso\n Resposta: ", '\n'


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
     Question(question_prompts[4], "b"),
     Question(question_prompts[5], "b"),
     Question(question_prompts[6], "a"),
     Question(question_prompts[7], "a"),
     Question(question_prompts[8], "a"),
     Question(question_prompts[9], "b"),
     Question(question_prompts[10], "b"),
     Question(question_prompts[11], "c"),
     Question(question_prompts[12], "a"),
     Question(question_prompts[13], "d"),
     Question(question_prompts[14], "b"),
              ]
def run_quiz(questions):
     score = 0
     c = 0
     answered_questions = []
     while c<=4:
          random = randint(0, 14)
          question = questions[random]
          if question in answered_questions:
               continue
          answer = input(question.prompt)
          if answer == question.answer:
               score += 1
          c += 1
          answered_questions.append(question)
     print("\n{0}, Você acertou {1} das 5 perguntas.".format(name, score, len(questions)))

run_quiz(questions)
input("Aperte Enter para sair do jogo!")
