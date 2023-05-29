import multiprocessing as mp
import time
import matplotlib.pyplot as plt
import pandas as pd
import csv


def pi_calc_MC (q, min, max):
    pi = 0
    for i in range(min, max):
        numerador =  (-1)**i
        denominador = 2*i + 1
        pi += numerador/denominador
    q.put(pi*4)


def pi_calc(num_interacoes):
    pi = 0
    t1 = time.time()
    for i in range(num_interacoes):
        numerador =  (-1)**i
        denominador = 2*i + 1
        pi += numerador/denominador
    t2 = time.time()
    pi = pi*4
    return (t2 - t1)

def multicore(num_interacoes,nthreads):
    resul = 0
    tmp1 = time.time()
    tp = mp.Queue()
    for i in range(nthreads):
        min = int (i*num_interacoes / nthreads)
        max = int ( (i+1)*num_interacoes / nthreads)
        procs = mp.Process(target=pi_calc_MC, args=(tp, min, max))
        procs.start()

    
    for i in range(nthreads):
        resul += tp.get()
    tmp2 = time.time()
    return (tmp2 - tmp1)

if __name__ == '__main__':

    num_interacoes = int(input("Digite o número de interações: "))
    num_repeticoes = int(input("Digite o número de repetições: "))
    num_threads = int(input("Digite o número de threads: "))
    variancia = []
    desvio_padrao = []
    tm = []
    ts = []
    tt = []
    x = []
    acelera = []
    x = range(1, num_repeticoes+1)
    for i in range(1, num_repeticoes+1):
        t1_sc = pi_calc(num_interacoes)
        t1_mc = multicore(num_interacoes,mp.cpu_count())
        ts.append(t1_sc)
        tm.append(t1_mc)
        acelera.append(t1_sc/t1_mc)

    
    for i in range(1, num_threads+1):
        t_aux = multicore(num_interacoes,i)
        tt.append(t_aux)
    
    ts_media = sum(ts)/len(ts)
    tm_media = sum(tm)/len(tm)
    
    print("\n\n")
    print("Tempo médio sequencial: ", ts_media)
    print("Tempo médio multicore: ", tm_media)
    print("Aceleração: ", ts_media/tm_media)
    print("Eficiência: ", (ts_media/tm_media)/mp.cpu_count())    

    plt.plot(x, ts,linewidth=0.5)
    plt.plot(x, tm, linewidth=0.5)
    plt.ylabel('Tempo de execução')
    plt.title('Tempo de execução x repetições')
    plt.legend(['Sequencial', 'Multicore', 'Média multicore', 'Média sequencial'])
    plt.show()

    plt.plot(range(1,(num_threads)+1), tt)
    plt.xlabel('Número de threads')
    plt.ylabel('Tempo de execução')
    plt.legend(['Multicore', 'Média multicore'])
    plt.title('Tempo de execução x threads')
    plt.show()

    with open('data.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Num_interacoes", "Num_repeticoes", "Tempo_sequencial", "Tempo_multicore", "Aceleracao", "Eficiencia"])
        writer.writerow([num_interacoes, num_repeticoes, ts_media, tm_media, ts_media/tm_media, (ts_media/tm_media)/mp.cpu_count()])
    pd.DataFrame(tt).to_csv('medias.csv',index_label='threads', header=['Tempo de execução'])

    





    