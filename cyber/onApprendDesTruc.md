ssh -J oXXXXXXXX@acces-tp.iut45.univ-orleans.fr \
-o StrictHostKeyChecking=no oXXXXXXXX@<IP de la VM>

-J : destination


1. Quelle est la machine passerelle? Pourquoi ne vous demande-t-on pas votre mot de passe des machines du
département?
La machine passerelle est "acces-tp.iut45.univ-orleans.fr". 
On ne vous demande pas votre mot de passe des machines du département car l'authentification 
se fait via la machine passerelle, qui agit comme un intermédiaire sécurisé. Une fois connecté 
à la machine passerelle, vous pouvez accéder aux autres machines sans avoir à ressaisir vos informations 
d'identification, souvent grâce à des clés SSH préconfigurées.

2. Quelle est la méthode d’authentification utilisée pour se connecter à la VM?
La méthode d'authentification utilisée pour se connecter à la VM est 
l'authentification par clé SSH. Cela permet une connexion sécurisée sans
 avoir à entrer un mot de passe, en utilisant une paire de clés publique/privée
  pour vérifier l'identité de l'utilisateur.

3. Précisez le rôle de l’option StrictHostKeyChecking=no.
L'option StrictHostKeyChecking=no désactive la vérification stricte de 
l'empreinte de la clé hôte lors de la connexion SSH. Cela signifie que si la 
clé hôte du serveur n'est pas reconnue (par exemple, lors de la première connexion), 
le client SSH acceptera automatiquement la clé sans demander confirmation à l'utilisateur. 
Cela peut être utile pour éviter les interruptions lors de connexions automatisées, mais 
cela peut aussi présenter un risque de sécurité, car cela rend le client vulnérable aux attaques de


