"""Regression tests for probability assumptions that could mislead crafting decisions."""
import sys
import unittest
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from craft import calc

def mod(text, weight, side='Prefix', level=75, family='target'):
    return dict(text=text, weight=weight, gen=side, level=level, family=family)

class CraftingModels(unittest.TestCase):
    def test_weight_one_is_never_silently_discarded(self):
        with patch.object(calc.db, 'pool', return_value=[mod('mana', 1),mod('life', 9,family='life')]):
            with self.assertRaisesRegex(ValueError, 'unverified'):
                calc.chance('Amulets', 80, 'mana')
            self.assertAlmostEqual(calc.chance('Amulets',80,'mana',assume_published_weights=True),.1)

    def test_state_and_currency_constraints(self):
        rows=[mod('mana',10),mod('low mana',30,level=20),mod('resist',20,side='Suffix',family='resist')]
        with patch.object(calc.db,'pool',return_value=rows):
            self.assertEqual(calc.chance('Amulets',80,'mana',side='Prefix',orb='perfect'),1)
            self.assertEqual(calc.chance('Amulets',80,'mana',side='Prefix',sides_open=('Suffix',)),0)
            self.assertEqual(calc.chance('Amulets',80,'mana',taken=('target',)),0)
            self.assertEqual(calc.chance('Amulets',10,'mana'),0)

    def test_all_conflicting_families_are_blocked(self):
        row=mod('mana',10);row['families']=['target','shared']
        with patch.object(calc.db,'pool',return_value=[row]):
            self.assertEqual(calc.chance('Amulets',80,'mana',taken=('shared',)),0)

    def test_desecration_requires_explicit_assumption(self):
        with self.assertRaisesRegex(ValueError,'unverified'):calc.desecrate(8)
        self.assertAlmostEqual(calc.desecrate(8,assume_uniform=True),3/8)
        self.assertAlmostEqual(calc.desecrate(8,True,assume_uniform=True),1-(5/8)**2)
        with self.assertRaises(ValueError):calc.desecrate(0,assume_uniform=True)

    def test_missing_prices_stay_unknown(self):
        self.assertIsNone(calc.price('Unobserved Currency'))
        self.assertIsNone(calc.est(.25,None)['div'])
        self.assertEqual(calc.tries(1),1)
        with self.assertRaises(ValueError):calc.tries(1.01)

if __name__=='__main__':unittest.main()
