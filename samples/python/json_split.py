string = 'zone:json:{"os":"true", "radio":"false"}'
print(string)

string_pieces = string.split(":")
print(string_pieces)

var = "%s:%s" % (string_pieces[0], string_pieces[1])
print(var)

string_pieces.pop(0)
string_pieces.pop(0)
print(string_pieces)

val = ":".join(string_pieces)
print(val)
