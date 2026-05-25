from sklearn.ensemble import IsolationForest

def detect_anomalies(X):
    model = IsolationForest()
    model.fit(X)
    return model.predict(X).tolist()