# Jantar dos filósofos

# Prevenção do starvation

***Gera um tempo máximo e vai incrementando a cada vez que tenta pegar os garfos***

***Caso chegue no tempo máximo sem comer ele recebe prioridade, os garfos são liberados ele começa a comer***

```python
def comer(self):
        garfo1, garfo2 = self.garfo_esquerda, self.garfo_direita
        max_tempo_sem_comer = int(random.uniform(5, 20))
        tempo_sem_comer = 0

        print('%s esta tentando pegar os garfos.' % self.nome)
        while self.executando:
            if tempo_sem_comer == max_tempo_sem_comer:
                print('%s ganhou prioridade.' % self.nome)
                garfo1.release()
                garfo2.release()
```

***Funciona como definido em tempo aleatório para o máximo de tempo para um filosofo comer, então se cada loop que passar e a contagem do tempo_sem_comer = 0 . que começaria 0 e vai subindo conforme ele não consegue buscar esse 2 garfos e comer.*** 

***Exemplo, se o máximo de um filosofo x for defino em 5 no max_de_tempo_sem_comer. ele vai ocorrer a prioridade onde acontece o release() que você solta os garfos para que esse filosofo possa comer***

# Deadlock

No código a seguir

```python
	garfo1.acquire()
            garfo2_disponivel = garfo2.acquire()
            if garfo2_disponivel: break
            garfo1.release()
            tempo_sem_comer += 1
```

no  ***garfo1.acquire() ele vai tentar pegar o garfo, e vai retornar um valor true ou false, e indo para o garfo2, que verifica se esta disponível, se estiver, ele faz o break e sai do loop, indo para a linha a linha mostrada abaixo, que fica seria o tempo aleatório de que cada filosofo leva para comer*** 

```python
print('%s pegou e esta comendo.' % self.nome)
        time.sleep(random.uniform(1, 10))
```

***e caso ele não consiga pegar esse garfo2, ele vai liberar o 1 garfo, liberando o recurso para que outro filosofo tente pegar, que não faz sentido vc guardar um recurso que na hora não será utilizado. e também depois dessa liberação e ele soma um para tempo que ele não conseguiu comer.***

```python
 tempo_sem_comer += 1
```

E o problema vai funcionar que ele os filósofos ou vão estar pensando ou comendo, então ele começa nessa função de pensar que é um loop, ele fica pensando no time.sleep(random.uniform(3,13)) ele vai ficar num tempo aleatório entre 3 a 13 segundos até ir na próxima linha, que seria a função comer

```python
    def pensar(self):
        while (self.executando):
            print('%s esta pensando.' % self.nome)
            time.sleep(random.uniform(3, 13))
            self.comer()
```

CODIGO COMPLETO

filosofo.py

```python
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
```

main.py

```python
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
```
