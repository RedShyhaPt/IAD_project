from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta

default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "start_date": datetime(2022, 10, 30),
    "email": ["airflow@airflow.com"],
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
    # 'queue': 'bash_queue',
    # 'pool': 'backfill',
    # 'priority_weight': 10,
    # 'end_date': datetime(2016, 1, 1),
}

dag = DAG("data_processing", default_args=default_args, schedule_interval=timedelta(1))

# t1, t2 and t3 are examples of tasks created by instantiating operators
t1 = BashOperator(task_id="print_date", bash_command="date", dag=dag)

t2 = BashOperator(task_id="sleep", bash_command="sleep 5", retries=3, dag=dag)

templated_command = """
    {% for i in range(5) %}
        echo "{{ ds }}"
        echo "{{ macros.ds_add(ds, 7)}}"
        echo "{{ params.my_param }}"
    {% endfor %}
"""

# import sklearn.pipeline as pipe
# from sklearn.model_selection import train_test_split
# import pandas as pd 
# import numpy as np 
# from sklearn.preprocessing import Normalizer
# from sklearn.preprocessing import StandardScaler, MinMaxScaler
# import os.path, time
# import numpy as np
# import matplotlib.style
# import matplotlib as mpl
# mpl.style.use('classic')
# mpl.rcParams['axes.formatter.useoffset'] = False
# import matplotlib.pyplot as plt
# dataFile = 'YNDX_190114_190115.csv'
# #dataFile = 'YNDX_190114_190115-1.csv'
# #dataFile = 'YNDX_190114_190115-2.csv'
# #dataFile = 'YNDX_190114_190115-3.csv'
# #dataFile = 'YNDX_181201_190115-4.csv'
# import nltk
# from nltk.tokenize import word_tokenize
# from nltk.corpus import stopwords
# from nltk.stem.porter import PorterStemmer

# def my_split( s, seps ): # this function splits line to parts separated with given separators
#     res = [s]
#     for sep in seps:
#         s, res = res, []
#         for seq in s:
#             res += seq.split( sep )
#     i = 0
#     while i < len( res ):
#         if res[i] == '':
#             res.pop(i)
#             continue
#         i += 1
#     return res

# def loadFinamCsv( fname ):
#     if not os.path.isfile( fname ):
#         raise ValueError( 'wrong file name: %s' % fname )  

#     counter = 0

#     fi = open( fname, 'r' )

#     tickerNameIsFound = False

#     for line in fi: # this loop counts number of bars and reads ticker name from the first bar
#         firstSymbol = line[ :1 ]
#         if firstSymbol == '' or firstSymbol == '<':
#             continue
#         if not tickerNameIsFound:
#             parsed = my_split( line, ',\n' )
#             ticker = parsed[0]
#             period = parsed[1]
#             tickerNameIsFound = True
#         counter += 1

#     bars = np.zeros( ( counter, 6 ), dtype = np.float64 ) # create matrix for reading the whole file

#     print( counter )

#     fi.seek( 0, 0 ) # move file pointer to the beginning 

#     counter = 0
                 
#     for line in fi:
#         firstSymbol = line[ :1 ]
#         if firstSymbol == '' or firstSymbol == '<':
#             continue
        
#         parsed = my_split( line, ';,\n' )     

#         timeStamp = parsed[2] + parsed[3]
#         dtime = time.strptime( timeStamp + '+0300', '%Y%m%d%H%M%S%z' )
#         timeEpoch = time.mktime( dtime )

#         bars[ counter, : ] = np.array( ( timeEpoch, np.float64(parsed[4]), np.float64(parsed[5]),
#                                          np.float64(parsed[6]), np.float64(parsed[7]), np.float64(parsed[8]) ) )

#         counter += 1
#         if counter % 1000 == 0:
#             print( int( counter / 1000 ), end = ' ' )
        
#     fi.close()
#     print( '\n' )

#     return { 'ticker': ticker, 'period': period, 'bars': bars }


