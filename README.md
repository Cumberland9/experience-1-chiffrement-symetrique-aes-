# Expérience 1 — Chiffrement symétrique AES-GCM

## Description
Cette application Streamlit simule une communication sécurisée entre Alice et Bob à l'aide du chiffrement symétrique AES-GCM . Elle démontre comment un message peut être chiffré, transmis, puis déchiffré, tout en illustrant les propriétés d'authentification et d'intégrité offertes par le mode GCM.

## Objectifs
- Comprendre le fonctionnement du chiffrement symétrique AES-GCM
- Observer le rôle de la clé secrète partagée entre Alice et Bob
- montre comment Eve, une attaquante interceptant la communication, ne peut ni lire ni modifier le message sans être détectée
- Vérifier l'intégrité et l'authenticité des messages grâce au tag d'authentification GCM

## Fonctionnalités
- Génération d'une clé AES
- Chiffrement d'un message en texte clair saisi par l'utilisateur
- Simulation de l'interception du message par Eve
- Déchiffrement du message par Bob à l'aide de la clé partagée
- Détection d'une modification du texte chiffré (test d'intégrité)

## Technologies utilisées
- Streamlit — interface utilisateur
- PyCryptodome — implémentation du chiffrement AES-GCM

## Installation

```bash
pip install -r requirements.txt
```

## Auteur
Ilyass Taouani
