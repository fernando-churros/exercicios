import re

e = 'fernando_churos@pm.com'

x = re.search(".+@..+\.com", e) 
print(x)

