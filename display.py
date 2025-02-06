import os
import psutil
import socket
from time import sleep
from luma.oled.device import ssd1306
from luma.core.interface.serial import i2c
from luma.core.render import canvas
from PIL import ImageFont

# Setup I2C OLED Display
serial = i2c(port=1, address=0x3C)
device = ssd1306(serial)

# Load a basic font
font = ImageFont.load_default()

def get_local_ip():
    """Get the Raspberry Pi's actual local IPv4 address."""
    try:
        # Get the IP from the wlan0 (Wi-Fi) or eth0 (Ethernet) interface
        ip = os.popen("hostname -I | awk '{print $1}'").read().strip()
        if not ip:
            ip = "No IP"
        return ip
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

    # Clear the display before writing new content
    #device.clear()

    # Format the values to ensure they fit
    cpu_usage_str = f"CPU: {cpu_usage:.1f}%"
    ram_usage_str = f"RAM: {ram_usage:.1f}%"
    temp_str = f"Temp: {temp}"

    # Create an image buffer and write to the OLED
    with canvas(device) as draw:
        # Adjust the starting positions and line spacing
        draw.text((5, 0), f"IP: {ip_address}", font=font, fill="white")
        draw.text((5, 16), cpu_usage_str[:16], font=font, fill="white")  # Limit to 16 chars
        draw.text((5, 32), ram_usage_str[:16], font=font, fill="white")  # Limit to 16 chars
        draw.text((5, 48), temp_str[:16], font=font, fill="white")  # Limit to 16 chars

    sleep(2)  # Update every 2 seconds

