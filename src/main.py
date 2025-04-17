"""
Module principal pour le projet de test Jenkins
"""

from src.calculator import Calculator


def main():
    """Fonction principale qui démontre les fonctionnalités du calculateur"""
    calc = Calculator()
    
    print("Bienvenue dans le calculateur Python pour tester Jenkins!")
    print(f"Addition: 5 + 7 = {calc.add(5, 7)}")
    print(f"Soustraction: 10 - 5 = {calc.subtract(10, 5)}")
    print(f"Multiplication: 4 * 6 = {calc.multiply(4, 6)}")
    print(f"Division: 20 / 4 = {calc.divide(20, 4)}")
    print(f"Puissance: 5 ** 2 = {calc.power(5, 2)}")
    print("\nTest terminé avec succès!")


if __name__ == "__main__":
    main()
