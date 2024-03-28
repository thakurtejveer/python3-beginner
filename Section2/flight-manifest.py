manifest = 'Flight : ABCD1234 | Gate : 13A | Destination : Singapore'
#Strings are immutable 
# manifest[0] = 'D'

#Indexing 

print(manifest[10])

# Slicing

print(manifest[9:18])

# Concatenation
passengers = ' | Passengers : 180'

manifest+=passengers

print(manifest)

# Length of String 
print(len(manifest))

# Membership

print('ABCD1234' in manifest)

# Replication

print(manifest * 3)