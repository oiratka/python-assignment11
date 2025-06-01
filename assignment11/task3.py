import plotly.express as px
import plotly.data as pldata

df = pldata.wind(return_type='pandas')

print(df.head(10))
print(df.tail(10))

def replace_ranges(val):
    if '-' in val:
        parts = val.split('-')
        return str((float(parts[0]) + float(parts[1]))/2)
    else:
        return val
df['strength'] = df['strength'].apply(replace_ranges)

df['strength'] = df['strength'].str.replace('+', '', regex= False)
df['strength'] = df['strength'].astype(float)

print(df['strength'].tail(10))

fig = px.scatter(
    df, 
    x='strength',
    y='frequency',
    color='direction',
    title='Strength vs Frequency by Direction',
    labels={'strength': "Strength", "frequency": "Frequency"},
    hover_data=['strength', 'frequency', 'direction']
)
fig.show()
fig.write_html('wind.html', auto_open=True)
