import re
import pyperclip

phone_regex = re.compile(r'''
(
(?:(?:\d\d\d)|(?:\(\d\d\d\)))?
(?:\s|-)
(?:\d\d\d) 
- 
(?:\d\d\d\d)
)
'''
,re.VERBOSE)

emailregex = re.compile(r'''
[a-zA-z0-9.+_]+
@
\w+
.
(?:com|gr|net)

''',re.VERBOSE)

sample_text = pyperclip.paste()
phone_nums = phone_regex.findall(sample_text,0)
emails = emailregex.findall(sample_text)

phone_catalog = '\n'.join(phone_nums)
email_catalog = '\n'.join(emails)
print(phone_catalog)
print(email_catalog)
