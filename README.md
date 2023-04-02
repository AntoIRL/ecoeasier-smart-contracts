# Crowdfunding de projets d'énergies renouvelables
Ce projet est un smart contract écrit en SmartPy pour permettre le financement participatif de projets d'énergies renouvelables sur la blockchain Tezos.

## Fonctionnement du smart contract
Le smart contract contient les fonctionnalités suivantes :

`buy_tokens(value: int)` : cette fonction permet à un utilisateur d'acheter des jetons en échange de tez (la monnaie de la blockchain Tezos). Le prix d'un jeton est défini lors du déploiement du contrat par l'administrateur. Les jetons sont stockés dans une liste qui associe chaque utilisateur à son nombre de jetons.

`update_price(value: int)` : cette fonction permet à l'administrateur de mettre à jour le prix des jetons.

`transfer(_to: str, value: int)` : cette fonction permet à un utilisateur d'envoyer des jetons à un autre utilisateur.

## Déploiement du smart contract
Le déploiement du smart contract peut être effectué à l'aide d'un explorateur de blocs Tezos, comme Better Call Dev.

Le smart contract peut être déployé en définissant deux paramètres : le prix d'un jeton et l'adresse de l'administrateur.

## Utilisation du smart contract
Une fois déployé, le smart contract peut être utilisé en appelant les fonctions décrites ci-dessus à l'aide d'un portefeuille Tezos compatible avec les smart contracts.

Par exemple, pour acheter des jetons, l'utilisateur peut appeler la fonction buy_tokens en spécifiant le nombre de jetons à acheter et en envoyant le montant correspondant en tez.

## Tests du smart contract
Des tests unitaires ont été écrits pour valider le fonctionnement du smart contract. Les tests peuvent être exécutés à l'aide de l'outil de test SmartPy.

## Contributeurs
- Mathis LIGOUT 
- Julie IRLÈS 
- Benoît Diene
- Carl VICTOR
- Antonin IRLÈS
