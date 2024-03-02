# Same formula of the multiple linear regression, but in the mlr for every b is a diferent x; In the polynomial linear regression is the same x but the power changes (that why is polynomial)

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

class polynomial_regression:
    def __init__(self):
        print("PR")
    def load_data(self):
        dataset = pd.read_csv('./Position_Salaries.csv')
        self.X = dataset.iloc[:,1:-1].values
        self.y = dataset.iloc[:,-1].values

    def training_the_lr(self):
        from sklearn.linear_model import LinearRegression
        self.lin_reg = LinearRegression()
        self.lin_reg.fit(self.X,self.y)

    def training_the_pr(self):
        from sklearn.preprocessing import PolynomialFeatures
        from sklearn.linear_model import LinearRegression
        self.poly_reg = PolynomialFeatures(degree = 4)
        self.x_poly = self.poly_reg.fit_transform(self.X)
        self.lin_reg_2 = LinearRegression()
        self.lin_reg_2.fit(self.x_poly,self.y)


    def visualising_lr_results(self):
        plt.scatter(self.X, self.y, color='red')
        plt.plot(self.X, self.lin_reg.predict(self.X),color='blue')
        plt.title("Truth or Bluff (Linear Regression)")
        plt.xlabel('Position Level')
        plt.ylabel('Salary')
        plt.savefig('./visualising_lr_results.png')
        plt.show()

    
    def visualising_pr_results(self):
        plt.scatter(self.X, self.y, color='red')
        plt.plot(self.X, self.lin_reg_2.predict(self.x_poly),color='blue')
        plt.title("Truth or Bluff (Polynomial Regression)")
        plt.xlabel('Position Level')
        plt.ylabel('Salary')
        plt.savefig('./visualising_pr_results.png')
        plt.show()


if __name__=="__main__":
    plr = polynomial_regression()
    plr.load_data()
    plr.training_the_lr()
    plr.training_the_pr()
    plr.visualising_lr_results()
    plr.visualising_pr_results()


    
