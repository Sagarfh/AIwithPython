#Check for URL in a String
import re
myString = "This is a link http://www.google.com"
print ("The URL is : ",re.search("(?P<url>https?://[^\s]+)", myString).group("url"))