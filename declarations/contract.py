"""
    Contract module
"""
import pprint
from typing import List, Dict, Optional

class Contract():
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

    def parse(self, source_unit_object: str):
        """
        Within the contract structure, parse for functions, events, and 
        variables
        """
        pass
