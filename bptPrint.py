# -*- coding: utf-8 -*-
"""
Christopher Stewart
SDSS:

HeII
__________________
SELECT TOP 500000
x.specobjid, x.ra, x.dec,
x.Flux_HeII_4685, x.Flux_HeII_4685_Err
FROM EmissionLinesPort AS x
WHERE 
x.Flux_HeII_4685_ER > 0 


"""
import time
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from astropy.io import fits
from astropy.table import Table


def plotContOnPoints(data):
    plt.figure(1)
    plt.subplot(2,1,1)
    plt.hist2d(data['xAxis'], data['yAxis'], bins = 1000, normed = False)
    bptcont = np.histogram2d(data['xAxis'], data['yAxis'], bins = 100)
    contourdata = np.asarray(bptcont[0])
    xbins = np.asarray(bptcont[1])
    ybins = np.asarray(bptcont[2])
    plt.contour(xbins[0:100], ybins[0:100], np.flipud(np.rot90(contourdata)), 20)
    fig = plt.figure(1)
    fig.savefig('testPlot.svg', format='svg', dpi=1200, bbox_inches='tight')
    
def fuck(data):
    plt.figure(1)
    plt.subplot(2,1,1)
    plt.hist2d(data['xAxis'], data['yAxis'], bins = 1000, normed = False)
    plt.subplot(2,1,2)
    
def plotHex(data):
    data.plot(subplots=True, figsize=(6, 6)).hexbin(x='xAxis', y='yAxis', gridsize=100)
    plt.show()
    
def getDataSet(filename):
    tp = pd.read_csv(filename, iterator=True, chunksize=1000)  
    df = pd.concat(tp, ignore_index=True)
    return df

    
def BPT(data):
    start_time = time.time()
    data.loc[:,'yAxis'] = data['oiii_5007_flux'].map(np.log) -data['h_beta_flux'].map(np.log)
    data.loc[:,'xAxis'] = data['nii_6584_flux'].map(np.log) -data['h_alpha_flux'].map(np.log)
    plotContOnPoints(data)
    'plotHex(data)'
    print("--- %s seconds ---" % (time.time() - start_time))
    return True

    
def filterSN(data):
    newDF = data.loc[data['Flux_HeII_4685'] > 3*data['Flux_HeII_4685_Err']]    
    return newDF
    
    
"http://stackoverflow.com/questions/23460345/selecting-unique-rows-between-two-dataframes-in-pandas"

def filterDataFrame(df1,df2):
    return df1[~df1.specobjid.isin(df2.specobjid)]
               
def plots():
    sndData = getDataSet('largeTestFile.csv')
    HeData = getDataSet("HeII.csv")
    filterDF = filterSN(HeData)
    result = filterDataFrame(sndData,filterDF)
    BPT(sndData)
    'BPT(result)'

plots()
