def podio_olimpico(tempo_chegada1, tempo_chegada2, tempo_chegada3):

    resultado = ""

    if (tempo_chegada1 < tempo_chegada2 and tempo_chegada1 < tempo_chegada3):
        if (tempo_chegada2 < tempo_chegada3):
            resultado = f"1 - {tempo_chegada1} minutos\n2 - {tempo_chegada2} minutos\n3 - {tempo_chegada3} minutos\n"
        else:
            resultado = f"1 - {tempo_chegada1} minutos\n2 - {tempo_chegada3} minutos\n3 - {tempo_chegada2} minutos\n"
    elif (tempo_chegada2 < tempo_chegada1 and tempo_chegada2 < tempo_chegada3):
        if (tempo_chegada1 < tempo_chegada3):
            resultado = f"1 - {tempo_chegada2} minutos\n2 - {tempo_chegada1} minutos\n3 - {tempo_chegada3} minutos\n"
        else:
            resultado = f"1 - {tempo_chegada2} minutos\n2 - {tempo_chegada3} minutos\n3 - {tempo_chegada1} minutos\n"
    else:
        if (tempo_chegada1 < tempo_chegada2):
            resultado = f"1 - {tempo_chegada3} minutos\n2 - {tempo_chegada1} minutos\n3 - {tempo_chegada2} minutos\n"
        else:
            resultado = f"1 - {tempo_chegada3} minutos\n2 - {tempo_chegada2} minutos\n3 - {tempo_chegada1} minutos\n"

    return resultado


tempo_chegada1 = 120
tempo_chegada2 = 90
tempo_chegada3 = 110

resultado = podio_olimpico(tempo_chegada1, tempo_chegada2, tempo_chegada3)
print(resultado)
