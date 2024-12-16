import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency
sns.set(style='dark')

#MEMBUAT DATAFRAME
#Import Dataframe season_2011_data
def create_season_2011_df():
    season_2011_data = all_df[(all_df['type'] == 'season') & (all_df['year'] == '2011')]

    melted_data = season_2011_data.melt(
    id_vars=['category'],
    value_vars=['casual', 'registered'])
    
    return melted_data

#Import Dataframe season_2012_data
def create_season_2012_df():
    season_2012_data = all_df[(all_df['type'] == 'season') & (all_df['year'] == '2012')]

    melted_data = season_2012_data.melt(
    id_vars=['category'],
    value_vars=['casual', 'registered'])

    return melted_data

#Import Dataframe season_data
def create_season_join_df():
    season_data = all_df[(all_df['type'] == 'season') & (all_df['year'].isin(['2011', '2012']))]

    return season_data

#Import Dataframe wthr_2011_data
def create_wthr_2011_df():
    wthr_2011_data = all_df[(all_df['type'] == 'weather') & (all_df['year'] == '2011')]

    return wthr_2011_data

#Import Dataframe wthr_2012_data
def create_wthr_2012_df():
    wthr_2012_data = all_df[(all_df['type'] == 'weather') & (all_df['year'] == '2012')]

    return wthr_2012_data

#Import Dataframe time_2011_data
def create_time_2011_df():
    time_2011_data = all_df[(all_df['type'] == 'time') & (all_df['year'] == '2011')]

    time_2011_totals = time_2011_data.groupby('category')['cnt'].sum()

    return time_2011_totals

#Import Dataframe time_2012_data
def create_time_2012_df():
    time_2012_data = all_df[(all_df['type'] == 'time') & (all_df['year'] == '2012')]

    time_2012_totals = time_2012_data.groupby('category')['cnt'].sum()

    return time_2012_totals

#Membaca File CSV
all_df = pd.read_csv("dashboard/main_data.csv")

#MEMBUAT DASHBOARD
all_df['year'] = all_df['year'].astype(str)

#Memanggil Helper Function Sebelumnya
season_2011_df = create_season_2011_df()
season_2012_df = create_season_2012_df()
season_join_df = create_season_join_df()
wthr_2011_df = create_wthr_2011_df()
wthr_2012_df = create_wthr_2012_df()
time_2011_df = create_time_2011_df()
time_2012_df = create_time_2012_df()

#Header
st.header('Bike Sharing :bike:')

#Menampilkan Customers Demograpics
st.subheader("Customer Demographics by Season")

fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(35, 15))
colors = ["#90CAF9", "#D3D3D3", "#D3D3D3"]

#Season 2011
sns.barplot(
    data=season_2011_df,
    x='category',
    y='value',
    hue='variable',
    palette='Set2',
    ax=ax[0],
    errorbar=None
)

ax[0].set_ylabel(None)
ax[0].set_xlabel(None)
ax[0].set_title("Season 2011", loc="center", fontsize=50)
ax[0].tick_params(axis='y', labelsize=35)
ax[0].tick_params(axis='x', labelsize=35)
ax[0].legend(fontsize=25, loc='upper right')

#Season 2012
sns.barplot(
    data=season_2012_df,
    x='category',
    y='value',
    hue='variable',
    palette='Set3',
    ax=ax[1],
    errorbar=None
)
ax[1].set_ylabel(None)
ax[1].set_xlabel(None)
ax[1].set_title("Season 2012", loc="center", fontsize=50)
ax[1].tick_params(axis='y', labelsize=35)
ax[1].tick_params(axis='x', labelsize=35)
ax[1].legend(fontsize=25, loc='upper right')

st.pyplot(fig)

st.markdown("\n\n\n")

#Season 2011 dan 2012
fig, ax = plt.subplots(figsize=(20, 10))
sns.lineplot(
    data=season_join_df,
    x='category',
    y='cnt',
    hue='year',
    marker='o',
    palette='Set1',
    linewidth=4,
    ci=None
)
ax.set_title("Bike Sharing Usage by Season (2011 and 2012)", loc="center", fontsize=30)
ax.set_ylabel(None)
ax.set_xlabel(None)
ax.tick_params(axis='y', labelsize=20)
ax.tick_params(axis='x', labelsize=20)
ax.legend(fontsize=20, loc='upper right')

st.pyplot(fig)

st.markdown("\n\n\n\n\n\n\n")

#Menampilkan Weather
st.subheader("Total Bike Sharing by Weather Condition")

fig, ax = plt.subplots(nrows=2, ncols=1, figsize=(35, 35), gridspec_kw={'hspace': 0.3})

#Weather 2011
sns.barplot(
    data=wthr_2011_df,
    x='cnt',
    y='category',
    palette=["#FF7F3E", "#A6AEBF", "#A6AEBF"],
    ax=ax[0],
    errorbar=None
)
ax[0].xaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f'{int(x):}'))
ax[0].set_ylabel(None)
ax[0].set_xlabel(None)
ax[0].set_title("Weather 2011", loc="center", fontsize=50)
ax[0].tick_params(axis='y', labelsize=35)
ax[0].tick_params(axis='x', labelsize=35)

for container in ax[0].containers:  
    ax[0].bar_label(
        container, 
        fmt='%d', 
        fontsize=30, 
        label_type='edge',
        rotation=270
    )  
st.markdown("\n\n\n")

#Weather 2012
sns.barplot(
    data=wthr_2012_df,
    x='cnt',
    y='category',
    palette=["#3D3BF3", "#A6AEBF", "#A6AEBF"],
    ax=ax[1],
    errorbar=None
)
ax[1].xaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f'{int(x):}'))
ax[1].set_ylabel(None)
ax[1].set_xlabel(None)
ax[1].set_title("Weather 2012", loc="center", fontsize=50)
ax[1].tick_params(axis='y', labelsize=35)
ax[1].tick_params(axis='x', labelsize=35)

for container in ax[1].containers: 
    ax[1].bar_label(
        container, 
        fmt='%d', 
        fontsize=30, 
        label_type='edge',
         rotation=270
    )

st.pyplot(fig)

st.markdown("\n\n\n\n\n\n\n")

#Menampilkan Time Bike Sharing
st.subheader("Total Bike Sharing by Time of Day")

fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(35, 15))
colors_2011 = sns.color_palette('Set2') 
colors_2012 = sns.color_palette('Set3')

#Time 2011
ax[0].pie(
    time_2011_df,
    labels=time_2011_df.index,
    autopct='%1.1f%%',
    colors=colors_2011,
    startangle=90,
    textprops={'fontsize':30}
)
ax[0].set_title("Season 2011", loc="center", fontsize=50)

#Time 2012
ax[1].pie(
    time_2012_df,
    labels=time_2012_df.index,
    autopct='%1.1f%%',
    colors=colors_2012,
    startangle=90,
    textprops={'fontsize':30}

)
ax[1].set_title("Season 2012", loc="center", fontsize=50)

st.pyplot(fig)
