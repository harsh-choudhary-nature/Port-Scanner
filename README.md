# Python Port Scanner

A simple Python-based port scanner that uses multithreading to scan ports efficiently. This project is useful for checking open ports on a target IP address.

## Features

- Scans a range of ports on a target IP address.
- Utilizes multithreading for faster scanning.
- Simple and lightweight implementation using Python.

## Requirements

- Python 3.x

## Installation

1. Clone this repository:
    ```bash
    git clone https://github.com/your-username/python-port-scanner.git
    cd python-port-scanner
    ```

2. Install any required dependencies (if applicable):
    ```bash
    pip install -r requirements.txt
    ```

   > Note: This project only uses Python's standard libraries, so no additional dependencies are required.

## Usage

1. Edit the `target_ip` and `port_range` variables in the script to match your requirements:
    ```python
    target_ip = "192.168.1.1"  # Replace with the target IP
    port_range = range(1, 1025)  # Adjust the port range as needed
    ```

2. Run the script:
    ```bash
    python port_scanner.py
    ```

3. The script will print a list of open ports for the target IP:
    ```
    Port 22 is open on 192.168.1.1
    Port 80 is open on 192.168.1.1
    ```

## Example Output

When scanning a target IP, the script will display the open ports:
