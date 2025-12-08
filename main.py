import logging
from processing.processingdata import ProcesaDatos



def main():

    # Declaración de logs
    logging.basicConfig(
        level=logging.INFO,
        format='%(message)s', # Para agregar fecha y hora automática: %(asctime)s 
        handlers=[
            logging.FileHandler("execution_hmsp.log"),
            logging.StreamHandler()
        ]
    )

    logging.info(">>>> Propuestas de solución para 'Homogeneous Multiprocessor Scheduling Problem'<<<<")
    
    # Número de procesadores fijo = 10
    num_processors = 10

    # Número de tareas por instancia
    tamanio_tareas = [50, 100, 200, 400]

    #Tipo de distribución de tareas que va a generar
    tipo_distribucion="exponencial" 
    #tipo_distribucion="pareto"

    processing = ProcesaDatos()
    
    processing.Procesamiento(tipo_distribucion, tamanio_tareas, num_processors)

    #Aquí se agrega la línea para graficar
    #processing.graficar()
    logging.info(">>>> FIN DE LA EJECUCIÓN <<<<")


if __name__ == "__main__":
    main()