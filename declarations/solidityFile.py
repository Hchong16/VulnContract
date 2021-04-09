"""
    Main module to hold all related data around Solidity File
"""
from typing import List, Dict, Optional
from solidity_parser import parser

from declarations.pragmas import Pragma
from declarations.contract import Contract
#from declarations.imports import Import


class SolidityFile:
    def __init__(self):
        self._filename: Optional[str] = None
        self._file_path: Optional[str] = None

        self._pragmas: Dict[str, Pragma] = {}
        self._imports: Dict[str, Contract] = {} # Track imports here
        self._underlying_contract: Dict[str, Contract] = {}
    
    @property
    def filename(self) -> Optional[str]:
        return self._filename

    @filename.setter
    def filename(self, filename: str):
        self._filename = filename

    @property
    def file_path(self) -> Optional[str]:
        return self._file_path

    @file_path.setter
    def file_path(self, file_path: str):
        self._file_path = file_path

    @property
    def pragmas(self) -> Dict[str, Contract]:
        """Return dict of pragmas"""
        return self._pragmas

    @property
    def imports(self) -> Dict[str, Contract]:
        """Return dict of imports"""
        return self._imports

    @property
    def underlying_contract(self) -> Dict[str, Contract]:
        """Return dict of inner contracts"""
        return self._underlying_contract

    def convert_to_ast(self):
        """ 
        Break down Solidity Contract into an AST object.
        """
        self.source_unit = parser.parse_file(self.file_path)

        # Subparse AST into objects for nicer interfaces: Create a nested 
        # object structure from AST
        self.source_unit_object = parser.objectify(self.source_unit)

    def parse_top_level(self):
        """ 
        Parse out underlying contracts. For each contract, parse for functions,
        events, and variables.
        """
        self.convert_to_ast()

        # Create pragma class for all pragma defined by the file
        for pragma_data in self.source_unit_object.pragmas:
            pragma_obj = Pragma()
            pragma_obj.name = pragma_data['name']
            pragma_obj.kind = pragma_data['type'] # 'PragmaDirective'
            pragma_obj.version = pragma_data['value']

            self._pragmas[pragma_obj.name] = pragma_obj



        # Iterate through all underlying contract keys and assign/create
        # contract class for each.
        # for contract_name in self.source_unit_object.contracts.keys():
        #     underlying_contract = Contract()
        #     underlying_contract.name = contract_name
        #     underlying_contract.parse(self.source_unit_object)

        #     # Append parsed out underlying contract into main contract dictionary
        #     self._underlying_contract[contract_name] = underlying_contract



