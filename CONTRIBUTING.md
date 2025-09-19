# Guide de Contribution - PytDm

Merci de votre intérêt à contribuer à PytDm ! Ce guide vous aidera à comprendre comment contribuer efficacement au projet.

## 📋 Table des matières

- [Code de Conduite](#code-de-conduite)
- [Comment Contribuer](#comment-contribuer)
- [Configuration de l'Environnement](#configuration-de-lenvironnement)
- [Processus de Contribution](#processus-de-contribution)
- [Standards de Code](#standards-de-code)
- [Tests](#tests)
- [Documentation](#documentation)
- [Types de Contributions](#types-de-contributions)

## 🤝 Code de Conduite

### Nos Engagements

Nous nous engageons à créer un environnement accueillant et inclusif pour tous les contributeurs, indépendamment de :

- L'âge, la taille, le handicap, l'ethnicité
- L'identité et l'expression de genre
- Le niveau d'expérience, la nationalité
- L'apparence personnelle, la race, la religion
- L'identité et l'orientation sexuelles

### Comportements Acceptables

- Utiliser un langage accueillant et inclusif
- Respecter les différents points de vue et expériences
- Accepter gracieusement les critiques constructives
- Se concentrer sur ce qui est le mieux pour la communauté
- Faire preuve d'empathie envers les autres membres

### Comportements Inacceptables

- L'utilisation de langage ou d'images sexualisés
- Le trolling, les commentaires insultants ou désobligeants
- Le harcèlement public ou privé
- La publication d'informations privées sans permission
- Toute conduite inappropriée dans un contexte professionnel

## 🚀 Comment Contribuer

### 1. Fork et Clone

```bash
# Fork le repository sur GitHub, puis clonez votre fork
git clone https://github.com/VOTRE_USERNAME/PytDm.git
cd PytDm

# Ajoutez le repository original comme remote
git remote add upstream https://github.com/Docteur-Parfait/PytDm.git
```

### 2. Configuration de l'Environnement

```bash
# Créez un environnement virtuel
python -m venv venv

# Activez l'environnement virtuel
# Sur Windows:
venv\Scripts\activate
# Sur macOS/Linux:
source venv/bin/activate

# Installez les dépendances
pip install -r requirements.txt
pip install -r requirements-dev.txt  # Pour le développement
```

### 3. Créer une Branche

```bash
# Synchronisez avec le repository principal
git fetch upstream
git checkout main
git merge upstream/main

# Créez une nouvelle branche pour votre fonctionnalité
git checkout -b feature/nom-de-votre-fonctionnalite
# ou pour un bug fix:
git checkout -b fix/description-du-bug
```

## 🛠️ Configuration de l'Environnement

### Dépendances de Développement

```bash
pip install -r requirements-dev.txt
```

### Outils Recommandés

- **IDE** : VS Code, PyCharm, ou Vim/Neovim
- **Linting** : flake8, black, isort
- **Tests** : pytest, pytest-cov
- **Type Checking** : mypy (optionnel)

### Configuration VS Code

Créez `.vscode/settings.json` :

```json
{
  "python.linting.enabled": true,
  "python.linting.flake8Enabled": true,
  "python.formatting.provider": "black",
  "python.testing.pytestEnabled": true,
  "editor.formatOnSave": true
}
```

## 📝 Processus de Contribution

### 1. Développement

- Écrivez du code propre et bien documenté
- Suivez les standards de code du projet
- Ajoutez des tests pour vos modifications
- Mettez à jour la documentation si nécessaire

### 2. Tests

```bash
# Lancer tous les tests
python -m pytest

# Tests avec couverture
python -m pytest --cov=download --cov-report=html

# Tests spécifiques
python -m pytest tests/test_download.py::test_download_function
```

### 3. Commit

```bash
# Ajoutez vos modifications
git add .

# Commitez avec un message descriptif
git commit -m "feat: ajouter support des téléchargements multiples"
```

### Format des Messages de Commit

Utilisez le format [Conventional Commits](https://www.conventionalcommits.org/) :

```
type(scope): description

[body optionnel]

[footer optionnel]
```

**Types** :

- `feat` : nouvelle fonctionnalité
- `fix` : correction de bug
- `docs` : documentation
- `style` : formatage, point-virgules manquants, etc.
- `refactor` : refactoring de code
- `test` : ajout de tests
- `chore` : maintenance

**Exemples** :

```
feat(ui): ajouter barre de progression animée
fix(download): corriger reprise de téléchargement
docs(readme): mettre à jour instructions d'installation
```

### 4. Push et Pull Request

```bash
# Pushez votre branche
git push origin feature/nom-de-votre-fonctionnalite

# Créez une Pull Request sur GitHub
```

## 📏 Standards de Code

### Style Python

- **PEP 8** : Suivez les conventions de style Python
- **Longueur de ligne** : Maximum 88 caractères (black)
- **Imports** : Organisés selon isort
- **Docstrings** : Format Google ou NumPy

### Exemple de Code

```python
def download_file(url: str, destination: str) -> bool:
    """
    Télécharge un fichier depuis une URL.

    Args:
        url: URL du fichier à télécharger
        destination: Chemin de destination

    Returns:
        True si le téléchargement réussit, False sinon

    Raises:
        requests.RequestException: En cas d'erreur de téléchargement
    """
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()

        with open(destination, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)

        return True
    except requests.RequestException as e:
        logger.error(f"Erreur de téléchargement: {e}")
        return False
```

### Nommage

- **Variables** : `snake_case`
- **Fonctions** : `snake_case`
- **Classes** : `PascalCase`
- **Constantes** : `UPPER_SNAKE_CASE`

## 🧪 Tests

### Structure des Tests

```
tests/
├── __init__.py
├── test_download.py      # Tests de téléchargement
├── test_gui.py          # Tests d'interface
├── test_utils.py        # Tests utilitaires
└── fixtures/            # Données de test
    └── sample_files/
```

### Écrire des Tests

```python
import pytest
from unittest.mock import patch, Mock
from download import DownloadManager

class TestDownloadManager:
    def test_download_success(self):
        """Test téléchargement réussi."""
        manager = DownloadManager()
        # Votre test ici

    def test_download_failure(self):
        """Test échec de téléchargement."""
        manager = DownloadManager()
        # Votre test ici

    @patch('requests.get')
    def test_download_with_mock(self, mock_get):
        """Test avec mock."""
        mock_response = Mock()
        mock_response.raise_for_status.return_value = None
        mock_response.iter_content.return_value = [b'data']
        mock_get.return_value = mock_response

        # Votre test ici
```

### Couverture de Code

Maintenez une couverture de code d'au moins 80% :

```bash
pytest --cov=download --cov-report=term-missing
```

## 📚 Documentation

### Docstrings

Utilisez des docstrings pour toutes les fonctions publiques :

```python
def calculate_download_speed(downloaded: int, time_elapsed: float) -> float:
    """
    Calcule la vitesse de téléchargement en MB/s.

    Args:
        downloaded: Nombre d'octets téléchargés
        time_elapsed: Temps écoulé en secondes

    Returns:
        Vitesse de téléchargement en MB/s

    Example:
        >>> calculate_download_speed(1048576, 1.0)
        1.0
    """
    return downloaded / (1024 * 1024) / time_elapsed
```

### Commentaires

- Expliquez le **pourquoi**, pas le **quoi**
- Utilisez des commentaires pour les algorithmes complexes
- Mettez à jour les commentaires quand vous modifiez le code

### README

- Mettez à jour le README pour les nouvelles fonctionnalités
- Ajoutez des exemples d'utilisation
- Documentez les nouvelles options de configuration

## 🎯 Types de Contributions

### 🐛 Correction de Bugs

1. Vérifiez les [issues existantes](https://github.com/Docteur-Parfait/PytDm/issues)
2. Créez une issue si le bug n'existe pas
3. Assignez-vous l'issue
4. Créez une branche `fix/description-du-bug`
5. Corrigez le bug et ajoutez des tests
6. Créez une Pull Request

### ✨ Nouvelles Fonctionnalités

1. Créez une issue pour discuter de la fonctionnalité
2. Attendez l'approbation des mainteneurs
3. Créez une branche `feature/nom-de-la-fonctionnalite`
4. Implémentez la fonctionnalité avec des tests
5. Mettez à jour la documentation
6. Créez une Pull Request

### 📚 Amélioration de la Documentation

- Correction de fautes de frappe
- Amélioration de la clarté
- Ajout d'exemples
- Traduction (nous acceptons les traductions !)

### 🎨 Amélioration de l'Interface

- Amélioration de l'UX/UI
- Nouveaux thèmes
- Responsivité
- Accessibilité

### 🧪 Tests

- Ajout de tests unitaires
- Tests d'intégration
- Tests de performance
- Amélioration de la couverture

## 🔍 Review Process

### Pour les Contributeurs

1. **Vérifiez** que votre code respecte les standards
2. **Testez** localement avant de soumettre
3. **Documentez** vos changements
4. **Répondez** aux commentaires de review

### Pour les Reviewers

1. **Vérifiez** la qualité du code
2. **Testez** les fonctionnalités
3. **Vérifiez** la documentation
4. **Soyez constructif** dans vos commentaires

## 🚀 Release Process

### Versioning

Nous utilisons [Semantic Versioning](https://semver.org/) :

- **MAJOR** : Changements incompatibles
- **MINOR** : Nouvelles fonctionnalités compatibles
- **PATCH** : Corrections de bugs

### Changelog

Mettez à jour le `CHANGELOG.md` pour chaque release :

```markdown
## [1.1.0] - 2024-01-15

### Added

- Support des téléchargements multiples
- Thème sombre

### Changed

- Amélioration de l'interface utilisateur

### Fixed

- Correction du bug de reprise de téléchargement
```

## ❓ Questions ?

- **Issues** : [GitHub Issues](https://github.com/Docteur-Parfait/PytDm/issues)
- **Discussions** : [GitHub Discussions](https://github.com/Docteur-Parfait/PytDm/discussions)
- **Email** : docteur.parfait@example.com

## 🙏 Remerciements

Merci à tous les contributeurs qui rendent ce projet possible !

---

**Happy Coding! 🚀**
