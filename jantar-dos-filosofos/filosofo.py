import threading
import time
import random

class Filosofo(threading.Thread):
    executando = True

    def __init__(self, nome, garfo_esquerda, garfo_direita):
        threading.Thread.__init__(self)
        self.nome = nome
        self.garfo_esquerda = garfo_esquerda
        self.garfo_direita = garfo_direita

    def run(self): # blibio thread
        self.pensar()

    def pensar(self):
        while (self.executando):
            print('%s esta pensando.' % self.nome)
            time.sleep(random.uniform(3, 13))
            self.comer()

    def comer(self):
        garfo1, garfo2 = self.garfo_esquerda, self.garfo_direita

        # prevenção do starvation
        # gera um tempo máximo e vai incrementando a cada vez que tenta pegar os garfos
        # caso chegue no tempo máximo sem comer ele recebe prioridade, os garfos são liberados ele começa a comer
        max_tempo_sem_comer = int(random.uniform(5, 20))
        tempo_sem_comer = 0

        print('%s esta tentando pegar os garfos.' % self.nome)
        while self.executando:
            if tempo_sem_comer == max_tempo_sem_comer:
                print('%s ganhou prioridade.' % self.nome)
                garfo1.release()
                garfo2.release()
            garfo1.acquire()
            garfo2_disponivel = garfo2.acquire()
            if garfo2_disponivel: break
            garfo1.release() 
            tempo_sem_comer += 1
            sleep(1)
        else:
            return

        print('%s pegou e esta comendo.' % self.nome)
        time.sleep(random.uniform(1, 10))
        print('%s parou de comer.' % self.nome)
        garfo2.release()
        garfo1.release()