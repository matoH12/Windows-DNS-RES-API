# Windows-DNS-RES-API

# virtual.cloud-API

WEB rozhranie pre pridavanie a odoberanie DNS zaznamov vo windows prostredi. 

Program je napisany pomocou python a flask kniznice


Instalacia:

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

#Spustenie programu:

```python dns_api.py```





Testovanie programu:


1. Vytvorenie DNS zaznamu A:

```curl -X POST -H "Content-Type: application/json" -d '{"name": "test", "type": "A", "value": "192.168.1.1"}' http://localhost:5000/dns/add ```


2. Zmazanie DNS zaznamu A:

``` curl -X POST -H "Content-Type: application/json" -d '{"name": "test", "type": "A"}' http://localhost:5000/dns/delete ```



3. Vytvorenie PTR zaznamu:

```curl -X POST -H "Content-Type: application/json" -d '{"name": "test", "type": "A", "value": "192.168.1.1"}' http://localhost:5000/dns/add ```


4. Zmazanie zaznamu PTR:

```curl -X POST -H "Content-Type: application/json" -d '{"name": "test", "type": "A"}' http://localhost:5000/dns/delete ```
