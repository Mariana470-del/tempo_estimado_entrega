nome_restaurante = ""
tempo_estimado_entrega = 0

nome_restaurante = input("Qual o nome do seu restaurante? \n")
tempo_estimado_entrega = int(input("Qual o tempo estimado de entrega do seu restaurante em minutos?\n"))

texto = f"O restaurante {nome_restaurante} entrega em {tempo_estimado_entrega} minutos \n"
print(f"{texto}")