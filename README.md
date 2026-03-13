# 🍓 Pi Bots - Bots de Telegram para Raspberry Pi

Colección de bots de Telegram que corren en una Raspberry Pi 5. Cada bot vive en su propia carpeta y se ejecuta como servicio independiente.

---

## 📁 Estructura

```
pi-bots/
├── pi-monitor/        → Monitor del sistema
└── pi-recordatorios/  → Bot de recordatorios
```

---

## 🖥️ Pi Monitor

Bot que monitoriza el estado de la Raspberry Pi en tiempo real. Manda alertas automáticas y responde a comandos.

### Alertas automáticas
Anti-spam: máximo 1 alerta cada 10 minutos.

- ⚠️ CPU superior al 80%
- ⚠️ RAM superior al 80%
- 🌡️ Temperatura superior a 70°C
- 💾 Disco superior al 80%
- 🔴 Pérdida de conexión a internet
- 🟢 Recuperación de conexión
- 📡 Nuevo dispositivo en la red
- 🍓 Aviso cuando el Pi arranca

**Informe diario automático** a las 8h.

### Comandos

| Comando | Descripción |
|---|---|
| `/estado` | CPU, RAM, temperatura, disco y uptime |
| `/disco` | Espacio usado, libre y total en GB |
| `/ip` | IP local y IP de Tailscale |
| `/procesos` | Top 5 procesos por CPU |
| `/pihole` | Dominios bloqueados hoy |
| `/docker` | Contenedores Docker activos |
| `/tiempo` | Previsión meteorológica mañana (10h-18h) |
| `/reiniciar` | Reinicia el Pi remotamente |
| `/ayuda` | Lista todos los comandos |

### Instalación

```bash
cd pi-monitor
cp config.example.py config.py
nano config.py
python3 bot.py
```

### config.py
```python
TOKEN = "tu-token-de-botfather"
CHAT_ID = "tu-chat-id"
PIHOLE_PASSWORD = "tu-password-de-pihole"
```

---

## ⏰ Pi Recordatorios

Bot para gestionar recordatorios desde Telegram con lenguaje natural.

### Uso

Escribe directamente sin comandos:
- `a las 18h recuérdame sacar la lavadora`
- `a las 18:30 recuérdame llamar al médico`
- `en 30 minutos recuérdame apagar el horno`

### Comandos

| Comando | Descripción |
|---|---|
| `/recordatorios` | Ver todos los pendientes |
| `/borrar 1` | Borrar el recordatorio número 1 |
| `/borrar todo` | Borrar todos los recordatorios |
| `/ayuda` | Instrucciones de uso |

### Instalación

```bash
cd pi-recordatorios
cp config.example.py config.py
nano config.py
python3 bot.py
```

### config.py
```python
TOKEN = "tu-token-de-botfather"
CHAT_ID = "tu-chat-id"
```

---

## Ejecutar como servicio

Para que cada bot arranque solo al reiniciar el Pi:

```bash
sudo nano /etc/systemd/system/nombre-bot.service
```

```
[Unit]
Description=Nombre del bot
After=network.target

[Service]
User=tu-usuario
WorkingDirectory=/home/tu-usuario/bots_telegram/nombre-bot
ExecStart=/usr/bin/python3 /home/tu-usuario/bots_telegram/nombre-bot/bot.py
Restart=always

[Install]
WantedBy=multi-user.target
```

```bash
sudo systemctl enable nombre-bot
sudo systemctl start nombre-bot
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
- `pip3 install requests --break-system-packages`
- Pi-hole (para `/pihole`)
- Docker (para `/docker`)
- Conexión a internet
