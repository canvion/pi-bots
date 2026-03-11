import requests
import time
import config

def get_cpu():
    f = open("/proc/stat", "r")
    line = f.readline()
    f.close()
    valores = line.split()
    total = sum(int(x) for x in valores[1:])
    idle = int(valores[4])
    return total, idle

def calcular_cpu_porcentaje():
    total1, idle1 = get_cpu()
    time.sleep(1)
    total2, idle2 = get_cpu()
    diferencia_total = total2 - total1
    diferencia_idle = idle2 - idle1
    cpu = 100 * (diferencia_total - diferencia_idle) / diferencia_total
    return round(cpu, 1)

def get_ram():
    f = open("/proc/meminfo", "r")
    lineas = f.readlines()
    f.close()
    total = int(lineas[0].split()[1])
    disponible = int(lineas[2].split()[1])
    usada = total - disponible
    porcentaje = round(100 * usada / total, 1)
    return porcentaje

def get_temperatura():
    f = open("/sys/class/thermal/thermal_zone0/temp", "r")
    temp = f.read()
    f.close()
    return round(int(temp) / 1000, 1)

def mandar_mensaje(texto):
    url = "https://api.telegram.org/bot" + config.TOKEN + "/sendMessage"
    datos = {
        "chat_id": config.CHAT_ID,
        "text": texto
    }
    requests.post(url, data=datos)

while True:
    cpu = calcular_cpu_porcentaje()
    ram = get_ram()
    temp = get_temperatura()

    if cpu > 70:
        mandar_mensaje("⚠️ CPU alta: " + str(cpu) + "%")

    if ram > 70:
        mandar_mensaje("⚠️ RAM alta: " + str(ram) + "%")

    if temp > 60:
        mandar_mensaje("🌡️ Temperatura alta: " + str(temp) + "°C")

    time.sleep(60)
