import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
class Linear_regression:
    def __init__(self):
        print("LINEAR REGRESSION")

    def loading_dataset(self,verbose=False,dataset_path=""):
        dataset = pd.read_csv(dataset_path)
        self.X = dataset.iloc[:,:-1].values
        self.y = dataset.iloc[:,-1].values
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(self.X,self.y, test_size=0.2,random_state=0)
        if verbose:
            print(f"X_train:\n{self.X_train}")
            print(f"X_test:\n{self.X_test}")
            print(f"y_train:\n{self.y_train}")
            print(f"y_test:\n{self.y_test}")
        
    def training_simple_linear(self):
        self.regressor=LinearRegression()
        self.regressor.fit(self.X_train,self.y_train)

    def predicting_results(self,verbose=False):
        self.y_pred = self.regressor.predict(self.X_test)

    def visualizing_training_results(self):
        plt.scatter(self.X_train, self.y_train, color='red')
        plt.plot(self.X_train, self.regressor.predict(self.X_train),color='blue')
        plt.title('Salary vs Experience (Training Set)')
        plt.xlabel('Years of Experience')
        plt.ylabel('Salary')
        plt.savefig("training_results.png")
        plt.show()

    def visualizing_test_sets(self):
        plt.scatter(self.X_test, self.y_test, color='red')
        plt.plot(self.X_train, self.regressor.predict(self.X_train),color='blue')
        plt.title('Salary vs Experience (Test Set)')
        plt.xlabel('Years of Experience')
        plt.ylabel('Salary')
        plt.savefig("test_results.png")
        plt.show()
            
            
            



if __name__=="__main__":
    linear = Linear_regression()
    linear.loading_dataset(verbose=False,dataset_path="./Salary_Data.csv")
    linear.training_simple_linear()
    linear.visualizing_training_results()
    linear.visualizing_test_sets()




#Simple linear regression, every x is multiply by a bias
