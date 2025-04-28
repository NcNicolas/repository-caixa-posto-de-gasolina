# valor da gasolina.
def gasolina(a):
    a = a * 6.69
    return a

def gasolina2(a):
    a = a * 6.89
    return a

# valor da gasolina aditivada.
def gasolinaadv(a):
    a = a * 6.99
    return a

# valor do oleo s10 e comum.
def oleo(a):
    a = a * 6.99
    return a

def oleo2(a):
    a = a * 6.79
    return a

def formatatacao_de_cores(valor):

    return f"{GREEN}"

# numerações das bombas
def numeracao():
    nume1 = ponto(input("Numeração(noite) 1: "))
    nume2 = ponto(input("Numeração(manhão) 2: "))
    if nume1 == "":
        nume1 = float(0)
        return nume1
    elif nume2 == "":
        nume2 = float(0)
        return nume2

    nume1 = float(nume1)
    nume2 = float(nume2)

    if nume1 < nume2:
        litros = float(nume2 - nume1)
    else:
        litros = float(nume1 - nume2)
    return litros


# Troca , por . para evitar erros.
def ponto(a):
    b = ',' in a
    if b:
        c = a.replace(",", ".")
    else:
        return a
    return c


# Cores no terminal
RED = "\033[31m"
GREEN = "\033[32m"
RESET = "\033[0m"

print("=" * 50)
print("CAIXA".center(50))
print("=" * 50)
print('Litragem dos tanques dia anterior')


try:
    valor_litros_gasolina = float(input("Tanque de gasolina(L): "))
except:
    valor_litros_gasolina = 0
try:
    valor_litros_s10 = float(input("Tanque de S-10(L): "))
except:
    valor_litros_s10 = 0
try:
    valor_litros_s500 = float(input("Tanque de s-500(L): "))
except:
    valor_litros_s500 = 0
try:
    valor_litros_vpower = float(input("Tanque de V-Power(L): "))
except:

    valor_litros_vpower = 0
print("")
# Bombas de Gasolina
print("Gasolina")
litros_bomba_gasolina1 = numeracao()
reais_bomba_gasolina1 = gasolina(litros_bomba_gasolina1)
print(f"Litros: ", RED + F"{litros_bomba_gasolina1:.2f}" + RESET, "Reais: ",
      GREEN + f"{reais_bomba_gasolina1:.2f}" + RESET)

print("=" * 50)

print("Gasolina2")
litros_bomba_gasolina2 = numeracao()
reais_bomba_gasolina2 = gasolina2(litros_bomba_gasolina2)
print(f"Litros: ", RED + f"{litros_bomba_gasolina2:.2f}" + RESET, "Reais: ",
      GREEN + f"{reais_bomba_gasolina2:.2f}" + RESET)
print("=" * 50)

print("Gasolina3")
litros_bomba_gasolina3 = numeracao()
reais_bomba_gasolina3 = gasolina(litros_bomba_gasolina3)
print(f"Litros: ", RED + f"{litros_bomba_gasolina3:.2f}" + RESET, "Reais: ",
      GREEN + f"{reais_bomba_gasolina3:.2f}" + RESET)
print("=" * 50)

# Bomba Gasolina Aditivada

print(f"Gasolina Aditivada")
print("V-Power")
litros_bomba_gasolina_adv = numeracao()
reais_bomba_gasolina_adv = gasolinaadv(litros_bomba_gasolina_adv)
print(f"litros: ", RED + f"{litros_bomba_gasolina_adv:.2f}" + RESET, "Reais :",
      GREEN + f"{reais_bomba_gasolina_adv:.2f}" + RESET)
print("=" * 50)

# Bomba oleo Comum e S10
print("Oleo Comum & S10")
print("S-10")
litros_bomba_oleo_s10_2 = numeracao()
reais_bomba_oelo_s10_2 = oleo(litros_bomba_oleo_s10_2)
print(f"litros: ", RED + f"{litros_bomba_oleo_s10_2:.2f}" + RESET, "Reias :",
      GREEN + f"{reais_bomba_oelo_s10_2:.2f}" + RESET)

print("=" * 50)

print("S-10")
litros_bomba_oleo_s10 = numeracao()
reais_bomba_oelo_s10 = oleo2(litros_bomba_oleo_s10)
print(f"litros:", RED + f"{litros_bomba_oleo_s10:.2f}" + RESET, "reias:",
      GREEN + f"{reais_bomba_oelo_s10:.2f}" + RESET)
print("=" * 50)

print("S-500")
litros_bomba_oleo_s500 = numeracao()
reais_bomba_oelo_s500 = oleo2(litros_bomba_oleo_s500)
print(f"litros:", RED + f"{litros_bomba_oleo_s500:.2f}" + RESET, "reias:",
      GREEN + f"{reais_bomba_oelo_s500:.2f}" + RESET)

# vendas a parte.

