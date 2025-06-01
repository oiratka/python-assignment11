import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

query = """
    SELECT last_name, SUM(price * quantity) AS revenue
    FROM employees e
    JOIN orders o ON e.employee_id = o.employee_id
    JOIN line_items l ON o.order_id = l.order_id
    JOIN products p ON l.product_id = p.product_id
    GROUP BY e.employee_id;
    """
with sqlite3.connect("./db/lesson.db") as conn:
    employee_results = pd.read_sql(query, conn)
print(employee_results.head())

pd_plotting = employee_results.plot(
    x="last_name", 
    y="revenue",
    title="Employee Revenue Report",
    kind="bar",
    color="blue")
pd_plotting.set_xlabel("Employee Last name")
pd_plotting.set_ylabel("Revenue")
plt.show()




