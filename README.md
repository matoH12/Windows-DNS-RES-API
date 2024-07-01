# Windows-DNS-RES-API


Web Interface for Adding and Removing DNS Records in a Windows Environment

The program is written using Python and the Flask library.

Instalation:

1. Priprava operacneho systemu:

```Install-WindowsFeature -Name "WindowsPowerShellWebAccess"```

```Enable-PSRemoting -Force```

```Set-Item WSMan:\localhost\Client\TrustedHosts -Value "RemoteHostName"```

```Enable-NetFirewallRule -Name "WINRM-HTTP-In-TCP"```

```Enable-NetFirewallRule -Name "WINRM-HTTPS-In-TCP"```

```Set-NetFirewallRule -Name "WINRM-HTTP-In-TCP" -Enabled True```

```winrm enumerate winrm/config/listener```

```Enable-PSRemoting -Force```

#curl install

```Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))```

```choco install curl -y```


#Instalacia balikov python: 

```https://www.python.org/downloads/release/python-3124/```

#Instalacia python balikov:

```pip install flask pywinrm```

#program run:

```python dns_api.py```


#Install to windows services 

```pip install pywin32```

```python flask_service.py install```

```python flask_service.py start```


```python flask_service.py stop```

```python flask_service.py remove```









#Testing:


1. Create DNS record A:

```curl -X POST -H "Content-Type: application/json" -d '{"name": "test", "type": "A", "value": "192.168.1.1"}' http://localhost:5000/dns/add ```


2. Delete DNS record A:

``` curl -X POST -H "Content-Type: application/json" -d '{"name": "test", "type": "A"}' http://localhost:5000/dns/delete ```



3. create PTR record:

```curl -X POST -H "Content-Type: application/json" -d '{"name": "test", "type": "A", "value": "192.168.1.1"}' http://localhost:5000/dns/add ```


4. delete DNS record PTR:

```curl -X POST -H "Content-Type: application/json" -d '{"name": "test", "type": "A"}' http://localhost:5000/dns/delete ```
