#definition for music_func goes here
def music_func(music_type = "Classic Rock", music_group = "The Beatles", vocalist = "Freddie Mercury"):
    print("The best kind of music is {}".format(music_type))
    print("The music group is {}".format(music_group))
    print("The best lead vocalist is {}".format(vocalist))

def main():
    music, group, singer = input("Input music, group, singer: ").split(',')
    music_func(music, group, singer)
    music_func()

main()