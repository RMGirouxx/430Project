import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori

# Import .csv into python
df = pd.read_csv("languagesSplit.csv", header=None)

# Fill 'nan' values with '0's for later evaluation
df = df.fillna('0')

# make a list of each unique item in the dataset
uniqueItems = pd.unique(df[0])

# convert dataset to string list
languages = df.astype(str).values.tolist()

# convert list into boolean array and back into dataset for apriori
transactions = TransactionEncoder()
tranArr = transactions.fit(languages).transform(languages)
df = pd.DataFrame(tranArr, columns=transactions.columns_)

# initiate apriori function
langPairs = apriori(df, min_support=0.3, use_colnames=True, max_len=2)

# create row displaying length of pairs
langPairs['length'] = langPairs['itemsets'].apply(lambda x: len(x))

# set max support and length for evaluation
langPairs = langPairs[(langPairs['length'] == 2) &
                      (langPairs['support'] <= .6)]

# remove any frequent itemsets that contain a '0' as one value in the tuplet
for i in range(len(df.columns)):
    if i != '0':
        langPairs = langPairs[langPairs['itemsets'] != {'0', uniqueItems[i]}]
        langPairs = langPairs[langPairs['itemsets'] != {uniqueItems[i], '0'}]

# print apriori results
print(langPairs)
