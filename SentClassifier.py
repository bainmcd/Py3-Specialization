## We have provided some synthetic (fake, semi-randomly generated) twitter data in a csv file named project_twitter_data.csv which has the text of a tweet, the number of retweets of that tweet, and the number of replies to that tweet.
## We have also words that express positive sentiment and negative sentiment, in the files positive_words.txt and negative_words.txt.
## Your task is to build a sentiment classifier, which will detect how positive or negative each tweet is.
## You will create a csv file, which contains columns for the
# Number of Retweets,
# Number of Replies,
# Positive Score (which is how many happy words are in the tweet),
# Negative Score (which is how many angry words are in the tweet),
# and the Net Score for each tweet.
# At the end, you upload the csv file to Excel or Google Sheets, and produce a graph of the Net Score vs Number of Retweets.

## To start, define a function called strip_punctuation which takes one parameter,
# a string which represents a word,
# and removes characters considered punctuation from everywhere in the word. (Hint: remember the .replace() method for strings.)

def strip_punctuation(st):
    punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
    ns = ""
    for c in st:
        if c not in punctuation_chars:
            ns = ns + c
    return ns

## Define a function called get_pos which takes one parameter,
# a string which represents a one or more sentences,
# and calculates how many words in the string are considered positive words.
# Use the list, positive_words to determine what words will count as positive.
# The function should return a positive integer - how many occurances there are of positive words in the text.

# list of positive words to use in the 'get_pos' function, a global variable from 'positive_words.txt' file
positive_words = []
with open("positive_words.txt") as pos_f:       # I have not yet learned abbout a with statement
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())
            
def get_pos(st):
    pTot = 0
    wLst = st.split()
    for w in wLst:
        if strip_punctuation(w) in positive_words:
            pTot += 1
    return pTot

## Define a function called get_neg which takes one parameter,
# a string which represents a one or more sentences,
# and calculates how many words in the string are considered negative words.
# Use the list, negative_words to determine what words will count as negative.
# The function should return a positive integer - how many occurances there are of negative words in the text.

# list of negative words to use in the 'get_neg' function, a global variable from 'negative_words.txt' file
negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())
            
def get_neg(st):
    nTot = 0
    wLst = st.split()
    for w in wLst:
        if strip_punctuation(w) in negative_words:
            nTot += 1
    return nTot

## Open the file project_twitter_data.csv which has the fake generated twitter data (the text of a tweet, the number of retweets of that tweet, and the number of replies to that tweet).
## Your task is to build a sentiment classifier, which will detect how positive or negative each tweet is.
# Create a csv file called resulting_data.csv, which contains the
# Number of Retweets,
# Number of Replies,
# Positive Score (which is how many happy words are in the tweet),
# Negative Score (which is how many angry words are in the tweet),
# Net Score (how positive or negative the text is overall) for each tweet.
# The file should have those headers in that order.
## Remember that there is another component to this project. You will upload the csv file to Excel and produce a graph of the Net Score vs Number of Retweets.

sent_file = open("project_twitter_data.csv","r")
score_file = open("resulting_data.csv", "w")

header = 'Number of Retweets,Number of Replies,Positive Score,Negative Score,Net Score\n' 
fields = []
idx = 0
rstring = ""
for line in sent_file.readlines():
    if idx == 0:
        score_file.write(header)
    else:
        fields = line.split(",") # this should have tweet(st),retweets(num),replys(num)
        rstring = '{},{},{},{},{}\n'.format(int(fields[1]),int(fields[2]),get_pos(fields[0]),get_neg(fields[0]),get_pos(fields[0]) - get_neg(fields[0]))
        score_file.write(rstring)        
    idx += 1
    
sent_file.close()
score_file.close()
    
            
            