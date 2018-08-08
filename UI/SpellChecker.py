def verify_valid_words(input_text):
    from nltk.corpus import wordnet
    from nltk.tokenize import word_tokenize
    import nltk


    word_Tokens = word_tokenize(input_text)
    word = nltk.word_tokenize(input_text)
    #print(nltk.pos_tag(word))

    valid_count = invalid_count =  0
    for word in word:
        #print(word)
        if wordnet.synsets(word):
            valid_count = valid_count + 1
            print("valid ", word)
        else:
            invalid_count = invalid_count+1
            print("invalid ", word)

    print (valid_count)
    print (invalid_count)
    if(valid_count < 2 and invalid_count ==0 ):
        return True
    elif(valid_count >3):
        return True
    elif(invalid_count > 2):
        return False
    else:
        return False
# English Word
verify_valid_words("I have a problem with the login to the application")
#verify_valid_words("hello i am rahgkashgdafgkjvi")
