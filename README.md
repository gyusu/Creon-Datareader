# Creon-Datareader
대신증권의 HTS인 CREON의 Plus API를 사용하여 주가 데이터를 받아오는 PyQt 기반의 프로그램입니다.

데이터를 받아오는 기능만 구현하려한 것이 아니기때문에, 재사용성과 확장성을 염두에 두고 개발하였습니다.
프로그램 기능을 확장할 예정이므로 binary file로 배포하지 않습니다.


## 실행 / 개발 환경

우선 [CREON Plus] 공식 웹사이트를 참고하여 계좌 개설 및 HTS 설치 등의 절차를 진행하여야 합니다.
[CREON Plus]:http://money2.creontrade.com/e5/mboard/ptype_basic/plusPDS/DW_Basic_Read.aspx?boardseq=299&seq=35&page=1&searchString=&prd=&lang=8&p=8833&v=8639&m=9505

1. Anaconda 32-bit 설치
	만약 Anaconda 64-bit을 사용하고 있는 경우
    - 32-bit도 설치 또는,
    - `set CONDA_FORCE_32BIT`을 이용하여 32-bit 가상환경을 만들어야 합니다.
2. 32-bit anaconda `python=3.6` 가상환경에서
	`conda install`을 이용하여 `pyqt5`, `sqlite3`, `pandas`, `pywin32` 설치
    `conda install`이 안되는 경우 `pip`로 설치하시면 됩니다.
---

##### **데이터 제한** (18.02.23 기준)
	이 프로그램은 일봉, 분봉의 데이터만 받도록 구현되어있습니다.
	Creon Plus API에서 현재
	1분봉 약 18.5만개(약 2년치 데이터) 조회 가능
	5분봉 약 9만개(약 5년치 데이터) 조회 가능

