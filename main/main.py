
def gasolina(a):
    a = a * 6.60
    return a


def gasolinaadv(a):
    a = a * 6.77
    return a


def oleo(a):
    a = a * 6.59
    return a


def negative(Num1, Num2):
    if Num1 < Num2:
        a = float(f"{Num2 - Num1:.2f}")
    else:
        a = float(f'{Num1 - Num2:.2f}')
    return a

RED = "\033[31m"
GREEN = "\033[32m"
RESET = "\033[0m"


print("=" * 46)
print(f'{"CAIXA":>25}')
print("=" * 46)

print("")
#Bombas de Gasolina
print("Gasolina")
(Bomba_comum) = float(input("Numeração 1: "))
Bomba1_comum = float(input("Numeração 2: "))
result_bomba = negative(Bomba_comum, Bomba1_comum)
valor_em_reais = gasolina(result_bomba)
print(f"Litros: ", RED + F"{result_bomba:.2f}" + RESET,"Reais: ", GREEN +f"{valor_em_reais:.2f}" + RESET)

print("=" * 46)

print("Gasolina2")
Bomba_comum2 = float(input("Numeração 1: "))
Bomba_comum3 = float(input("Numeração 2: "))
result_bomba2 = negative(Bomba_comum2, Bomba_comum3)
valor_em_reais2 = gasolina(result_bomba2)
print(f"Litros: ", RED + f"{result_bomba2:.2f}" + RESET,"Reais: ", GREEN+ f"{valor_em_reais2:.2f}" + RESET)
print("=" * 46)

print("Gasolina3")
Bomba_comum4 = float(input("Numeração 1: "))
Bomba_comum5 = float(input("Numeração 2: "))
result_bomba3 = negative(Bomba_comum4, Bomba_comum5)
valor_em_reais3 = gasolina(result_bomba3)
print(f"Litros: ", RED + f"{result_bomba3:.2f}" + RESET,"Reais: ", GREEN + f"{valor_em_reais3:.2f}" + RESET)
print("=" * 46)

#Bomba Gasolina Aditivada
print(f"Gasolina Aditivada")
print("V-Power")
Bomba_adv = float(input("Numeração 1: "))
Bomba_adv2 = float(input("Numeração 2: "))
result_bomba4 = negative(Bomba_adv, Bomba_adv2)
valor_em_reais4 = gasolinaadv(result_bomba4)
print(f"litros: ", RED + f"{result_bomba4:.2f}" + RESET, "Reais :", GREEN + f"{valor_em_reais4:.2f}" + RESET)
print("=" * 46)

#Bomba oleo Comum e S10
print("     Oleo Comum & S10     ")
print("S-10")
bomba_s10 = float(input("Numeração 1: "))
bomba_s102 = float(input("Numeração 2: "))
result_bomba5 = negative(bomba_s10, bomba_s102)
valor_em_reais5 = oleo(result_bomba5)
print(f"litros: ", RED + f"{result_bomba5:.2f}" + RESET, "Reias :", GREEN + f"{valor_em_reais5:.2f}" + RESET )

print("=" * 46)

print("S-10")
bomba_s101 = float(input("Numeração 1: "))
bomba_s103 = float(input("Numeração 2: "))
result_bomba6 = negative(bomba_s101, bomba_s103)
valor_em_reais6 = oleo(result_bomba6)
print(f"litros:", RED + f"{result_bomba6:.2f}" + RESET, "reias:", GREEN + f"{valor_em_reais6:.2f}" + RESET)
print("=" * 46)

print("S-500")
bomba_s500 = float(input("Numeração 1: "))
bomba_s5002 = float(input("Numeração 2: "))
result_bomba7 = negative(bomba_s500, bomba_s5002)
valor_em_reais7 = oleo(result_bomba7)
print(f"litros:", RED + f"{result_bomba7:.2f}" + RESET, "reias:", GREEN + f"{valor_em_reais7:.2f}" + RESET)

Total_litros = float(result_bomba + result_bomba2 + result_bomba3 + result_bomba4 + result_bomba5 + result_bomba6 + result_bomba7)
Total_reias = float(valor_em_reais + valor_em_reais2 + valor_em_reais3 + valor_em_reais4 + valor_em_reais5 + valor_em_reais6 + valor_em_reais7)

print("=" * 46)

print(f"Gasolina:", RED + f"{result_bomba:<10}" + RESET,  "->", GREEN + f"{valor_em_reais:.2f}" + RESET)
print(f"Gasolina:", RED + f"{result_bomba2:<10}" + RESET, "->", GREEN + f"{valor_em_reais2:.2f}" + RESET)
print(f"Gasolina:", RED + f"{result_bomba3:<10}" + RESET, "->", GREEN + f"{valor_em_reais3:.2f}" + RESET)
print(f"V-Power:", RED + f"{result_bomba4:<10}" + RESET, "->", GREEN + f"{valor_em_reais4:.2f}" + RESET)
print(f"S-10:   ", RED + f"{result_bomba5:<10}" + RESET, "->", GREEN + f"{valor_em_reais5:.2f}" + RESET)
print(f"S-10:   ", RED + f"{result_bomba6:<10}" + RESET, "->", GREEN + f"{valor_em_reais6:.2f}" + RESET)
print(f"S-500:  ", RED + f"{result_bomba7:<10}" + RESET, "->", GREEN + f"{valor_em_reais7:.2f}" + RESET)
print(f"Total Reais :", GREEN +f"{Total_reias:.2f}" + RESET)
diversos = float(input("Diversos:"))
print("=" * 46)
print(F"Total litros:", RED +f"{Total_litros:.2f}" + RESET)
print(f"Total Reais + Diversos :", GREEN +f"{Total_reias + diversos:.2f}" + RESET)
print("=" * 46)

total_gasolina = result_bomba + result_bomba2 + result_bomba3
total_s10 = result_bomba5 + result_bomba6

valor_litros_gasolina = float(input("Litros G dia anterior: "))
valor_litros_s10 = float(input("Litros S-10 dia anterior: "))
valor_litros_s500 = float(input("Litros S500 dia anterior: "))
valor_litros_vpower = float(input("Litros V-Power dias anterior: "))

print("=" * 46)

print(f"{'Gasolina':<10} | {'S-10':<10} | {'S-500':<10} | {'V-Power'}")
print(GREEN + f"{valor_litros_gasolina:<10}" + RESET,"|",GREEN + f"{valor_litros_s10:<10}" + RESET, "|", GREEN + f"{valor_litros_s500:<10}" + RESET,"|", GREEN +
      f"{valor_litros_vpower}" + RESET)
print(RED + f"{total_gasolina:<10}" + RESET,"|",RED + f"{total_s10:<10}" + RESET, "|", RED + f"{result_bomba7:<10}" + RESET,"|", RED +
      f"{result_bomba4}" + RESET)
print(GREEN + f"{valor_litros_gasolina - total_gasolina:<10}" + RESET,"|", GREEN + f"{valor_litros_s10 - total_s10:<10}" + RESET, "|",
        GREEN + f"{valor_litros_s500 - result_bomba7:<10}" + RESET,"|", GREEN + f"{valor_litros_vpower - result_bomba4}" + RESET)

while True:
    comando = input("Digite 'sair' para encerrar o programa: ")
    if comando.lower() == 'sair':
        break
        
