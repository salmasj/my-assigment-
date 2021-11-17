#!/usr/bin/env python
# coding: utf-8

# In[157]:


# Import Data

import pandas as pd
data_frame = pd.read_csv("C:/Programming Things/Data/financial.csv")
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows' , None)


# # Data Understanding

# In[158]:


# Rows of sales
print("Number of Sales's Rows :", len(data_frame['Sales']))


# In[159]:


# How much columns and their name
print("Number of Columns :", len(data_frame.columns))
print("Columns's Name :", list(data_frame.columns))


# In[160]:


# Types of Data in Each Columns
print("Types of Data in Each Columns : ")
print(data_frame.dtypes)


# In[161]:


# Ordinal Type Attribute

# Answer : Atribut bertipe ordinal adalah DiscountBand, 
#          dengan nilai None, Low, Medium, High.


# In[162]:


# Range 
print("- Range Numerical Attributes -")

# Units Sold
min_1 = data_frame.min()
max_1 = data_frame.max()
range_1 = max_1['UnitsSold'] - min_1['UnitsSold'] 
print("Range Units Sold :", int(range_1))

# Manufacturing Price 
min_2 = data_frame.min()
max_2 = data_frame.max()
range_2 = max_2['ManufacturingPrice'] - min_2['ManufacturingPrice'] 
print("Range Manufacturing Price :", int(range_2))

# Sale Price
min_3 = data_frame.min()
max_3 = data_frame.max()
range_3 = max_3['SalePrice'] - min_3['SalePrice'] 
print("Range Sale Price :", int(range_3))

# Gross Sales
min_4 = data_frame.min()
max_4 = data_frame.max()
range_4 = max_4['GrossSales'] - min_4['GrossSales'] 
print("Range Gross Sales :", int(range_4))

# Discounts
min_5 = data_frame.min()
max_5 = data_frame.max()
range_5 = max_5['Discounts'] - min_5['Discounts'] 
print("Range Discounts :", int(range_5))

# Sales
min_6 = data_frame.min()
max_6 = data_frame.max()
range_6 = max_6['Sales'] - min_6['Sales'] 
print("Range Sales :", int(range_6))

# COGS
min_7 = data_frame.min()
max_7 = data_frame.max()
range_7 = max_7['COGS'] - min_7['COGS'] 
print("Range COGS :", int(range_7))

# Profit
min_8 = data_frame.min()
max_8 = data_frame.max()
range_8 = max_8['Profit'] - min_8['Profit'] 
print("Range Profit :", int(range_8))


# In[163]:


# Data Kotor


# In[164]:


# Mencari tahu data kosong pada kolom
print(data_frame.isna().sum())


# In[165]:


# Data berisi nilai aneh 

# 1. Untuk kolom Discount
print('Banyaknya data aneh pada kolom', data_frame.loc[(data_frame['Discounts']>100)][["Discounts"]].count())
# 2. Untuk kolom UnitsSold
print('Banyaknya data aneh pada kolom', data_frame.loc[(data_frame['UnitsSold']%1!=0)][["UnitsSold"]].count())


# In[166]:


# Memperlakukan data kotor

# Mengisi angka 0 pada data kosong kolom Discounts
data_frame['Discounts'].fillna(0)


# In[167]:


# Mengisi angka 0 pada data kosong kolom Profit
data_frame['Profit'].fillna(0)


# # Statistics

# In[168]:


# UnitsSold 
print("- Units Sold -")

maximum_units_sold, minimum_units_sold = (data_frame['UnitsSold'].max(), data_frame['UnitsSold'].min())
print("Maximum Units Sold :", maximum_units_sold) ; print("Minimum Units Sold :", minimum_units_sold)

units_sold_mean = data_frame['UnitsSold'].mean()
print("Mean of Units Sold :", units_sold_mean)

percentile_1 = data_frame['UnitsSold'].quantile(0.25)
print("Percentile 25% :", percentile_1)

percentile_2 = data_frame['UnitsSold'].quantile(0.50)
print("Percentile 50% :", percentile_2)

percentile_3 = data_frame['UnitsSold'].quantile(0.75)
print("Percentile 75% :", percentile_3)

print("")

# Manufacturing Price
print("- Manufacturing Price -")

maximum_manufacturing_price, minimum_manufacturing_price = (data_frame['ManufacturingPrice'].max(), data_frame['ManufacturingPrice'].min())
print("Maximum Manufacturing Price :", maximum_manufacturing_price) ; print("Minimum Manufacturing Price :", minimum_manufacturing_price)

manufacturing_price_mean = data_frame['ManufacturingPrice'].mean()
print("Mean of Manufacturing Price :", manufacturing_price_mean)

