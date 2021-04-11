import unittest
import sys
import json
sys.path.append("../..")

from declarations.solidityFile import SolidityFile

class TestContractParser(unittest.TestCase):
    filename = 'suicidal.sol'
    file_path = '../../examples/{}'.format(filename)

    def test_convert_to_ast(self):
        smart_contract = SolidityFile(self.filename, self.file_path)
        smart_contract.convert_to_ast()

        with open('../../tests/expected_jsons/suicidal.json', 'r') as f:
            expected_json_data = json.load(f)

        self.assertEqual(smart_contract.source_unit, expected_json_data)

    def test_parse_top_level(self):
        smart_contract = SolidityFile(self.filename, self.file_path)
        smart_contract.parse_top_level()

        # Check if parse function discover all pragmas, imports, and contracts
        self.assertEqual(len(smart_contract.pragmas), 1)
        self.assertEqual(len(smart_contract.imports), 0)
        self.assertEqual(len(smart_contract.underlying_contracts), 5)

if __name__ == '__main__':
    unittest.main()
