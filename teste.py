st.set_page_config(layout="wide", page_title="Arquivo.pt em números", page_icon=":chart:")

st.markdown("<div style='text-align: center;'><img src='https://arquivo.pt/img/arquivo-logo-white.svg'></div>", unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center;'>em números</h1>", unsafe_allow_html=True)


#Add image
#col1, col2 = st.columns(2)
#with col1:
#    image = Image.open('1.png')
#    st.image(image)

#with col2:
#    st.title("Arquivo.pt em números")


#Load the data from the dataframe
colnames=['Year', 'January - April Size', 'May - August Size', 'September - December Size', 'Total Year Size', 'January - April Nr Collections', 'May - August Nr Collections', 'September - December Nr Collections', 'Total Year Nr Collections'] 
df = pd.read_csv("1.csv", sep=',', names=colnames, header=None)

#Prepare your data
categories = df['Year'][1:]
heights = df['Total Year Size'][1:].astype(int)


#Create a bar chart object
bar_chart = go.Bar(x=categories, y=heights)

#Create a figure and add the bar chart object
fig1 = go.Figure()
fig1.add_trace(bar_chart)

#Customize the chart (optional)
fig1.update_layout(
    title='Total stored (TB) per year',
    xaxis_title='Year',
    yaxis_title='Total stored (TB)'
    )

#st.plotly_chart(fig)

df['Cumulative'] = df['Total Year Size'][1:].astype(int).cumsum()
print(df['Cumulative'])
# Step 4: Create a bar chart object
bar_chart = go.Bar(x=categories, y=df['Cumulative'])

# Step 5: Create a figure and add the bar chart object
fig2 = go.Figure()
fig2.add_trace(bar_chart)

# Step 6: Customize the chart (optional)
fig2.update_layout(
    title='Total stored (TB) per year cumulative',
    xaxis_title='Year',
    yaxis_title='Total stored (TB)'
)

#st.plotly_chart(fig)

col1, col2 = st.columns(2)

with col1:
    st.plotly_chart(fig1)

with col2:
    st.plotly_chart(fig2)

#########################################################################################################


# Step 3: Prepare your data
categories = df['Year'][1:]
heights = df['Total Year Nr Collections'][1:].astype(int)

# Step 4: Create a bar chart object
bar_chart = go.Bar(x=categories, y=heights)

# Step 5: Create a figure and add the bar chart object
fig3 = go.Figure()
fig3.add_trace(bar_chart)

# Step 6: Customize the chart (optional)
fig3.update_layout(
    title='Total nr collections per year',
    xaxis_title='Year',
    yaxis_title='Nr collections'
    )

#st.plotly_chart(fig3)

df['Cumulative'] = df['Total Year Nr Collections'][1:].astype(int).cumsum()
print(df['Cumulative'])
# Step 4: Create a bar chart object
bar_chart = go.Bar(x=categories, y=df['Cumulative'])

# Step 5: Create a figure and add the bar chart object
fig4 = go.Figure()
fig4.add_trace(bar_chart)

# Step 6: Customize the chart (optional)
fig4.update_layout(
    title='Total nr collections per year cumulative',
    xaxis_title='Year',
    yaxis_title='Nr collections'
)

#st.plotly_chart(fig4)

col1, col2 = st.columns(2)

with col1:
    st.plotly_chart(fig3)

with col2:
    st.plotly_chart(fig4)

# Add a sidebar for the 'Year' field
#selected_year = st.sidebar.selectbox('Select Year', df['Year'])

# Filter the data based on the selected year
#filtered_df = df[df['Year'] == selected_year]

# Display the filtered data
#st.write(filtered_df)

# Sample data for demonstration
cities = ['youtube.com', 'farm4.static.flickr.com', 'google.com', '2-bp.blogspot.com', '3-bp.blogspot.com']
population = [2347260, 343767, 341582, 300851, 300636]

# Sort the cities based on population in descending order
sorted_data = sorted(zip(population, cities))
population, cities = zip(*sorted_data)

# Create a horizontal bar chart using Plotly
fig = go.Figure(data=go.Bar(y=cities, x=population, orientation='h'))

# Customize the chart layout
fig.update_layout(
    title='Top 5 domains in Arquivo.pt',
    xaxis_title='Nr URLs',
    yaxis_title='Domains'
)

st.plotly_chart(fig)
