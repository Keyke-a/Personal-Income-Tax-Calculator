#task
#writing a code to calculate personal income tax (PIT) for the citizen of XYZ.

Name = (input('What is your name? '))
Income = float(input('how much do you earn? '))
category_a = round((0.18 * Income) - 556.2) #income less than 85,528 thalers
category_b = round(14839.2 + (0.32 * Income / 85528)) #income greater than 85,528 thalers

if category_a < 0:
    print('no tax' + str(category_a))

elif Income <= 85528:
    print('Dear ' + Name + '\n' + 'your personal income tax is ' + str(category_a) + '\n' + 'Thank you')

else:
    print('Dear ' + Name + '\n' + 'your personal income tax is ' + str(category_b) + '\n' + 'Thank you')