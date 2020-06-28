import numpy as np 
import pandas as pd 
import seaborn as sns 
import matplotlib.pyplot as plt 
pd.set_option("display.max_rows", None, "display.max_columns", None)
df_may=pd.read_csv("/home/apurva/Documents/code/news_headlines/news_may.csv")
df_jun=pd.read_csv("/home/apurva/Documents/code/news_headlines/news_jun.csv")
df=pd.concat([df_may,df_jun],ignore_index=True)
df.drop_duplicates(inplace=True)
#Data frame containing news articles with cord count >0
zero_len=df[df.word_count==0]
df_zl=df[df.word_count!=0]
df_zl.pub_date=pd.to_datetime(df_zl.pub_date)

#Distribution of word count vs number of articles
ax=sns.distplot(df_zl.word_count, bins=np.arange(0,df_zl.word_count.max(),10), kde=False, hist_kws=dict(ec="k"))
plt.ylabel("# of articles")
plt.show()

#Distribution of type of material
ax1=sns.countplot(x=df_zl.type_of_material)
plt.xticks(rotation=45)
plt.show()

#Distribution of section name
ax3=sns.countplot(x=df_zl.section_name)
plt.xticks(rotation=90)
plt.show()
df_print=df_zl[df_zl.print_page.isna()!=True]
#Distribution of word count for print page
for num in df_print.print_page.unique():
    df_print_un=df_print[df_print.print_page==num]
    ax3=sns.distplot(df_print_un.word_count, bins=np.arange(0,df_print_un.word_count.max(),10), kde=False, hist_kws=dict(ec="k"))
    plt.show()


print("Mean word count by print page",df_print.groupby(["print_page"]).word_count.median())
print("Mean word count by section",df_zl.groupby(["section_name"]).word_count.median())
print("Sections wrt print page",df_zl.groupby(["print_page"]).section_name.value_counts())
#ax2=sns.lineplot(x=df_print.word_count,y=df_print.print_page,hue=df_print.section_name)
#plt.show()
#Distribution of publicatio date vs type of material
ax = sns.countplot(x=df_zl.pub_date.dt.date, hue="type_of_material", data=df_zl)
plt.xticks(rotation=90)
plt.show()