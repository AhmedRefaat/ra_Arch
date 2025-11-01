# This file makes the pages directory a Python package
# It allows importing modules from this directory

from . import homepage
from . import our_services
from . import contact_us

__all__ = ['homepage', 'our_services', 'contact_us']