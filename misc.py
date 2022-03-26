"""
    ********
   ********
  ********
 ********
********
 ********
  ********
   ********
    ********
"""
"""
import time, sys
space = 0
try:
    while True:
        time.sleep(0.3)
        for x in reversed (range(0, 5)):
            print ((' '* x), end = '')
            print ('********')
        #print (x)

        for y in range(1,5):
            print ((' '* y), end = '')
            print ('********')
            #print (y)
            #break

except KeyboardInterrupt:
    print ('Program end!')
    sys.exit()
"""
import time, sys
indent = 0 # How many spaces to indent.
indentIncreasing = True # Whether the indentation is increasing or not.

try:
    while True: # The main program loop.
        print(' ' * indent, end='')
        print('********')
        time.sleep(0.1) # Pause for 1/10 of a second.

        if indentIncreasing:
            # Increase the number of spaces:
            indent = indent + 1
            if indent == 20:
                # Change direction:
                indentIncreasing = False

        else:
            # Decrease the number of spaces:
            indent = indent - 1
            if indent == 0:
                # Change direction:
                indentIncreasing = True
except KeyboardInterrupt:
    sys.exit()
    






