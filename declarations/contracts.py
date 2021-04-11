"""
    Contracts module
"""
from typing import Dict, Optional

from declarations.functions import Function

class Contract():
    def __init__(self, name: str, contract_data):
        self._name: Optional[str] = name
        self.contract_data = contract_data
        self._functions: Dict[str] = {}

        self.parse_functions()

    @property
    def name(self) -> Optional[str]:
        return self._name

    @property
    def functions(self) -> Dict[str, Function]:
        """Return dict of defined functions in the contract"""
        return self._functions

    def parse_functions(self):
        # Create function class for each underlying function within the contract
        for function_name in self.contract_data.functions.keys():
            function_obj = Function(function_name, self.contract_data.functions[function_name])
            self._functions[function_name] = function_obj
