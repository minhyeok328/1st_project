# 개발 환경

## 준비물

- Python 3.12 이상을 기준으로 준비합니다. `main.py`의 같은 따옴표를 중첩한 f-string 구문은 이전 버전에서 구문 오류가 날 수 있습니다.
- 로컬 MySQL과 DB 생성·조회·적재 권한이 있는 개발용 계정이 필요합니다.
- `assets/logo.png`, `data/vehicles`의 CSV 두 개와 정비 기준 SQL을 준비합니다.
- 유가 조회에는 네트워크와 `OPINET_API_KEY`가 필요합니다. 키가 없으면 실패값을 반환하고 화면은 대체 단가를 사용합니다.

## 패키지 설치

저장소에는 requirements·pyproject·잠금 파일이 없습니다. 다음은 실제 import에 대응하는 설치 예시이며 검증된 고정 버전 조합은 아닙니다. 프로젝트 루트에서 실행합니다.

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\python.exe -m pip install streamlit pandas mysql-connector-python python-dotenv requests beautifulsoup4
```

XML·CSV·URL 처리는 표준 라이브러리를 사용합니다. 다른 환경의 재현을 위해 실제 사용한 패키지 버전을 별도로 기록해야 합니다.

## 환경 변수

루트의 로컬 `.env` 또는 프로세스 환경에 아래 이름을 설정합니다. 값은 문서에 기록하지 않습니다. `.env`는 Git 제외 대상입니다.

| 이름 | 읽는 위치 | 용도 |
| --- | --- | --- |
| `DB_USER` | `DB_Side/DBLoader.py` | DB 사용자 |
| `DB_PASSWORD` | `DB_Side/DBLoader.py` | DB 인증 |
| `OPINET_API_KEY` | `API_Side/OilPrice.py` | 유가 조회 |
| `CAR_ID` | `API_Side/CarOil.py` | 별도 차량 수집 모듈 |

DB 호스트 `localhost`, 포트 `3306`, DB명 `tco_system`은 소스에 고정됩니다. `DB_HOST` 같은 변수를 추가해도 현재 코드는 읽지 않습니다.

차량 수집 모듈의 요청 URL과 일부 인증 구성이 소스에 고정되어 있습니다. `CAR_ID` 헤더 설정만으로 모든 인증 구성이 바뀌지는 않습니다. 실제 값을 출력하거나 문서에 옮기지 말고 재수집 전에 설정 방식을 확인합니다. 제공 CSV를 이용한 앱 실행과 외부 데이터 재수집을 구분합니다.

[실행과 운영](run-and-operations.md) · [문서 목록](../README.md)
