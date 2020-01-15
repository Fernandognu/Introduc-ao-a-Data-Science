import pandas as pd
import seaborn as sns


notas = pd.read_csv('/Users/fernandogarcia/Documents/GitHub/Introduçao a Data Science/ml-1m/ratings.csv')
filmes = pd.read_csv('/Users/fernandogarcia/Documents/GitHub/Introduçao a Data Science/ml-1m/movies.csv')


notas.columns = ["usuarioId", "filmeId", "nota", "momento"]
filmes.columns = ["filmeId", "titulo", "generos"]
notas.nota.head()
notas.nota.plot(kind='hist')
notas.nota.describe()

print(filmes)