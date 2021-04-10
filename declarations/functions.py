"""
    Functions module
"""
from typing import Dict, Optional

class Function():
    def __init__(self, name: str, function_data):
        """Store all related data regarding function in Dict"""
        self._name: Optional[str] = name
        self.visibility: Optional[str] = function_data.visibility # Public/Private/Internal/Default
        self.state_mutability: Optional[str] = function_data.stateMutability
        
        self.function_data = function_data
        self.arguments: Dict[str] = function_data.arguments
        self.declarations: Dict[str] = function_data.declarations
        self.identifiers: Dict[str] = function_data.identifiers.idents
        self.returns: Dict[str] = function_data.returns
        
        # Future Implementation: Detectors can check memeory address accessed by function in
        # function_data.visitIdentifier and function_data.visitAssemblyCall dicts.
