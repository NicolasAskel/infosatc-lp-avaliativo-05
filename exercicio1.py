  nome = (input("Digite o seu nome"))
  sobrenome = (input("Digite seu sobrenome"))
  email = (input("Insira seu e-mail ex:nome@nome"))
  cpf = (input("Insira seu cpf"))
  senha = (input("Insira sua senha"))
  endereço = (input("Informe o seu endereço"))
  celular = (input("Digite o seu numero de contato"))
  saldo = 0
  nomepadrao= ("aaa")
  sobrenomepadrao= ("aaa")
  senhapadrao=("aaaa@")
  emailpadrao=("nome@nome")

  len(nome)
  len(nomepadrao)
  len(sobrenome)
  len(sobrenomepadrao)
  len(senha)
  len(senhapadrao)
  len(email)
  len(emailpadrao)

if len(nome) > len(nomepadrao)
 if len(sobrenome) > len(sobrenomepadrao)
  if len(senha) > len(senhapadrao)
   if len(email) > len(emailpadrao)
    menu = int(input("escolha uma das opçoes: 1-Sacar 2-Depositar 3-Conferir Saldo 4-Transferir 5-Encerrar Conta")) 
     if(menu==1):
     depositar=(input("Deposite uma quantia:"))
          saldo=saldo+depositar
          print("Saldo:",saldo)
            else  :
              pass
        if(menu==1):
        depositar=(input("Deposite uma quantia:"))
           saldo=saldo+depositar
            print("Saldo:",saldo)
             else  :
              pass    
          if(menu==2):
           sacar=(input("saque uma quantia:"))
           saldo=saldo-sacar
            if sacar > saldo 
             print("voce nao possui essa quantia pra sacar")
               else:

                print("Saldo:",saldo)
              else  :
                  pass    
                    if(menu==3):
                        
               print("Saldo:",saldo)
                 else  :
                  pass    
                if(menu==4):
                   transferir=(input("tranfira uma quantia:"))
                     saldo=saldo-transferir
                    if transferir > saldo
                       print ("voce nao possui o saldo para transferir")
                         else :
                          print("Saldo:",saldo)
                           else  :
                            pass 
                   if(menu==5):
                     print("voce encerrou sua conta")
                        else  :
                           pass           

else :
print("digite seu nome novamente ele precisa conter no mínimo 3 letras")
    else :
    print("digite seu sobrenome novamente ele precisa conter no mínimo 3 letras")
      else :
    print("digite sua senha novamente com pelo menos 5 digitos contendo um caractere especial")
         else :
    print("digite seu e-mail novamente algo esta errado")
