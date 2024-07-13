
# Windows-DNS-RES-API

## Introduction
This project provides a web interface for adding and removing DNS records in a Windows environment. The program is written using Python and the Flask library, enabling easy management of DNS records through a REST API.

## Table of Contents
- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Dependencies](#dependencies)
- [Configuration](#configuration)
- [Testing](#testing)
- [Contributors](#contributors)
- [License](#license)

## Installation

### Operating System Preparation
1. Install necessary Windows features and enable PSRemoting:
   ```sh
   Install-WindowsFeature -Name "WindowsPowerShellWebAccess"
   Enable-PSRemoting -Force
   Set-Item WSMan:\localhost\Client\TrustedHosts -Value "RemoteHostName"
   Enable-NetFirewallRule -Name "WINRM-HTTP-In-TCP"
   Enable-NetFirewallRule -Name "WINRM-HTTPS-In-TCP"
   Set-NetFirewallRule -Name "WINRM-HTTP-In-TCP" -Enabled True
   winrm enumerate winrm/config/listener
   Enable-PSRemoting -Force
   ```

2. Install `curl`:
   ```sh
   Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))
   choco install curl -y
   ```

### Python and Package Installation
1. Install Python from [python.org](https://www.python.org/downloads/release/python-3124/).

2. Install required Python packages:
   ```sh
   pip install flask pywinrm
   ```

### Running the Program
1. Run the DNS API program:
   ```sh
   python dns_api.py
   ```

### Install as a Windows Service
1. Install `pywin32` package:
   ```sh
   pip install pywin32
   ```

2. Install and start the service:
   ```sh
   python flask_service.py install
   python flask_service.py start
   sc config FlaskDNSService start= auto
   ```

### Removing the Service
1. Stop and remove the service:
   ```sh
   python flask_service.py stop
   python flask_service.py remove
   ```

## Usage
The API provides endpoints to add and remove DNS records. Below are examples of how to use the API with `curl`.

### Testing

1. Create DNS record A:
   ```sh
   curl -X POST -H "Content-Type: application/json" -d "{\"name\": \"test\", \"type\": \"A\", \"value\": \"192.168.1.1\"}" http://localhost:5000/dns/add
   ```

2. Delete DNS record A:
   ```sh
   curl -X POST -H "Content-Type: application/json" -d "{\"name\": \"test\", \"type\": \"A\", \"value\": \"192.168.1.1\"}" http://localhost:5000/dns/delete
   ```

3. Create PTR record:
   ```sh
   curl -X POST -H "Content-Type: application/json" -d "{\"ip\": \"147.232.204.10\", \"ptr_name\": \"example.yourdomain.com\"}" http://localhost:5000/dns/add_ptr
   ```

4. Delete DNS record PTR:
   ```sh
   curl -X POST -H "Content-Type: application/json" -d "{\"ip\": \"147.232.204.10\"}" http://localhost:5000/dns/delete_ptr
   ```

## Features
- Web interface for managing DNS records
- Support for A and PTR records
- Easy integration with Windows services

## Dependencies
- Windows OS with PowerShell Web Access
- Python 3.12.4 or later
- Flask
- pywinrm
- pywin32

## Configuration
No additional configuration is required beyond the installation steps provided.

## Contributors
- Martin Hasin [@matoh12](https://github.com/matoh12)

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
