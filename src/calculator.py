"""
Module de calculatrice pour le projet de test Jenkins
"""

class Calculator:
    """Classe qui implémente des opérations mathématiques de base"""
    
    def add(self, a, b):
        """Additionne deux nombres
        
        Args:
            a: Premier nombre
            b: Deuxième nombre
            
        Returns:
            La somme des deux nombres
        """
        return a + b
    
    def subtract(self, a, b):
        """Soustrait le deuxième nombre du premier
        
        Args:
            a: Premier nombre
            b: Deuxième nombre
            
        Returns:
            La différence entre les deux nombres
        """
        return a - b
    
    def multiply(self, a, b):
        """Multiplie deux nombres
        
        Args:
            a: Premier nombre
            b: Deuxième nombre
            
        Returns:
            Le produit des deux nombres
        """
        return a * b
    
    def divide(self, a, b):
        """Divise le premier nombre par le deuxième
        
        Args:
            a: Premier nombre (dividende)
            b: Deuxième nombre (diviseur)
            
        Returns:
            Le quotient de la division
            
        Raises:
            ZeroDivisionError: Si le diviseur est zéro
        """
        if b == 0:
            raise ZeroDivisionError("Division par zéro impossible")
        return a / b

    def power(self, a, b):

        return a ** b

    def modulo(self, a, b):

        return a % b