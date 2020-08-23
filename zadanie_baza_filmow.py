import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('tmdb_movies.csv')
q3 = np.percentile(df.vote_count, 75)
df_sub = df['vote_count'] > q3

"""
1. Zwróć listę 10 najwyżej ocenianych filmów (vote_average), których liczba głosów (vote_count) jest większa od 3. kwartyla rozkładu liczby głosów.

"""
top_ten = df.loc[(df["vote_count"] > q3)]
print(top_ten.head(10))

"""
2. Pogrupuj tabelę w taki sposób, aby otrzymać średni przychód (revenue)
oraz średni budżet (budget) w danym roku dla filmów opublikowanych od 2010 (włącznie) do 2016 roku (włącznie). 
Następnie na tej podstawie stwórz wykres, w którym średnie przychody są wykresem kolumnowym, 
a średnie przychody wykresem liniowym na tych samych osiach. 
Sformatuj odpowiednio oś X oraz oś Y. 
Dodaj tytuł wykresu oraz legendę, która znajduje się w prawym górnym rogu płótna, lecz poza obszarem osi. 
"""

df['Year'] = pd.DatetimeIndex(df['release_date']).year
years_df = df.loc[(df['Year'] >= 2010) & (df['Year'] < 2017)]
df0 = years_df[['revenue', 'budget', 'Year']].groupby(['Year']).mean().round(decimals=2)

df0.plot(kind='bar', y='revenue')
plt.legend(loc=(1.05, 1.0))
df0.plot(kind='line', y='budget')
plt.xlabel('Rok')
plt.ylabel('Budżet')
plt.title('Średni przychód i budżet filmu w latach 2010-2016')
plt.legend(loc=(1.05, 1.0))
plt.show()


"""
3. Baza filmów zawiera kolumnę z id gatunku (genre_id). Na tej podstawie połącz ze sobą bazę filmów z bazą gatunków,
 tak aby w bazie filmów można było odczytać nazwę gatunku filmu.
"""

baza_filmow = pd.read_csv('tmdb_movies.csv')
baza_gatunkow = pd.read_csv('tmdb_genres.csv')
new_baza_gatunkow = baza_gatunkow.rename(columns={"Unnamed: 0": "genre_id"})
after_merged = pd.merge(baza_filmow, new_baza_gatunkow, on='genre_id', how='inner')
print(after_merged)

"""
4. Jaki gatunek filmu z bazy pojawia się w niej najczęściej? Ile filmów tego gatunku znajduje się w bazie?
"""
df1 = after_merged.groupby(['genres']).count()
print(df1)
after_sorting = df1.sort_values(by='Unnamed: 0', ascending=False)
print(after_sorting)

"""
5. Filmy, którego gatunku trwają średnio najdłużej (runtime)?
"""
df2 = after_merged.groupby(['genres']).mean().sort_values(by='runtime', ascending=False).round(decimals=2)
print(df2)

"""
Stwórz histogram czasu trwania filmów z gatunku, który cechuje się największym średnim czasem trwania.
"""
df2.plot(kind='bar', x='genre_id', y='runtime')
plt.show()
