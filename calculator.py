# Mini programme d'opérations simples

# On définit deux nombres
a = 12
b = 4

print(f"a = {a} et b = {b}")
print("--------------------")

# Opérations
addition = a + b
soustraction = a - b
multiplication = a * b
division = a / b
puissance = a ** b
reste = a % b

# Affichage des résultats
print(f"Addition : {a} + {b} = {addition}")
print(f"Soustraction : {a} - {b} = {soustraction}")
print(f"Multiplication : {a} * {b} = {multiplication}")
print(f"Division : {a} / {b} = {division}")
print(f"Puissance : {a} ** {b} = {puissance}")
print(f"Reste de la division : {a} % {b} = {reste}")

# Un petit bonus : moyenne
moyenne = (a + b) / 2
print("--------------------")
print(f"La moyenne de {a} et {b} est : {moyenne}")