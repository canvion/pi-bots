# 🍓 Telegram Bot - Raspberry Pi Monitor

Bot de Telegram para monitorizar el estado de una Raspberry Pi en tiempo real. Manda alertas automáticas cuando algo va mal y responde a comandos manuales.

## ¿Qué hace?

**Alertas automáticas** (anti-spam: máximo 1 alerta cada 10 minutos):
- ⚠️ CPU superior al 80%
- ⚠️ RAM superior al 80%
- 🌡️ Temperatura superior a 70°C
- 💾 Disco superior al 80%
- 🔴 Pérdida de conexión a internet
- 🟢 Recuperación de conexión a internet
- 📡 Nuevo dispositivo conectado a la red
- 🍓 Aviso cuando el Pi arranca

**Informe diario automático** a las 8h con CPU, RAM, temperatura, disco y uptime.

## Comandos disponibles

| Comando | Descripción |
|---|---|
| `/estado` | CPU, RAM, temperatura, disco y uptime |
| `/disco` | Espacio usado, libre y total en GB |
| `/ip` | IP local y IP de Tailscale |
| `/procesos` | Top 5 procesos que más CPU consumen |
| `/pihole` | Dominios bloqueados hoy y porcentaje |
| `/docker` | Contenedores Docker activos |
| `/tiempo` | Previsión meteorológica de mañana (10h-18h) |
| `/reiniciar` | Reinicia el Pi remotamente |
| `/ayuda` | Lista todos los comandos |

## Instalación

**1. Clona el repositorio:**
```bash
git clone https://github.com/tu-usuario/telegrambot-RaspberryPi.git
cd telegrambot-RaspberryPi
```

**2. Crea tu archivo de configuración:**
```bash
cp config.example.py config.py
nano config.py
```

Rellena tus datos:
```python
TOKEN = "tu-token-de-botfather"
CHAT_ID = "tu-chat-id"
PIHOLE_PASSWORD = "tu-password-de-pihole"
```

**3. Ejecuta el bot:**
```bash
python3 bot.py
```

## Ejecutar como servicio (arranque automático)

Para que el bot arranque solo cada vez que el Pi se reinicie:

```bash
sudo nano /etc/systemd/system/telegrambot.service
```

```
[Unit]
Description=Telegram Bot Monitor
After=network.target

[Service]
User=tu-usuario
WorkingDirectory=/home/tu-usuario/telegrambot-RaspberryPi
ExecStart=/usr/bin/python3 /home/tu-usuario/telegrambot-RaspberryPi/bot.py
Restart=always

[Install]
WantedBy=multi-user.target
```

```bash
sudo systemctl enable telegrambot
sudo systemctl start telegrambot
```

## ¿Cómo obtener el Token y el Chat ID?

1. Abre Telegram y busca `@BotFather`
2. Escríbele `/newbot` y sigue los pasos
3. Copia el Token que te da
4. Busca tu bot, escríbele cualquier mensaje y entra en:
   `https://api.telegram.org/botTU_TOKEN/getUpdates`
5. Copia el valor del campo `"id"` dentro de `"chat"`

## Requisitos

- Raspberry Pi con Raspberry Pi OS
- Python 3
- Librería `requests` (`pip3 install requests --break-system-packages`)
- Pi-hole instalado (para el comando `/pihole`)
- Docker instalado (para el comando `/docker`)
- Conexión a internet
