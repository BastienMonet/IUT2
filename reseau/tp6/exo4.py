import subprocess
import time
import asyncio

async def ping_address_sync(ip):
    """
    On utilise subprocess.run pour lancer le ping (sous linux)
    Tente de pinger une adresse IP.
    -c 1 : Envoie 1 seul paquet.
    -W 1 : Attend au maximum 1 seconde pour la réponse.
    on ignore les sorties standard et d’erreur en renvoyant tout vers DEVNULL
    """
    # Le programme est bloqué ici tant que le ping n’est pas fini
    cmd = f'ping -c 1 -W 1 {ip}'
    result = await asyncio.create_subprocess_shell(
        cmd,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )
    stdout, stderr = await result.communicate()

    # returncode est le code retour du processus. Si le ping fonctionne, il retourne 0
    return ip, result.returncode

async def main():
    # Plage d’adresses à pinger
    base_ip = "192.168.28."
    start_range = 1
    end_range = 100

    print(f"Lancement du scan sur {base_ip}{start_range} à {end_range}...\n")
    start_time = time.perf_counter()
    results = []

    for i in range(start_range, end_range):
            # construction de l’adresse IP
            ip = f"{base_ip}{i}"
            # On exécute les pings
            results.append(ping_address_sync(ip))

    afficheips = await asyncio.gather(* results)
    for afficheip in afficheips:
        if (afficheip[1]):
              print(afficheip[0] + " : ONLINE")
        else:
            print(afficheip[0] + ' : OFFLINE')



    end_time = time.perf_counter()
    print(f"\nScan terminé en {end_time - start_time:.2f} secondes.")

if __name__ == "__main__":
    asyncio.run(main())
