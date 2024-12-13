Un outil pour lancer facilement les conteneurs en ligne de commande avec omv-docker-compose.

## Commandes

- Lancer toutes les stacks:

  ```sh
  python3 omv-docker-compose-helper.py up
  ```

- Arrêter toutes les stacks:

  ```sh
  python3 omv-docker-compose-helper.py down
  ```
  
  - On peut ajouter ```--ignore``` pour omettre certaines stacks: ```--ignore stack1,stack2```

- Lancer seulement  une stack

  ```sh
  python3 omv-docker-compose-helper.py --stack stack up
  ```

  - On peut ajouter ```--ignore``` pour omettre certaines stacks: ```--ignore stack1,stack2```

- Arrêter seulement une stack:

  ```sh
  python3 omv-docker-compose-helper.py --stack stack down
  ```

- Lister les stacks:

  ```sh
  python3 omv-docker-compose-helper.py
  ```

  

