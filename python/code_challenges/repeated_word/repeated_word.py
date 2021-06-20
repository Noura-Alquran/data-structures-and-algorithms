def first_repeated_word(string):
    split_words =[]
    temp = ''
    for i in string:
        if i == ' ':
            split_words+=[temp.lower()]
            temp = ''
        else:
            temp += i
    if temp:
        split_words+=[temp.lower()]
    # print(split_words)
    lists=[]
    for key in split_words:
        if key in lists:
            return f"First repeated word is -> {key}"
        else:
            lists+=[key]



if __name__ == "__main__":
    str1="Once upon a time, there was a brave princess who..."
    print(first_repeated_word(str1))
    str2="It was the best of times , it was the worst of times , it was the age of wisdom , it was the age of foolishness , it was the epoch of belief , it was the epoch of incredulity , it was the season of Light , it was the season of Darkness , it was the spring of hope , it was the winter of despair , we had everything before us , we had nothing before us , we were all going direct to Heaven , we were all going direct the other way – in short , the period was so far like the present period , that some of its noisiest authorities insisted on its being received , for good or for evil , in the superlative degree of comparison only..."
    print(first_repeated_word(str2))
    str3="It was a queer, sultry summer , the summer they electrocuted the Rosenbergs , and I didn’t know what I was doing in New York..."
    print(first_repeated_word(str3))
