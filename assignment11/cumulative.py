import sqlite3
import pandas as pd
import matplotlib.pyplot as plt


query = """
    SELECT o.order_id, SUM(quantity*price) as total_price
    FROM orders as o
    JOIN line_items as l ON  o.order_id = l.order_id
    JOIN products as p ON l.product_id = p.product_id
    GROUP BY o.order_id
"""
with sqlite3.connect('./db/lesson.db') as conn:
    df = pd.read_sql(query, conn)

df = df.sort_values(by='order_id')
df = df.reset_index(drop=True)

def cumulative(row):
    totals_above = df['total_price'][0:row.name +1]
    return totals_above.sum()

df['cumulative'] = df.apply(cumulative, axis=1)

print(df.head())

first_twenty = df.head(20)

chart = first_twenty.plot(
    x = "order_id",
    y = "cumulative",
    kind = 'line',
    color = 'green',
    title = "Cumulative revenue"
)
chart.set_xlabel("Order")
chart.set_ylabel("Revenue $")
plt.show()
