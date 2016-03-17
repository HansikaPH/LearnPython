#use of escape sequences

#two ways to add a new line
#using \n escape sequence
#uisng triple double quotes """

tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."


#""" adds two new lines one before the parapraph starts and after the paragraph ends
fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat
