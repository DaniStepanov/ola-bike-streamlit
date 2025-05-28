
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

# App title
st.title('🚲 Ola Bike Ride Analysis')

# Load dataset
df = pd.read_csv('ola.csv')  # make sure the file is in the same folder or add full path

# Convert datetime and add time features
df['datetime'] = pd.to_datetime(df['datetime'])
df['hour'] = df['datetime'].dt.hour
df['day'] = df['datetime'].dt.dayofweek
df['month'] = df['datetime'].dt.month

st.subheader('📊 Dataset Preview')
st.dataframe(df.head())

# Total ride count distribution
st.subheader('1. Distribution of Total Rides')
fig1 = sns.histplot(data=df, x='count', bins=30, kde=True)
plt.title('Distribution of Total Rides')
st.pyplot(plt.gcf())
plt.clf()

# Rides by hour of day
st.subheader('2. Total Rides by Hour')
fig2 = sns.lineplot(data=df, x='hour', y='count', ci=None)
plt.title('Rides by Hour of Day')
st.pyplot(plt.gcf())
plt.clf()

# Temperature vs Ride count
st.subheader('3. Rides vs Temperature')
fig3 = sns.scatterplot(data=df, x='temp', y='count')
plt.title('Ride Count vs Temperature')
st.pyplot(plt.gcf())
plt.clf()

# Weather and ride count
st.subheader('4. Rides by Weather Condition')
fig4 = sns.boxplot(data=df, x='weather', y='count')
plt.title('Rides Based on Weather')
st.pyplot(plt.gcf())
plt.clf()

# Casual vs registered users over time
st.subheader('5. Casual vs Registered Users Over Time')
df_melt = df.melt(id_vars=['datetime'], value_vars=['casual', 'registered'], var_name='user_type', value_name='rides')
fig5 = sns.lineplot(data=df_melt, x='datetime', y='rides', hue='user_type')
plt.title('Casual vs Registered Rides Over Time')
st.pyplot(plt.gcf())
plt.clf()

st.markdown("Made by Danila Stepanov 😎")
