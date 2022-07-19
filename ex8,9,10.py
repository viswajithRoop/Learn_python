formatter = "{} {} {} {}"

print(formatter.format(1,2,3,4))
print(formatter.format("one","two","three","four"))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
          "Try your",
          "Own text here",
          "Maybe a poem",
          "Or a song about fear"
          ))
print()

days = "Mon Tue Wed Thu Fri Sat Sun"
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug\nSep\nOct\nNov\nDec"
print("here are the days: ", days)
print("here are the months: ", months)
print("""
   There's something going on here.
   with the three double-quotes.
   We'll be able to type as much as we like.
   even 4 lines if we want, or 5, or 6.
   """)
print()

tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line"
backslash_cat = "I'm \\ a \\ cat"

fat_cat = """
I'll do a list:
\t> cat food
\t> fishies
\t> catnip\n\t> grass
"""
print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)
