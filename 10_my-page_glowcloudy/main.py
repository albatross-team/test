import streamlit as st

st.title('F1 퀄리파잉 top5 기록 비교')
st.header('퀄리파잉')

my_site = st.text_input('오늘 내가 만들어보고 싶은 사이트는?!')
st.write(my_site)

if st.button(f'{my_site} 접속하기'):
    st.success(f'{my_site} 접속 중')