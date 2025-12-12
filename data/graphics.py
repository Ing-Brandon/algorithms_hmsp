import numpy as np
import matplotlib.pyplot as plt
import numpy as np

class GraficaMakespan:
    def __init__(self,makespan_gurobi,makespan_greedy1,makespan_greedy2):
        self.makespan={}
        self.makespan["GOROBI"]={}
        self.makespan["GREEDY1"]={}
        self.makespan["GREEDY2"]={}

        self.medias_gurobi=[]
        self.medias_greedy1=[]
        self.medias_greedy2=[]

        self.y_err_greedy1 = []
        self.y_err_greedy2 = []

        self.n_tareas_list=[50,100,200,400]
    def procesar_informacion(self,makespan_gurobi,makespan_greedy1,makespan_greedy2):
        for i,n_tareas in enumerate([50,100,200,400]):
            self.makespan["GOROBI"][n_tareas]=makespan_gurobi[i] ## SE MANDA A LLAMAR FUNCION DE GOROBI REGRESA ARREGLO DE MAKESPANS Y TIEMPOS 
            self.makespan["GREEDY1"][n_tareas]=makespan_greedy1[i] ## SE MANDA A LLAMAR FUNCION DE GOROBI REGRESA ARREGLO DE MAKESPANS Y TIEMPOS
            self.makespan["GREEDY2"][n_tareas]=makespan_greedy2[i] ## SE MANDA A LLAMAR FUNCION DE GOROBI REGRESA ARREGLO DE MAKESPANS Y TIEMPOS

            #NORMALIZACIÓN
            self.makespan["GOROBI"][n_tareas]=np.array(self.makespan["GOROBI"][n_tareas])/np.array(self.makespan["GOROBI"][n_tareas]) 
            self.makespan["GREEDY1"][n_tareas]=np.array(self.makespan["GREEDY1"][n_tareas])/np.array(self.makespan["GOROBI"][n_tareas]) 
            self.makespan["GREEDY2"][n_tareas]=np.array(self.makespan["GREEDY2"][n_tareas])/np.array(self.makespan["GOROBI"][n_tareas])

            #GENERACION DE PUNTOS EN LA RECTA

            self.medias_gurobi=self.makespan["GOROBI"][n_tareas].mean()
            self.medias_greedy1=self.makespan["GREEDY1"][n_tareas].mean()
            self.medias_greedy2=self.makespan["GREEDY2"][n_tareas].mean()
            self.y_err_greedy1.append(1.96*self.makespan["GREEDY1"][n_tareas].std())
            self.y_err_greedy2.append(1.96*self.makespan["GREEDY2"][n_tareas].std())


    #self.medias_gurobi=[1,1,1,1]
    #self.medias_greedy1=[1.2,1.3,1.1,1.4]
    #self.medias_greedy2=[1.6,1.4,1.8,1.7]

    #y_err_greedy1 = [0.03,0.06,0.04,0.07]
    #y_err_greedy2 = [0.05,0.03,0.02,0.03]

    def graficar(self):
        fig, ax = plt.subplots()
        ax.plot(self.n_tareas_list,self.medias_gurobi,'b-',linewidth=2)
        ax.plot(self.n_tareas_list,self.medias_greedy1,'r-',linewidth=2)
        ax.plot(self.n_tareas_list,self.medias_greedy2,'g-',linewidth=2)
        ax.plot(self.n_tareas_list,4*[1.5],'c--')
        ax.plot(self.n_tareas_list,4*[2],'y--')
        ax.errorbar(self.n_tareas_list,self.medias_greedy1,self.y_err_greedy1,fmt='ro',capsize=3)
        ax.errorbar(self.n_tareas_list,self.medias_greedy2,self.y_err_greedy2,fmt='go',capsize=3)

        ax.legend(["Gurobi","Greedy 1","Greedy 2"])

        plt.show()

class GraficaTiempos:
    def __init__(self,tiempos_gurobi,tiempos_greedy1,tiempos_greedy2):
        self.tiempos={}
        self.tiempos["GOROBI"]={}
        self.tiempos["GREEDY1"]={}
        self.tiempos["GREEDY2"]={}

        self.medias_gurobi=[]
        self.medias_greedy1=[]
        self.medias_greedy2=[]

        self.y_err_greedy1 = []
        self.y_err_greedy2 = []

        self.n_tareas_list=[50,100,200,400]
    def procesar_informacion(self,tiempos_gurobi,tiempos_greedy1,tiempos_greedy2):
        for i,n_tareas in enumerate([50,100,200,400]):
            self.tiempos["GOROBI"][n_tareas]=tiempos_gurobi[i] ## SE MANDA A LLAMAR FUNCION DE GOROBI REGRESA ARREGLO DE MAKESPANS Y TIEMPOS 
            self.tiempos["GREEDY1"][n_tareas]=tiempos_greedy1[i] ## SE MANDA A LLAMAR FUNCION DE GOROBI REGRESA ARREGLO DE MAKESPANS Y TIEMPOS
            self.tiempos["GREEDY2"][n_tareas]=tiempos_greedy2[i] ## SE MANDA A LLAMAR FUNCION DE GOROBI REGRESA ARREGLO DE MAKESPANS Y TIEMPOS

            #NORMALIZACIÓN
            #self.tiempos["GOROBI"][n_tareas]=np.array(self.tiempos["GOROBI"][n_tareas])/np.array(self.tiempos["GOROBI"][n_tareas]) 
            #self.tiempos["GREEDY1"][n_tareas]=np.array(self.tiempos["GREEDY1"][n_tareas])/np.array(self.tiempos["GOROBI"][n_tareas]) 
            #self.tiempos["GREEDY2"][n_tareas]=np.array(self.tiempos["GREEDY2"][n_tareas])/np.array(self.tiempos["GOROBI"][n_tareas])

            #GENERACION DE PUNTOS EN LA RECTA

            self.medias_gurobi=self.tiempos["GOROBI"][n_tareas].mean()
            self.medias_greedy1=self.tiempos["GREEDY1"][n_tareas].mean()
            self.medias_greedy2=self.tiempos["GREEDY2"][n_tareas].mean()
            self.y_err_greedy1.append(1.96*self.tiempos["GREEDY1"][n_tareas].std())
            self.y_err_greedy2.append(1.96*self.tiempos["GREEDY2"][n_tareas].std())


    #self.medias_gurobi=[1,1,1,1]
    #self.medias_greedy1=[1.2,1.3,1.1,1.4]
    #self.medias_greedy2=[1.6,1.4,1.8,1.7]

    #y_err_greedy1 = [0.03,0.06,0.04,0.07]
    #y_err_greedy2 = [0.05,0.03,0.02,0.03]

    def graficar(self):
        fig, ax = plt.subplots()
        ax.plot(self.n_tareas_list,self.medias_gurobi,'b-',linewidth=2)
        ax.plot(self.n_tareas_list,self.medias_greedy1,'r-',linewidth=2)
        ax.plot(self.n_tareas_list,self.medias_greedy2,'g-',linewidth=2)
        ax.plot(self.n_tareas_list,4*[1.5],'c--')
        ax.plot(self.n_tareas_list,4*[2],'y--')
        ax.errorbar(self.n_tareas_list,self.medias_greedy1,self.y_err_greedy1,fmt='ro',capsize=3)
        ax.errorbar(self.n_tareas_list,self.medias_greedy2,self.y_err_greedy2,fmt='go',capsize=3)

        ax.legend(["Gurobi","Greedy 1","Greedy 2"])

        plt.show()