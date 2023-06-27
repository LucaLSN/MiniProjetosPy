import time 
redtext='\033[91m'

print("Bem vindo ao Conversor de Temperatura F°>C°")
time.sleep(1)
print("\33[91m\33[1mPor favor, digite a temperatura em F°")
tempf= float(input("Temperatura:"))
tempc = round(((tempf-32)*5/9),1)
time.sleep(2)
print("\33[93mCalculando...")
time.sleep(3)
print(f"Temperatura digitada F°: {tempf} equivale a {tempc} Graus Celcius")