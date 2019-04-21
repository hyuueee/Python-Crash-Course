def greet_users(names):
    for name in names:
        message = 'Hello, ' + name.title() + '!'
        print(message)
greet_users(['A','B'])