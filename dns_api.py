from flask import Flask, request, jsonify
import winrm

app = Flask(__name__)

# Replace with your Windows DNS server details
DNS_SERVER = 'localhost'
USERNAME = 'Administrator'
PASSWORD = 'Jahod@'

# Function to execute PowerShell command on remote Windows server
def run_powershell_command(command):
    session = winrm.Session(f'http://{DNS_SERVER}:5985/wsman', auth=(USERNAME, PASSWORD))
    result = session.run_ps(command)
    if result.status_code == 0:
        return result.std_out.decode()
    else:
        raise Exception(result.std_err.decode())
    
def create_ptr_zone(ip_address: str) -> str:
    # Split the IP address into its components
    ip_parts = ip_address.split('.')

    # Remove the last octet
    ip_parts = ip_parts[:-1]

    # Reverse the remaining parts
    reversed_ip_parts = ip_parts[::-1]

    # Join the reversed parts with dots and add the in-addr.arpa suffix
    ptr_zone = '.'.join(reversed_ip_parts) + '.in-addr.arpa'

    return ptr_zone



@app.route('/dns/add', methods=['POST'])
def add_record():

    try:
        data = request.json
        record_name = data.get('name')
        record_type = data.get('type', 'A')  # Default to A record
        record_value = data.get('value')
        
        command = f"Add-DnsServerResourceRecord{record_type} -ZoneName 'virtual.cloud.tuke.sk' -Name '{record_name}' -IPv4Address '{record_value}'"
        response = run_powershell_command(command)
        
        return jsonify({'status': 'success', 'response': response}), 200
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500

@app.route('/dns/delete', methods=['POST'])
def delete_record():
    try:
        data = request.json
        record_name = data.get('name')
        record_type = data.get('type', 'A')  # Default to A record
        
        command = f"Remove-DnsServerResourceRecord -ZoneName 'virtual.cloud.tuke.sk' -Name '{record_name}' -RRType '{record_type}' -Force"
        response = run_powershell_command(command)
        
        return jsonify({'status': 'success', 'response': response}), 200
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500


@app.route('/dns/add_ptr', methods=['POST'])
def add_ptr_record():
    try:
        data = request.json
        ip_address = data.get('ip')
        ptr_name = data.get('ptr_name')
        ptr_zone = create_ptr_zone(ip_address)

        # Convert IP address to PTR record format
        reversed_ip = '.'.join(reversed(ip_address.split('.'))) + '.in-addr.arpa'
        
        command = f"Add-DnsServerResourceRecordPtr -ZoneName '{ptr_zone}' -Name '{reversed_ip}' -PtrDomainName '{ptr_name}'"
        response = run_powershell_command(command)
        
        return jsonify({'status': 'success', 'response': response}), 200
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500

@app.route('/dns/delete_ptr', methods=['POST'])
def delete_ptr_record():
    try:
        data = request.json
        ip_address = data.get('ip')
        ptr_zone = create_ptr_zone(ip_address)

        # Convert IP address to PTR record format
        reversed_ip = '.'.join(reversed(ip_address.split('.'))) + '.in-addr.arpa'
        
        command = f"Remove-DnsServerResourceRecord -ZoneName '{ptr_zone}' -Name '{reversed_ip}' -RRType 'PTR' -Force"
        response = run_powershell_command(command)
        
        return jsonify({'status': 'success', 'response': response}), 200
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
