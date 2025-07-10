import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import StandardScaler, MinMaxScaler


def plot_fit(X, y, degree, title, figsize=(10, 6)):
    poly = PolynomialFeatures(degree=degree)
    x_poly = poly.fit_transform(X)

    scaler = StandardScaler()
    x_poly = scaler.fit_transform(x_poly)

    model = LinearRegression()
    model.fit(x_poly, y)
    y_pred = model.predict(x_poly)

    plt.figure(figsize=figsize)
    plt.scatter(X, y, label="Data", color="blue", alpha=0.3)
    plt.plot(X, y_pred, label=f"Fitted Curve", color="red")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title(title)
    plt.legend()
    plt.grid()
    plt.show()
