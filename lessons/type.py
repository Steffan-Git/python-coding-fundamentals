from typing import TypeAlias, Dict, TypedDict
from dataclasses import dataclass

# # basic type hints:

# price: int = 4
# flavour: str = "vanilla"

# price1: int = "4"
# flavour1: str = "vanilla"

# basic type alias:
# an alias is just a label,
# potentially makes type hints easier to follow. 
# Does not make an actual new type NewType. 

# Price: TypeAlias = int
# Flavour: TypeAlias = str
# ShakeId: TypeAlias = str

# shake_price: Price = 5
# shake_flavour: Flavour = "vanilla"
# shake_id: ShakeId = "10"

# loose dictionary shape from typing:
# aliasing uses capital to distinguish from vars. 
# NOT ENFORCED must use a type checker externally. 

# Menu = Dict[str, tuple[int, str]] 


# milkshakes: Menu = {
#     "1": (3, "vanilla"),
#     "2": (3, "choc")
# }

# TypedDict - control the key:values of the inner dictionary. 
# inner dict keys will automatically be strings. NewType available for full control.

# class ShakeDict(TypedDict):
#     price: int
#     flavour: str

# milkshakes: dict[str, ShakeDict] = {
#     "1": {"flavour": "vanilla", "price": 10}
# }

# dataClass - returns a real class, used for modelling our own objects.  
# python gnerates usuful mehtods automatically. 

# @dataclass
# class Shake:
#     price: int
#     flavour: str



# milkshakes: dict[str, Shake] = {
#     "1": Shake(10, "vanilla")
# }






