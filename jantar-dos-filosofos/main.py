import threading
from filosofo import Filosofo

def main():
    garfos = [threading.Semaphore(1) for n in range(5)]
    nomes = ['Datena', 'Marçal', 'Boulos', 'Nunes', 'Tabata']
    filosofos = [Filosofo('%s (%s)' % (nomes[i], i), garfos[i % 5], garfos[(i + 1) % 5]) for i in range(5)] 

    Filosofo.executando = True
    while True:
        for f in filosofos:
            try:
                f.start()
            except:
                pass
    Filosofo.executando = False


if __name__ == '__main__':
    main()