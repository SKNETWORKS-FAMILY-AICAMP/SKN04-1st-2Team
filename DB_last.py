import psycopg2
import requests
import json
import elcet_car_crawling

# PostgreSQL 데이터베이스에 연결
conn = psycopg2.connect(
    host='localhost',
    dbname='postgres',
    user='postgres',
    password='7276',
    port=5432
)

# 테이블 생성 및 데이터 삽입
with conn.cursor() as cur:
    # years 테이블 생성 // 연도별 코드
    cur.execute('''
        CREATE TABLE IF NOT EXISTS years (
            year_id SERIAL PRIMARY KEY,
            year VARCHAR(6) UNIQUE
        )
    ''')

    # locations 테이블 생성 // 지역별 코드
    cur.execute('''
        CREATE TABLE IF NOT EXISTS locations (
            location_id SERIAL PRIMARY KEY,
            location_name VARCHAR(50) UNIQUE
        )
    ''')

    # data 테이블 생성 // 전기차
    cur.execute('''
        CREATE TABLE IF NOT EXISTS data (
            id SERIAL PRIMARY KEY,
            year_id INT REFERENCES years(year_id),
            location_id INT REFERENCES locations(location_id),
            value INT
        )
    ''')

    # total_car 테이블 생성 // 전기차, 일반차 연도별 합
    cur.execute('''
        CREATE TABLE IF NOT EXISTS total_car(
            year_id INT PRIMARY KEY REFERENCES years(year_id),
            total_count INT,
            common_total_count INT
        )
    ''')

    # data_common 테이블 생성 // 전체 차
    cur.execute('''
        CREATE TABLE IF NOT EXISTS data_common (
            id SERIAL PRIMARY KEY,
            year_id INT REFERENCES years(year_id),
            location_id INT REFERENCES locations(location_id),
            vehicle_count BIGINT
        )
    ''')

    conn.commit()

# 전기차 등록 현황
electric_car_last_count = elcet_car_crawling.electric_car_crawling()

# 전체 차량 등록 현황
with open('col2.txt', 'r',encoding='UTF8') as file:
    lines_list = [line.strip().split() for line in file]

total = []
locations2 = lines_list[0][:-3]
list_ = ['2011-12', '2012-12', '2013-12', '2014-12', '2015-12', '2016-12', '2017-12', '2018-12', '2019-12', '2020-12', '2021-12', '2022-12', '2023-12', '2024-02']
for i in range(1, len(lines_list)):
    if lines_list[i][0] in list_:
        lines_list[i][0] = lines_list[i][0].replace('-', '')
        total.append(lines_list[i][:-1])

# 지역 리스트
locations = ['서울', '부산', '대구', '인천', '광주', '대전', '울산', '세종', '경기', '강원', '충북', '충남', '전북', '전남', '경북', '경남', '제주']

# locations 테이블
with conn.cursor() as cur:
    for location in locations:
        cur.execute('''
            INSERT INTO locations (location_name) VALUES (%s) ON CONFLICT (location_name) DO NOTHING RETURNING location_id
        ''', (location,))
    conn.commit()

# years, data 테이블
with conn.cursor() as cur:
    for row in electric_car_last_count:
        year = row[0]

        cur.execute('''
            INSERT INTO years (year) VALUES (%s) ON CONFLICT (year) DO NOTHING RETURNING year_id
        ''', (year,))
        year_id = cur.fetchone()[0] if cur.rowcount > 0 else None

        for i, location in enumerate(locations):
            value = row[i + 1]

            # location_id 가져오기
            cur.execute('SELECT location_id FROM locations WHERE location_name = %s', (location,))
            location_id = cur.fetchone()[0]

            cur.execute('''
                INSERT INTO data (year_id, location_id, value) VALUES (%s, %s, %s)
            ''', (year_id, location_id, value))

    conn.commit()

# total_car 테이블
with conn.cursor() as cur:
    cur.execute('SELECT year_id FROM years')
    years = cur.fetchall()

    for year_id, in years:
        cur.execute('''
            SELECT SUM(value) FROM data WHERE year_id = %s
        ''', (year_id,))
        total_count = cur.fetchone()[0]

        cur.execute('''
            INSERT INTO total_car (year_id, total_count)
            VALUES (%s, %s)
        ''', (year_id, total_count))

    conn.commit()

# data_common 테이블
with conn.cursor() as cur:
    for row in total:
        year = row[0]

        cur.execute('SELECT year_id FROM years WHERE year = %s', (year,))
        year_id = cur.fetchone()[0]

        for i, location in enumerate(locations):
            vehicle_count = int(row[i + 1].replace(',', ''))

            cur.execute('SELECT location_id FROM locations WHERE location_name = %s', (location,))
            location_id = cur.fetchone()[0]

            cur.execute('''
                INSERT INTO data_common (year_id, location_id, vehicle_count)
                VALUES (%s, %s, %s)
            ''', (year_id, location_id, vehicle_count))

    conn.commit()

# data_common 테이블의 합 total_car에 추가
with conn.cursor() as cur:
    for year_id, in years:
        cur.execute('''
            SELECT SUM(vehicle_count) FROM data_common WHERE year_id = %s
        ''', (year_id,))
        common_total_count = cur.fetchone()[0]

        cur.execute('''
            UPDATE total_car
            SET common_total_count = %s
            WHERE year_id = %s
        ''', (common_total_count, year_id))

    conn.commit()

conn.close()
