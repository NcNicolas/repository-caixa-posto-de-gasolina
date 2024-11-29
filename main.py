# valor da gasolina
def gasolina(a):
    a = a * 6.60
    return a


# valor da gasolina aditivada
def gasolinaadv(a):
    a = a * 6.77
    return a


# valor do oleo s10 e comum
def oleo(a):
    a = a * 6.59
    return a
 
def numeracao():
    nume1 = ponto(input("Numeração 1: "))
    nume2 = ponto(input("Numeração 2: "))
    nume1 = float(nume1)
    nume2 = float(nume2)
    if nume1 < nume2:
        litros = float(nume2 - nume1)
    else:
        litros = float(nume1 - nume2)
    return litros

 #Troca a , por . para evitar erros
def ponto(a):
    b = ',' in a
    if b:
        c = a.replace(",", ".")
    else:
        return a
    return c


RED = "\033[31m"
GREEN = "\033[32m"
RESET = "\033[0m"

print("=" * 46)
print(f'{"CAIXA":>25}')
print("=" * 46)

print("")
# Bombas de Gasolina
print("Gasolina")
litros_bomba_gasolina1 = numeracao()
reais_bomba_gasolina1 = gasolina(litros_bomba_gasolina1)
print(f"Litros: ", RED + F"{litros_bomba_gasolina1:.2f}" + RESET, "Reais: ",
      GREEN + f"{reais_bomba_gasolina1:.2f}" + RESET)

print("=" * 46)

print("Gasolina2")
litros_bomba_gasolina2 = numeracao()
reais_bomba_gasolina2 = gasolina(litros_bomba_gasolina2)
print(f"Litros: ", RED + f"{litros_bomba_gasolina2:.2f}" + RESET, "Reais: ",
      GREEN + f"{reais_bomba_gasolina2:.2f}" + RESET)
print("=" * 46)

print("Gasolina3")
litros_bomba_gasolina3 = numeracao()
reais_bomba_gasolina3 = gasolina(litros_bomba_gasolina3)
print(f"Litros: ", RED + f"{litros_bomba_gasolina3:.2f}" + RESET, "Reais: ",
      GREEN + f"{reais_bomba_gasolina3:.2f}" + RESET)
print("=" * 46)

# Bomba Gasolina Aditivada
print(f"Gasolina Aditivada")
print("V-Power")
litros_bomba_gasolina_adv = numeracao()
reais_bomba_gasolina_adv = gasolinaadv(litros_bomba_gasolina_adv)
print(f"litros: ", RED + f"{litros_bomba_gasolina_adv:.2f}" + RESET, "Reais :",
      GREEN + f"{reais_bomba_gasolina_adv:.2f}" + RESET)
print("=" * 46)

# Bomba oleo Comum e S10
print("     Oleo Comum & S10     ")
print("S-10")
litros_bomba_oleo_s10 = numeracao()
reais_bomba_oelo_s10 = oleo(litros_bomba_oleo_s10)
print(f"litros: ", RED + f"{litros_bomba_oleo_s10:.2f}" + RESET, "Reias :",
      GREEN + f"{reais_bomba_oelo_s10:.2f}" + RESET)

print("=" * 46)

print("S-10")
litros_bomba_oleo_s10_2 = numeracao()
reais_bomba_oelo_s10_2 = oleo(litros_bomba_oleo_s10_2)
print(f"litros:", RED + f"{litros_bomba_oleo_s10:.2f}" + RESET, "reias:",
      GREEN + f"{reais_bomba_oelo_s10_2:.2f}" + RESET)
print("=" * 46)

print("S-500")
litros_bomba_oleo_s500 = numeracao()
reais_bomba_oelo_s500 = oleo(litros_bomba_oleo_s500)
print(f"litros:", RED + f"{litros_bomba_oleo_s500:.2f}" + RESET, "reias:",
      GREEN + f"{reais_bomba_oelo_s500:.2f}" + RESET)

diversos = float(input("Diversos:"))

