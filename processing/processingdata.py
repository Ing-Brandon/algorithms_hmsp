import logging
from data.datagenerator import GeneradorTareas
from algorithms.greedy_priority_queues import GreedyQueues
from algorithms.guroby_solution import GurobiSolution


class ProcesaDatos:
    
    #Esto lo vamos a usar para graficar
    def __init__(self):
        # Aquí se define la "memoria" del objeto.
        # Creamos una lista vacía que pertenecerá a la instancia.
        self.resultados_guardados = []


    def Procesamiento(self, tipo_distribucion, tamanio_tareas, num_processors):


        # Genera las instancias:
        gen = GeneradorTareas()
        media_duracion=10
        semilla=42
        flagI=True

        for i in len(tamanio_tareas):
            '''if (tipo_distribucion == "exponencial"):
                # Genera datos con distribución EXPONENCIAL
                tasks = gen.generar_exponencial(tamanio_tareas[i])
            else:
                 # Genera datos con distribución PARETO
                tasks = gen.generar_pareto(tamanio_tareas[i])'''
            
            tasks = gen.generar_instancia( tamanio_tareas[i], media_duracion, semilla, flagI)

            # >>>>>>>>>>>>>>> LIST SCHEDULING
            asignaciones_ls, cargas_ls, makespan_ls, tiempo_ls = GreedyQueues.schedule_tasks_on_processors(tasks, num_processors, flag=False)
            logging.info(f"\n >>> List Scheduling para instancia de {tamanio_tareas[i]} tareas <<<")
            #logging.info(">>>> Asignaciones")
            #for j, a_ls in enumerate(asignaciones_ls):
                #logging.info(f"Procesador {j}: {a_ls}")

            logging.info("\nCargas finales por procesador:")
            for k, c_ls in enumerate(cargas_ls):
                logging.info(f"Procesador {k}: {c_ls}")
            
            logging.info(f">> Makespan: {makespan_ls}")
            
            logging.info(f"\n >>> Tiempo de ejecución: {tiempo_ls:.5f} ms")


            # >>>>>>>>>>>>>>>>< LONGEST PROCESSING TIME FIRST
            asignaciones_lpt, cargas_lpt, makespan_lpt, tiempo_lpt = GreedyQueues.schedule_tasks_on_processors(tasks, num_processors, flag=True)
            logging.info(f"\n >>> Longest Processing Time First para instancia de {tamanio_tareas[i]} tareas <<<")
            #logging.info(">>>> Asignaciones")
            #for m, a_lpt in enumerate(asignaciones_lpt):
                #logging.info(f"Procesador {m}: {a_lpt}")

            logging.info("\nCargas finales por procesador:")
            for n, c_lpt in enumerate(cargas_lpt):
                logging.info(f"Procesador {n}: {c_lpt}")
            
            logging.info(f">> Makespan: {makespan_lpt}")
            
            logging.info(f"\n >>> Tiempo de ejecución: {tiempo_lpt:.5f} ms")
    

            # >>>>>>>>>>>>>>>>< GUROBI EXACTA
            tiempo_limite=30
            makespan_gurobi, tiempo_gurobi = GurobiSolution.resolver_exacto_gurobi(num_processors, tasks, tiempo_limite)
            #obj_exact, t_exact = resolver_exacto_gurobi(N_procesadores, instancia, LIMIT_GUROBI)
            #makespan_optimo, _ = GurobiSolution.resolver_exacto_gurobi(num_processors, tasks, tiempo_limite)
            logging.info(f"\n >>> obj_exact Gurobi: {makespan_gurobi:.5f} ms")
            logging.info(f"\n >>> t_exact Gurobi: {tiempo_gurobi:.5f} ms")

            return makespan_ls, tiempo_ls, makespan_lpt, tiempo_lpt, makespan_gurobi, tiempo_gurobi

    def graficar():
        pass