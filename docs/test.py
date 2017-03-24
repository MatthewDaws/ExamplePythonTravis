import os, sys

#sys.path.insert(0, os.path.join("C:\\","Users","MattUser","Documents","GitHub","ExamplePythonTravis"))

print("Top of search is now: '{}'".format(sys.path[0]))

print("Compared to: '{}'".format(os.path.abspath('..')))


sys.path.insert(0, os.path.abspath('..'))

import points