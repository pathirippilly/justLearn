import pandas as pd



#Dictionary into data frame
sales_data = {'sku':[91234567,92345678,93456789,94567891],'qty_sold':[5,8,4,3],'unit_price':[125,120,235,256],'date':['03/05/2018','03/05/2018','03/05/2018','03/05/2018']}
yealry_sum1 = {'year':[2005,2006,2007,2008],'total_sales(Millions)':[238,256,274,325]}
yealry_sum2 = {'year':[2007,2008,2009,2010,2010],'total_sales(Millions)':[273,324,336,368,368]}
date=['03/05/2018', '03/05/2018', '03/05/2018', '03/05/2018']
qty_sold =[5, 8, 4, 3]
sku =[91234567, 92345678, 93456789, 93456791]
sku1 =[91234567, 92345678, 93456789,93456790,93456791]
unit_price = [125, 120, 235, 256,112]
df1=pd.DataFrame(np.random.randn(5,4),['A','B','C','D','E'],['W','X','Y','Z'])
#print(df1)
#df1['id']=[1,2,3,4,5]
#df1.set_index('id',inplace=True)
#print(df1)
##df2=pd.DataFrame(df1.append(pd.DataFrame({'V':[11,22,33,44,55]})))
##print(df2)
##df1.drop(axis=[0,1],index=1,columns='W',inplace=True)
#print(df1.index.names)
#print(df1.loc(0).loc)



#Series examples
#s1=pd.Series(qty_sold,sku)
#s2=pd.Series(unit_price,sku1)
#s3=pd.Series(date,sku)
#print(f"{s1}\n{s2}\n{s3}\n")
##print(s1.aggregate([min,max,sum]))
#A=s1.align(s2,'left')
#B=s1.axes
#C=s1[s1.between(1,10)]
#
#print(D)




df=pd.DataFrame(sales_data) #converting in to data form, that is in to columns and rows
df1=pd.DataFrame(yealry_sum1)
df2=pd.DataFrame(yealry_sum2)
#print(df1)
#print(df1.mean(axis=0))
print('02/20'.find('/'))


#
#
#print(df)
#print(df1)
#print(df2)
#print(df.head(2)) # first two rows
#print(df.tail(2)) # last two rows
#
##Merge : This is similar to join operation in SQL
##************************************************
#print(df2.merge(df1)) #perform inner join on all columns
#print(df2.merge(df1,how='inner')) #perform inner join on all columns
#print(df2.merge(df1,how='inner',on='year')) #perform inner join on year column 
#print(df2.merge(df1,how='inner',left_on='year',right_on='year'))     #perform inner join on year column
#print(df2.merge(df1,how='inner',left_on='year',right_on='year',sort='True'))  #Sort the join keys lexicographically in the result DataFrame. 
##If False, the order of the join keys depends on the join type (how keyword)
#print(df2.merge(df1,how='outer',left_on='year',right_on='year',sort='True',indicator='true'))
##perform outer join with last column of the output data frame as an indicator 
##called "_merge" with information on the source of each row.
##print(df2.merge(df1,how='outer',left_on='year',right_on='year',sort='True',indicator='true',validate='1:1'))
##perform outer join after validating the 1:1 check, i.e, check if merge keys are unique in both left and right datasets.
##Sice they left voilates it, it will throw the error.
#
#print(df1.join(df2,lsuffix='_l',rsuffix='_r')) #perform left outer  join on index columns 
#print(df1.join(df2.set_index('year'),on='year',lsuffix='_l',rsuffix='_r')) #perform left outer  join on year columns 
#df_out=df1.set_index('year')
#
#print(df_out.join(df2.set_index('year'),lsuffix='_l',rsuffix='_r',how='right',on='year'))
##Parameter definitions of merge is given below
#'''
#right : DataFrame how : {'left', 'right', 'outer', 'inner'}, default 'inner'
#
#left: use only keys from left frame, similar to a SQL left outer join; preserve key order
#right: use only keys from right frame, similar to a SQL right outer join; preserve key order
#outer: use union of keys from both frames, similar to a SQL full outer join; sort keys lexicographically
#inner: use intersection of keys from both frames, similar to a SQL inner join; preserve the order of the left keys
#on : label or list
#Field names to join on. Must be found in both DataFrames. If on is None and not merging on indexes, 
#then it merges on the intersection of the columns by default.
#left_on : label or list, or array-like
#Field names to join on in left DataFrame. Can be a vector or list of vectors of the length of 
#the DataFrame to use a particular vector as the join key instead of columns
#right_on : label or list, or array-like
#Field names to join on in right DataFrame or vector/list of vectors per left_on docs
#left_index : boolean, default False
#Use the index from the left DataFrame as the join key(s). If it is a MultiIndex, the number 
#of keys in the other DataFrame (either the index or a number of columns) must match the number of levels
#right_index : boolean, default False
#Use the index from the right DataFrame as the join key. Same caveats as left_index
#sort : boolean, default False
#Sort the join keys lexicographically in the result DataFrame. If False, the order of the 
#join keys depends on the join type (how keyword)
#suffixes : 2-length sequence (tuple, list, ...)
#Suffix to apply to overlapping column names in the left and right side, respectively
#copy : boolean, default True
#If False, do not copy data unnecessarily
#indicator : boolean or string, default False
#If True, adds a column to output DataFrame called "_merge" with information on the source
# of each row. If string, column with information on source of each row will be added to
# output DataFrame, and column will be named value of string. Information column is 
# Categorical-type and takes on a value of "left_only" for observations whose merge 
# key only appears in 'left' DataFrame, "right_only" for observations whose merge 
# key only appears in 'right' DataFrame, and "both" if the observation's merge key is found in both.
#
#New in version 0.17.0.
#
#validate : string, default None
#If specified, checks if merge is of specified type.
#
#"one_to_one" or "1:1": check if merge keys are unique in both left and right datasets.
#"one_to_many" or "1:m": check if merge keys are unique in left dataset.
#"many_to_one" or "m:1": check if merge keys are unique in right dataset.
#"many_to_many" or "m:m": allowed, but does not result in checks.
#New in version 0.21.0.
#'''
