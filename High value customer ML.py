# Enter your code here. Read input from STDIN. Print output to STDOUT


import pandas as pd

df_prod = pd.read_csv('product_data.csv')
df_trans = pd.read_csv('transactions_data.csv')


#joining two tables (left join)
master = pd.merge(df_trans,df_prod, how = 'left' , on = 'product_id' )

#printing the most common color
print(master['color'].mode())


------------------------------


# Enter your code here. Read input from STDIN. Print output to STDOUT
import pandas as pd
import math
import numpy as np

df_prod = pd.read_csv('product_data.csv')
df_trans = pd.read_csv('transactions_data.csv')


#joining two tables (left join)
master = pd.merge(df_trans,df_prod, how = 'left' , on = 'product_id' )

#checking the data type of variables
#(type(master.unit_product_price[0]))
#(type(master.transaction_date[0]))

#converting date from str to date
master['transaction_date'] = pd.to_datetime(master['transaction_date'])
master['purchased_quantity'] = master['purchased_quantity'].astype('int')
master['total_price'] = master.unit_product_price* master.purchased_quantity
#print(type(master.transaction_date[0]))

#test and train split
Train = master[master.transaction_date < '2012-01-10']
Test = master[master.transaction_date >= '2012-01-10']

#copying master to create a distinct list of customers
train_agg = master['customer_id'].copy()
train_agg = train_agg.drop_duplicates()

#aggregating

Train_agg = Train.groupby('customer_id').aggregate({'transaction_id':'count', 'total_price':'sum'})

Test_agg = Test.groupby('customer_id').aggregate({'transaction_id':'count', 'total_price':'sum'})

master_train = pd.merge(Train_agg,Test_agg, how = 'left' , on = 'customer_id' )

#creating target variable
def func(row):
    if math.isnan(row['transaction_id_y']):
        return 0 
    else:
        return 1
        
master_train['target'] = master_train.apply(func, axis = 1)

#renaming columns
master_train.columns = ['transaction_count', 'total_spent', 'post_transaction_count', 'post_total_spent', 'target']

#splitting into test and train
msk = np.random.rand(len(master_train)) < 0.7
train = master_train[msk]
test = master_train[~msk]
len(train), len(test)
x_train = train[['transaction_count', 'total_spent']]
y_train = train['target']
x_test = test[['transaction_count', 'total_spent']]
y_test = test['target']


from sklearn.ensemble import RandomForestClassifier
clf=RandomForestClassifier(n_estimators=100)
clf.fit(x_train,y_train)
y_out = clf.predict(x_test)

y_pred = []
for i in y_out:
    if(i<0.55):
        y_pred.append(0)
    else:
        y_pred.append(1)
y_pred = np.array(y_pred)

#accuracy
from sklearn.metrics import accuracy_score
accuracy_score(y_pred, y_test)

print(x_train)


