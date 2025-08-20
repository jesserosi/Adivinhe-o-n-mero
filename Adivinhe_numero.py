
import random

numero_aleatorio = random.randint(1, 10)
tentativas = 0
acertou = False
nome = input("Digite seu nome:")
print("nome")


while not acertou:
        try: 
            numero = int(input("Digite um numero de 1 a 10:"))
            tentativas += 1

            if numero  == numero_aleatorio:
                acertou = True
                print(f"Parabéns! Você acertou em {tentativas} tentativas.")
                break
            elif numero < numero_aleatorio:
                 print("muito baixo. Tente novamente")
            elif numero > numero_aleatorio:
                 print("Muito alto. Tente novamete")
        except ValueError:
            print("Entrada inválida. Digite um número inteiro.")
