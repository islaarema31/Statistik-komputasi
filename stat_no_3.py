import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

class Barang() :
    #import dataframe
    data = pd.read_csv('ecommerce_lite.csv', usecols=['InvoiceNo','StockCode','Description','Quantity','InvoiceDate','UnitPrice','CustomerID','Country'])

    #pencarian data sesuai kode
    kd_barang = '22423'
    barang = data.loc[data['StockCode'] == kd_barang]

    #pengelompokkan berdasarkan negara
    groupData = data.groupby(['Country'])['Quantity'].sum()
    print(groupData)

    #presentase
    total = data['Quantity'].sum()
    persen_jualan = data.groupby('Country')['Quantity'].sum() / total * 100
    print(persen_jualan)

    #stok
    stok = data.groupby(['StockCode','Description'])['Quantity'].sum()
    print(stok.sort_values (ascending=False)[:5])