percentile_1 = data_frame['ManufacturingPrice'].quantile(0.25)
print("Percentile 25% :", percentile_1)

percentile_2 = data_frame['ManufacturingPrice'].quantile(0.50)
print("Percentile 50% :", percentile_2)

percentile_3 = data_frame['ManufacturingPrice'].quantile(0.75)
print("Percentile 75% :", percentile_3)

print("")

# Sale Price
print("- Sale Price -")

maximum_sale_price, minimum_sale_price = (data_frame['SalePrice'].max(), data_frame['SalePrice'].min())
print("Maximum Sale Price :", maximum_sale_price) ; print("Minimum Sale Price :", minimum_sale_price)

sale_price_mean = data_frame['SalePrice'].mean()
print("Mean of Sale Price :", sale_price_mean)

percentile_1 = data_frame['SalePrice'].quantile(0.25)
print("Percentile 25% :", percentile_1)

percentile_2 = data_frame['SalePrice'].quantile(0.50)
print("Percentile 50% :", percentile_2)

percentile_3 = data_frame['SalePrice'].quantile(0.75)
print("Percentile 75% :", percentile_3)

print("")

# Gross Sales
print("- Gross Sales -")

maximum_gross_sales, minimum_gross_sales = (data_frame['GrossSales'].max(), data_frame['GrossSales'].min())
print("Maximum Gross Sales :", maximum_gross_sales) ; print("Minimum Gross Sales :", minimum_gross_sales)

gross_sales_mean = data_frame['GrossSales'].mean()
print("Mean of Gross Sales :", gross_sales_mean)

percentile_1 = data_frame['GrossSales'].quantile(0.25)
print("Percentile 25% :", percentile_1)

percentile_2 = data_frame['GrossSales'].quantile(0.50)
print("Percentile 50% :", percentile_2)

percentile_3 = data_frame['GrossSales'].quantile(0.75)
print("Percentile 75% :", percentile_3)

print("")

# Discounts
print("- Discounts -")

maximum_discounts, minimum_discounts = (data_frame['Discounts'].max(), data_frame['Discounts'].min())
print("Maximum Discounts :", maximum_discounts) ; print("Minimum Discounts :", minimum_discounts)

discounts_mean = data_frame['Discounts'].mean()
print("Mean of Discounts :", discounts_mean)

percentile_1 = data_frame['Discounts'].quantile(0.25)
print("Percentile 25% :", percentile_1)

percentile_2 = data_frame['Discounts'].quantile(0.50)
print("Percentile 50% :", percentile_2)

percentile_3 = data_frame['Discounts'].quantile(0.75)
print("Percentile 75% :", percentile_3)

print("")

# Sales
print("- Sales -")

maximum_sales, minimum_sales = (data_frame['Sales'].max(), data_frame['Sales'].min())
print("Maximum Sales :", maximum_sales) ; print("Minimum Sales :", minimum_sales)

sales_mean = data_frame['Sales'].mean()
print("Mean of Sales :", sales_mean)

percentile_1 = data_frame['Sales'].quantile(0.25)
print("Percentile 25% :", percentile_1)

percentile_2 = data_frame['Sales'].quantile(0.50)
print("Percentile 50% :", percentile_2)

percentile_3 = data_frame['Sales'].quantile(0.75)
print("Percentile 75% :", percentile_3)

print("")

# COGS
print("- COGS -")

maximum_COGS, minimum_COGS = (data_frame['COGS'].max(), data_frame['COGS'].min())
print("Maximum COGS :", maximum_COGS) ; print("Minimum COGS :", minimum_COGS)

COGS_mean = data_frame['COGS'].mean()
print("Mean of COGS :", COGS_mean)

percentile_1 = data_frame['COGS'].quantile(0.25)
print("Percentile 25% :", percentile_1)

percentile_2 = data_frame['COGS'].quantile(0.50)
print("Percentile 50% :", percentile_2)

percentile_3 = data_frame['COGS'].quantile(0.75)
print("Percentile 75% :", percentile_3)

print("")

# Profit
print("- Profit -")

maximum_profit, minimum_profit = (data_frame['Profit'].max(), data_frame['Profit'].min())
print("Maximum Profit :", maximum_profit) ; print("Minimum profit :", minimum_profit)

profit_mean = data_frame['Profit'].mean()
print("Mean of Profit :", profit_mean)

percentile_1 = data_frame['Profit'].quantile(0.25)
print("Percentile 25% :", percentile_1)

percentile_2 = data_frame['Profit'].quantile(0.50)
print("Percentile 50% :", percentile_2)

