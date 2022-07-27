from replit import clear
import art
alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(start_text, shift_amount, cipher_direction):
  end_text = ""
  if cipher_direction == "decodificar":
    shift_amount *= -1
  for char in start_text:
    
    if not char in alfabeto:
      end_text += char
    else:
      position = alfabeto.index(char)
      new_position = position + shift_amount
      if new_position > 26:
        new_position -= 27
      end_text += alfabeto[new_position]
    
  print(f"Este es el resultado: {end_text}")

print(art.logo)

restart="si"
while restart=="si":
  direction = input("Escribe 'codificar' para encriptar, escribe 'decodificar' para desencriptar:\n")
  text = input("Escribe tu mensaje:\n").lower()
  shift = int(input("Escribe el número de desplazamiento:\n"))

  for i in range(27):
    if i%27 == shift%27:
      shift=i
  caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
  restart=input("Escirbe 'si' si quieres correr el programa de nuevo. De otra forma escribe 'no'.\n").lower()
  clear()