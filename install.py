import sys
from winpython import wppm, utils

try:
    dist = wppm.Distribution(sys.prefix)
    package = wppm.Package()
    dist.install(package)
except:
    raise Exception("Unable to install the package")