##
## Makefile pour tester Jenkins avec Python

# Règle par défaut
all: install

# Vérifier si Python et pip sont installés
install_python:
	apt-get update && apt-get install -y python3-pip)

install: check_python
	pip3 install pytest==7.3.1
	pip3 install pytest-cov==4.1.0
	@echo "Dépendances installées avec succès!"

# Exécution du programme
run:
	python3 src/main.py

# Exécution des tests
tests_run:
	python3 -m pytest tests/ -v
	@echo "Tests terminés avec succès!"

# Nettoyage des fichiers Python compilés et cache
clean:
	rm -rf __pycache__
	rm -rf src/__pycache__
	rm -rf tests/__pycache__
	rm -rf .pytest_cache
	rm -rf .coverage
	@echo "Fichiers cache supprimés."

# Nettoyage complet (cache et environnement virtuel)
fclean: clean
	rm -rf venv
	rm -rf *.egg-info
	rm -rf dist
	rm -rf build
	@echo "Environnement nettoyé complètement."

# Règles spéciales
.PHONY: all install run tests_run clean fclean
