#!/usr/bin/env python3
# Network Traffic Monitor
# Author: Rick Hayes
# License: MIT
# Version: 2.73
# README: Requires psutil. Monitors network traffic stats.

import psutil
import time
import argparse
import logging
import json

def setup_logging():
    """Configure logging to file."""
    logging.basicConfig(filename='network_traffic_monitor.log', level=logging.INFO,
                        format='%(asctime)s - %(levelname)s - %(message)s')

def load_config(config_file: str) -> dict:
    """Load configuration from JSON file."""
    try:
        with open(config_file, 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        logging.error(f"Config loading failed: {e}")
        return {"interface": None}

def monitor_traffic(interval: float, interface: str):
    """Monitor network traffic and log stats."""
    try:
        old_stats = psutil.net_io_counters(pernic=True).get(interface)
        if not old_stats:
            raise ValueError(f"Interface {interface} not found")
        
        while True:
            time.sleep(interval)
            new_stats = psutil.net_io_counters(pernic=True)[interface]
            sent = new_stats.bytes_sent - old_stats.bytes_sent
            recv = new_stats.bytes_recv - old_stats.bytes_recv
            info = f"Sent: {sent} bytes, Received: {recv} bytes in {interval}s"
            logging.info(info)
            print(info)
            old_stats = new_stats
    except (ValueError, KeyError) as e:
        logging.error(f"Traffic monitoring failed: {e}")
        print(f"Error: {e}")

def main():
    """Main function to parse args and monitor traffic."""
    parser = argparse.ArgumentParser(description="Network Traffic Monitor")
    parser.add_argument("--interval", type=float, default=1.0, help="Monitoring interval in seconds")
    parser.add_argument("--config", default="config.json", help="Config file path")
    args = parser.parse_args()

    setup_logging()
    config = load_config(args.config)

    if args.interval <= 0:
        logging.error("Interval must be positive")
        print("Error: Interval must be positive")
        return

    logging.info(f"Starting traffic monitor with interval {args.interval}s")
    monitor_traffic(args.interval, config["interface"])

if __name__ == "__main__":
    main()
