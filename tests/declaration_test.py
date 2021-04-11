import unittest
import sys
sys.path.append("../..")

from declarations.solidityFile import SolidityFile

class TestFunctionsModule(unittest.TestCase):
    filename = 'suicidal.sol'
    file_path = '../../examples/{}'.format(filename)

    smart_contract = SolidityFile(filename, file_path)
    smart_contract.parse_top_level()

    def test_pragmas(self):
        pragma_dict = self.smart_contract.pragmas
        pragma_obj = pragma_dict['solidity']
        
        expected_name = 'solidity'
        expected_kind = 'PragmaDirective'
        expected_version = '0.8.1'

        self.assertEqual(len(pragma_dict), 1) # Only 1 pragma in suicidal.sol
        self.assertEqual(pragma_obj.name, expected_name) 
        self.assertEqual(pragma_obj.kind, expected_kind) 
        self.assertEqual(pragma_obj.version, expected_version)

    def test_imports(self):
        import_dict = self.smart_contract.imports
        import_obj = import_dict['test']

        expected_path = 'test'
        expected_kind = 'ImportDirective'
        expected_symbol_aliases = {}
        expected_unit_alias = 'test'

        self.assertEqual(len(import_dict), 1) # Only 1 import in suicidal.sol
        self.assertEqual(import_obj.path, expected_path)
        self.assertEqual(import_obj.kind, expected_kind)
        self.assertEqual(import_obj.symbol_aliases, expected_symbol_aliases)
        self.assertEqual(import_obj.unit_alias, expected_unit_alias)

    def test_contracts(self):
        contract_dict = self.smart_contract.underlying_contracts
        expected_contracts = ['Contract_v1', 'Contract_v2', 'Contract_v3', 
            'Contract_v4', 'Contract_v5']

        if len(contract_dict) == 5:
            self.assertEqual(len(contract_dict), 5)
        else:
            return 

        # Evaluate each contract
        for contract in contract_dict.values():
            self.assertIn(contract.name, expected_contracts)
            self.assertEqual(len(contract.functions), 1)

    def test_functions(self):
        contract_dict = self.smart_contract.underlying_contracts

        # Evaluate function in Contract 1
        contract = contract_dict['Contract_v1']
        function = contract.functions['protected_kill_1']

        self.assertEqual(function.name, 'protected_kill_1')
        self.assertEqual(function.visibility, 'public')
        self.assertEqual(function.state_mutability, None)
        self.assertTrue(function.is_protected)

        self.assertEqual(len(function.arguments), 0)
        self.assertEqual(len(function.declarations), 0)
        self.assertEqual(len(function.identifiers), 5)
        self.assertEqual(len(function.returns), 0)

        # Evaluate function in Contract 2
        contract = contract_dict['Contract_v2']
        function = contract.functions['bad_kill_1']

        self.assertEqual(function.name, 'bad_kill_1')
        self.assertEqual(function.visibility, 'public')
        self.assertEqual(function.state_mutability, None)
        self.assertFalse(function.is_protected)

        self.assertEqual(len(function.arguments), 0)
        self.assertEqual(len(function.declarations), 1)
        self.assertEqual(len(function.identifiers), 6)
        self.assertEqual(len(function.returns), 0)

        # Evaluate function in Contract 3
        contract = contract_dict['Contract_v3']
        function = contract.functions['bad_kill_2']

        self.assertEqual(function.name, 'bad_kill_2')
        self.assertEqual(function.visibility, 'public')
        self.assertEqual(function.state_mutability, None)
        self.assertFalse(function.is_protected)

        self.assertEqual(len(function.arguments), 0)
        self.assertEqual(len(function.declarations), 0)
        self.assertEqual(len(function.identifiers), 2)
        self.assertEqual(len(function.returns), 0)

        # Evaluate function in Contract 4
        contract = contract_dict['Contract_v4']
        function = contract.functions['bad_kill_3']

        self.assertEqual(function.name, 'bad_kill_3')
        self.assertEqual(function.visibility, 'public')
        self.assertEqual(function.state_mutability, None)
        self.assertFalse(function.is_protected)

        self.assertEqual(len(function.arguments), 0)
        self.assertEqual(len(function.declarations), 0)
        self.assertEqual(len(function.identifiers), 5)
        self.assertEqual(len(function.returns), 0)

        # Evaluate function in Contract 5
        contract = contract_dict['Contract_v5']
        function = contract.functions['protected_kill_2']

        self.assertEqual(function.name, 'protected_kill_2')
        self.assertEqual(function.visibility, 'private')
        self.assertEqual(function.state_mutability, None)
        self.assertTrue(function.is_protected)

        self.assertEqual(len(function.arguments), 0)
        self.assertEqual(len(function.declarations), 0)
        self.assertEqual(len(function.identifiers), 2)
        self.assertEqual(len(function.returns), 0)

if __name__ == '__main__':
    unittest.main()
