import plotly.graph_objects as go
import pandas as pd
import streamlit as st

@st.cache
def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
    return df.to_csv().encode('utf-8')

st.write(st.experimental_user)
if "gomes" in str(st.experimental_user.email):
    st.write("Tu es Nabo")
else:
    print(st.experimental_user.email)
    colnames=['Month', 'Visits', 'Unique_users'] 
    df = pd.read_csv("Data.csv", sep=',', names=colnames, header=None)
    
       
    csv = convert_df(df)
    
    st.download_button(
        label="Download data as CSV",
        data=csv,
        file_name='Data.csv',
        mime='text/csv',
    )
    
    
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
    
    # Sample data for three years (replace with your own data)
    years = [2019, 2020, 2021]
    months = ['January', 'February', 'March', 'April', 'May', 'June']
    data = [
        [150, 200, 250, 300, 350, 400],  # Data for 2019
        [200, 250, 300, 350, 400, 450],  # Data for 2020
        [250, 300, 350, 400, 450, 500]   # Data for 2021
    ]

    # Create a list of traces for each year
    traces = []
    for i in range(len(years)):
        trace = go.Scatter(
            x=months,
            y=data[i],
            mode='lines+markers',
            name=str(years[i])
        )
        traces.append(trace)

    # Create the layout
    layout = go.Layout(
        title='Comparison of Data by Month',
        xaxis=dict(title='Month'),
        yaxis=dict(title='Data')
    )

    # Create the figure and plot it
    fig = go.Figure(data=traces, layout=layout)
    st.plotly_chart(fig)
