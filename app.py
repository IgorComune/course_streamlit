import pandas as pd
import streamlit as st
from PIL import Image
import numpy as np
import plotly.express as px

# config streamlit page
st.set_page_config(page_title='Title', 
                   layout='wide', 
                   initial_sidebar_state='collapsed')

def main():
    st.sidebar.success('Menu')
    # basics
    st.title('Hello World')
    st.text('Text')
    st.text('Test2')
    st.header('Header')
    st.subheader('SubHeader')
    st.markdown('#### Markdown')
    st.success('Succesful')
    st.warning('Danger')
    st.info('Information')
    st.error('Arrow')
    st.exception('Exception')
    st.write('write')
    st.write('### markdown write')
    
    # displaying data
    df = pd.read_csv(r'.\material\Module01\iris.csv')
    st.dataframe(df, 200, 100)
    st.write(df.head())   
    # st.table(df) full table
    # st.dataframe(df.style.highlight_max(axis=0))
    
    # json
    st.json({'data':'name'})
    
    # code
    st.code("""
            def hello_world():
                print('Hello World')
            """, language='python')
    
    if st.button('submit'):
        st.write('Button')
    if st.button('submit', key='new'):
        st.write('Button')
    
    st.radio('radio buttons', ('a', 'b', 'c'))
    st.checkbox('Show/Hide')
    st.expander('Python')

    # select
    my_lang = ['Python', 'Julia', 'Go', 'Rust']
    choice = st.selectbox('Language', my_lang)
    st.write(choice)
    
    # multi select
    spoken_lang = ('English', 'Spanish', 'French')
    st.multiselect('multi select', spoken_lang)
    
    # slider
    st.slider('Age',1,100)
    
    # slider for any data type
    color = st.select_slider('Choose Color: ',options=['yellow','red', 'blue', 'black', 'white'])
    
    # media files
    st.image('material\Module01\data\image_01.jpg')
    st.video('material\Module01\data\secret_of_success.mp4')
    st.audio('material\Module01\data\song.mp3')
    
    # text iput
    name = st.text_input('Enter you name')
    st.write(name)
    message = st.text_area('Enter you name')
    st.write(message)
    
    # number input
    n = st.number_input('Set a number: ')
    st.write(n)
    
    # date input
    date = st.date_input("Data")
    st.write(date)
    
    # time input
    time = st.time_input('Time')
    st.write(time)
    
    color = st.color_picker('Select color')
    
    # plotly dataviz
    df = pd.read_csv('material\Module01\data\prog_languages_data.csv')
    st.dataframe(df)
    
    fig = px.pie(df, values='Sum', names='lang')
    st.plotly_chart(fig)
    
    fig2 = px.bar(df, x='lang', y='Sum')
    st.plotly_chart(fig2)
    
if __name__ == '__main__':
    main()