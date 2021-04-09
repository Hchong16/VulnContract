"""
    Main module to hold all related data around Solidity File
"""
from typing import List, Dict, Optional
from solidity_parser import parser

from declarations.pragmas import Pragma
from declarations.contracts import Contract
from declarations.imports import Import

class SolidityFile:
    def __init__(self):
        # Track state of class. Invalid if parser fails.
        self.status = 'valid' 

        self._filename: Optional[str] = None
        self._file_path: Optional[str] = None

        self._pragmas: Dict[str, Pragma] = {}
        self._imports: Dict[str, Import] = {} # Track imports here
        self._underlying_contracts: Dict[str, Contract] = {}
    
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
    def pragmas(self) -> Dict[str, Pragma]:
        """Return dict of pragmas"""
        return self._pragmas

    @property
    def imports(self) -> Dict[str, Import]:
        """Return dict of imports"""
        return self._imports

    @property
    def underlying_contracts(self) -> Dict[str, Contract]:
        """Return dict of inner contracts"""
        return self._underlying_contracts

    def convert_to_ast(self):
        """ 
        Break down Solidity Contract into an AST object.
        """
        try:
            self.source_unit = parser.parse_file(self.file_path)

            # Subparse AST into objects for nicer interfaces: Create a nested 
            # object structure from AST
            self.source_unit_object = parser.objectify(self.source_unit)
        except AttributeError:
            self.status = 'invalid'

    def parse_top_level(self):
        """ 
        Parse out file pragmas, imports and underlying contracts. For each 
        contract, parse for functions, events, and variables.
        """
        self.convert_to_ast()

        if self.status == 'valid':
            # Create pragma class for all pragmas defined in the file
            for pragma_data in self.source_unit_object.pragmas:
                pragma_obj = Pragma(pragma_data)
                self._pragmas[pragma_obj.name] = pragma_obj

            # Create import class for all imports defined in the file
            for import_data in self.source_unit_object.imports:
                import_obj = Import(import_data)
                self._imports[import_obj.path] = import_obj

            # Create contract class for each underlying contracts in the file
            # Track all functions and variables within each subclass.
            for contract_name in self.source_unit_object.contracts.keys():
                contract_obj = Contract(contract_name, self.source_unit_object)
                self._underlying_contracts[contract_name] = contract_obj
        else: # Failed to parse file into an AST
            return
