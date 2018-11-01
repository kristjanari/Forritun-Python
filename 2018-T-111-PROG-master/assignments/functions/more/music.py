def music_func(best_music = "Classic Rock", best_music_group = "The Beatles", best_vocalist = "Freddie Mercury"):
    print("The best kind of music is " + best_music)
    print("The best music group is " + best_music_group)
    print("The best lead vocalist is " + best_vocalist)
    
def main():
    music, group, singer = input("Input music, group, singer: ").split(',')
    music_func(music, group, singer)
    music_func()

main()