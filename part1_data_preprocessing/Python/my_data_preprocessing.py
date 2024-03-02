import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.compose  import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder,LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split

class Data_preprocessing:
    def __init__(self):
        print("Loading class")
        

    def import_dat(self,data_folder="",verbose=False):
        '''Importing data'''
        dataset = pd.read_csv(data_folder)
        self.X = dataset.iloc[:,:-1].values
        self.y = dataset.iloc[:,-1].values
        if verbose:
            print("X")
            print(f"{self.X[0]}")
            print(f"{self.X[int(len(self.X)/2)]}")
            print(f"{self.X[-1]}")
            print("y")
            print(f"{self.y[0]}")
            print(f"{self.y[int(len(self.y)/2)]}")
            print(f"{self.y[-1]}")

    def fill_missing_data(self,verbose=False):
        '''Filling up missing data using SimpleImputer from sklearn'''
        imputer = SimpleImputer(missing_values=np.nan,strategy="mean")
        imputer.fit(self.X[:,1:3])
        self.X[:,1:3]=imputer.transform(self.X[:,1:3])
        if verbose:
            print(self.X)

    def encoding_categorical_data(self,verbose=False):
        '''Encoding categorical data like contry names to numerical values'''
        #Encoding the indenpendnet variable
        ct = ColumnTransformer(transformers=[('encoder',OneHotEncoder(),[0])],remainder='passthrough')
        self.X = np.array(ct.fit_transform(self.X))
        #Encoding the dependent variable
        le=LabelEncoder()
        self.y = le.fit_transform(self.y)
        if verbose:
            print(self.X)
            print(self.y)

    def spliting_the_data(self,verbose=False):
        #We apply feature scalling after spliting
        # because we the test set is a new and never seing set, so is wrong to aply in to the testset.
        # Feature scalling gets information from the training set. The testset is something that the ml never see before
        '''Appling split in to the dataset in the training and test set'''
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(self.X,self.y, test_size=0.2, random_state=1)
        if verbose:
            print("X train:")
            print(self.X_train)
            print("X test:")
            print(self.X_test)
            print("y train:")
            print(self.y_train)
            print("y test:")
            print(self.y_test)

    def feature_scaling(self,verbose=False):
        #We apply feature scalling after spliting
        # because we the test set is a new and never seing set, so is wrong to aply in to the testset.
        # Feature scalling gets information from the training set. The testset is something that the ml never see before
        '''Type of regressions:
        Multiple linear regression: eat element is mutiply to a bias
        Polynomial linear regression: eat element is mutiply to a bias but the element gets a pow, like: b1x1 + b2x1^2+b3x1^3 .... + bnx1^n'''
        # Standardisation:
        # x=x-mean(x) / standard_deviation(x)
        # This gets value beetween a interval like -3 and +3
        # Normalisation:
        # x = x-min(x) / max(x) - min(x)
        # This gets values beetween a interval of 0 and 1
        sc = StandardScaler()
        self.X_train[:, 3:] = sc.fit_transform(self.X_train[:,3:]) # fit and transform the values. Fit with the standard_deviation
        self.X_test[:, 3:] = sc.transform(self.X_test[:,3:]) # transform the test values
        if verbose:
            print("X train after feet and transform:")
            print(self.X_train)
            print("X test after feet:")
            print(self.X_test)
        

if __name__ == "__main__":
    datapre = Data_preprocessing()
    datapre.import_dat(data_folder='./Data.csv')
    datapre.fill_missing_data(verbose=False)
    datapre.encoding_categorical_data(verbose=False)
    datapre.spliting_the_data(verbose=False)
    datapre.feature_scaling(verbose=True)
    


    
        
