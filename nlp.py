import numpy as np 
import pandas as pd 
import seaborn as sns 
import matplotlib.pyplot as plt 
import spacy
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.manifold import TSNE
pd.set_option("display.max_rows", None, "display.max_columns", None)
df_may=pd.read_csv(".../news_may.csv")
df_jun=pd.read_csv("../news_jun.csv")
df=pd.concat([df_may,df_jun],ignore_index=True)
df.drop_duplicates(inplace=True)
df.to_csv("/home/apurva/Documents/code/news_headlines/combined.csv")
zero_len=df[df.word_count==0]
df_zl=df[df.word_count!=0]
df_zl.pub_date=pd.to_datetime(df_zl.pub_date)
nlp=spacy.load("en_core_web_sm")
df_zl['headline_proc']=df["headline"].apply(lambda x:nlp(x))
count_vect = CountVectorizer()
headline_counts = count_vect.fit_transform(df_zl.headline)
headline_proc=pd.DataFrame(data=headline_counts.toarray(),columns=count_vect.get_feature_names())
df_vec=pd.concat([df_zl.pub_date,headline_proc],axis=1)
df_vec["date"]=df_vec.pub_date.dt.date
df_vec_sum=df_vec.groupby(['date']).sum()
df_vec_sum.reset_index(inplace=True)
df_vec_sum["target"]=[0 if x<pd.to_datetime("2020-05-25") else 1 for x in df_vec_sum.date]
df_vec['target']=[0 if x<pd.to_datetime("2020-05-25") else 1 for x in df_vec.date]
df_vec.drop(['pub_date'],axis=1,inplace=True)
print(df_vec.columns)
def tSNE(in_x,label):
    X_transformed = TSNE(n_components=2).fit_transform(in_x)
    print("transformed",X_transformed.shape)
    ax=sns.scatterplot(x=X_transformed[:,0],y=X_transformed[:,1],hue=label,legend="full")
    plt.show()

tSNE(df_vec.loc[:,df_vec.columns!="date"],df_vec.target)