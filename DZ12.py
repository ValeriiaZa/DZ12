import string
a = string.punctuation
x = input('Write smth:')
x = x.title()
x = x.replace(' ', '')
for i in x:
    if i in a:
        x = x.replace(i, '')
my_hashtag = f"#{x}"
print(my_hashtag[:140])