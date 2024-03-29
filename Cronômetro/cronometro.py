import time

class Cronometro:
    def __init__(self):
        self.tempo_inicial = None
        
    def iniciar(self):
        self.tempo_inicial = time.time()
        
    def parar(self):
        if self.tempo_inicial is None:
            print("O cronômetro ainda não foi iniciado.")
            return    
    
        tempo_decorrido = time.time() - self.tempo_inicial
        horas = int(tempo_decorrido // 3600)
        minutos = int((tempo_decorrido % 3600) // 60)
        segundos = int(tempo_decorrido % 60)
        print(f"Tempo decorrido: {horas:02d}:{minutos:02d}:{segundos:02d}")
        
# Exemplo de uso 
cronometro = Cronometro()

print("Pressione Enter para iniciar o cronômetro...")
input()

cronometro.iniciar()

print("Cronômetro iniciado. Pressione Enter para parar...")
input()

cronometro.parar()
