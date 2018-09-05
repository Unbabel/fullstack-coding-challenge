#!c:\users\beeuser\desktop\workspace\translationrequestsapp\venv\scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'flask-appconfig==0.11.1','console_scripts','flask'
__requires__ = 'flask-appconfig==0.11.1'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('flask-appconfig==0.11.1', 'console_scripts', 'flask')()
    )
