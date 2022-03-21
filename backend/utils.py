import re
def pig_latin(word):
    # remove numbers
    word = re.sub('[0-9]','',word)

    if word:
        word = word.lower()
        words = word.split()
        punctuation_index = {}
        #only keep the punctuation in the last index
        for i in range(len(words)):
            word = words[i]
            if re.search("[^a-zA-z]",word[-1]):
                words[i] = re.sub("[^a-zA-z]",'',word[:-1])
                punctuation_index[word[-1]] = i
            else:
                continue

        #pig latin algorithm
        for i, word in enumerate(words):
            if word[0] in 'aeiou':
                words[i] = words[i] + "ay"
            else:
                has_vowel = False

                for j, letter in enumerate(word):
                    if letter in 'aeiou':
                        words[i] = word[j:] + word[:j] + "ay"
                        has_vowel = True
                        break

                # if the word doesn't have any vowel then simply postfix "ay"
                if (has_vowel == False):
                    words[i] = words[i] + "ay"

        #append the last punctuation to each word
        for punc,idx in punctuation_index.items():
            words[idx] += punc

        pig_latin = ' '.join(words)
        pig_latin = pig_latin[0].upper() + pig_latin[1:]


        return pig_latin

    return

if __name__ == '__main__':
    print(pig_latin('John Smith'))
    print(pig_latin('Joh,n,, Smith!'))