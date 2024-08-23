import streamlit as st
import pandas as pd
import time

st.title('전기차 승용차 등록 현황 비교')
st.divider()
user_input = '''안녕하세요!🚗⚡🔋 🛠️ 🌍 📊 🚘 
우리는 친환경 모빌리티의 미래를 데이터로 그려내는 프로젝트 팀입니다. 
국토교통부 통계누리의 일반 자동차 등록 현황과 charge info의 전기차 등록 현황을 바탕으로, 
우리나라의 자동차 생태계 변화를 분석합니다.

우리의 스트림릿 페이지는 전기차와 일반차의 등록 추이를 비교하여, 
친환경 모빌리티로의 전환 속도를 한눈에 보여줍니다. 
이를 통해 우리는 탄소 배출 감소와 지속 가능한 교통 체계 구축의 진행 상황을 파악할 수 있습니다. 

4명의 팀원이 크롤링, 데이터베이스 구축, 스트림릿 개발을 분담하여, 
복잡한 데이터를 누구나 쉽게 이해할 수 있는 시각적 정보로 변환했습니다. 
우리의 프로젝트는 더 깨끗하고 지속 가능한 미래를 향한 결정을 돕는 데 기여할 것입니다.🌍
'''

placeholder = st.empty()

if user_input:
    typed_text = ""
    for char in user_input:
        typed_text += char
        placeholder.text(typed_text)  # 한글자씩 업데이트
        time.sleep(0.02)  # 타이핑 속도 조절 (0.1초)
conn = st.connection('postgresql',type='sql')

total_car_table = conn.query('SELECT * FROM total_car a LEFT JOIN years b ON a.year_id = b.year_id', ttl=600)



total_car_table['year'] = total_car_table['year'].str[:4]


total_car_table = total_car_table.drop('year_id', axis = 1)
total_car_table.columns = ['전국 전기차 수', '전국 승용차 수', 'year']

st.title('⚡ 전기차 🚗 승용차 등록 현황 비교')

st.divider()



st.line_chart(total_car_table.set_index('year'))