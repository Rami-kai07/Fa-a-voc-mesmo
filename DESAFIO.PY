import math
pao_farofa = 0
pao_forma = 0
pao_frances= 0
pao_integral = 0
doce_liso = 0

valorfarofa = 0
valorliso = 0
valorforma= 0
valorintegral = 0
valorfrances = 0

while True: 
    print("------------PADARIA------------")
    print("[1] Pão Frances-1,04")
    print("[2] Pão Integral-1,04")
    print("[3] Pão Doce Liso-1,08")
    print("[4] Pão Doce Farofa-1,11")
    print("[5] Pão de Forma-0,95")
    print("[6] Fim da compra.")
    print("--------------------------------")
    opcao = int(input("Escolha sua opção: "))
    
    if opcao ==1:
        pao_frances = int(input("Quantidade de pão frances: "))
        valorfrances=pao_frances*1.04
        continue
    elif opcao ==2:
        pao_integral= int(input("Quantidade de pão integral: "))
        valorintegral=pao_integral*1.04
        continue
    elif opcao ==3:
        doce_liso= int(input("Quantidade de pão integral de doce liso: "))
        valorliso=doce_liso*1.08
        continue
    elif opcao ==4:
        pao_farofa= int(input("Quantidade de pão doce farofa: "))
        valorfarofa=pao_farofa*1.11
        continue
    elif opcao ==5:
        pao_forma= int(input("Quantidade de pão de forma: "))
        valorforma=pao_forma*0.95
        continue
    elif opcao ==6:
        break
    else:
        print("ERRO")


print("----------NOTA FISCAL----------")

if pao_frances >0:
    print(f"Pão Frances: {pao_frances} UNI X 1,04 = {valorfrances:.2f}")
    
if pao_integral >0:
    print(f"Pão Integral: {pao_integral} UNI X 1,04 = {valorintegral:.2f}")
    
if doce_liso >0:
    print(f"Pão Doce Liso: {doce_liso} UNI X 1,08 = {valorliso:.2f}")
    
if pao_farofa >0:
    print(f"Pão Farofa: {pao_farofa} UNI X 1,11 = {valorfarofa:.2f}")
    
if pao_forma >0:
    print(f"Pão de Forma: {pao_forma} UNI X 0,95 = {valorforma:.2f}")
    
total = valorfarofa+valorforma+valorfrances+valorintegral+valorliso

print("----------TOTAL DA COMPRA----------")
print(f"VALOR: R${total:.2f}")
print("--------------------------------")