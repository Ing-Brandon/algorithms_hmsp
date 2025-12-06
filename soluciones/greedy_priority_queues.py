import heapq
import time

class GreedyQueues:

    def schedule_tasks_on_processors(tasks, num_processors, flag):
        """
        Asigna tareas a procesadores homogéneos usando un min-heap.
        Cada procesador se representa como (carga_actual, id_procesador).
    
        Retorna:
            asignaciones: lista de listas; asignaciones[i] contiene las tareas asignadas al procesador i
            cargas: lista con la carga final de cada procesador
        """

        t0 = time.perf_counter()

        if flag==True:
            # 1. Ordenar tareas de mayor a menor duración para solución greedy 2
            tasks_sorted = sorted(tasks, reverse=True)
        else:
            tasks_sorted=tasks
        
        print(">>>>> Tareas a procesar: ", tasks_sorted)
        # Inicializar el heap con la carga 0 para cada procesador
        # Cada elemento es: (carga_actual, id_procesador)
        heap = [(0, pid) for pid in range(num_processors)]
        heapq.heapify(heap) # >>>>>>>>>>>>> Transforma una lista a min-heap

        # Para almacenar qué tareas le tocan a cada procesador
        asignaciones = [[] for _ in range(num_processors)]

        for t in tasks_sorted:
            # Sacar el procesador menos cargado
            carga, pid = heapq.heappop(heap) #>>>>>>>>>>>>> Devuelve el elemento más pequeño del heap
            # Asignar la tarea al procesador
            asignaciones[pid].append(t)
            nueva_carga = carga + t

            # Volver a insertar el procesador con su carga actualizada
            heapq.heappush(heap, (nueva_carga, pid))

        # Al final, las cargas quedan en el heap
        cargas_finales = [0] * num_processors
        for carga, pid in heap:
            cargas_finales[pid] = carga

        # ---- Fin: medir tiempo ----
        t1 = time.perf_counter()
        tiempo_ejecucion = (t1 - t0) * 1000

        return asignaciones, cargas_finales, tiempo_ejecucion



