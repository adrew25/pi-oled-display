import os
import psutil
import socket
import fcntl
import struct
from time import sleep
from luma.oled.device import ssd1306
from luma.core.interface.serial import i2c
from luma.core.render import canvas
from PIL import ImageFont, ImageDraw, Image

# Setup I2C OLED Display
serial = i2c(port=1, address=0x3C)
device = ssd1306(serial)

# Load a basic font
font = ImageFont.load_default()

def get_ip():
    """Get the Raspberry Pi's local IP address."""
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
    except:
        ip = "No IP"
    return ip


def get_local_ip():
    """Get the Raspberry Pi's actual local network IP."""
    try:
        # Check for Wi-Fi IP first
        ip = os.popen("ip a show wlan0 | grep inet | awk '{print $2}' | cut -d/ -f1").read().strip()
        if not ip:  # Fallback to Ethernet IP if no Wi-Fi
            ip = os.popen("ip a show eth0 | grep inet | awk '{print $2}' | cut -d/ -f1").read().strip()
        return ip if ip else "No IP"
    except:
        return "No IP"


def get_cpu_temp():
    """Get CPU temperature."""
    try:
        with open("/sys/class/thermal/thermal_zone0/temp", "r") as f:
            temp = int(f.read()) / 1000
        return f"{temp:.1f}°C"
    except:
        return "N/A"

while True:
    # Get system stats
    cpu_usage = psutil.cpu_percent()
    ram_usage = psutil.virtual_memory().percent
    temp = get_cpu_temp()
    ip_address = get_local_ip()

    # Create an image buffer
    with canvas(device) as draw:
        draw.text((5, 0), f"IP: {ip_address}", font=font, fill="white")
        draw.text((5, 12), f"CPU: {cpu_usage:.1f}%", font=font, fill="white")
        draw.text((5, 24), f"RAM: {ram_usage:.1f}%", font=font, fill="white")
        draw.text((5, 36), f"Temp: {temp}", font=font, fill="white")

    sleep(2)  # Update every 2 seconds

