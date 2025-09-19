# Changelog

Toutes les modifications notables de ce projet seront documentées dans ce fichier.

Le format est basé sur [Keep a Changelog](https://keepachangelog.com/fr/1.0.0/),
et ce projet adhère au [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added

- Support des téléchargements multiples
- Thème sombre
- Mode ligne de commande
- API REST

### Changed

- Amélioration de l'interface utilisateur
- Optimisation des performances

### Fixed

- Correction du bug de reprise de téléchargement
- Amélioration de la gestion des erreurs

## [1.0.0] - 2024-01-15

### Added

- Interface graphique moderne avec tkinter
- Téléchargement avec pause/reprise
- Barre de progression en temps réel
- Sélection de dossier personnalisé
- Gestion des erreurs intelligente
- Interface responsive et scrollable
- Reprise automatique des téléchargements interrompus
- Simulation de navigateur pour contourner les protections anti-bot
- Gestion des cookies et sessions
- Support multi-plateforme (Windows, macOS, Linux)
- Validation d'URL automatique
- Affichage de vitesse de téléchargement
- Raccourcis clavier
- Messages d'erreur spécifiques (403 Forbidden, 404, etc.)
- Configuration via variables d'environnement
- Support des redirections HTTP
- Gestion des fichiers partiellement téléchargés

### Technical

- Architecture modulaire avec classes séparées
- Gestion des threads pour la réactivité de l'interface
- Utilisation de requests.Session pour la persistance des cookies
- Headers HTTP réalistes pour simuler un navigateur
- Gestion robuste des exceptions
- Code documenté avec docstrings
- Support des tests unitaires

### Documentation

- README.md complet avec captures d'écran
- Guide de contribution détaillé
- Documentation des API
- Exemples d'utilisation
- Guide d'installation

## [0.1.0] - 2024-01-01

### Added

- Version initiale du projet
- Interface de base avec tkinter
- Téléchargement simple de fichiers
- Barre de progression basique

---

## Format des Entrées

### Types de Changements

- **Added** pour les nouvelles fonctionnalités
- **Changed** pour les changements de fonctionnalités existantes
- **Deprecated** pour les fonctionnalités qui seront supprimées
- **Removed** pour les fonctionnalités supprimées
- **Fixed** pour les corrections de bugs
- **Security** pour les corrections de vulnérabilités

### Exemples

```markdown
## [1.2.0] - 2024-02-01

### Added

- Support des téléchargements par lots
- Thème personnalisable

### Changed

- Amélioration de l'interface utilisateur
- Optimisation des performances de téléchargement

### Fixed

- Correction du bug de reprise sur Windows
- Amélioration de la gestion des erreurs réseau

### Security

- Correction de la vulnérabilité XSS dans l'interface
```

## Notes de Version

### Version 1.0.0

- Première version stable
- Interface graphique complète
- Toutes les fonctionnalités de base implémentées
- Documentation complète
- Tests unitaires

### Version 0.1.0

- Version de développement initiale
- Fonctionnalités de base
- Interface simple
