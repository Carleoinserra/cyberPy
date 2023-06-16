import sys

from scapy.layers.inet import IP, TCP,sr
from scapy.sendrecv import sr1
# Indirizzo IP dell'host di destinazione
target_ip = "172.217.168.206"  # Indirizzo IP corrispondente a google.com

# Porte da scannerizzare
ports = [80, 443]

# Esegui la scansione di porte
for port in ports:
    # Crea il pacchetto TCP con la porta di destinazione
    packet = IP(dst=target_ip) / TCP(dport=port, flags="S")

    # Invia il pacchetto e ricevi la risposta
    response = sr(packet, timeout=2, verbose=False)

    # Verifica se la porta è aperta
    if response and response[0][1].haslayer(TCP) and response[0][1][TCP].flags == "SA":
        print(f"Porta {port} aperta su google.com")
