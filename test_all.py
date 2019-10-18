import unittest

from core import core
from backup import backup

class TestAll(unittest.TestCase):
    def test_not_data_centric(self):
        """
        Test that not data centric will fail.
        """
        result = core('n')
        self.assertEqual(result, 'Fail')

    def test_data_centric_with_backups(self):
        result = core('y', 'y')
        self.assertEqual(result, 'Pass')

    def test_data_centric_without_backup(self):
        result = core('y', 'n')
        self.assertEqual(result, 'Fail')

    def test_has_backup_y(self):
        result = backup('y')
        self.assertEqual(result, 'Pass')

    def test_has_backup_n(self):
        result = backup('n')
        self.assertEqual(result, 'Fail')

if __name__ == '__main__':
    unittest.main()
