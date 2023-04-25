import multiprocessing as mp
import time
import matplotlib.pyplot as plt

MAX = 1000000000 # tamanho do intervalo
N = 5 # numero de repetições do experimento

def job(q, min, max):
    # print (min, max)
    res = 0
    for i in range(min, max):
        res += 1
    q.put(res)


def normal():
    res = 0
    t1 = time.time()
    for i in range(MAX):
        res += 1
    # q = mp.Queue()
    # p = mp.Process(target=job, args=(q, 0, MAX))
    # p.start()
    t2 = time.time()
    # print ('resultado siglecore = ', res)
    return (t2 - t1)

def multicore():
    resul = 0
    tmp1 = time.time()
    nthreads = 8
    q = mp.Queue()
    for i in range(nthreads):
        min_ = int (i*MAX / nthreads)
        max_ = int ( (i+1)*MAX / nthreads)
        p = mp.Process(target=job, args=(q, min_, max_))
        p.start()
    
    for i in range(nthreads):
        resul += q.get()
    tmp2 = time.time()
    # print ('resultado multicore = ', resul)
    return (tmp2 - tmp1)

if __name__ == '__main__':

    ts = []
    tm = []
    tg = []
    tspeedup = []
    teff = []
    x = range (1,N+1)
    for i in range (N):
        ts.append(normal())
        tm.append(multicore())
        tg.append(ts[i] - tm[i])
        tspeedup.append(ts[i]/tm[i])
        teff.append(100 * tspeedup[i]/8)
        print('------------------------')
        print('repetição = ', i+1)
        print('normal = ', ts[i])
        print('multicore = ', tm[i])
        print('ganho = ', tg[i])
        print('speedup = ', tspeedup[i])
        print('eficiencia = ', teff[i])
        print('------------------------')
    plt.plot(x, ts, label='singlecore')
    plt.plot(x, tm, label='multicores')
    plt.xlabel('repetições')
    plt.ylabel('tempo (s)')
    plt.legend()
    plt.show()

    plt.plot(x, tg, label='ganho')
    plt.xlabel('repetições')
    plt.ylabel('tempo (s)')
    plt.legend()
    plt.show()

    plt.plot(x, tspeedup, label='speedup')
    plt.xlabel('repetições')
    plt.ylabel('number of times better than singlecore')
    plt.legend()
    plt.show()

    plt.plot(x, teff, label='eficiencia')
    plt.xlabel('repetições')
    plt.ylabel('Efficiency per core (%)')
    plt.legend()
    plt.show()



    
    print('media normal = ', sum(ts)/N)
    print('media multicore = ', sum(tm)/N)
    print('media ganho = ', sum(tg)/N)
    print('media speedup = ', sum(tspeedup)/N)
    print('media eficiencia = ', sum(teff)/N)