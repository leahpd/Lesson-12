print('-'*65)
print('Grade Converter Bot:')
print()

grade = input('What is your numerical grade in the class out of 100? ')
grade = int(grade)


if grade >= 90:
	print('You have earned a A in the class.')
elif grade >= 80:
	print('You have earned a B in the class.')
elif grade >= 70:
	print('You have earned an C in the class.')
elif grade == 65:
	print('You have earned a D in the class.')
else:
	print('You have earned an F in the class.')

print('-'*65)