import random

import requests

nomes = [
    'Ana Silva',
    'Maria Santos',
    'Laura Oliveira',
    'Sofia Almeida',
    'Isabela Pereira',
    'Beatriz Costa',
    'Gabriela Rodrigues',
    'Clara Fernandes',
    'Manuela Carvalho',
    'Julia Martins',
    'Pedro Souza',
    'Lucas Lima',
    'Enzo Goncalves',
    'Miguel Ferreira',
    'Arthur Ribeiro',
    'Davi Barbosa',
    'Rafael Oliveira',
    'Matheus Silva',
    'Gabriel Alves',
    'Joao Santos',
]
random.shuffle(nomes)
for i in nomes:
    navegador = requests.post(
        'http://192.168.1.16:8000/users/',
        json={
            'username': f'{i}',
            'email': f'{i.replace(' ', '').lower()}@email.com',
            'password': 'luis1234',
        },
    )
