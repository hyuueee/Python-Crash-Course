magicians=['Alice', 'Bill', 'Charlie']
def show_magicians(magicians_list):
    for magician in magicians_list:
        print(magician.title())
show_magicians(magicians)

def make_great(magicians_list):
    for magician in magicians_list:
        return('The Great '+magician.title())
make_great(magicians)