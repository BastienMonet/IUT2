import ssl

address = ('wikipedia.org', 443)
certif = ssl.get_server_certificate(address)
print(certif)