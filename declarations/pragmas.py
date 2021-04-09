"""
    Pragma module
"""
import pprint
from typing import List, Dict, Optional

class Pragma():
    def __init__(self):
        self._name: Optional[str] = None
        self._kind: Optional[str] = None
        self._version: Optional[str] = None

    @property
    def name(self) -> Optional[str]:
        return self._name

    @name.setter
    def name(self, name: str):
        self._name = name

    @property
    def kind(self) -> Optional[str]:
        return self._kind

    @kind.setter
    def kind(self, kind: str):
        self._kind = kind

    @property
    def version(self) -> Optional[str]:
        return self._version

    @version.setter
    def version(self, version: str):
        self._version = version
