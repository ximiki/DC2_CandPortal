from math import *
import numpy as np
import pymongo
import pandas as pd
from pymongo import MongoClient

pd.set_option('display.height', 1000)
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 100)

'''
create similarity matrix between all candidates
    Whos most like each other?
        n*n matrix, n = each candidates. [0,1]
        Score off of questions in DB
        % same 100, and not at all = 0%
        “Root sum sq” for composites 
        start work on similarity matrix on all well-structured questions(fields)
            Start w simple yes/no questions, then advance
        Use numpy for lin. Alg.

References:
[1] https://en.wikipedia.org/wiki/Cosine_similarity
[2] http://bioinformatics.oxfordjournals.org/content/22/18/2298.full
[3] https://en.wikipedia.org/wiki/Euclidean_distance
[4] https://www.mathworks.com/matlabcentral/answers/293532-how-to-calculate-normalized-euclidean-distance-on-two-vectors?requestedDomain=www.mathworks.com
[5] http://www.econ.upf.edu/~michael/stanford/maeb4.pdf

'''
print "=============\n"


# 1. import MongoDB as pandas df, to process with numpy.
def import_db_as_df():
    '''
    -> pull data from mongodb to python for analysis.
    “Pymongo” lib
        Check old work from Udacity course
    “Monary” lib
        https://monary.readthedocs.io/index.html
        Types https://monary.readthedocs.io/reference.html?highlight=type
        https://www.youtube.com/watch?v=oteFpXIKBYg
        https://monary.readthedocs.io/examples/string.html 
        https://monary.readthedocs.io/installation.html 
    http://alexgaudio.com/2012/07/07/monarymongopandas.html 
    https://docs.mongodb.com/getting-started/python/insert/
    http://stackoverflow.com/questions/17805304/how-can-i-load-data-from-mongodb-collection-into-pandas-dataframe?noredirect=1&lq=1
    http://stackoverflow.com/questions/16249736/how-to-import-data-from-mongodb-to-pandas?noredirect=1&lq=1
    http://djcinnovations.com/index.php/archives/164
    http://djcinnovations.com/index.php/archives/103
    '''
    client = MongoClient() #client = MongoClient('localhost:27017')
    db = client.DC2_CP #db = client.database_name
    collection = db.general_info #collection = db.collection_name
    data = pd.DataFrame(list(collection.find())) #continue with this. <>
    
    ## preview data
    #print "data.size", data.size
    #print "data.head", data.head
    #with pd.option_context('display.max_rows', 10, 'display.max_columns', 10):
    #    print data.ix[:5,:5]
    #print data.ix[:5,:5]
    
    return data



# 2. generate similarity matrix

# 2.1. get 2 candidates

# 2.2. get similarity between 2 candidates
    '''
    Measures of similarity between two vectors
        Euclidean distance
        1-norm
        ∞-norm
        => Cosine measure (most widely used in lit.)
        Gabriel graph
        A measure derived from a consensus matrix
        Other ideas: Delaunay triangulation, Hamming distance or variation
    '''
vector_1 = [1,1,0,1,0]
vector_2 = [1,1,0,1,0]
vector_3 = [1,0,0,0,0]
vector_4 = [0,0,0,0,0]
vector_5 = [1,1,1,1,1]
vector_6 = [0,0,1,0,1] #opposite of vector_1



def method_5_EuclidDistSimilarity(v1, v2):
    '''
    Euclidean distance.
    
    [3]
    '''
    if len(v1) == len(v2):
        print "Euclidean Distance similarity: ", sqrt( np.sum(np.square( np.array(v1)-np.array(v2) )) )
    else:
        print "Error: Input vectors of different lengths."


        
# 2.3. repeat for all unique pairs


# 3. output compiled sensitivity matrix.





def test():
    #method_0_SimpleDiffSimilarity(vector_3, vector_6)
    #method_1_RootSumSqSimilarity(vector_3, vector_6)
    #method_2_cosineCoefSimilarity(vector_3, vector_6)
    #method_3_JaccardCoefSimilarity(vector_3, vector_6)
    #method_4_DiceCoefSimilarity(vector_3, vector_6)
    #method_5_EuclidDistSimilarity(vector_3, vector_6)
    #method_6_NormEuclidDistSimilarity(vector_3, vector_6)
    #method_7_WeightEuclidDistSimilarity(vector_3, vector_6)
    #print "np.square([1,2,3]): ", np.square([1,2,3]) 
    #print "np.sum(np.square([1,2,3])): ", np.sum(np.square([1,2,3]))

def test_import():
    #
    #pass
    importMongoDB()
    

def main():
    #test()
    test_import()

if __name__ == '__main__':
    main()




'''

>>> import numpy as np
>>> a = [3,5,6]
>>> b = [3,7,2]
>>> list(np.array(a) - np.array(b)) #for converting from np 'array' to 'list'
[0, -2, 4]

'''

# similarity matrix; 
## pca to k-means appraich to get clusters
## choice of similarity matrix
### normal eulc dist > cosine coef, bc distance is zero (so [1,0,0,0] v [0,1,0,0])
### - cos gives you 0, but the 2 zeros in eucl dist would show similarity
### 