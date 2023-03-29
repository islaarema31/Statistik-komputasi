import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

class Barang() :
    #import dataframe
    data = pd.read_csv('ecommerce_lite.csv', usecols=['InvoiceNo','StockCode','Description','Quantity','InvoiceDate','UnitPrice','CustomerID','Country'])

    #pencarian data sesuai kode
    kd_barang = '22423'
    barang = data.loc[data['StockCode'] == kd_barang]

    #nama barang
    nama_barang = barang['Description'].iloc[0]
    print("Nama Barang:", nama_barang)

    #mean, median dan modus harga
    mean = data['Quantity'].mean()
    median = data['Quantity'].median()
    modus = data['Quantity'].mode()[0]

    print("Mean:", mean)
    print("Median:", median)
    print("Modus:", modus)

    #mencari q1-q3 dan iqr
    q1 = data['Quantity'].quantile(0.25)
    q2 = data['Quantity'].median()
    q3 = data['Quantity'].quantile(0.75)
    iqr = q3-q1

    print("Q1:", q1)
    print("Q2:", q2)
    print("Q3:", q3)
    print("IQR:", iqr)

    #outliner
    bts_bawah = q1 - 1.5 * iqr
    bts_atas = q3 + 1.5 * iqr

    jmlh_outliner = data.loc[(data['Quantity'] < bts_bawah) | (data['Quantity'] > bts_atas)].shape[0]

    print("Jumlah outliner:", jmlh_outliner)

    #histogram
    barang['Quantity'].hist(bins=20)
    plt.xlabel('Quantity')
    plt.ylabel('Frequency')
    plt.show()