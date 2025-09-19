# PyDM - Python Download Manager

[![Python Version](https://img.shields.io/badge/python-3.7+-blue.svg)](https://python.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/Docteur-Parfait/pydm.svg)](https://github.com/Docteur-Parfait/pydm/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/Docteur-Parfait/pydm.svg)](https://github.com/Docteur-Parfait/pydm/network)

Un gestionnaire de téléchargement moderne et intuitif avec interface graphique, développé en Python avec tkinter.

## 🚀 Fonctionnalités

### ✨ Fonctionnalités Principales

- **Interface graphique moderne** avec tkinter
- **Téléchargement avec pause/reprise** - Reprenez vos téléchargements interrompus
- **Barre de progression en temps réel** - Suivez l'avancement de vos téléchargements
- **Sélection de dossier personnalisé** - Choisissez où sauvegarder vos fichiers
- **Gestion des erreurs intelligente** - Messages d'erreur clairs et informatifs
- **Interface responsive et scrollable** - Fonctionne sur toutes les tailles d'écran

### 🔧 Fonctionnalités Avancées

- **Reprise automatique** - Les téléchargements interrompus reprennent automatiquement
- **Simulation de navigateur** - Contourne les protections anti-bot
- **Gestion des cookies** - Maintient les sessions comme un navigateur
- **Support multi-plateforme** - Windows, macOS, Linux
- **Validation d'URL** - Vérification automatique des liens
- **Affichage de vitesse** - Vitesse de téléchargement en temps réel

## 📸 Captures d'écran

```
┌─────────────────────────────────────────────────────────────┐
│                    PyDM - Python Download Manager          │
├─────────────────────────────────────────────────────────────┤
│ 🔗 URL du fichier                                          │
│ ┌─────────────────────────────────────────────────────────┐ │
│ │ https://example.com/file.zip                           │ │
│ └─────────────────────────────────────────────────────────┘ │
│                                                             │
│ 📁 Dossier de téléchargement                               │
│ ┌─────────────────────────────────────────┐ ┌──────────┐   │
│ │ C:\Users\Username\Downloads             │ │ 📂 Parcourir │ │
│ └─────────────────────────────────────────┘ └──────────┘   │
│                                                             │
│ 📊 Progression                                             │
│ ████████████████████████████████████████ 85%              │
│ Téléchargé: 42.5 MB / 50.0 MB (85.0%)                     │
│ Vitesse: 2.3 MB/s                                          │
│                                                             │
│ ┌─────────────┐ ┌─────────────┐ ┌─────────────┐ ┌─────────┐ │
│ │ 🚀 Télécharger │ │ ⏸️ Pause    │ │ ❌ Annuler   │ │ 📂 Ouvrir │ │
│ └─────────────┘ └─────────────┘ └─────────────┘ └─────────┘ │
└─────────────────────────────────────────────────────────────┘
```

## 🛠️ Installation

### Prérequis

- Python 3.7 ou supérieur
- pip (gestionnaire de paquets Python)

### Installation rapide

```bash
# Cloner le repository
git clone https://github.com/Docteur-Parfait/pydm.git
cd pydm

# Installer les dépendances
pip install -r requirements.txt

# Lancer l'application
python download.py
```

### Installation avec pip (bientôt disponible)

```bash
pip install pydm
```

## 🚀 Utilisation

### Lancement de l'application

```bash
python download.py
```

### Guide d'utilisation

1. **Entrez l'URL** du fichier à télécharger dans le champ de saisie
2. **Choisissez le dossier** de destination (optionnel, par défaut: Downloads)
3. **Spécifiez un nom** de fichier personnalisé (optionnel)
4. **Cliquez sur "Télécharger"** pour commencer
5. **Utilisez les contrôles** :
   - ⏸️ **Pause/Reprendre** : Mettez en pause ou reprenez le téléchargement
   - ❌ **Annuler** : Arrêtez et supprimez le fichier partiel
   - 📂 **Ouvrir Dossier** : Accédez directement au dossier de téléchargement

### Raccourcis clavier

- **Entrée** : Démarrer le téléchargement (quand le champ URL est sélectionné)
- **Molette de souris** : Faire défiler l'interface

## 🔧 Configuration

### Variables d'environnement

```bash
# Dossier de téléchargement par défaut
export PYDM_DOWNLOAD_DIR="/path/to/downloads"

# User-Agent personnalisé
export PYDM_USER_AGENT="MonApp/1.0"
```

### Fichier de configuration

Créez un fichier `config.json` dans le répertoire de l'application :

```json
{
  "default_download_folder": "C:\\Users\\Username\\Downloads",
  "user_agent": "PyDM/1.0",
  "max_retries": 3,
  "timeout": 30
}
```

## 🏗️ Architecture

### Structure du projet

```
pydm/
├── download.py          # Application principale
├── requirements.txt     # Dépendances Python
├── setup.py            # Configuration d'installation
├── README.md           # Documentation principale
├── CONTRIBUTING.md     # Guide de contribution
├── LICENSE             # Licence MIT
└── tests/              # Tests unitaires (à venir)
    └── test_download.py
```

### Classes principales

- **`DownloadManager`** : Gère l'état des téléchargements
- **`DownloadGUI`** : Interface graphique principale
- **`DownloadThread`** : Thread de téléchargement (à venir)

## 🧪 Tests

```bash
# Lancer les tests
python -m pytest tests/

# Tests avec couverture
python -m pytest --cov=download tests/
```

## 🤝 Contribution

Nous accueillons toutes les contributions ! Consultez notre [Guide de Contribution](CONTRIBUTING.md) pour plus d'informations.

### Comment contribuer

1. **Fork** le projet
2. **Créez** une branche pour votre fonctionnalité (`git checkout -b feature/AmazingFeature`)
3. **Commitez** vos changements (`git commit -m 'Add some AmazingFeature'`)
4. **Pushez** vers la branche (`git push origin feature/AmazingFeature`)
5. **Ouvrez** une Pull Request

### Idées de contributions

- 🐛 **Correction de bugs**
- ✨ **Nouvelles fonctionnalités**
- 📚 **Amélioration de la documentation**
- 🧪 **Tests unitaires**
- 🎨 **Amélioration de l'interface**
- 🌐 **Support multilingue**

## 📋 Roadmap

### Version 1.1.0

- [ ] Support des téléchargements multiples
- [ ] Historique des téléchargements
- [ ] Thèmes personnalisables
- [ ] Notifications système

### Version 1.2.0

- [ ] Support des torrents
- [ ] Intégration cloud (Google Drive, Dropbox)
- [ ] API REST
- [ ] Mode ligne de commande

### Version 2.0.0

- [ ] Interface web
- [ ] Synchronisation multi-appareils
- [ ] Plugins système
- [ ] Base de données intégrée

## 🐛 Signaler un bug

Si vous trouvez un bug, merci de créer une [issue](https://github.com/Docteur-Parfait/pydm/issues) avec :

- Description détaillée du problème
- Étapes pour reproduire
- Version de Python utilisée
- Captures d'écran si applicable

## 💡 Demander une fonctionnalité

Pour demander une nouvelle fonctionnalité :

1. Vérifiez d'abord les [issues existantes](https://github.com/Docteur-Parfait/pydm/issues)
2. Créez une nouvelle issue avec le label "enhancement"
3. Décrivez clairement la fonctionnalité souhaitée

## 📄 Licence

Ce projet est sous licence MIT. Voir le fichier [LICENSE](LICENSE) pour plus de détails.

## 👥 Auteurs

- **Docteur-Parfait** - _Développement initial_ - [@Docteur-Parfait](https://github.com/Docteur-Parfait)

## 🙏 Remerciements

- [requests](https://github.com/psf/requests) - Bibliothèque HTTP
- [tkinter](https://docs.python.org/3/library/tkinter.html) - Interface graphique
- Tous les contributeurs de la communauté open source

## 📊 Statistiques

![GitHub stars](https://img.shields.io/github/stars/Docteur-Parfait/pydm?style=social)
![GitHub forks](https://img.shields.io/github/forks/Docteur-Parfait/pydm?style=social)
![GitHub issues](https://img.shields.io/github/issues/Docteur-Parfait/pydm)
![GitHub pull requests](https://img.shields.io/github/issues-pr/Docteur-Parfait/pydm)

---

⭐ **Si ce projet vous plaît, n'hésitez pas à lui donner une étoile !** ⭐
