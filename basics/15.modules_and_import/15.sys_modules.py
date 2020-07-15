''' work with sys 2 '''

import sys

for k, v in sys.modules.items():
    print(k,': ', v)
