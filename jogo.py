j1 = 0
j2 = 0
ept = 0
resp = "S"

print("|Bem-vindo ao JOKENPO| 1 - pedra ; 2 - tesoura ; 3 - papel")
while resp == "S":
    for x in range(3):
        player1 = input("Jogador 1, informe sua jogada: ")
        while player1 != "1" and player1 != "2" and player1 != "3":
            player1 = input("Opção inválida, informe novamente: ")
        player2 = input("Jogador 2, informe sua jogada: ")
        while player2 != "1" and player2 != "2" and player2 != "3":
            player2 = input("Opção inválida, informe novamente: ")
        if player1 == player2:
            print("Rodada empatada!")
            print()
            ept += 1
        elif (player1 == "1" and player2 == "2") or (player1 == "2" and player2 == "3") or (player1 == "3" and player2 == "1"):
            print("Jogador01 venceu a rodada e foi somado um ponto.")
            print()
            j1 += 1
        else:
            print("Jogador02 venceu a rodada e foi somado um ponto.")
            print()
            j2 += 1
    if ept >= j1 and ept >= j2:
        print("Jogo empatada, tentem novamente.")
    else:
        if j1 > j2:
            print("Jogador01 foi o grande vencedor, parabéns!")
        else:
            print("Jogador02 foi o grande vencedor, parabéns!")
    resp = input("Deseja jogar novamente? [S/N]: ")
print()
print("Jogo encerrado.")