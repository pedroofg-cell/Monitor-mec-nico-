# Monitor de Máquinas Industriais - RJ 2026

import time
import random
from datetime import datetime

class MonitorMecanica:
    def __init__(self):
        self.temperatura = 0
        self.vibracao = 0
        self.pressao = 0
        self.status = "NORMAL"
        
    def ler_sensores(self):
        # Simula sensores reais
        self.temperatura = random.uniform(40, 85)
        self.vibracao = random.uniform(1, 7)
        self.pressao = random.uniform(2, 9)
    
    def analisar_falhas(self):
        alertas = []
        
        if self.temperatura > 70:
            alertas.append("SUPERAQUECIMENTO")
            self.status = "CRÍTICO"
        elif self.vibracao > 5:
            alertas.append("VIBRAÇÃO ALTA")
            self.status = "ATENÇÃO"
        elif self.pressao < 3:
            alertas.append("PRESSÃO BAIXA")
            self.status = "ATENÇÃO"
        else:
            self.status = "NORMAL"
        
        return alertas
    
    def gerar_relatorio(self):
        timestamp = datetime.now().strftime("%d/%m/%Y %H:%M")
        print(f"RELATÓRIO - {timestamp}")
        print(f"Temperatura: {self.temperatura:.1f}°C")
        print(f"Vibração: {self.vibracao:.1f} mm/s") 
        print(f"Pressão: {self.pressao:.1f} bar")
        print(f"Status: {self.status}")
        print("---" * 20)

# === EXECUÇÃO PRINCIPAL ===
monitor = MonitorMecanica()

print("🔧 MONITOR INDUSTRIAL - INICIADO")
print("Pressione Ctrl+C para parar")

try:
    while True:
        monitor.ler_sensores()
        alertas = monitor.analisar_falhas()
        
        monitor.gerar_relatorio()
        
        if alertas:
            for alerta in alertas:
                print(alerta)
        
        time.sleep(3)  # Lê a cada 3 segundos (tempo real industrial)
        
except KeyboardInterrupt:
    print("\n")
print("monitor finalizado com sucesso!")
