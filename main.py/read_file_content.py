

def read_file_content(file_name):
    openfile = open("./story.txt", "r")
    read_file_content = openfile.read()
    return read_file_content
def countwords():
    text = read_file_content("./story.txt")
    split_text = text.split()
    #print(split_text)
    count = {}
    for i in split_text:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
    return count

print(countwords()) 
