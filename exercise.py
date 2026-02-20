# Build a small program that turns a fullname into its initials
# eg. make_initials("Will Smith") #=> 'W.S'

# Parameters
#    - fullname, a string (eg. "Xiao Chan")
# Returns
#    - string (eg. 'X.C')
# Side effects
#    - None
def make_initials(fullname):
    initials = [name[0].upper() for name in fullname.split()]
    return ".".join(initials)


# Tasks
# - 

print(make_initials('Will Smith'))