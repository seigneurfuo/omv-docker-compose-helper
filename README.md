Un outil pour lancer facilement les conteneurs en ligne de commande avec le plugin docker-compose de OMV-extras.

Note: Bien penser à modifier la variable du chemin par défaut de l'emplacement des stacks.

## Commandes

- Lancer toutes les stacks:

  ```sh
  python3 omv-docker-compose-helper.py up
  ```

  - On peut ajouter ```--ignore``` pour omettre certaines stacks: ```--ignore stack1,stack2```

- Arrêter toutes les stacks:

  ```sh
  python3 omv-docker-compose-helper.py down
  ```
  
  - On peut ajouter ```--ignore``` pour omettre certaines stacks: ```--ignore stack1,stack2```

- Lancer seulement  une stack

  ```sh
  python3 omv-docker-compose-helper.py --stack stack up
  ```

- Arrêter seulement une stack:

  ```sh
  python3 omv-docker-compose-helper.py --stack stack down
  ```

- Lister les stacks:

  ```sh
  python3 omv-docker-compose-helper.py
  ```

