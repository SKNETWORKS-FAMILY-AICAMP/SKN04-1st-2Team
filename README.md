<p align="center">
  <img src="https://private-user-images.githubusercontent.com/174983658/359888401-641c367d-ab91-410f-8687-11624d871d56.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MjQyNDI1MTAsIm5iZiI6MTcyNDI0MjIxMCwicGF0aCI6Ii8xNzQ5ODM2NTgvMzU5ODg4NDAxLTY0MWMzNjdkLWFiOTEtNDEwZi04Njg3LTExNjI0ZDg3MWQ1Ni5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjQwODIxJTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI0MDgyMVQxMjEwMTBaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT02MjNjYTZjNTU1NDI5ZDBlYWE2MmMzNzljMDFjYTM2OGY1YTAzZTNhZmEzNjZmZTk4YmY3NDVmYWRlNGVlYzhjJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCZhY3Rvcl9pZD0wJmtleV9pZD0wJnJlcG9faWQ9MCJ9.iqPkZ71_ZxZ84lH3ucNb1GbMGBZB_kPkc5ztwdNqvk4">
</p>

# SKN04-1st-2Team
## 목차 🐈
  - [팀 소개 ](#팀-소개) 
  - [프로젝트 개요](#프로젝트-개요)
  - [기술스택](#기술스택)
  - [ERD](#erd)
  - [주요 프로시저](#주요-프로시저)
  - [프로젝트 결과](#프로젝트-결과)
  - [한줄 회고](#한줄-회고)

## 팀 소개
### 팀명 : 쌍리김박 팀
### 팀원 소개


|박병헌|이진섭|이시연|김태욱|
|:---:|:---:|:---:|:---:|
|<img src="https://i.namu.wiki/i/th5M0fN833rYrn-Gqn3zFnu6iBmKLktgYb0GUaeqaON15MWKmPdWSUIWJt-4VoPmBGjmIGCGCPEm9UpdkpBTzwL0zITO2JuqOAY-Q_wFfy-RznlA56Ka8SteyOuIcXaDCu4fZdg971Z7qrmBbEjPwg.webp" width="150" height="150"/>|<img src="https://postfiles.pstatic.net/MjAxOTAzMjlfMjEx/MDAxNTUzNzkxNDAxOTYx.RtpW2iMudAEJl2aWlSeJjgmopo8rqnRfW7pTi5VjF8kg.6MtlTJLwURN-2Jy8TGYX3QV-QOeqRV2z_QrCRx9aVwYg.JPEG.sssss747/SE-dd1f2bcc-9a2c-41c1-ade6-1d977c8b3cf8.jpg?type=w3840" width="150" height="150"/> |<img src="https://media.discordapp.net/attachments/1273954886563922033/1276338408205189192/KakaoTalk_20240823_093257123.jpg?ex=66c92a45&is=66c7d8c5&hm=83915cdc0756d7c60f3bf1c0fdc90881d7d67ab91fdc7bb708281a2c2c4b563b&=&format=webp&width=409&height=545" width="150" height="150"/> | <img src="https://avatars.githubusercontent.com/u/174983658?s=400&u=5f1662f95ced679e306eeca0c47b6da33aed1f8f&v=4" width="150" height="150"/> |
|[@BH1107](https://github.com/BH1107)|[@jururuj](https://github.com/jururuj)|[@lotusflwrr](https://github.com/lotusflwrr)|[@Taeuk-Dog](https://github.com/Taeuk-Dog)|
|**Project Leader**<br/>Streamlit|Database|Crawling|Database|


##  프로젝트 개요
>### 개발 기간 
2024-08-21 ~ 2024-08-23
>### 프로젝트 명 
전국 자동차 등록 현황 및 기업 FAQ 조회시스템

>### 프로젝트 소개
&nbsp;안녕하세요!🚗⚡🔋 🛠️ 🌍 📊 🚘 
우리는 친환경 모빌리티의 미래를 데이터로 그려내는 프로젝트 팀입니다. 
국토교통부 통계누리의 상용 자동차 등록 현황과 charge info의 전기차 등록 현황을 바탕으로, 
대한민국 자동차 생태계의 변화를 깊이 있게 분석하고 있습니다.

&nbsp;우리의 스트림릿 페이지는 전기차와 상용차의 등록 추이를 비교하여, 
친환경 모빌리티로의 전환 속도를 한눈에 보여줍니다. 

&nbsp;4명의 팀원이 크롤링, 데이터베이스 구축, 스트림릿 개발을 분담하여, 
복잡한 데이터를 누구나 쉽게 이해할 수 있는 시각적 정보로 변환했습니다. 
데이터에 기반한 통찰력을 통해 교통과 환경의 미래를 함께 만들어 나가고자 합니다.

>### 프로젝트 필요성
&nbsp; 우리의 프로젝트는 정책 입안자, 환경 운동가, 그리고 일반 시민들에게 중요한 인사이트를 제공하여 더 깨끗하고 지속 가능한 미래를 위한 결정을 지원하는 데 기여할 것입니다. 🌍 전 세계적으로 기후 변화와 대기 오염 문제가 심각해지면서, 교통 부문의 탈탄소화는 필수적인 과제로 부각되고 있습니다. 전기차는 내연기관 자동차에 비해 이산화탄소와 미세먼지 배출을 획기적으로 줄일 수 있는 친환경적인 대안으로, 이러한 변화는 제조업체, 공급망, 정비업체 등 다양한 산업 생태계에 중대한 영향을 미치고 있습니다.

&nbsp;자동차 산업은 내연기관에서 전기차로의 전환이라는 커다란 변화를 겪고 있으며, 전기차와 상용차의 등록 데이터를 통해 이러한 시장 변화를 명확하게 이해할 수 있습니다. 이를 바탕으로 관련 산업이 변화에 어떻게 대응해야 할지 전략을 수립하는 데 유용한 인사이트를 제공하며, 전기차 보급 현황을 분석하고 이해하는 것은 우리 사회의 지속 가능한 발전을 위한 중요한 첫걸음이 될 것입니다.

>### 프로젝트 목표 
- **기능1**: 연도별, 지역별 내연기관 자동차 등록량 추이를 볼 수 있습니다.
- **기능2**: 연도별 전기 자동차 등록량 추이를 볼 수 있습니다. 
- **기능3**: 필요한 기업 FAQ를 조회할 수 있습니다.



##  기술스택

 **Envionment**

<img src="https://img.shields.io/badge/git-F05032?style=for-the-badge&logo=git&logoColor=white">
<img src="https://img.shields.io/badge/Visual Studio-5C2D91?style=for-the-badge&logo=Visual Studio&logoColor=white"/>
<img src="https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=Docker&logoColor=white"/>

 **Development**

   <img src="https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white">
   <img src="https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=white">

 **Database**

 <img src="https://img.shields.io/badge/PostgreSQL-4169e1?style=for-the-badge&logo=PostgreSQL&logoColor=white">
 
 **Test automation tool**

 <img src="https://img.shields.io/badge/Selenium-43B02A?style=for-the-badge&logo=Selenium&logoColor=white"/>

 
<hr>

### Usage

```cmd
streamlit run main.py
```


## ERD
<img src="https://media.discordapp.net/attachments/1273954886098358295/1276372185820168285/Screenshot_2024-08-23_at_11.47.16_AM.png?ex=66c949ba&is=66c7f83a&hm=d381fd15713d307d6e69b267bf5e9fa2f1888ba1076da474bd28b5b8b8bf6a2e&=&format=webp&quality=lossless&width=766&height=671" width="700" height="500"/>


## 주요 프로시저


<img src="https://media.discordapp.net/attachments/1273954886563922038/1276371522730197083/image.png?ex=66c9491c&is=66c7f79c&hm=7902ec0df803752f353ea5652e3dc367addfa0d0ad89b5875381dac3c4de8cc0&=&format=webp&quality=lossless&width=550&height=293" width="700" height="400"/>


##  프로젝트 결과
| 지역별 전기차 승용차 등록 현황 비교 | 지역별 전기차 수 | 
|--|--|
| <img src="https://media.discordapp.net/attachments/1273954886563922033/1276418809908957194/2024-08-23_145152.png?ex=66c97526&is=66c823a6&hm=7d0fb920072de630ba8de24e35ee63d941d37fa746a46485ac18337c9d9079d9&=&format=webp&quality=lossless&width=720&height=435" width="300" height="300"/> | <img src="https://media.discordapp.net/attachments/1273954886098358295/1276361622910275688/Screenshot_2024-08-23_at_11.04.31_AM.png?ex=66c93fe4&is=66c7ee64&hm=718ec59cd1faf338e44cd9d0290f416acb35d8eb4698f5e76b2c00db09192266&=&format=webp&quality=lossless&width=898&height=671" width="300" height="300"/>|
| 지역별 승용차 수 | FAQ 조회 시스템 |
| <img src="https://media.discordapp.net/attachments/1273954886098358295/1276361622910275688/Screenshot_2024-08-23_at_11.04.31_AM.png?ex=66c93fe4&is=66c7ee64&hm=718ec59cd1faf338e44cd9d0290f416acb35d8eb4698f5e76b2c00db09192266&=&format=webp&quality=lossless&width=898&height=671" width="300" height="300"/> |<img src="https://media.discordapp.net/attachments/1273954886098358295/1276362162276667525/Screenshot_2024-08-23_at_11.07.26_AM.png?ex=66c94065&is=66c7eee5&hm=dd53cfb424b64aad8c1ef5bebabba8dc0b751c806e276527b74b07d792fb7b64&=&format=webp&quality=lossless&width=719&height=671" width="300" height="300"/>
<br>

##   한줄 회고 
처음 진행하는 프로젝트로서 쉽지 않았지만, 좋은 팀원을 만나 무사히 마무리할 수 있었다.