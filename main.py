import logging
import time
from processing.processingdata import ProcesaDatos
from data.graphicclass import Graphics


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

    avg_makespan_ls = []
    avg_makespan_lpt = []
    avg_times_gurobi = []
    avg_times_ls = []
    avg_times_lpt = []
    
    #Aquí va el for de las 10 instancias
    for i in range(repeticiones):
        print(">>>>>>>>>>>>>>>> Repetición: ",i)
        sum_makespan_ls = 0
        sum_makespan_lpt = 0
        sum_time_gurobi = 0
        sum_time_ls = 0
        sum_time_lpt = 0

        makespan_ls, tiempo_ls, makespan_lpt, tiempo_lpt, makespan_gurobi, tiempo_gurobi = processing.Procesamiento(tipo_distribucion, tamanio_tareas, num_processors)

        if makespan_gurobi > 0:
            sum_makespan_ls += (makespan_ls / makespan_gurobi)
            sum_makespan_lpt += (makespan_lpt / makespan_gurobi)
        else:
            sum_makespan_ls += 1
            sum_makespan_lpt += 1
    
        sum_time_gurobi += tiempo_gurobi
        sum_time_ls  += tiempo_ls
        sum_time_lpt += tiempo_lpt
    

    avg_makespan_ls.append(sum_makespan_ls / repeticiones)
    avg_makespan_lpt.append(sum_makespan_lpt / repeticiones)
        
    avg_times_gurobi.append(sum_time_gurobi / repeticiones)
    avg_times_ls.append(sum_time_ls / repeticiones)
    avg_times_lpt.append(sum_time_lpt / repeticiones)

    #Aquí se agrega la línea para graficar

    Graphics.graficar_resultados(tamanio_tareas, avg_makespan_ls, avg_makespan_lpt, avg_times_gurobi, avg_times_ls, avg_times_lpt)
    #processing.graficar()
    logging.info(">>>> FIN DE LA EJECUCIÓN <<<<")
    tf=time.time() - start_time
    logging.info("Tiempo total: ", tf)


if __name__ == "__main__":
    main()