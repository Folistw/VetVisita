import plotly.graph_objects as go
import pandas as pd

colnames=['Month', 'Visits'] 
df = pd.read_csv("Data.csv", sep=',', names=colnames, header=None)

# Step 3: Prepare your data
categories = df['Month'][1:]
heights = df['Visits'][1:]

# Step 4: Create a bar chart object
bar_chart = go.Bar(x=categories, y=heights)

# Step 5: Create a figure and add the bar chart object
fig = go.Figure()
fig.add_trace(bar_chart)

# Step 6: Customize the chart (optional)
fig.update_layout(
    title='Visits per month',
    xaxis_title='Months',
    yaxis_title='Visits'
)

st.plotly_chart(fig)
