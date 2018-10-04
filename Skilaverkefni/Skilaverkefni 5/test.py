#import random
#import string

#def scramble_string(word):
#    if word.isalnum():
#        scramble_list = list(word[1:len(word)-1])
#    else:
#        scramble_list = list(word[1:len(word)-2])
#    random.shuffle(scramble_list)
#    scramble = "".join(scramble_list)
#    scrambled_word = word[0] + scramble + word[len(word)-2:]
#    return scrambled_word

#print(scramble_string("melóna,"))

string = """At least 384 people are confirmed dead and 540 are injured after a tsunami, caused by two earthquakes in quick succession, ripped through the Pacific Ring of Fire and crashed into an Indonesian coast city on Friday.
Indonesian media, citing the national disaster agency, said Saturday that almost 400 people had died in Palu City alone, on the the Indonesian island of Sulawesi. 
Fears are mounting for the the fishing town of Donggala, which was closer to the epicentre of the quake, but which rescuers have not been able to reach. 
The town of Mamuju was also severely affected but currently impossible to access due to damaged roads and disrupted telecommunications."""

new_string = string.strip("\n")
a_list = new_string.split()
print(a_list)