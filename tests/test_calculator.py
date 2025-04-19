"""
Tests pour le module calculator
"""
import pytest
from src.calculator import Calculator


class TestCalculator:
    """Classe de tests pour la classe Calculator"""
    
    def setup_method(self):
        """Configuration avant chaque test"""
        self.calc = Calculator()
    
    def test_add(self):
        """Test de la méthode add"""
        assert self.calc.add(5, 7) == 12
        assert self.calc.add(-1, 1) == 0
        assert self.calc.add(0, 0) == 0
    
    def test_subtract(self):
        """Test de la méthode subtract"""
        assert self.calc.subtract(10, 3) == 7
        assert self.calc.subtract(5, 5) == 0
        assert self.calc.subtract(0, 5) == -5
    
    def test_multiply(self):
        """Test de la méthode multiply"""
        assert self.calc.multiply(4, 6) == 24
        assert self.calc.multiply(0, 5) == 0
        assert self.calc.multiply(-2, 3) == -6
    
    def test_divide(self):
        """Test de la méthode divide"""
        assert self.calc.divide(20, 4) == 5
        assert self.calc.divide(0, 5) == 0
        assert self.calc.divide(5, 2) == 2.5
    
    def test_divide_by_zero(self):
        """Test de la division par zéro"""
        with pytest.raises(ZeroDivisionError):
            self.calc.divide(5, 0)

    def test_power(self):
        assert self.calc.power(2, 3) == 8
        assert self.calc.power(0, 0) == 1
        assert self.calc.power(1, 0) == 1
        assert self.calc.power(-1, 2) == 1
        assert self.calc.power(2, -3) == 0.125
        assert self.calc.power(9, 9) == 81

    def test_modulo(self):
        assert self.calc.modulo(10, 3) == 1
        assert self.calc.modulo(5, 5) == 0
        assert self.calc.modulo(0, 5) == 0
