def converter_tempo(segundos):
    horas = segundos // 3600
    segundos_restantes = segundos % 3600
    minutos = segundos_restantes // 60
    segundos_restantes = segundos_restantes % 60
    return horas, minutos, segundos_restantes

tempo_segundos = 3672  
horas, minutos, segundos = converter_tempo(tempo_segundos)

print(f'{tempo_segundos} segundos são equivalentes a {horas} horas, {minutos} minutos e {segundos} segundos.')
