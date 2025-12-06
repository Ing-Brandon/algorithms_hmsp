import numpy as np
import matplotlib.pyplot as plt
import numpy as np

makespan={}
makespan["GOROBI"]={}
makespan["GREEDY1"]={}
makespan["GREEDY2"]={}

medias_gurobi=[]
medias_greedy1=[]
medias_greedy2=[]

y_err_greedy1 = []
y_err_greedy2 = []

n_tareas_list=[50,100,200,400]
for n_tareas in [50,100,200,400]:
    makespan["GOROBI"][n_tareas]=[1,2,3,4,8,7,9,64,4,17] ## SE MANDA A LLAMAR FUNCION DE GOROBI REGRESA ARREGLO DE MAKESPANS Y TIEMPOS
    makespan["GREEDY1"][n_tareas]=[1,2,3,4,8,7,9,64,4,17] ## SE MANDA A LLAMAR FUNCION DE GOROBI REGRESA ARREGLO DE MAKESPANS Y TIEMPOS
    makespan["GREEDY2"][n_tareas]=[1,2,3,4,8,7,9,64,4,17] ## SE MANDA A LLAMAR FUNCION DE GOROBI REGRESA ARREGLO DE MAKESPANS Y TIEMPOS

    #NORMALIZACIÓN
    makespan["GOROBI"][n_tareas]=np.array(makespan["GOROBI"][n_tareas])/np.array(makespan["GOROBI"][n_tareas]) 
    makespan["GREEDY1"][n_tareas]=np.array(makespan["GREEDY1"][n_tareas])/np.array(makespan["GOROBI"][n_tareas]) 
    makespan["GREEDY2"][n_tareas]=np.array(makespan["GREEDY2"][n_tareas])/np.array(makespan["GOROBI"][n_tareas])

    #GENERACION DE PUNTOS EN LA RECTA

    #medias_gurobi=makespan["GOROBI"][n_tareas].mean()
    #medias_greedy1=makespan["GREEDY1"][n_tareas].mean()
    #medias_greedy2=makespan["GREEDY2"][n_tareas].mean()
    #y_err_greedy1.append(1.96*makespan["GREEDY1"][n_tareas].std())
    #y_err_greedy2.append(1.96*makespan["GREEDY2"][n_tareas].std())


medias_gurobi=[1,1,1,1]
medias_greedy1=[1.2,1.3,1.1,1.4]
medias_greedy2=[1.6,1.4,1.8,1.7]

y_err_greedy1 = [0.03,0.06,0.04,0.07]
y_err_greedy2 = [0.05,0.03,0.02,0.03]


fig, ax = plt.subplots()
ax.plot(n_tareas_list,medias_gurobi,'b-',linewidth=2)
ax.plot(n_tareas_list,medias_greedy1,'r-',linewidth=2)
ax.plot(n_tareas_list,medias_greedy2,'g-',linewidth=2)
ax.plot(n_tareas_list,4*[1.5],'c--')
ax.plot(n_tareas_list,4*[2],'y--')
ax.errorbar(n_tareas_list,medias_greedy1,y_err_greedy1,fmt='ro',capsize=3)
ax.errorbar(n_tareas_list,medias_greedy2,y_err_greedy2,fmt='go',capsize=3)

ax.legend(["Gurobi","Greedy 1","Greedy 2"])

plt.show()