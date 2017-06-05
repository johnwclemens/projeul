import re
pattern = r'(\d+):#include\s+.+'
m = re.match(pattern, '12:#include "util/RegistryInitializer.h"')
print("%s" % (m))
if m:
    lineNum = m.group(1)
    print("%s" % (lineNum))
