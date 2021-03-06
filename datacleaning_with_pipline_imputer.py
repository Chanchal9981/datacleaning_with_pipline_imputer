# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

train=pd.read_csv("C:\\Users\\patid\\Downloads\\train (2).csv")
test=pd.read_csv("C:\\Users\\patid\\Downloads\\test (1).csv")
print("shape of train_data is=",train.shape)
print("shape of test_data is=",test.shape)

X_train=train.drop("SalePrice",axis=1)
y_train=train["SalePrice"]
X_test=test.copy()
print("shape of X_train is=",X_train.shape)
print("shape of y_train is=",y_train.shape)
print("shape of x_test is=",X_test.shape)

num_vars=X_train.select_dtypes(include=['int64','float64'])
null_columns=[var for var in num_vars.columns if num_vars[var].isnull().sum()>0]
null_columns

cat_vars=X_train.select_dtypes(include=['object'])
cat_columns=[var for var in cat_vars.columns if cat_vars[var].isnull().sum()>0]
cat_columns

num_vars_mean=['LotFrontage']
num_vars_median=['MasVnrArea', 'GarageYrBlt']
cat_vars_mode=['Alley',
 'MasVnrType',
 'BsmtQual',
 'BsmtCond',
 'BsmtExposure',
 'BsmtFinType1',
 'BsmtFinType2',
 'Electrical',
 'FireplaceQu',]
cat_vars_missing=['GarageType',
 'GarageFinish',
 'GarageQual',
 'GarageCond',
 'PoolQC',
 'Fence',
 'MiscFeature']

num_vars_mean_imputer=Pipeline(steps=[("imputer",SimpleImputer(strategy="mean"))])
num_vars_median_imputer=Pipeline(steps=[("imputer",SimpleImputer(strategy="median"))])
cat_vars_mode_imputer=Pipeline(steps=[("imputer",SimpleImputer(strategy="most_frequent"))])
cat_vars_missing_imputer=Pipeline(steps=[("imputer",SimpleImputer(strategy="constant",fill_value="missing"))])

prossecor=ColumnTransformer(transformers=[("mean_imputer",num_vars_mean_imputer,num_vars_mean),
                                      ("median_imputer",num_vars_median_imputer,num_vars_median),
                                      ("mode_imputer",cat_vars_mode_imputer,cat_vars_mode),
                                      ("missing_imputer",cat_vars_missing_imputer,cat_vars_missing)])

prossecor.fit(X_train)

prossecor.transform

prossecor.named_transformers_["mean_imputer"].named_steps["imputer"].statistics_

prossecor.named_transformers_["mode_imputer"].named_steps["imputer"].statistics_

X_train_clean=prossecor.transform(X_train)
X_test_clean=prossecor.transform(X_test)

X_train_clean

prossecor.transformers_

X_train_missing_vars=pd.DataFrame(X_train_clean,columns=num_vars_mean+num_vars_median+cat_vars_mode+cat_vars_missing)
X_train_missing_vars

X_train_missing_vars.isnull().sum().sum()

# Create Clean X_train DataFrame with call variables
remainder_vars_index= [0,
   1,
   2,
   4,
   5,
   7,
   8,
   9,
   10,
   11,
   12,
   13,
   14,
   15,
   16,
   17,
   18,
   19,
   20,
   21,
   22,
   23,
   24,
   27,
   28,
   29,
   34,
   36,
   37,
   38,
   39,
   40,
   41,
   43,
   44,
   45,
   46,
   47,
   48,
   49,
   50,
   51,
   52,
   53,
   54,
   55,
   56,
   61,
   62,
   65,
   66,
   67,
   68,
   69,
   70,
   71,
   75,
   76,
   77,
   78,
   79]
x1=np.reshape(remainder_vars_index,61)
x1



x=set(X_train)
y=set(X_train_missing_vars)
z=x.difference(y)
z1=list(z)
z1

X_train=pd.concat([X_train_missing_vars,train[z1]],axis=1)
X_train.isnull().sum().sum()
X_train.shape

"""# #for clean dataset"""

X_test_clean

X_test_clean_miss_var = pd.DataFrame(X_test_clean, columns=num_vars_mean+num_vars_median+cat_vars_mode+cat_vars_missing)
X_test_clean_miss_var.shape

X_test_clean_miss_var.isnull().sum().sum()

p=set(X_test)
q=set(X_test_clean_miss_var)
r=p.difference(q)
s=list(r)
len(s)

X_test=pd.concat([X_test_clean_miss_var,test[s]],axis=1)
X_test.isnull().sum().sum()

pd.set_option('display.Max_columns',None)
pd.set_option('display.Max_rows',None)

X_test.isnull().sum()

X_test_vars=X_test.select_dtypes(include=['int64','float64'])
X_test_miss_vars=[var for var in X_test_vars.columns if X_test_vars[var].isnull().sum()>0]
X_test_miss_vars

X_test_cat=X_test.select_dtypes(include=['object'])
X_test_miss_cat=[var for var in X_test_cat.columns if X_test_cat[var].isnull().sum()>0]
X_test_miss_cat

imputer_test_mean=['BsmtFullBath',
 'BsmtFinSF2',
 'BsmtHalfBath',
 'GarageArea',
 'BsmtFinSF1',
 'TotalBsmtSF',
 'GarageCars',
 'BsmtUnfSF']
imputer_test_mode=['KitchenQual',
 'MSZoning',
 'Exterior1st',
 'SaleType',
 'Utilities',
 'Functional',
 'Exterior2nd']

imputer_mean=SimpleImputer(strategy='mean')
imputer_mean_variables=imputer_mean.fit(X_test[X_test_miss_vars])
imputer_mean_variables

imputer_mean_variables.statistics_

X_test[X_test_miss_vars]=imputer_mean_variables.transform(X_test[X_test_miss_vars])
X_test[X_test_miss_vars]

imputer_mod=SimpleImputer(strategy='most_frequent')
imputer_mod_cats=imputer_mod.fit(X_test[X_test_miss_cat])
imputer_mod_cats

X_test[X_test_miss_cat]=imputer_mod_cats.transform(X_test[X_test_miss_cat])
X_test[X_test_miss_cat]

X_test.isnull().sum().sum()

