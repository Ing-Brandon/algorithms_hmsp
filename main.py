import logging
import time
from processing.processingdata import ProcesaDatos
from data.graphicclass import Graphics
from data.graphics import Grafica

def main():
    

    start_time = time.time()
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
    

    #Número de repeticiones: 10
    repeticiones=10

    # Número de procesadores fijo = 10
    num_processors = 10

    # Número de tareas por instancia
    tamanio_tareas = [50, 100, 200, 400]

    #Tipo de distribución de tareas que va a generar
    tipo_distribucion="exponencial" 
    #tipo_distribucion="pareto"

    processing = ProcesaDatos()



    makespans_t_gurobi, makespans_t_ls, makespans_t_lpt,  tiempos_t_gurobi,  tiempos_t_ls,  tiempos_t_lpt = processing.Procesamiento(repeticiones, tamanio_tareas, num_processors)

    
    logging.info("makespans_totales_gurobi")
    for fila_mg in makespans_t_gurobi:
        logging.info(fila_mg)

    
    logging.info("makespans_totales_ls")
    for fila_mls in makespans_t_ls:
        logging.info(fila_mls)
    
    logging.info("makespans_totales_lpt")
    for fila_lpt in makespans_t_lpt:
        logging.info(fila_lpt)
    
    logging.info("tiempos_totales_gurobi")
    for fila_tg in tiempos_t_gurobi:
        logging.info(fila_tg)

    logging.info("tiempos_totales_ls")
    for fila_tls in tiempos_t_ls:
        logging.info(fila_tls)

    logging.info("tiempos_totales_lpt")
    for fila_tlpt in tiempos_t_lpt:
        logging.info(fila_tlpt)



    #Aquí se agrega la línea para graficar

    #Graphics.graficar_resultados(tamanio_tareas, avg_makespan_ls, avg_makespan_lpt, avg_times_gurobi, avg_times_ls, avg_times_lpt)
    #processing.graficar()
    graficas=Grafica()
    graficas.procesar_informacion_makespan(makespans_t_gurobi, makespans_t_ls, makespans_t_lpt)
    graficas.procesar_informacion_tiempos(tiempos_t_gurobi,  tiempos_t_ls,  tiempos_t_lpt)
    graficas.guardar_grafica(tipo_distribucion+".jpg")
    logging.info(">>>> FIN DE LA EJECUCIÓN <<<<")
    tf=time.time() - start_time
    logging.info(f"Tiempo total: {tf}")


if __name__ == "__main__":
    main()