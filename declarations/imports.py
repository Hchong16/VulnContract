"""
    Imports module
"""
from typing import Dict, Optional

class Import():
    def __init__(self, data):
        self._path: Optional[str] = data['path'] # Treat path as the import name
        self._kind: Optional[str] = data['type'] # ImportDirective
        self._symbol_aliases: Optional[str] = data['symbolAliases']
        self._unit_alias: Optional[str] = data['unitAlias']

    @property
    def path(self) -> Optional[str]:
        return self._path

    @property
    def kind(self) -> Optional[str]:
        return self._kind

    @property
    def symbol_aliases(self) -> Optional[str]:
        return self._symbol_aliases

    @property
    def unit_alias(self) -> Optional[str]:
        return self._unit_alias
