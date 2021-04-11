import unittest
import sys
sys.path.append("../..")

from declarations.solidityFile import SolidityFile
from detectors.suicidal import Suicidal

class TestDetection(unittest.TestCase):
    filename = 'suicidal.sol'
    file_path = '../../examples/{}'.format(filename)

    def test_suicidal_detection(self):
        smart_contract = SolidityFile(self.filename, self.file_path)
        smart_contract.parse_top_level() # Parse file into an AST object in JSON format

        # Perform vulnerability detectors on smart contract 
        output = Suicidal().detect_driver(smart_contract)

        # Output should return 3 vulnerabilities: bad_kill_1, bad_kill_2, and bad_kill_3
        expected = [['bad_kill_1', ' allows anyone to terminate the contract'],
                    ['bad_kill_2', ' allows anyone to terminate the contract'],
                    ['bad_kill_3', ' allows anyone to terminate the contract']]

        self.assertEqual(len(output), 3)
        self.assertCountEqual(output, expected)

if __name__ == '__main__':
    unittest.main()
