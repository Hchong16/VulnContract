"""
    Contract module
"""
from typing import List, Dict, Optional

class Contract:
    """
    Contract class
    """

    def __init__(self):
        self._name: Optional[str] = None
        self._kind: Optional[str] = None

        self._functions: Dict[str] = {}
        self._variables: Dict[str] = {}
        self._events: Dict[str] = {}

    @property
    def name(self) -> Optional[str]:
        return self._name

    @name.setter
    def name(self, name: str):
        self._name = name

    @property
    def contract_names(self) -> List[str]:
        """Return list of defined contracts."""
        return self._contract_names

    @contract_names.setter
    def contract_names(self, contract_name: str):
        self._contract_names.append(contract_name)
