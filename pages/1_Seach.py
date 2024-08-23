import streamlit as st
import pandas as pd

st.title('지역별 전기차 승용차 등록 현황 비교')

conn = st.connection('postgresql',type='sql')

load_elect_table = conn.query('SELECT * FROM data a JOIN years b ON a.year_id = b.year_id JOIN locations e ON e.location_id = a.location_id', ttl=600)
load_common_table = conn.query('SELECT * FROM data_common c JOIN years d ON c.year_id = d.year_id JOIN locations e ON e.location_id= c.location_id' , ttl=600)
#load_elect_table['year'] = load_elect_table['year'].str[:4]

load_elect_table = load_elect_table.drop('year_id', axis = 1)
load_elect_table = load_elect_table.drop('location_id', axis = 1)
load_common_table = load_common_table.drop('year_id', axis = 1)
load_common_table = load_common_table.drop('location_id', axis = 1)

location = ['서울', '부산', '대구', '인천', '광주', '대전', '울산', '세종', '경기', '강원', '충북', '충남', '전북', '전남', '경북', '경남', '제주']
choice = st.selectbox('자료를 열람할 지역을 선택하세요',location)

if choice:
    location_table_ = pd.DataFrame({'year':load_elect_table[load_elect_table['location_name']==f'{choice}']['year'].str[0:4],
                                    f'{choice}의 전기차 수':load_elect_table[load_elect_table['location_name']==f'{choice}']['value']})
    location_table_ = location_table_.set_index('year')
    location_table_ = location_table_.sort_index(ascending=True)
 

    show_common_table = pd.DataFrame({'year':load_common_table[load_common_table['location_name']==f'{choice}']['year'].str[0:4],
                                    f'{choice}의 승용차 수':load_common_table[load_common_table['location_name']==f'{choice}']['vehicle_count']})
    show_common_table = show_common_table.set_index('year')

    join_table = show_common_table.join(location_table_)
    
    st.line_chart(join_table)
    
    with st.expander('테이블 보기'):
        st.table(location_table_)
        st.table(show_common_table)

