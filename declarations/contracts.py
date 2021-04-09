"""
    Contracts module
"""
import pprint
from typing import List, Dict, Optional

from declarations.functions import Function

class Contract():
    def __init__(self, name: str, source_unit_object):
        self._name: Optional[str] = name
        self._kind: Optional[str] = None
        self.source_unit_object = source_unit_object

        self._functions: Dict[str] = {}
        self._variables: Dict[str] = {}
        self._events: Dict[str] = {}

        # Parse for functions within contract
        self.parse_functions()

    @property
    def name(self) -> Optional[str]:
        return self._name

    def parse_functions(self):
        pprint.pprint(self.source_unit_object.contracts[self.name].functions.keys())  # Get all functions in contract: "contractName"
   
        # pprint.pprint(sourceUnitObject.contracts["Contract"].functions.keys())  # Get all functions in contract: "contractName"
        # pprint.pprint(sourceUnitObject.contracts["Counter_v1"].functions["getCount"].visibility)  # get "kill"s visibility (or stateMutability)

        # print("Arguments:")
        # pprint.pprint(sourceUnitObject.contracts["Counter_v1"].functions["kill"].arguments)   

        # print("Declarations:")
        # pprint.pprint(sourceUnitObject.contracts["Counter_v1"].functions["kill"].declarations)

        # print("Identifiers:")
        # pprint.pprint(sourceUnitObject.contracts["Counter_v1"].functions["kill"].identifiers.idents)

        # print("Returns:")
        # pprint.pprint(sourceUnitObject.contracts["Counter_v1"].functions["kill"].returns)

        # print("State Mutability:")
        # pprint.pprint(sourceUnitObject.contracts["Counter_v1"].functions["kill"].stateMutability)
        #print(dir(sourceUnitObject.contracts["Counter_v1"].functions["kill"])) # get "kill"s

        # with open('data/parsed.json', 'w') as outfile:
        #     #json.dump(smart_contract.source_unit, outfile, indent=4)
        #     json.dump(smart_contract.source_unit, outfile)
