# Network Traffic Monitor

## Overview
The Network Traffic Monitor is a Python tool that tracks network traffic statistics using the `psutil` library. It reports bytes sent and received over a specified interval, optionally for a specific interface.

## Author
Rick Hayes

## License
MIT

## Version
2.73

## Requirements
- Python 3.x
- `psutil` library (`pip install psutil`)

## Usage
Run the script with the following arguments:

```bash
python3 network_traffic_monitor.py [--interval <SECONDS>] [--config <CONFIG_FILE>]
