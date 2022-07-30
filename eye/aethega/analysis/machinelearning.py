
#Dependencies
import pandas as pd
import numpy as np
import sklearn as sk
from sklearn import linear_model


#-------------------------------------------------------------------------------------------------------------------


def machineLearning():
    data = pd.read_csv("Python\\Data\\AAPL.csv")
    data = data[["Adj Close", "Volume"]]
    predict = "Adj Close"

    X = np.array(data.drop([predict], 1))
    y = np.array(data[predict])

    x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(X, y, test_size = 0.1)
    linear = linear_model.LinearRegression()

    linear.fit(x_train, y_train)
    acc = linear.score(x_test, y_test)
    print(acc)

    link = "https://finviz.com/screener.ashx?v=111"
    website = requests.get(link)
    results = bs(website.content, "html.parser")
    print(results)