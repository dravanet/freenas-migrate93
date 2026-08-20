import logging
import os


log = logging.getLogger('support.utils')
LICENSE_FILE = '/data/license'


def get_license():
    # Treat the installed system as unlicensed
    return None, None
