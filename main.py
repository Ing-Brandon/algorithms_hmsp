from data.datagenerator import GeneradorTareas
from soluciones.greedy_priority_queues import GreedyQueues


# Genera datos con distribución específica


gen = GeneradorTareas()
#>>>>>>>>>>> Generación de tareas con distribución exponencial
tasks_exp50 = gen.generar_exponencial(50)
task_exp100 = gen.generar_exponencial(100)
task_exp200 = gen.generar_exponencial(200)
task_exp200 = gen.generar_exponencial(100)

#>>>>>>>>>>> Generación de tareas con distribución exponencial
tasks_par50 = gen.generar_pareto(50)
tasks_par100 = gen.generar_pareto(100)
tasks_par200 = gen.generar_pareto(200)
tasks_par400 = gen.generar_pareto(400)
#print("pareto", tasks_par[:10])


#Ejemplo para 10 ordenadores con distribución exponencial Greedy con min-heap

asignaciones, cargas, tiempo = GreedyQueues.schedule_tasks_on_processors(tasks_exp50, num_processors=10, flag=False)


print("\n >>> Asignaciones:")
for i, a in enumerate(asignaciones):
    print(f"Procesador {i}: {a}")

print("\nCargas finales por procesador:")
for i, c in enumerate(cargas):
    print(f"Procesador {i}: {c}")

print(f"\n >>> Tiempo de ejecución: {tiempo:.5f} ms")


#Ejemplo para 10 ordenadores con distribución pareto Greedy con min-heap

asignaciones2, cargas2, tiempo2 = GreedyQueues.schedule_tasks_on_processors(tasks_par50, num_processors=10, flag=True)

print("\n >>> Asignaciones:")
for i, a in enumerate(asignaciones):
    print(f"Procesador {i}: {a}")

print("\nCargas finales por procesador:")
for i, c in enumerate(cargas2):
    print(f"Procesador {i}: {c}")

print("\n >>> Asignaciones:")
for i, a in enumerate(asignaciones2):
    print(f"Procesador {i}: {a}")


print(f"\n >>> Tiempo de ejecución 2: {tiempo2:.5f} ms")