div = input("Diversos:")
if div == "":
    div = float(0)
diversos = float(div)
print(GREEN + f'{diversos}'+ RESET)

Total_litros = sum([litros_bomba_oleo_s10, litros_bomba_oleo_s10_2, litros_bomba_gasolina1, litros_bomba_gasolina2,
                    litros_bomba_gasolina3, litros_bomba_gasolina_adv, litros_bomba_oleo_s500])
Total_reias = sum(
    [reais_bomba_oelo_s10, reais_bomba_gasolina1, reais_bomba_oelo_s10_2, reais_bomba_gasolina2, reais_bomba_gasolina3,
     reais_bomba_oelo_s500, reais_bomba_gasolina_adv])
total_gasolina = sum([litros_bomba_gasolina1, litros_bomba_gasolina2, litros_bomba_gasolina3])
total_s10 = sum([litros_bomba_oleo_s10, litros_bomba_oleo_s10_2])
print("=" * 50)


#VENDAS DE COMBUSTIVEIS
print("=" * 50)
print('VENDA DE COMBUSTIVEIS'.center(50))
print("=" * 50)
print("")
print(f"{'Bico':<7} | {'Preço':<11} | {'Litros':<11} | {'Reais'}")
print(f"Gasolina:",f"{"6,69":<12}", RED + f"{"%.2f" % litros_bomba_gasolina1:<10}" + RESET, "->", GREEN + f"{reais_bomba_gasolina1:.2f}" + RESET)
print(f"Gasolina:",f"{"6,89":<12}", RED + f"{"%.2f" % litros_bomba_gasolina2:<10}" + RESET, "->", GREEN + f"{reais_bomba_gasolina2:.2f}" + RESET)
print(f"Gasolina:",f"{"6,69":<12}", RED + f"{"%.2f" % litros_bomba_gasolina3:<10}" + RESET, "->", GREEN + f"{reais_bomba_gasolina3:.2f}" + RESET)
print(f"V-Power :",f"{"6,99":<12}", RED + f"{"%.2f" % litros_bomba_gasolina_adv:<10}" + RESET, "->",
      GREEN + f"{reais_bomba_gasolina_adv:.2f}" + RESET)
print(f"S-10    :"f"{"6,79":<12}", RED + f"{"%.2f" % litros_bomba_oleo_s10:<10}" + RESET, "->", GREEN + f"{reais_bomba_oelo_s10:.2f}" + RESET)
print(f"S-10    :"f"{"6,89":<12}", RED + f"{"%.2f" % litros_bomba_oleo_s10_2:<10}" + RESET, "->",
      GREEN + f"{reais_bomba_oelo_s10_2:.2f}" + RESET)
print(f"S-500   :", f"{"6,79":<12}", RED + f"{"%.2f" % litros_bomba_oleo_s500:<10}" + RESET, "->", GREEN + f"{reais_bomba_oelo_s500:.2f}" + RESET)
print(f"Total Reais :", GREEN + f"{Total_reias:.2f}" + RESET)
print(f"Total Diversos:", GREEN + f'{diversos}'+ RESET)
print(f"Total Reais + Diversos :", GREEN + f"{Total_reias + diversos:.2f}" + RESET)
print("=" * 50)
print("TANQUES DE COMBUSTIVEIS".center(50))
print("=" * 50)
print(f"{'Gasolina':<11} | {'S-10':<11} | {'S-500':<11} | {'V-Power'}")

print(GREEN + f"{"%.2f" % valor_litros_gasolina:<11}" + RESET, "|", GREEN + f"{"%.2f" % valor_litros_s10:<11}" + RESET, "|",
      GREEN + f"{"%.2f" % valor_litros_s500:<11}" + RESET, "|", GREEN +
      f"{"%.2f" % valor_litros_vpower}" + RESET)
print(RED + f"{"%.2f" % total_gasolina:<11}" + RESET, "|", RED + f"{"%.2f" % total_s10:<11}" + RESET, "|",
      RED + f"{"%.2f" % litros_bomba_oleo_s500:<11}" + RESET, "|", RED +
      f"{"%.2f" % litros_bomba_gasolina_adv}" + RESET)
def dimunir(num1,num2):
    r = num1 - num2
    return r

print(GREEN + f"{"%.2f" % dimunir(valor_litros_gasolina,total_gasolina):<11}" + RESET, "|",
      GREEN + f"{"%.2f" % dimunir(valor_litros_s10,total_s10):<11}" + RESET, "|",
      GREEN + f"{"%.2f" % dimunir(valor_litros_s500,litros_bomba_oleo_s500):<11}" + RESET, "|",
      GREEN + f"{"%.2f" % dimunir(valor_litros_vpower,litros_bomba_gasolina_adv)}" + RESET)
while True:
    comando = input("Digite 'sair' para encerrar o programa: ")
    if comando.lower() == 'sair':
        break
