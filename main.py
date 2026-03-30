import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# load
df = pd.read_csv("data/movies.csv")
df.fillna('', inplace=True)

# combine
df['c'] = df['genre'] + " " + df['overview'] + " " + df['keywords']

# vector
cv = CountVectorizer(stop_words='english')
m = cv.fit_transform(df['c'])

# similarity
sim = cosine_similarity(m)

# ---------------- #

def rec(x):
    if x not in df['title'].values:
        print("not found")
        return
    
    i = df[df['title'] == x].index[0]
    s = list(enumerate(sim[i]))
    s = sorted(s, key=lambda a: a[1], reverse=True)

    print("\nrec:")
    for k, j in enumerate(s[1:6], 1):
        print(k, df.iloc[j[0]].title)


def gen(g):
    print("\n", g, "movies:")
    r = df[df['genre'].str.contains(g, case=False)]

    if len(r) == 0:
        print("none")
    else:
        for i, t in enumerate(r['title'].head(10), 1):
            print(i, t)


def tag(tg):
    print("\n", tg, "movies:")
    r = df[df['keywords'].str.contains(tg, case=False)]

    if len(r) == 0:
        print("none")
    else:
        for i, t in enumerate(r['title'].head(10), 1):
            print(i, t)


def showg():
    print("\ngenres:")
    for g in sorted(df['genre'].unique()):
        print("-", g)


def showt():
    print("\ntags:")
    st = set()
    for k in df['keywords']:
        for w in k.split():
            st.add(w)
    
    for x in sorted(st):
        print("-", x)


# ---------------- #

while True:
    print("\n1 enter movie for rec")
    print("2 enter genre")
    print("3 enter tag")
    print("4 show all genres")
    print("5 show all tags")
    print("6 exit")

    ch = input(">> ")

    if ch == "1":
        rec(input("movie: "))

    elif ch == "2":
        gen(input("genre: "))

    elif ch == "3":
        tag(input("tag: "))

    elif ch == "4":
        showg()

    elif ch == "5":
        showt()

    elif ch == "6":
        break

    else:
        print("wrong")
