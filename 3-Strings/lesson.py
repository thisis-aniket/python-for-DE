# Strings are Immutable

a = "hallucination"

# Slicing
print(a[1:5]) # allu
print(a[:-1]) # hallucinatio
print(a[-1:]) # n
print(a[-5:-1]) # atio

print(a[1:8:3]) # ANSWER -> aun

# Functions

print(len(a))
print(a.endswith("nation"))
print(a.count("a"))
print(a.capitalize())
print(a.find("tion"))

replaced_string = a.replace("l", "r")
print(replaced_string)

# Escape Characters
# /n -> newline
# /t -> tab
# /' -> single quote
# \\ -> backslash