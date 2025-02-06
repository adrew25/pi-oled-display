# Pi OLED Display

A small project to display live system stats on an OLED screen using a Raspberry Pi. The display shows the Pi's local IP address and real-time system performance, such as CPU usage and memory stats.

## Features

- Displays **real-time system stats** on an OLED screen.
- Shows the **Pi's local IP address** (Wi-Fi or Ethernet).
- Utilizes **I2C** to interface with the OLED display.
- Lightweight and runs on a Raspberry Pi with Docker.

## Requirements

- **Raspberry Pi** (any model with I2C support).
- **OLED Display** (using I2C interface).
- **Docker** (to run the app in a container).
- **Python 3** for the script.

## Installation

1. **Clone this repository**:
   ```bash
   git clone https://github.com/yourusername/pi-oled-display.git
   cd pi-oled-display
	```
2. **Build and start the Docker container:**
	```bash
	docker-compose up --build -d
	```
3. **Ensure the I2C interface is enabled on your Raspberry Pi:**
	- Open raspi-config:
	```bash
		sudo raspi-config
		```
	- Navigate to Interfacing Options → I2C → Enable.
	- Reboot the Raspberry Pi
4. **Connect your OLED display to the Raspberry Pi's I2C pins (SCL and SDA).**

## Running the Application
Once the container is running, the system stats will be displayed on your OLED screen. It will continuously update with the Pi's IP address, CPU usage, and memory usage.

## Project Structure
- display.py: The Python script that gathers system stats and updates the OLED display.
- Dockerfile: Contains instructions to build the Docker image.
- docker-compose.yml: Defines the Docker container setup.
- requirements.txt: Lists Python dependencies

## Dependencies
- psutil – For gathering system stats.
- Adafruit_SSD1306 – For controlling the OLED display.
- RPi.GPIO – For GPIO interaction
- docker – To run the application inside a container.

## License

This project is licensed under the MIT License - see the LICENSE file for details.


## Acknowledgments

- Based on the Adafruit SSD1306 library for OLED displays.
- Special thanks to psutil for system monitoring capabilities.


