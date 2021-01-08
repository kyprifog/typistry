from dataclasses import dataclass
from typing import Optional

@dataclass
class TypedDict:
    attributes: dict
    type: str
    
    def all_attributes(self):
        atts = self.attributes.copy()
        atts["type"] = self.type
        return atts
