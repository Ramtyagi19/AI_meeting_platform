from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans

def cluster_topics(texts):

    vectorizer = TfidfVectorizer()

    X = vectorizer.fit_transform(texts)

    model = KMeans(
        n_clusters=2,
        random_state=42
    )

    model.fit(X)

    return model.labels_.tolist()