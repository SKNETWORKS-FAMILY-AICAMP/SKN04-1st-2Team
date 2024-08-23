import streamlit as st
from streamlit_option_menu import option_menu

conn = st.connection('postgresql',type='sql')
df = conn.query('SELECT * FROM stack', ttl=600)

#with st.sidebar:
#    choose = option_menu("App Gallery", ["About", "Photo Editing"],
#                         icons=['house', 'camera fill', 'kanban'],
 #                        menu_icon="app-indicator", default_index=0,
 #                        styles={
 #       "container": {"padding": "5!important", "background-color": "#fafafa"},
 #       "icon": {"color": "orange", "font-size": "25px"}, 
 #       "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
 #       "nav-link-selected": {"background-color": "#02ab21"},
 #   }
 #   )

tab1, tab2= st.tabs(['전체조회' , '검색조회'])

with tab1:
    st.title('Title: 전국 자동차 등록 현황')

    st.divider()
    st.write('Hello World')
    st.write(df)
    st.write('데이터 베이스 잘 옮겨서 넣기')


with tab2:
    st.write('종목검색')
    select_code = st.text_input(
    '종목코드를 입력하세요', max_chars=10
    )
    tmp_df = df[df['stock_id']== select_code]
    st.table(tmp_df.head())



st.divider()

st.header('FAQ', divider =True)

with st.expander('Q.1'):
    st.write('여기에 대답 내용을 적으면 된다')

with st.expander('Q.2'):
    st.write('여기에 대답 내용을 적으면 된다')

with st.expander('Q.3'):
    st.write('여기에 대답 내용을 적으면 된다')

with st.expander('Q.4'):
    st.write('여기에 대답 내용을 적으면 된다')