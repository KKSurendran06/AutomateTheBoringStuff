# 1
assert spam>10

# 2
assert bacon.upper() != eggs.lower() and bacon.lower() != eggs.lower()

# 3
assert 4<0

# 4
* import logging

* logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s -  %(levelname)s -  %(message)s')

# 6
* logging.debug()

* logging.info()

* logging.warning()

* logging.error()

* logging.critical()

# 7
* logging.disable(logging.CRITICAL)

# 8
because once debugging is done, we have to remove all the print statement manually while when logging is used we could just disable logging

# 9
* Step In - executes the code line by line including function 

* Step Over - executes the code line by line but, it does not go line by line through a function 

* Step Out - when a function is being debugged, we can chose to end it and move on to next line 

# 10
end of the code or at the `Breakpoints`

# 11
`Breakpoints` can be lines of code that cause the debugger to stop

# 12
by marking the line with a red dot
