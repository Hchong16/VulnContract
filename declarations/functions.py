"""
    Functions module
"""
from typing import Dict, Optional

class Function():
    def __init__(self, name: str, function_data):
        """Store all related data regarding function in Dict"""
        self.name: Optional[str] = name
        self.visibility: Optional[str] = function_data.visibility # public/private/internal/default
        self.state_mutability: Optional[str] = function_data.stateMutability
        
        self.function_data = function_data
        self.arguments: Dict[str] = function_data.arguments
        self.declarations: Dict[str] = function_data.declarations
        self.identifiers: Dict[str] = function_data.identifiers.idents
        self.returns: Dict[str] = function_data.returns

        self.check_protection()
        
    def check_protection(self):
        if self.visibility == "private":
            self.is_protected = True
        else:
            # Check if function is protected using required(msg.sender). Must have 'msg.sender' as the
            # direct condition.

            # These key values must appear in this order in the array for the function to be protected: 
            # 'require', 'msg', 'owner'
            checker1 = 0 # Tracker for 'require'
            checker2 = 0 # Tracker for 'msg'
            checker3 = 0 # Tracker for 'owner'
            for idents in self.identifiers:
                # Edge case: If suicide or selfdestruct appears before any required statement is found, this is unprotected!
                if (idents.name == 'suicide' or idents.name == 'selfdestruct') and checker1 == 0:
                    self.is_protected = False
                    return

                if idents.name == 'require' and checker2 == 0 and checker3 == 0:
                    checker1 = 1

                if idents.name == 'msg' and checker1 == 1 and checker3 == 0:
                    checker2 = 1

                if idents.name == 'owner' and checker1 == 1 and checker2 == 1:
                    checker3 = 1

                if checker1 == 1 and checker2 == 1 and checker3 == 1:
                    self.is_protected = True
                    return

                # If idents is not one of the specified key words, reset counter.
                if idents.name not in ['require', 'msg', 'owner']:
                    checker1, checker2, checker3 = 0, 0, 0

            self.is_protected = False

    # Future Implementation: Retrieve information about a function on a deeper level.
    # Detectors could evaluate memeory address accessed by the function through the 
    # function_data.visitIdentifier and function_data.visitAssemblyCall dicts.
