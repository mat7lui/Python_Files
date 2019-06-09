import re

text_to_search = '''
abcdefghijklmnopqrstuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890

Ha HaHa

coreyms.com

321-555-4321
123.555.1234

Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T
'''
emails = '''
CoreyMSchafer@gmail.com
corey.schafer@university.edu
corey-321-schafer@my-work.net
'''

urls = '''
https://www.google.com
http://coreyms.com
https://youtube.com
https://www.nasa.gov
'''
sentence = 'Start a sentence and then bring it to an end.'

pattern = re.compile(r"https?://(www\.)?(\w+)(\.\w{2,4})")

subbed_urls = pattern.sub(r'\2\3', urls)

print(subbed_urls)
matches = pattern.findall(urls)

for match in matches:
    print(match)