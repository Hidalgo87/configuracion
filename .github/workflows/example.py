import schedule
import time

# Variable de estado para terminar el bucle después de ejecutar la tarea
tarea_ejecutada = False

def tarea_de_prueba():
    global tarea_ejecutada
    # Imprime un mensaje para probar la programación
    print('¡La tarea programada se ha ejecutado con éxito!')
    # Marca la tarea como ejecutada para detener el bucle
    tarea_ejecutada = True

# Programa la tarea
schedule.every(1).minutes.do(tarea_de_prueba)

# Ejecuta el programador
while not tarea_ejecutada:
    schedule.run_pending()
    time.sleep(3)  # Espera un segundo antes de volver a comprobar el horario
