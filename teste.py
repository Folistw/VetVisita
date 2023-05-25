import plotly.graph_objects as go
import pandas as pd
import streamlit as st

st.write(st.experimental_user)
if "gomes" in str(st.experimental_user.email):
    st.write("Tu es Nabo")
else:
    print(st.experimental_user.email)
    colnames=['Month', 'Visits', 'Unique_users'] 
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

    # Step 3: Prepare your data
    categories = df['Month'][1:]
    heights = df['Unique_users'][1:]

    # Step 4: Create a bar chart object
    bar_chart = go.Bar(x=categories, y=heights)

    # Step 5: Create a figure and add the bar chart object
    fig = go.Figure()
    fig.add_trace(bar_chart)

    # Step 6: Customize the chart (optional)
    fig.update_layout(
        title='Unique users per month',
        xaxis_title='Months',
        yaxis_title='Unique Users'
    )

    st.plotly_chart(fig)
