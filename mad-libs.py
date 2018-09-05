# Here we define each variable,
# but also we attach a string to them
# that prompts the user what to input.
#
# Later we will replace the variable contents with user-inputs.

place1 = '> Please input a place... <'
place2 = '> Please input another place... <'
profession_plural1 = '> Please input a type of professional, in plural form... <'
adjective1 = '> Please input an adjective... <'
objects_plural1 = '> Please input an inaminate object, in plural form... <'
objects_plural2 = '> Please input an inaminate object, in plural form again. .. <'
objects_plural3 = '> Please input an inaminate object a third time, in plural form... <'
verb_gerund1 = '> Please input a gerund verb (a verb that ends in -ing)... <'
verb_present1 = '> Please input a present-tense verb... <'
verb_present2 = '> Please input another present-tense verb... <'
adverb1 = '> Please input an adverb... <'

# Here we put each 'word' in a word list.
# This will simplify our code later since we can loop through the list.

word_list = [place1, place2, profession_plural1, adjective1, objects_plural1, objects_plural2, objects_plural3, verb_gerund1, verb_present1, verb_present2, adverb1]

# Finally, we define our story.
# I made up this story myself!

instructions = '''
====================
Welcome to Mad Libs!
====================
Instructions:

Follow the on-screen prompt,
it will ask you to input data.

After you do so, hit "enter",
to confirm that you are done.

Lets begin!
'''

# This for loop will loop through each variable and ask the user for input in each.

def mad_libs():
	print(instructions)
	word_counter = 0
	for word in word_list:
		print(word)
		word_list[word_counter]=input("> ")
		word_counter+=1
	place1 = word_list[0]
	place2 = word_list[1]
	profession_plural1 = word_list[2]
	adjective1 = word_list[3]
	objects_plural1 = word_list[4]
	objects_plural2 = word_list[5]
	objects_plural3 = word_list[6]
	verb_gerund1 = word_list[7]
	verb_present1 = word_list[8]
	verb_present2 = word_list[9]
	adverb1 = word_list[10]

	story = f'''Once upon a time in a land far far away... An island named {place1} was in peril.
The disaster was foretold by the {profession_plural1} who saw signs in their {adjective1} {objects_plural1}.
They called this event "the {verb_gerund1}". In the coming days, the island began to {verb_present1} {adverb1}.
This is when the people really began to worry. Frantically, they began to flee the island in boats built out of {objects_plural2}.
However the people had luck on this fateful day! Their neighboring island, {place2}, had a large supply of {objects_plural3}.
They came to aid the island, using their {objects_plural3} to {verb_present2} all the {objects_plural2}.
In doing this, the disaster faded. The people rejoiced! Peace settled into the island of {place1} once again.'''
	print(story)

mad_libs()
