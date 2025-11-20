## le NAT

transforme les addresse public en adresse privé


### Fonctionnement du NAT
Lorsqu'un appareil d'un réseau privé envoie un paquet vers Internet, le routeur NAT modifie l'adresse source du paquet en remplaçant l'adresse IP privée par une adresse IP publique. Lorsque la réponse revient, le routeur NAT remplace l'adresse IP publique par l'adresse IP privée correspondante avant de transmettre le paquet à l'appareil d'origine.


### Attention
le NAT permet d'utiliser les adresse publique uniquement pour les connexions sortantes. donc si tout le monde utilise le NAT, il n'y aura plus d'adresse publique disponible pour les connexions entrantes.

Pourquoi utiliser un NAT: 
pour palier le peu d'IPv4 + securité


on peut interagir avec l'exterieur, mais l'exterieur ne peut pas nous appeler


table d'association dans le router, le NAT est configuré dans le Routeur


## Complementaire

ACL : access control list : le truc des parfeu (donne les permisson que à ...)

nat source : ont peut pas voir de l'exterieur mais on peut appeler de l'interieur (seul les client on des nat puisque les serveur on besoin de repondre)



- @pc1 ping @pc2
- ICMP request
- la gateway renvoie au routeur
- le nat transforme l'adresse publique en adresse privé
- le router dit dans quel reseau est @pc2 entre ces port eth et ces routes par default defini (avec ip route)
- @pc1 trouve @pc2
- ICMP reply 





