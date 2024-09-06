import schedule
import time

def tarea_de_prueba():
    # Imprime un mensaje para probar la programación
    print('¡La tarea programada se ha ejecutado con éxito!')

# Programa la tarea de prueba a una hora específica
hora_envio = '17:08'  # Hora en formato 24 horas

# Programa la tarea
schedule.every().day.at(hora_envio).do(tarea_de_prueba)

# Ejecuta el programador
while True:
    schedule.run_pending()
    time.sleep(1)  # Espera un minuto antes de volver a comprobar el horario
