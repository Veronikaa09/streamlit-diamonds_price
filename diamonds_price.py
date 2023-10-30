import pickle 
import streamlit as st 

model = pickle.load(open('diamonds_price.sav', 'rb'))

st.title('Estimasi Harga Diamonds')

carat = st.number_input('Input Jumlah Karat')
depth = st.number_input('Input Jumlah Ketebalan')
table = st.number_input('Input Jumlah Table')
x = st.number_input('Input Jumlah X')
y = st.number_input('Input Jumlah Y')
z = st.number_input('Input Jumlah Z')

predict = ''

if st.button('Harga Diamonds '):
    predict = model.predict(
        [[carat, depth, table, x, y, z]]
    )
    st.write('Harga Diamonds: ', predict)