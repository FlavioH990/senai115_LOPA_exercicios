ContAlunos = 1
qtAlunos = 6
qtNotas = 2
qtdaprovados = 0
qtdReprovados = 0
qtdExame = 0
somaMedias = 0

while ContAlunos <=qtAlunos:
    print(f"Alunos{ContAlunos}")
    
    nota1 = int(input("Digite a primeira nota: "))
    nota2 = int(input("Digite a segunda nota: "))
    
    media = (nota1 + nota2) / qtNotas
    
    
    if media < 3:
        print("Reprovado")
    elif media >= 3 and media < 7:
        print("Exame")
        qtdExame += 1
        
    elif media >= 7:
        print("Aprovado")
        qtdaprovados += 1
        
     
    ContAlunos += 1
    


