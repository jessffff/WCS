import pandas as pd
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import tempfile

df=pd.read_csv('https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv')


# Créer des boutons pour filtrer les résultats par région
region = st.sidebar.radio('Sélectionner une région', ['Toutes régions', ' US.', ' Europe.', ' Japan.'])
if region != 'Toutes régions':
    df = df[df['continent'] == region]

# Afficher les statistiques descriptives selon région sélectionnée
st.write('## Statistiques descriptives', region)
st.write(df.describe())



# Afficher la corrélation entre les variables
st.write('## Corrélation entre les variables', region)
corr_map = sns.heatmap(df.corr(), cmap='coolwarm', center=0)
st.pyplot()
st.set_option('deprecation.showPyplotGlobalUse', False)
with tempfile.NamedTemporaryFile(delete=False, suffix='.png') as tmp_file:
    corr_map.figure.savefig(tmp_file.name)

# Afficher les graphiques de distribution des variables
st.write('## Distribution des variables ', region)
fig = plt.figure(figsize=(12, 10))
grid = plt.GridSpec(4, 2, hspace=0.5)
num_cols = df.select_dtypes(include=['float', 'int']).columns
for i, col in enumerate(num_cols):
    if df[col].dtype != 'object':
        ax = fig.add_subplot(grid[i])
        sns.histplot(data=df, x=col, ax=ax, bins=20, color='steelblue')
        ax.set_title(col)
        ax.set_xlabel('')
        ax.set_ylabel('')
        ax.tick_params(axis='both', which='both', length=0)

# Afficher la grille
plt.tight_layout()
st.pyplot(fig)


# Commentaires sur les résultats
st.write('## Commentaires')
if region == 'Toutes régions' :
    st.write('La corrélation entre les variables "mpg" et "cubicinches" est négative, ce qui indique que les voitures avec une consommation de carburant plus élevée ont tendance à avoir des moteurs de plus petite taille.')
    st.write('La distribution de la variable "time-to-60" est symétrique, ce qui indique que la plupart des voitures prennent environ 15 à 20 secondes pour atteindre 60 mph.')
elif region == ' US.' :
   st.write("La distribution de la variable cylinders montre qu'il y a beaucoup de grosses cylindrées aux US.")
elif region == ' Japan.' :
    st.write("La distribution de la variable cylinders montre qu'il n'y a quasiment que des 4 CV au Japon")
elif region == ' Europe.' :
    st.write("La distribution de la variable weightlbs montre que les voitures ne sont pas très lourdes en Europe")
    