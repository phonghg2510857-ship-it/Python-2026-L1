n = input('What is your favorite color?: ').strip().capitalize()
color = ['Green', 'Blue', 'Red']
if n in color :
    idx = color.index(n)
    print(f'your color is at index {idx} in my list')
else:
    print('Sorry, I could not find your color')