print("Let's practice everything.")
print("You\'d need to know \'bout escapes with \\ that do:")
print("\n newlines and \t tabs.")

poem="""
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from ituition
and requires an explanation
\n\t\twhere there is none.
"""

print("---------------")
print(poem)
print("---------------")

five = 10 - 2 + 3 - 6
print(f"This should be {five}")

def secret_formular(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates


start_point = 10000
beans, jars, crates = secret_formular(start_point)

#Remember this is another way to formulate a string
print("With a start point of {}".format(start_point))
#It's just like with an f"" string
print(f"We'd have {beans} beans, {jars} jars, and {crates} crates.")

start_point = start_point / 10

print("We can do that this way:")
formular = secret_formular(start_point)

#This is an easy way to apply a list to a format string
print("We'd had {} beans, {} jars, and {} crates".format(*formular))