Total_litros = sum([litros_bomba_oleo_s10, litros_bomba_oleo_s10_2, litros_bomba_gasolina1, litros_bomba_gasolina2,
                    litros_bomba_gasolina3, litros_bomba_gasolina_adv, litros_bomba_oleo_s500])
Total_reias = sum(
    [reais_bomba_oelo_s10, reais_bomba_gasolina1, reais_bomba_oelo_s10_2, reais_bomba_gasolina2, reais_bomba_gasolina3,
     reais_bomba_oelo_s500, reais_bomba_gasolina_adv])
total_gasolina = sum([litros_bomba_gasolina1, litros_bomba_gasolina2, litros_bomba_gasolina3])
total_s10 = sum([litros_bomba_oleo_s10, litros_bomba_oleo_s10_2])
print("=" * 46)

valor_litros_gasolina = float(input("Litros Gasolina dia anterior: "))
valor_litros_s10 = float(input("Litros S-10 dia anterior: "))
valor_litros_s500 = float(input("Litros S500 dia anterior: "))
valor_litros_vpower = float(input("Litros V-Power dias anterior: "))
print("=" * 46)

print("")
print("")
print(f"Gasolina:", RED + f"{litros_bomba_gasolina1:<10}" + RESET, "->", GREEN + f"{reais_bomba_gasolina1:.2f}" + RESET)
print(f"Gasolina:", RED + f"{litros_bomba_gasolina2:<10}" + RESET, "->", GREEN + f"{reais_bomba_gasolina2:.2f}" + RESET)
print(f"Gasolina:", RED + f"{litros_bomba_gasolina3:<10}" + RESET, "->", GREEN + f"{reais_bomba_gasolina3:.2f}" + RESET)
print(f"V-Power :", RED + f"{litros_bomba_gasolina_adv:<10}" + RESET, "->",
      GREEN + f"{reais_bomba_gasolina_adv:.2f}" + RESET)
print(f"S-10    :", RED + f"{litros_bomba_oleo_s10:<10}" + RESET, "->", GREEN + f"{reais_bomba_oelo_s10:.2f}" + RESET)
print(f"S-10    :", RED + f"{litros_bomba_oleo_s10_2:<10}" + RESET, "->",
      GREEN + f"{reais_bomba_oelo_s10_2:.2f}" + RESET)
print(f"S-500   :", RED + f"{litros_bomba_oleo_s500:<10}" + RESET, "->", GREEN + f"{reais_bomba_oelo_s500:.2f}" + RESET)
print(f"Total Reais :", GREEN + f"{Total_reias:.2f}" + RESET)
print(f"Total Reais + Diversos :", GREEN + f"{Total_reias + diversos:.2f}" + RESET)
print("")
print("")
print(f"{'Gasolina':<11} | {'S-10':<11} | {'S-500':<11} | {'V-Power'}")

print(GREEN + f"{valor_litros_gasolina:<11}" + RESET, "|", GREEN + f"{valor_litros_s10:<11}" + RESET, "|",
      GREEN + f"{valor_litros_s500:<11}" + RESET, "|", GREEN +
      f"{valor_litros_vpower}" + RESET)
print(RED + f"{total_gasolina:<11}" + RESET, "|", RED + f"{total_s10:<11}" + RESET, "|",
      RED + f"{litros_bomba_oleo_s500:<11}" + RESET, "|", RED +
      f"{litros_bomba_gasolina_adv}" + RESET)
print(GREEN + f"{valor_litros_gasolina - total_gasolina:<11}" + RESET, "|",
      GREEN + f"{valor_litros_s10 - total_s10:<11}" + RESET, "|",
      GREEN + f"{valor_litros_s500 - litros_bomba_oleo_s500:<11}" + RESET, "|",
      GREEN + f"{valor_litros_vpower - litros_bomba_gasolina_adv}" + RESET)
while True:
    comando = input("Digite 'sair' para encerrar o programa: ")
    if comando.lower() == 'sair':
        break
