import pandas as pd
import streamlit as st
import requests
from sklearn.neighbors import NearestNeighbors
import seaborn as sns
import matplotlib.pyplot as plt

df=pd.read_csv('https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv')


# Créer des boutons pour filtrer les résultats par région
region = st.sidebar.radio('Sélectionner une région', ['US', 'Europe', 'Japan'])
if region == 'US':
    df = df[df['continent'] == 'US']
elif region == 'Europe':
    df = df[df['continent'] == 'Europe']
else:
    df = df[df['continent'] == 'Japan']

# Afficher les statistiques descriptives de la base de données
st.write('## Statistiques descriptives')
st.write(df.describe())

# Afficher la corrélation entre les variables
st.write('## Corrélation entre les variables')
sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
st.pyplot()

# Afficher la distribution des variables
st.write('## Distribution des variables')
for column in df.columns:
    if df[column].dtype != 'object':
        fig, ax = plt.subplots()
        sns.histplot(df[column], ax=ax, kde=True)
        st.pyplot(fig)

# Commentaires sur les résultats
st.write('## Commentaires')
st.write('La corrélation entre les variables "mpg" et "cubicinches" est négative, ce qui indique que les voitures avec une consommation de carburant plus élevée ont tendance à avoir des moteurs de plus petite taille.')
st.write('La distribution de la variable "hp" est asymétrique à droite, ce qui indique que la plupart des voitures ont une puissance relativement faible.')
st.write('La distribution de la variable "time-to-60" est symétrique, ce qui indique que la plupart des voitures prennent environ 15 à 20 secondes pour atteindre 60 mph.')