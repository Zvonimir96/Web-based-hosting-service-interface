"""
This module is used to initialize data structures required for Github module.
"""

from .repository import Repository
from .commit import Commit
from .user import User
from .branch import Branch


# Function that appends query parameters to url
def add_query_parameters(url, parameters):
    if len(parameters) > 0:
        # Query parameters begin with symbol '?'
        url += '?'

        # Append each parameter to url
        for i, item in enumerate(parameters.items()):
            # Each query parameter is spaced with symbol '&'
            if i != 0:
                url += '&'

            url += f'{item[0]}={item[1]}'

    return url
