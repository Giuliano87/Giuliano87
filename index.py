def sacar(valor):
    saldo = 1000
    if saldo >= valor:
        print("Seu saldo é de R$", saldo)
        saldo -= valor
        print("Saque de R$", valor, "efetuado com sucesso!")
        print("Seu novo saldo é de R$", saldo)
    
    sacar(500)

        
  



      

