import random
import math
import matplotlib.pyplot as plt

class GeneradorTareas:

    def generar_exponencial(self, num_tareas, alfa=0.2):
        """
        Genera num_tareas duraciones con distribución exponencial (parámetro alfa).
        Regresa una lista de duraciones.
        """
        duraciones = []
        for _ in range(num_tareas):
            x = random.random()
            duration = -math.log(1 - x) / alfa    #duration=math.log(1-x)/(-1*a)
            duraciones.append(duration)
        return duraciones

    def generar_pareto(self, num_tareas, xm=10, alfa=10):
        """
        Genera num_tareas duraciones con distribución Pareto.
        xm = valor mínimo
        alpha = parámetro de forma
        """
        duraciones = []
        for _ in range(num_tareas):
            x = random.random()
            duration = xm * (1 - x)**(-1/alfa)    #duration=xm*(1-x)**(-1/a) 
            duraciones.append(duration)
        return duraciones


    def generar_instancia(self, num_tareas, media_duracion, semilla, flag):
        """
        Genera una instancia del problema.
        - num_tareas: Número de tareas (n)
        - media_duracion: 1/lambda para la distribución exponencial
        - semilla: Para reproducibilidad
        """
        random.seed(semilla)
        # Generamos tiempos usando distribución exponencial
        # random.expovariate(lambd) toma lambd = 1 / media
        lambd = 1.0 / media_duracion

        if flag:
            duraciones = [random.expovariate(lambd) for _ in range(num_tareas)]
        else:
            duraciones = [random.paretovariate(lambd) for _ in range(num_tareas)]
        
        # Redondeamos a 2 decimales para facilitar la lectura, aunque Gurobi maneja floats
        duraciones = [round(d, 2) for d in duraciones]
        
        return duraciones
    


    def graficar(self, duraciones, titulo="Histograma", bins=100):
        """
        Genera la gráfica de un histograma para las duraciones dadas.
        """
        plt.hist(duraciones, bins=bins, density=True, edgecolor='black')
        plt.title(titulo)
        plt.xlabel("Valor")
        plt.ylabel("Densidad")
        plt.show()

    def generar_y_graficar_exponencial(self, num_tareas, alfa, bins=100):
        dur = self.generar_exponencial(num_tareas, alfa)
        self.graficar(dur, f"Distribución Exponencial (α={alfa})", bins=bins)
        return dur

    def generar_y_graficar_pareto(self, num_tareas, xm, alfa, bins=100):
        dur = self.generar_pareto(num_tareas, xm, alfa)
        self.graficar(dur, f"Distribución Pareto (xm={xm}, α={alfa})", bins=bins)
        return dur
