import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

#Title---
st.title("FAASTECH INNOVATIONS- ")
st.title("AI CPU MONITORING DASHBOARD")

#loads dataset---
df=pd.read_csv("dataset.csv")

df['timestamp']=pd.to_datetime(df['timestamp'])


#anomaly detection logic---
mean=df['value'].mean()
std=df['value'].std()

#automatic Thrushold----
threshold= mean + 2 * std

#finding anomalies---
anomalies=df[df['value']> threshold]


#showing stats---
st.write("## System stats")
st.write(f"Mean CPU Usage: {mean:.2f}")
st.write(f"Threshold: {threshold:.2f}")
st.write(f"Anomalies Detected: {len(anomalies)}")

#plot---
fig,ax =plt.subplots()

ax.plot(df['timestamp'],df['value'],label="CPU Usage")
ax.scatter(anomalies['timestamp'],anomalies['value'],color='red',label='anomalies')
ax.axhline(y=threshold,color='green',linestyle='--',label='Threshold')

#data---
plt.plot(df['timestamp'],df['value'],label="CPU  Usage")

#labeling--
ax.set_xlabel("Time")
ax.set_ylabel("CPU Usage")
ax.set_title("CPU Monitoring with Anomaly Detection")
ax.legend()

#show plot in ui----
st.pyplot(fig)