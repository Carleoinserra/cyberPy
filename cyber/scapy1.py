from scapy.layers.inet import IP, ICMP
from scapy.sendrecv import sr1

# Crea un pacchetto ICMP "ping" con l'indirizzo IP di destinazione di Google
packet = IP(dst="8.8.8.8") / ICMP()

# Invia il pacchetto e ricevi la risposta
reply = sr1(packet, timeout=2)

# Verifica se la risposta è stata ricevuta
if reply is not None:
    print(f"Risposta ricevuta da {reply.src}")
else:
    print("Nessuna risposta ricevuta")
