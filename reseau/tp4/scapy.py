paquet = Ether(src = 'ca:39:4a:d8:87:a2' , dst = 'fe:ea:4e:7f:18:53')
sendp( paquet , iface = 'eth0')


192.168.0.X

IP_FANTOME = '192.168.128.1'

def repondre(p):
    if ARP in p and p.pdst == IP_FANTOME and p.op == 1:
        paquet = Ether(src='ca:39:4a:d8:87:a2', dist=paquet.src) / ARP(op= 2, hwrsc='ca:39:4a:d8:87:a2',
                                                                       psrc=IP_FANTOME, hwdst=p.src,
                                                                       pdst=paquet.psrc)
        
