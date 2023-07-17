#import urllib.request
#After some tests this method is better than a requests.get
#urllib.request.urlretrieve("https://repositorio.ul.pt/bitstream/10451/55944/1/ulflsmcreis_tm.pdf", "random_string.pdf")


import pandas as pd

import streamlit as st
from PIL import Image

#image = Image.open('1.png')
#st.image(image)
#st.title("VetVisita")
#st.write("Veterinária ao domicílio ")
#st.write("Whatsapp 919595959595 ")
#st.write("Instagram @VetVisita ")


#age = st.slider('How old are you?', 0, 130, 25)
#st.write("I'm ", age, 'years old')


#import streamlit as st
#import pandas as pd
#import numpy as np

#chart_data = pd.DataFrame(
#    np.random.randn(20, 3),
#    columns=['a', 'b', 'c'])

#st.line_chart(chart_data)




#fig = go.Figure(
#    data=[go.Bar(y=list(df.columns))],
#    layout_title_text="A Figure Displayed with fig.show()"
#)


#st.line_chart(df)
#print(list(df['Month']))
#print(list(df['Visits'][1:]))
#list_values = [ int(x) for x in df['Visits'][1:] ]
#import plotly.express as px
#fig = px.bar(x=df['Month'][1:], y = df['Visits'][1:])

import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from urlextract import URLExtract
import plotly.graph_objects as go


# Import Module
import PyPDF2
from PyPDF2.utils import PdfReadError



def run_sentiment_analysis(text):
    # Initialize the sentiment analyzer
    sid = SentimentIntensityAnalyzer()

    # Perform sentiment analysis
    sentiment_scores = sid.polarity_scores(text)

    # Interpret the sentiment scores
    if sentiment_scores['compound'] >= 0.05:
        sentiment = 'Positive'
    elif sentiment_scores['compound'] <= -0.05:
        sentiment = 'Negative'
    else:
        sentiment = 'Neutral'

    # Return the sentiment and sentiment scores
    return sentiment, sentiment_scores

# Extract URLs from text
def extract_urls(text):
    extractor = URLExtract()
    urls = extractor.find_urls(text)
    for url in urls:
        url = url.replace(",", "")
        if "http" in url:
            url = url[url.find('http'):]
        if url not in list_urls:
            list_urls.append(url)

def pdf_url(pdfFileObject):
  
    pdfReader = PyPDF2.PdfFileReader(pdfFileObject)

    # Iterate through all pages
    for page_number in range(pdfReader.numPages):
         
        pageObject = pdfReader.getPage(page_number)
        
        # Extract text from page
        pdf_text = pageObject.extractText()

        extract_urls(pdf_text)

#import streamlit as st

#list_urls = []

#txt = st.text_area('Extract URLs from Text', '''Example''')

#st.write('Sentiment:', run_sentiment_analysis(txt))

#st.write('PDF URL:', extract_urls(txt))

#uploaded_file = st.file_uploader("Choose a file")

#pdf_url(uploaded_file)

#st.write('PDF URL:', list_urls)

import streamlit as st
import PyPDF2
import re


def extract_urls_from_pdf(pdf_file):
    urls = []
    pdf_reader = PyPDF2.PdfFileReader(pdf_file)
    num_pages = pdf_reader.numPages

    for page_num in range(num_pages):
        page = pdf_reader.getPage(page_num)
        content = page.extractText()

        # Use regular expression to find URLs
        pattern = r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+"
        extracted_urls = re.findall(pattern, content)

        urls.extend(extracted_urls)

    return urls


def main():

    
    image = Image.open('2.png')
    st.image(image)
    st.title("PDF URL Extractor")
    st.write("Upload a PDF file to extract URLs.")

    uploaded_file = st.file_uploader("Choose a PDF file", type=["pdf"])

    if uploaded_file:
        if st.button("Extract URLs"):
            urls = extract_urls_from_pdf(uploaded_file)
            st.write("Extracted URLs:")
            for url in urls:
                st.write(url)


#if __name__ == "__main__":
#    main()

#st.set_page_config(layout="wide")
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


#cat Roteiro.cdxj | cut -d ')' -f 1 | uniq -c
