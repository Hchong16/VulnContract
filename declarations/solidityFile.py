
from typing import List, Dict, Optional
from solidity_parser import parser

from declarations.contract import Contract

class SolidityFile:
    """
    Main class to hold all related data around Solidity File
    """

    def __init__(self):
        self._filename: Optional[str] = None
        self._file_path: Optional[str] = None
        self._underlying_contract: Dict[Contract] = {}

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
        Parse out underlying contracts, functions, variables.
        """
        # Create Contract Class for each underlying contract in the file
        #for underlying_contract in self.source_unit_object.contracts.keys():
        #    self.underlying_contract = self.contract_name
