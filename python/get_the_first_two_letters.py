# the task is given a name , return the first 2 letters of that name. in capital

def abbrev_name(name):
    name = name.split()
    return ".".join([name[0][0],name[1][0]]).upper()



def abbrevName(name):
    return '.'.join(w[0] for w in name.split()).upper()



# the first is clunky and the second is clever . but it could be written in better ways 