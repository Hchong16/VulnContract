"""
    Pragmas module
"""
from typing import Optional

class Pragma():
    def __init__(self, data):
        self._name: Optional[str] = data['name']
        self._kind: Optional[str] = data['type'] # PragmaDirective
        self._version: Optional[str] = data['value']

    @property
    def name(self) -> Optional[str]:
        return self._name

    @property
    def kind(self) -> Optional[str]:
        return self._kind

    @property
    def version(self) -> Optional[str]:
        return self._version
