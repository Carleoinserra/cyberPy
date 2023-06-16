import nmap

def scan_network(target):
    nm = nmap.PortScanner()
    nm.scan(target, arguments='-p 1-1000')

    for host in nm.all_hosts():
        print('Host:', host)
        for proto in nm[host].all_protocols():
            print('Protocol:', proto)

            ports = nm[host][proto].keys()
            for port in ports:
                print('Port:', port, 'State:', nm[host][proto][port]['state'])

# Esempio di utilizzo
target = '192.168.1.241'  # Specifica la tua rete o l'indirizzo IP di destinazione
scan_network(target)