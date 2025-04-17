##
## Makefile pour tester Jenkins avec Python

# Règle par défaut
all: install

# Installation des dépendances
install:
	pip3 install -r requirements.txt
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
