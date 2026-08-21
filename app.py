import streamlit as st 
import pickle 
import numpy as np
import pandas as pd


pipe=pickle.load(open('pipe.pkl','rb'))
df=pickle.load(open('df.pkl','rb'))

st.title("Laptop Predictor")
company=st.selectbox('Brand',df['Company'].unique())

type=st.selectbox('Type',df['TypeName'].unique())

ram=st.selectbox('Ram (GB) ',[2,4,6,8,12,16,24,32,64])

weight=st.number_input('Weight of the laptop')

touchscreen=st.selectbox('TouchScreen',['No','Yes'])

ips=st.selectbox('IPS',['No','Yes'])

screen_size=st.number_input('Screen Size')

resolution=st.selectbox('Screen Resolution',['1920x1080','1366x768','3840x2160','2899x1800','2560x1600','2560x1440','2304x1440'])

cpu=st.selectbox('CPU',df['Processor'].unique())

hdd=st.selectbox('HDD(in GB)',[0,128,256,512,1024,2048])
ssd=st.selectbox('SSD(in GB)',[0,8,128,256,512,1024])
gpu=st.selectbox('GPU',df['GpuBrand'].unique())
os=st.selectbox('OS',df['os'].unique())

if st.button('Predict Price'):
    x_res=int(resolution.split('x')[0])
    y_res=int(resolution.split('x')[1])

    ppi=((x_res**2)+(y_res**2))**0.5/screen_size
    if touchscreen == 'Yes':
        touchscreen=1
    else:
        touchscreen=0
    if ips=='Yes':
        ips=1
    else:
        ips=0

    # query=np.array([company,type,ram,weight,touchscreen,ips,ppi,cpu,hdd,ssd,gpu,os])
    query = pd.DataFrame({
    'Company': [company],
    'TypeName': [type],
    'Ram': [ram],
    'Weight': [weight],
    'TouchScreen': [touchscreen],
    'IPS': [ips],
    'ppi': [ppi],
    'Processor': [cpu],
    'HDD': [hdd],
    'SSD': [ssd],
    'GpuBrand': [gpu],
    'os': [os]
})
    # query=query.reshape(1,12)
    st.title("The price of the product will be : " + str(int(np.exp(pipe.predict(query)[0]))))