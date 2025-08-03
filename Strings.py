# blogHeading = "into to nodeJS"
# print(blogHeading.capitalize())


blogHeading = "Intro TO nOdeJS"
print(blogHeading.capitalize())

print(blogHeading.title())

# Returns Index of first occurence 
print(blogHeading.find("TO"))
print(blogHeading.isalnum())
print(blogHeading.isalpha())

# In below case there is no whitespace, hence the string isalpha
blogHeading = "Himanshu"
print(blogHeading.isalpha())

print(blogHeading.isprintable())

# Below string is not printable as it contains a \n (i.e an escape sequence character)
blogHeading = "Himanshu\n"
print(blogHeading.isprintable())
