# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}



def read_file_content(filename):
    # [assignment] Add your code here 
    # pp = open('story.txt')
    # content = pp.read()
    # print(content)
    with open("story.txt", "r") as f:
        file = f.read()
        print(file)
result = read_file_content("story.txt")
print(result)
    
filename = 'story.txt'

def count_words():
    text = read_file_content("./story.txt")
    # [assignment] Add your code here
    counts = 0
    words = str.split()

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts

print(count_words("story.txt"))


# pp = open('story.txt')
# content = pp.read()
# print(content)

# var = content.split()
# count = 0
# d = ()
# for word in var:
#     if word in d:
#         d[word] += 1
#     else:
#         d[word] = 1

# for x in d.keys():
#     print(var(count))
    

# print(count)