# def convertPeriodString( periodRaw ):
#     try:
#         numMins = int( periodRaw )
#         if numMins % 60 != 0:
#             return 'M%d' % numMins
#         else:
#             return 'H%d' % ( numMins // 60 )
#     except ValueError:
#         return periodRaw

# timeZoneDiffSecs = 3 * 3600 # we need to know in advance the time zone difference between UTC
# pt = 0.01 # we need to know in advance the min price step (point)

# data = loadFinamCsv( dataFile )
# ticker = data[ 'ticker' ]
# period = data[ 'period' ]
# bars = data[ 'bars' ]

# periodFine = convertPeriodString( period )


# xs = np.array( range( bars.shape[0] ) )

# bodyCentres = 0.5 * ( bars[ :, 1 ] + bars[ :, 4 ] )
# bodySpans = 0.5 * ( bars[ :, 4 ] - bars[ :, 1 ] )
# totalCentres = 0.5 * ( bars[ :, 2 ] + bars[ :, 3 ] )
# totalSpans = 0.5 * ( bars[ :, 2 ] - bars[ :, 3 ] )

# blackBars = np.abs( bodySpans ) < 0.25 * pt
# greenBars = np.logical_and( np.logical_not( blackBars ),
#                             bodySpans >= 0.25 * pt )
# redBars = np.logical_not( np.logical_or( blackBars, greenBars ) )
# # Обработка текста
# def compute_tf(word_dict, l):
#     tf = {}
#     sum_nk = len(l)
#     for word, count in word_dict.items():
#         tf[word] = count/sum_nk
#     return tf
    
# tf_A = compute_tf(word_dict_A, l_A)
# tf_B = compute_tf(word_dict_B, l_B)
# tf_C = compute_tf(word_dict_C, l_C)

# def compute_idf(strings_list):
#     n = len(strings_list)
#     idf = dict.fromkeys(strings_list[0].keys(), 0)
#     for l in strings_list:
#         for word, count in l.items():
#             if count > 0:
#                 idf[word] += 1
    
#     for word, v in idf.items():
#         idf[word] = log(n / float(v))
#     return idf
    
# idf = compute_idf([word_dict_A, word_dict_B, word_dict_C])

# def compute_tf_idf(tf, idf):
#     tf_idf = dict.fromkeys(tf.keys(), 0)
#     for word, v in tf.items():
#         tf_idf[word] = v * idf[word]
#     return tf_idf
    
# tf_idf_A = compute_tf_idf(tf_A, idf)
# tf_idf_B = compute_tf_idf(tf_B, idf)
# tf_idf_C = compute_tf_idf(tf_C, idf)

# from sklearn.feature_extraction.text import TfidfVectorizer
# from sklearn.cluster import KMeans


# all_textall_text  = """
#  Google and Facebook are strangling the free press to death. Democracy is the loserGoogle an 
# Your 60-second guide to security stuff Google touted today at Next '18
# A Guide to Using Android Without Selling Your Soul to Google
# Review: Lenovo’s Google Smart Display is pretty and intelligent
# Google Maps user spots mysterious object submerged off the coast of Greece - and no-one knows what it is
# Android is better than IOS
# In information retrieval, tf–idf or TFIDF, short for term frequency–inverse document frequency
# is a numerical statistic that is intended to reflect
# how important a word is to a document in a collection or corpus.
# It is often used as a weighting factor in searches of information retrieval
# text mining, and user modeling. The tf-idf value increases proportionally
# to the number of times a word appears in the document
# and is offset by the frequency of the word in the corpus
# """.split("\n")[1:-1]

# # Preprocessing and tokenizing
# def preprocessing(line):
#     line = line.lower()
#     line = re.sub(r"[{}]".format(string.punctuation), " ", line)
#     return line

# tfidf_vectorizer = TfidfVectorizer(preprocessor=preprocessing)
# tfidf = tfidf_vectorizer.fit_transform(all_text)

# kmeans = KMeans(n_clusters=2).fit(tfidf)

# lines_for_predicting = ["tf and idf is awesome!", "some androids is there"]
# kmeans.predict(tfidf_vectorizer.transform(lines_for_predicting))