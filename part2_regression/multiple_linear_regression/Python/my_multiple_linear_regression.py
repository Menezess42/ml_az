# Dumy variables:
# - Dumy variables is a variable that makes categorical variables a numerical variable. Like if you have tree categorical variables like (dog,cat,bird) you conver to a categorical variabe like [[1,0,0],[0,1,0],[0,0,1]] First column is dogs, second is cat and third is bird.

# P-value
# - In classical statics, the p-values is the probability of obtaining a test statistic equal to or more extreme than that observed in a sample, under the null hypothesis. For exemple, in hypothesis testing, you can reject the null hypothesis at 5% if the p-values is less than 5%.

# Building a Model
# - Clean garbage; If you put garbage in, than the output will be garbage.
# - Select the right variables to clean the input
    # -- 5 methods of building models
        # --1 All-in:
            # --> Throw all the variables in;
            # --> Prior knowledge; or
            # --> You have to; or
            # --> Preparing for a backward Elimination
        # --2 Backward Elimination:
            # --> Step 1: Select a significance level to saty in the model (ex SL = 0.05);
            # --> Step 2: Fit the full model with all possible predictors
            # --> Step 3: Consider the predictor with the highest P-values. If P > SL, go to Step 4, otherwise go to FIN
            # --> Step 4: Remove the predictor;
            # --> Step 5: Fit model without this variable; Then gets to Step 3 again... you keep doing this until P < SL, than your are finished;
        # --3 Forward Selection:
            # --> Step 1: Select a significance level to enter the model (ex SL = 0.05);
            # --> Step 2: Fit all simple regression models y ~ xn Select the one with the lowest P-value
            # --> Step 3: Keep this variabe and fit all possible models with one extra predictor added to the one(s)
            # --> Step 4: Consider the predictor with the lowest P-value. If P < SL, go to Step 3, otherwise go to FIN;
        # --4 Bidirectional Elimination:
            # --> Step 1: Select a significance level to enter and to stay in the model (ex SLENTER=0.05, SLSTAY = 0.05)
            # --> Step 2: Perform the next step of Foward Selection (new variables must have: P < SLENTER to enter)
            # --> Step 3: Perform ALL steps of Backward Elimination (old variables must have P < SLSTAY to stay)
            # --> No new variables can enter and no old variables can exit
        # --5 Score Comparison:
            # --> Step 1: Select a criterion of goodnes of fit (ex Akaike critetrion)
            # --> Step 2: Construc all possible Regression Models: (2^n)-1 total combinations
            # --> Step 3: Select the one with the best criterion
        # -> You can heare abut stepwise regression in two ways:
            # --> Reference to the 2,3 and 4 methods
            # --> Reference to the 4th method
