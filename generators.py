generators = list()

def james_smith(f, l):
    return f.lower() + '_' + l.lower()
generators.append(james_smith)

def jamesminsmith(f, l):
    return f.lower() + '-' + l.lower()
generators.append(jamesminsmith)

def jamesdotsmith(f, l):
    return f.lower() + '.' + l.lower()
generators.append(jamesdotsmith)

def jamessmith(f,l):
    return f.lower() + l.lower()
generators.append(jamessmith)

def jamess(f,l):
    return f.lower() + l[0].lower()
generators.append(jamess)

def jamesdots(f,l):
    return f.lower() + "." + l[0].lower()
generators.append(jamesdots)

def james_s(f,l):
    return f.lower() + "_" + l[0].lower()
generators.append(james_s)

def jsmith(f,l):
    return f[0].lower() + l.lower()
generators.append(jsmith)

def jdotsmith(f,l):
    return f[0].lower() + "." + l.lower()
generators.append(jdotsmith)

def jminsmith(f,l):
    return f[0].lower() + "-" + l.lower()
generators.append(jminsmith)

def j_smith(f,l):
    return f[0].lower() + "_" + l.lower()
generators.append(j_smith)



