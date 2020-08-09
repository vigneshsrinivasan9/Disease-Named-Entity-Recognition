def get_tagged_sentences(data): 
    '''
    Objective: To get list of sentences along with labelled tags.
    Returns a list of lists of (word,tag) tuples. 
    Each inner list contains a words of a sentence along with tags. 
    '''
    
    agg_func = lambda s: [(w, t) for w, t in zip(s["Word"].values.tolist(), s["tag"].values.tolist())] 
    grouped = data.groupby("Sent_ID").apply(agg_func) 
    sentences = [s for s in grouped] 
    return sentences 

def get_test_sentences(data): 
    '''
    Objective: To get list of sentences.
    Returns a list of lists of words. 
    Each inner list contains a words of a sentence.
    '''
    
    agg_func = lambda s: [w for w in s["Word"].values.tolist()] 
    grouped = data.groupby("Sent_ID").apply(agg_func) 
    sentences = [s for s in grouped] 
    return sentences
