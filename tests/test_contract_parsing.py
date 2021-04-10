import unittest
import json

from declarations.solidityFile import SolidityFile

class TestContractParsing(unittest.TestCase):
    def test_convert_to_ast(self):
        filename = "suicidal.sol"
        file_path = "examples/"

        smart_contract = SolidityFile()
        smart_contract.filename = filename
        smart_contract.file_path = file_path
        smart_contract.convert_to_ast()

        with open('./tests/expected_jsons/suicidal.json', 'r') as f:
            expected_json_data = json.load(f)

        self.assertEqual(smart_contract.source_unit, expected_json_data)

if __name__ == '__main__':
    unittest.main()
