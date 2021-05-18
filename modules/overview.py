# Use 'from fibo import *' to import all from fibo
# Use 'import fibo as fib' to add custom name 'fib' for module 'fibo'
# Use 'from fibo import fib as fibonacci' to add custom name for sub-module 'fib' in 'fibo'
# Use 'from fibo import fib, fib2' to import sub-module 'fib' and 'fib2' of module 'fibo'
import fibo

fibo.fib(1000)
print(fibo.fib2(100))
print(fibo.__name__)

fib = fibo.fib
fib(500)
