#! python3
# Finds phone and emails in a string

import re, pyperclip

phoneRegex = re.compile(r'''(
	(\d{3}|\(\d{3}\))?				# represents the area code
	(\s|-|\.)?						# represents a separator
	(\d{3})							# next 3 digits
	(\s|-|\.)						# represents a separator
	(\d{4})							# next 4 digits
	(\s*(ext|x|ext.)\s*(\d{2,5}))? 	# extension
	)''', re.VERBOSE)


emailRegex = re.compile(r'''(
	[a-zA-Z0-9._%+-]+				# username
	@								# at symbol
	[a-zA-Z0-9.-]+					# domain
	(\.[a-zA-Z]{2,4})				# dot something
	)''', re.VERBOSE)


# Find all the matches in the clipboard
text = str(pyperclip.paste())
matches = []
for groups in phoneRegex.findall(text):
	phoneNum = '-'.join([groups[1], groups[3], groups[5]])
	if groups[8] != '':
		# There is an extension
		phoneNum += ' x' + groups[8]
	matches.append(phoneNum)
for groups in emailRegex.findall(text):
	matches.append(groups[0])



if (len(matches) > 0):
	pyperclip.copy('\n'.join(matches))
	print('Copied to the clipboard: ')
	print('\n'.join(matches))
else:
	print('No numbers or emails found.')

# TODO: paste results to clipboard



