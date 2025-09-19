#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Setup script for PytDm - Python Download Manager
"""

from setuptools import setup, find_packages
import os

# Lire le README pour la description longue
def read_readme():
    with open("README.md", "r", encoding="utf-8") as fh:
        return fh.read()

# Lire les requirements
def read_requirements():
    with open("requirements.txt", "r", encoding="utf-8") as fh:
        return [line.strip() for line in fh if line.strip() and not line.startswith("#")]

# Lire la version depuis le fichier
def get_version():
    version_file = os.path.join("download.py")
    with open(version_file, "r", encoding="utf-8") as f:
        for line in f:
            if line.startswith("__version__"):
                return line.split("=")[1].strip().strip('"').strip("'")
    return "1.0.0"

setup(
    name="PytDm",
    version=get_version(),
    author="Docteur-Parfait",
    author_email="docteur.parfait@example.com",
    description="Un gestionnaire de téléchargement moderne avec interface graphique",
    long_description=read_readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/Docteur-Parfait/PytDm",
    project_urls={
        "Bug Reports": "https://github.com/Docteur-Parfait/PytDm/issues",
        "Source": "https://github.com/Docteur-Parfait/PytDm",
        "Documentation": "https://github.com/Docteur-Parfait/PytDm#readme",
    },
    packages=find_packages(),
    py_modules=["download"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: End Users/Desktop",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: System :: Archiving",
        "Topic :: System :: Networking",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Operating System :: OS Independent",
        "Environment :: X11 Applications :: Qt",
        "Environment :: Win32 (MS Windows)",
        "Environment :: MacOS X",
    ],
    python_requires=">=3.7",
    install_requires=read_requirements(),
    extras_require={
        "dev": [
            "pytest>=7.4.0",
            "pytest-cov>=4.1.0",
            "flake8>=6.0.0",
            "black>=23.0.0",
            "isort>=5.12.0",
            "mypy>=1.5.0",
        ],
        "docs": [
            "sphinx>=7.1.0",
            "sphinx-rtd-theme>=1.3.0",
            "mkdocs>=1.5.0",
            "mkdocs-material>=9.2.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "PytDm=download:main",
        ],
        "gui_scripts": [
            "PytDm-gui=download:main",
        ],
    },
    keywords=[
        "download", "manager", "gui", "tkinter", "python", 
        "http", "files", "progress", "resume", "pause"
    ],
    include_package_data=True,
    zip_safe=False,
    platforms=["any"],
    license="MIT",
    # Métadonnées additionnelles
    download_url="https://github.com/Docteur-Parfait/PytDm/archive/v{}.tar.gz".format(get_version()),
    keywords="download manager gui tkinter python http files progress resume pause",
    # Configuration pour les tests
    test_suite="tests",
    tests_require=[
        "pytest>=7.4.0",
        "pytest-cov>=4.1.0",
    ],
    # Configuration pour les données de package
    package_data={
        "": ["*.md", "*.txt", "*.yml", "*.yaml"],
    },
    # Configuration pour les scripts
    scripts=[
        "scripts/PytDm-cli.py",
    ] if os.path.exists("scripts/PytDm-cli.py") else [],
)
