from .aaon import parse_aaon
from .amana import parse_amana
from .armstrong import parse_armstrong
from .bryant import parse_bryant
from .carrier import parse_carrier
from .champion import parse_champion
from .daikin import parse_daikin
from .evapco import parse_evapco
from .firstco import parse_firstco
from .goodman import parse_goodman
from .heil import parse_heil
from .icp import parse_icp
from .johnson import parse_johnson
from .lennox import parse_lennox
from .payne import parse_payne
from .rheem import parse_rheem
from .trane import parse_trane
from .york import parse_york

# Map manufacturer names to their parser functions
parser_map = {
    "AAON": parse_aaon,
    "Amana": parse_amana,
    "Armstrong": parse_armstrong,
    "Bryant": parse_bryant,
    "Carrier": parse_carrier,
    "Champion": parse_champion,
    "Daikin": parse_daikin,
    "Evapco": parse_evapco,
    "First Co": parse_firstco,
    "Goodman": parse_goodman,
    "Heil": parse_heil,
    "ICP": parse_icp,
    "Johnson": parse_johnson,
    "Lennox": parse_lennox,
    "Payne": parse_payne,
    "Rheem": parse_rheem,
    "Trane": parse_trane,
    "York": parse_york,
}

def get_parser(manufacturer: str):
    """Return the parser function for a given manufacturer."""
    return parser_map.get(manufacturer)
