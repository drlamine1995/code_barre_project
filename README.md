# Documentation du projet  

# initialisation git : 
```bash
git init
git remote add origin SSH_REPO
git status
git add NOM_FICHIER
git commit
git commit -m "first commit"
git branch -M main
git push -u origin main

git add --all
git commit -m "modification des scipt js et index"
git push origin main
```

Dans le git commit ,    shortcut i pour insert et esc pour sortir 
                        shortcut : puis write w et q pour quit ( on ecrit wq )
                        pour quit c'est q! pour forcer le quit

On peut utiliser le -m directement pour ne pas lancer l'editeur de text 

# code_barre_project

## Objectif du projet
Le projet est une application web conçue pour gérer des bouteilles de gaz. L'application permet aux utilisateurs de suivre et de gérer les informations relatives à ces bouteilles, notamment en utilisant des codes-barres.

## Fonctionnalités principales

### 1. Gestion des bouteilles de gaz
- L'application offre des fonctionnalités CRUD (Création, Lecture, Mise à jour, Suppression) pour les bouteilles de gaz.
- Les utilisateurs peuvent ajouter de nouvelles bouteilles, les modifier, les rechercher par code-barres et les supprimer.

### 2. Base de données PostgreSQL
- Les informations sur les bouteilles de gaz sont stockées dans une base de données PostgreSQL.
- La table `bouteilles_de_gaz` contient des détails tels que le code-barres, le numéro de machine, la description, la quantité, l'emplacement et la date d'ajout.

### 3. Interface utilisateur
- L'application offre une interface utilisateur simple et intuitive pour interagir avec les données.
- Les utilisateurs peuvent rechercher des bouteilles par code-barres, voir une liste de toutes les bouteilles, ajouter de nouvelles bouteilles et modifier les bouteilles existantes.

### 4. Docker et Docker Compose
- Le projet utilise Docker pour conteneuriser l'application et ses dépendances, ce qui facilite le déploiement et l'exécution.
- Le fichier `docker-compose.yml` définit la configuration pour exécuter l'application et la base de données à l'aide de Docker Compose.

### 5. pgAdmin
- Le projet inclut également pgAdmin, une plateforme d'administration et de gestion pour PostgreSQL. Cela permet une gestion facile de la base de données via une interface web.

## Résumé
Le projet `code_barre_project` est une application web qui aide à gérer et à suivre les bouteilles de gaz en utilisant des codes-barres. Il utilise Flask pour le backend, PostgreSQL pour la base de données, et Docker pour la conteneurisation. L'application offre une interface utilisateur pour ajouter, modifier, rechercher et supprimer des bouteilles de gaz.