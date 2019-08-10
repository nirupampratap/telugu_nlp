from nltk.corpus import stopwords

def get_stop_words_te():
    # Define stop words - using nltk
    stop_words = stopwords.words('telugu')
    stop_words.append("చేత")
    stop_words.append("వలన")
    stop_words.append("గూర్చి")
    stop_words.append("కొరకు")
    stop_words.append("పట్టి")
    stop_words.append("కంటె")
    stop_words.append("లోపల")
    stop_words.append("అందు")
    stop_words.append("ఓరీ")
    stop_words.append("ఓయీ")
    stop_words.append("ఓసీ")
    stop_words.append("ఈ")
    stop_words.append("ఆ")
    stop_words.append("నుంచి")
    stop_words.append("కూడా")
    stop_words.append("మీ")
    stop_words.append("నా")
    stop_words.append("ఉన్")
    stop_words.append("ఒక")
    stop_words.append("ఉంది")
    stop_words.append("అ")
    stop_words.append("కానీ")
    stop_words.append("ఇది")
    stop_words.append("కోసం")
    stop_words.append("త")
    stop_words.append("అయితే")
    stop_words.append("మ")
    stop_words.append("అంటే")
    stop_words.append("చాలా")
    stop_words.append("ఇలా")
    stop_words.append("ఉండే")
    stop_words.append("అనే")
    stop_words.append("వారి")
    stop_words.append("మీరు")
    stop_words.append("ఎలా")
    stop_words.append("పేరు")
    stop_words.append("వీటి")
    stop_words.append("ఇప్పు")
    stop_words.append("గురించి")
    stop_words.append("వర")
    stop_words.append("పన్")
    stop_words.append("అందు")
    stop_words.append("పాటు")
    stop_words.append("అన్")
    stop_words.append("2")
    stop_words.append("ప")
    stop_words.append("3")
    stop_words.append("4")
    stop_words.append("5")
    stop_words.append("6")
    stop_words.append("7")
    stop_words.append("8")
    stop_words.append("9")
    stop_words.append("10")
    stop_words.append("దీ")
    stop_words.append('')
    stop_words.append('ఓ')
    stop_words.append('అని')
    
    return stop_words

def remove_non_words(word_list):
    
    dummy_words = ["<g/>"]
    
    texts_out = []
    
    for word in word_list:
        if(word not in dummy_words):
            texts_out.append(word)
            
    return texts_out

# Define functions for stopwords and stemming
# Could have done a pattern match, but felt this might be faster compared to a pattern match. 
# Would consider changing this later. NLTK tokenizer is not working as intended. Hence resorting to this
def clean_word(word):
    word = word.replace("\u200c","")
    word = word.replace(":","")
    word = word.replace(",","")
    word = word.replace(";","")
    word = word.replace("`","")
    word = word.replace("'","")
    word = word.replace(".","")
    word = word.replace("\"","")
    word = word.replace("\\","")
    word = word.replace("\n","")
    word = word.replace("/n","")
    word = word.replace("#","")
    word = word.replace("%","")
    word = word.replace("&","")
    word = word.replace("*","")
    word = word.replace("(","")
    word = word.replace(")","")
    word = word.replace("{","")
    word = word.replace("}","")
    word = word.replace("[","")
    word = word.replace("=","")
    word = word.replace("]","")
    word = word.replace("-","")
    word = word.replace("_","")
    word = word.replace("+","")
    word = word.replace("‘","")
    word = word.replace("?","")
    word = word.replace("!","")
    word = word.replace("~","")
    
    return word

def remove_stopwords(texts):
    
    stop_words = get_stop_words_te()
    
    #return [[clean_word(word) for word in doc if word not in stop_words] for doc in texts]
    texts_out = []
    for sent in texts:
        texts = []
        for word in sent:
            c_word = clean_word(word)
            
            if(c_word != None and c_word != "" and len(c_word) > 0 and c_word not in stop_words):
                texts.append(c_word)

        texts_out.append(texts)
    
    return texts_out

def remove_stopwords_single_stmt(sent):
    
    stop_words = get_stop_words_te()
    
    #return [[clean_word(word) for word in doc if word not in stop_words] for doc in texts]
    texts_out = []

    for word in sent:
        c_word = clean_word(word)

        if(c_word != None and c_word != "" and len(c_word) > 0 and c_word not in stop_words):
            texts.append(c_word)

    texts_out.append(texts)
    
    return texts_out