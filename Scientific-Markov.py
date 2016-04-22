import random

def markov(input_file):
    """
    The purpose of "Scientific Markov" is to create a Markov chain from a given 
    scientific text, journal article or collection of articles. 
    A Markov chain takes input from text and can create realistic-sounding 
    sentences based upon frequency of words from the text inputted by user.
    This program also (through Markov Sentences) outputs a 5-6 line markov 
    generated 'abstract'. NOT TO BE USED FOR ANY PURPOSES OTHER THAN RESEARCH. 

    Run the program, input a .txt file in same directory as program, and the 
    program will output a markov generated abstract.
    """

    #The First Task of this program is to open a text file which will be used to determine frequency of words.
    with open(input_file, "r") as file1:
        #An empty list is created
        line_list = []
        #For Each Line in the test file, a list is created with individual words
        for line in file1:
            line_list.append(line.split())    
        #print(line_list)
    word_dict = {} #Create a blank dictionary for Word Dict

    for list_words in line_list: 
            #This For Loop will go through each word in list
        i = 0
        new_list = list_words[:-1]
        for word in new_list:
            word = word.lower()
            next_word = list_words[i+1].lower()
            if word in word_dict:
                word_dict[word].append(next_word)
            else:            
                word_dict[word] = [next_word]
            i += 1

    str(word_dict)
    return word_dict

def markovsentence(word_dictionary):
    list_keys = list(word_dictionary.keys())
    #print(list_keys)
    mark_sentence = []
    mark_sentence.append(random.choice(list_keys))
    while mark_sentence[-1] in word_dictionary:
        mark_sentence.append(random.choice(word_dictionary[mark_sentence[-1]]))
        if len(mark_sentence) > 99:
            return mark_sentence
    return mark_sentence

def main():
    file_text = input("What File Would You Like to Open? ")
    

    SciSentences = []
    SciPaper = "Abstract: "
    print(markovsentence(markov(file_text)))
    for i in range(0, 6):
        SciSentences.append(markovsentence(markov(file_text)))
        for words in SciSentences[i]:
            SciPaper += str(words) + " "
    print(SciPaper)
    plt.show()

if __name__ == "__main__":
    main()
