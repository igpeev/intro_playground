"""A module for Exception Handling demo"""
import sys


def convert(s):
    """Convert to an integer"""

    res = -1
    try:
        res = int(s)
    # except (ValueError, TypeError):
    except (ValueError, TypeError) as err:  # <-- we reference whichever in the tuple is present to 'err'
        pass        # a NOOP operator (solution for empty statements not allowed)
        print('Error details: {}'.format(str(err)), file= sys.stderr)
        # raise     # to re-raise the except (benefit is that we have our msg printed along the way)
    finally:
        print('Done...')

    return res
