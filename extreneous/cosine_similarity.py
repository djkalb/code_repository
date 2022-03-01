import string
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer

from nltk.corpus import stopwords
stopwords = stopwords.words('english')

def clean_string(text):
    text = ''.join([word for word in text if word not in string.punctuation])
    text = text.lower()
    text = " ".join([word for word in text.split() if word not in stopwords])
    return text



def vectorMaker(cleanList):
    vectorizer = CountVectorizer().fit_transform(cleanList)
    return vectorizer.toarray()



def cosine_sim_vectors(vec1, vec2):
    #print(vec1)
    vec1 = vec1.reshape(1, -1)
    print(vec2)
    vec2 = vec2.reshape(1, -1)
    print(vec2)

    return cosine_similarity(vec1, vec2)[0][0]

# compare every vector return unsorted list of values above 
def compare_cosine_sim(vectors):
    
    results = []
    for vec in vectors[1:]:
        vec = vec.reshape(1, -1)
        
        results.append(float(cosine_similarity(vectors[0].reshape(1, -1), vec)))
    return results


# takes in a list of text as an arg returns/ list of relative similarity
# it fucking works man
def cos_sim_results(lst):
    #removes punctuation / stopwords / uppercase letters
    cleanedList = list(map(clean_string, lst))

    vectors = vectorMaker(cleanedList)
    
    # returns list of relative similarity to first item
    return compare_cosine_sim(vectors)

sentences = ['foo bar sentence',
    'testing with more foo bar sentences',
    'another string quite similar previous ones',
    'sentence similar foo bar sentence',
    'also another string']

