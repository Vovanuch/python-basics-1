#пользуемся импортируемыми функциями

import imported_functions

print('2 + 3 =', imported_functions.imp_sum(2, 3))

from imported_functions import imp_multiply

print('2 * 3 =', imp_multiply(2, 3)) 

from imported_functions import imp_power as power

print('2 ^ 3 =', power(2, 3)) 

from imported_functions import *

print('2 - 3 =', imp_subtract(2, 3)) 
print('2 / 3 =', imp_division(2, 3)) 