percentile_3 = data_frame['Profit'].quantile(0.75)
print("Percentile 75% :", percentile_3)

print("")


# # Data Exploration

# In[169]:


# Data in December Year 2014
data_frame.loc[(data_frame["MonthName"] == 'December') & (data_frame["Year"] == 2014)]


# In[170]:


# Data Product Paseo with Units Sold > 1000
data_frame.loc[(data_frame["Product"] == 'Paseo') & (data_frame["UnitsSold"] > 1000)]


# In[171]:


# Data with 10 highest value of Sales
Sales = data_frame.sort_values(['Sales'], ascending=[0])
Sales.head(10)


# In[172]:


# Data Country with Total Profit
data_frame.groupby("Country")["Profit"].sum()


# In[173]:


# Data Frequency per Segment Year 2013
data_segment_year_2013 = data_frame.loc[data_frame["Year"] == 2013]
data_segment_year_2013['Segment'].value_counts()


# In[174]:


# Orders of Data based on Year and Month Number
data_frame.sort_values(['Year', 'MonthNumber'], ascending=[1, 1])


# In[175]:


# Orders of Data based on Product
data_frame.sort_values(["Product"], ascending=[1])


# # Visualisasi 
# 

# In[176]:


import matplotlib.pyplot as plt


# In[177]:


#Data of Total Units Sold Distribution per Month in 2014

new_df = data_frame.loc[data_frame["Year"] == 2014].groupby("MonthNumber")["UnitsSold"].sum()
new_df.plot(kind='bar', x='MonthNumber', y='UnitsSold', color="lightgreen", figsize=(10, 6))

plt.title('Data of Total Units Sold Distribution per Month in 2014 ')
plt.ylabel('Total Units Sold')
plt.xlabel('Month')
plt.show()


# In[178]:


# Reason : Menurut saya tipe grafik bar sangat cocok untuk menampilkan distribusi penjualan setiap bulan
#          karena kita dapat dengan jelas membandingkan total unit yang terjual setiap bulannya.  


# In[179]:


# Ratio of Total Sales and Total Profit per Product in 2014

new_df_1 = data_frame.loc[data_frame["Year"] == 2014].groupby("Product")["Sales"].sum()
new_df_2 = data_frame.loc[data_frame["Year"] == 2014].groupby("Product")["Profit"].sum()

ax=plt.gca()

new_df_1.plot(kind='barh', x='Product', y='Sales', color="Pink", figsize=(10, 6), ax=ax)
new_df_2.plot(kind='barh', x='Product', y='Profit', color="Grey", figsize=(10, 6), ax=ax)

plt.title('Ratio of Total Sales and Total Profit per Product in 2014')
plt.ylabel('Product')
plt.xlabel('Ratio Total Value')
plt.legend(['Sales', 'Profit'])
plt.show()


# In[180]:


# Reason : Alasan saya memilih tipe grafik barh yang digabungkan karena menurut saya kita dapat dengan mudah membandingkan
#          nilai total sales dan total profit (variabel x) dalam satu variabel y yang sama, yaitu product.


# In[181]:


# Ratio of Mean between Sale Price and Manufacturing Price in USA 2014

plt.bar("Sale Price", (data_frame.loc[data_frame['Country'] == 'United States of America'] ['SalePrice'].mean()), color='tan')
plt.bar("Manufacturing Price", (data_frame.loc[data_frame['Country'] == 'United States of America'] ['ManufacturingPrice'].mean()), color='papayawhip')
plt.title('Ratio of Mean between Sale Price and Manufacturing Price in USA 2014')
plt.ylabel('Mean')
plt.show()


# In[182]:


# Reason : Alasan saya memilih tipe grafik bar karena kita bisa dengan mudah melihat perbandingan
#          rata-rata dari sale price dan manufacturing price dengan variabel y sebagai nilai rata-rata.


# In[183]:


# Percentace of Total Units Sold per Product

new_df_7 = data_frame.groupby("Product")["UnitsSold"].sum()
mycolors = ["lightgray", "lightcoral", "peachpuff", "khaki", "lightcyan", "thistle"]
new_df_7.plot(kind='pie', autopct='%1.1f%%', figsize=(10, 6), colors=mycolors)
plt.title('Percentace of Total Units Sold per Product')
plt.show()


# In[184]:


# Reason : Alasan saya memilih plot pie karena grafik pie paling cocok untuk memvisualisasikan persentase komposisi 
#          dibandingkan model plot lain.


# In[185]:


# Percentace of Total Units Sold per Country

