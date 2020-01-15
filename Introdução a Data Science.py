import pandas as pd
import seaborn as sns


notas = pd.read_csv('/Users/fernandogarcia/Documents/GitHub/Introduçao a Data Science/ml-1m/ratings.csv')

notas.columns = ["usuarioId", "filmeId", "nota", "momento"]
notas.nota.head()
notas.nota.plot(kind='hist')
notas.nota.describe()

grafico = sns.boxplot(notas.nota)