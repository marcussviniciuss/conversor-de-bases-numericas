print ('Olá, seja bem vindo!')
opçao = 0
while opçao !=5:    
    print('''Escolha uma das opções:
    [1] Converter para Binário 
    [2] Converter para Octal
    [3] Converter para Hexadecimal 
    [4] Sobre 
    [5] Sair ''')
    opçao = int(input("Qual a sua opção? "))
    if opçao == 1:
        n1 = int(input("Digite um número inteiro: "))
        binarIo = ""
        while n1> 0:
            resto = n1 % 2
            binarIo = str(resto) + binarIo
            n1 = int (n1 /2)
        print ("O número escolhido em Binário é:", binarIo)
    elif opçao == 2:
        n1 = int(input("Digite um número inteiro: "))
        octal = ""
        while n1> 0:
            resto = n1 % 8
            octal = str(resto) + octal
            n1 = int (n1 /8)
        print ("O número escolhido em Octal é:", octal)
    elif opçao == 3:
        n1 = int(input("Digite um número inteiro: "))
        dec_to_hex = {
            "10" : "A",
            "11" : "B",
            "12" : "C",
            "13" : "D",
            "14" : "E",
            "15" : "F"
        }
        hexadecimal = ""
        while n1> 0:
            resto = n1 % 16
            if str(resto) in dec_to_hex.keys():
                resto = dec_to_hex[str(resto)]
            hexadecimal = str(resto) + hexadecimal
            n1 = int (n1 /16)            
        print("O número escolhido em Hexadecimal é:", hexadecimal)
    elif opçao == 4:
        print('''---------------------------------------     
    Conversor de bases numéricas
        
       Desenvolvido por:
Marcus Vinícius Souza Oliveira.
        
        Versão: 1.0
    Desenvolvido em 2022'''
        )
    elif opçao == 5:                                  
        print("Finalizando...")
    else: print("Opção invalida")
    print("---------------------------------------")
print("Fim do programa. Volte sempre!")