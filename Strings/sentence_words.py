from os import sep


def words(sentence):
    words=sentence.split(sep=" ")
    print("sentence: {0}\nwords: {1}".format(sentence,words))
    for w in words:
        print("{0}\t length: {1}".format(w,len(w)))

sentence="hello Oussama , how are you today ?"
words(sentence)


