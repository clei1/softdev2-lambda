file = open("57061-0.txt")
book = file.read()

words = book.split()

def freq(word):
    return len([ x for x in words if word == x ])

def multiple(words):
    return reduce(lambda x, y : x + y, [freq(word) for word in words])

def high():
    return reduce(lambda x, y : x if freq(x) > freq(y) else y, words)

print "forward: ", freq("forward")
print "century: ", freq("century")
print "[forward, century]: ", multiple(["forward", "century"])
print high()
