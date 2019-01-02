import time
import random

print('_'*65)
print('Magic Eight Ball')
print()

question = input('Should I go to Disney for Spring break?')
print('Shaking!')
time.sleep(1)
print('...thinking...')
time.sleep(1)
print('...thinking...')
time.sleep(1)

choice = random.randint(1,4)

if choice == 1:
	print('YES DO IT!')
elif choice == 2:
	print('Definetly not.')
elif choice == 3:
	print('Maybe you should try to go another time.')
elif choice == 4:
	print('Ask again later.')

print('_'*65)