new_df_8 = data_frame.groupby("Country")["UnitsSold"].sum()
mycolors = ["lightskyblue", "greenyellow", "darkorange", "lightsalmon", "plum"]
new_df_8.plot(kind='pie', autopct='%1.1f%%', figsize=(10, 6), colors=mycolors, startangle = 90)
plt.title('Percentace of Total Units Sold per Country')
plt.show()


# In[186]:


# Reason : Alasan saya memilih plot pie karena grafik pie paling cocok untuk memvisualisasikan persentase komposisi 
#          dibandingkan model plot lain.


# In[187]:


# Perkembangan jumlah Sales dari bulan ke bulan tiap negara pada tahun 2013

month = ["September", "October", "November", "December"]
canada = data_frame.loc[(data_frame['Year'] == 2013) & (data_frame["Country"] == 'Canada')].groupby(['MonthNumber'], sort=True)['Sales'].sum()
usa = data_frame.loc[(data_frame['Year'] == 2013) & (data_frame["Country"] == 'United States of America')].groupby(['MonthNumber'], sort=True)['Sales'].sum()
germany = data_frame.loc[(data_frame['Year'] == 2013) & (data_frame["Country"] == 'Germany')].groupby(['MonthNumber'], sort=True)['Sales'].sum()
mexico = data_frame.loc[(data_frame['Year'] == 2013) & (data_frame["Country"] == 'Mexico')].groupby(['MonthNumber'], sort=True)['Sales'].sum()
france = data_frame.loc[(data_frame['Year'] == 2013) & (data_frame["Country"] == 'France')].groupby(['MonthNumber'], sort=True)['Sales'].sum()

plt.plot(month, canada, color='lightcoral')
plt.plot(month, usa, color='orange')
plt.plot(month, germany, color='lightgreen')
plt.plot(month, mexico, color='cyan')
plt.plot(month, france, color='cornflowerblue')
plt.legend(['Canada', 'USA', 'Germany', 'Mexico', 'France'])
plt.show()


# In[188]:


# Reason : Alasan saya memilih line plot karena dengan line plot kita bisa melihat kekontinuan dan perkembangan
#          data dari bulan ke bulan.


# # Hubungan antara Discounts dan Profit

# In[189]:


# Scatter Plot between Discounts and Profit
data_frame.plot(kind='scatter', x='Discounts', y='Profit', color="c")
plt.show()


# In[190]:


# Correlation Value
data_frame["Discounts"].corr(data_frame["Profit"])


# In[191]:


# Hubungan Korelasi

#  Answer : Korelasi antara kedua kolom tersebut berbanding lurus 
#           namun korelasinya tidak begitu dekat karena
#           nilai korelasinya cukup jauh dari angka 1 
#           dan dapat dilihat dari plot scatter bahwa data menyebar.


# # 3 product paling menguntungkan per segment

# In[192]:


# 3 product dengan total profit tertinggi dari masing-masing segment

# Cara 1
datas = data_frame.groupby(["Segment", "Product"]).agg({'Profit':sum})
datas_1 = datas["Profit"].groupby(level=0, group_keys=False)
datas_1.nlargest(3)


# In[193]:


# 3 product dengan total profit tertinggi dari masing-masing segment

# Cara 2
datas_1 = data_frame.loc[data_frame['Segment'] == 'Channel Partners'].groupby(['Product'])["Profit"].sum()
datas_2 = data_frame.loc[data_frame['Segment'] == 'Government'].groupby(['Product'])["Profit"].sum()
datas_3 = data_frame.loc[data_frame['Segment'] == 'Enterprise'].groupby(['Product'])["Profit"].sum()
datas_4 = data_frame.loc[data_frame['Segment'] == 'Midmarket'].groupby(['Product'])["Profit"].sum()
datas_5 = data_frame.loc[data_frame['Segment'] == 'Small Business'].groupby(['Product'])["Profit"].sum()

print('Segment : Channel Partners')
print(datas_1.sort_values(ascending=False).head(3).reset_index())
print('')

print('Segment : Government')
print(datas_2.sort_values(ascending=False).head(3).reset_index())
print('')

print('Segment : Enterprise')
print(datas_3.sort_values(ascending=False).head(3).reset_index())
print('')

print('Segment : Midmarket')
print(datas_4.sort_values(ascending=False).head(3).reset_index())
print('')

print('Segment : Small Business')
print(datas_5.sort_values(ascending=False).head(3).reset_index())
print('')


# In[194]:


# Teknik analisis data yang dapat digunakan adalah teknik Grouping dan mengkombinasikannya
# dengan fungsi sum, teknik Filtering, dan teknik Sorting. 


# In[ ]:




