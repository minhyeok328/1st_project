# TCO Insight

차량 제원과 주행 조건을 바탕으로 연료비·자동차세·정비비를 월간·연간 비용으로 계산하는 Streamlit 프로젝트입니다.

## 프로젝트 소개

차량 구매 가격만으로는 보유 중 반복해서 발생하는 비용을 비교하기 어렵습니다. TCO Insight는 차량별 연비, 배기량, 소모품 교체 주기와 사용자가 입력한 주행거리를 결합해 운영비의 구성과 규모를 보여줍니다.

차량 제원과 가격은 저장된 CSV를 MySQL에 적재해 조회합니다. 연료 단가는 오피넷 조회 결과 또는 코드의 대체 단가를 사용하며 전기는 고정 단가입니다. 산출값은 동일 조건에서 운영비를 살펴보기 위한 추정치입니다. 구매비·보험료·금융비용·감가상각을 모두 포함한 전체 보유비용은 아닙니다.

## 주요 기능

| 기능 | 설명 |
| --- | --- |
| 차량 검색 | 모델명으로 검색하고 연비 등급·출시연도로 결과를 좁힙니다. |
| 제원·가격 확인 | 복합·도심·고속도로 효율과 가격 범위를 확인합니다. |
| 주행 조건 설정 | 주행 패턴과 월간 예상 주행거리를 입력합니다. |
| 정비비 조정 | 배기량 구간별 기본 부품 단가를 불러오고 금액을 수정합니다. |
| 전기차 항목 처리 | 전기차의 엔진 관련 정비 항목 네 가지를 제외합니다. |
| 비용 합산 | 연료비·자동차세·정비비와 월간·연간 합계를 표시합니다. |

## 사용 흐름

1. 모델명을 입력하고 차량 사양을 조회합니다.
2. 검색 결과에서 세부 모델과 가격 정보를 선택합니다.
3. 주행 패턴과 월간 주행거리를 정합니다.
4. 부품별 기본 단가와 예상 교체 시기를 확인하고 금액을 조정합니다.
5. 결과 버튼을 눌러 항목별 비용과 합계를 확인합니다.

![운영비 계산 결과](images/ui_result.png)

저장소에 보관된 화면 예시입니다. 실제 결과는 DB 데이터와 입력 조건에 따라 달라집니다.

## 기술 구성

| 영역 | 기술·구성 |
| --- | --- |
| 화면·계산 | Python, Streamlit, pandas |
| 저장소 | MySQL, mysql-connector-python |
| 데이터 수집 | requests, Beautiful Soup, urllib, XML 파싱 |
| 설정 | python-dotenv |
| 데이터 | 차량 연비 CSV, 가격 CSV, 정비 기준 SQL |

화면과 계산은 하나의 Python 프로세스에서 실행됩니다. 별도 REST 서버나 학습 모델은 없습니다.

## 프로젝트 구조

```text
1st_project/
├── main.py                 # 화면, 상태, 운영비 계산
├── package_loader.py       # 차량 CSV를 DB에 적재
├── API_Side/               # 차량·가격·유가 수집 모듈
├── DB_Side/                # DB 접근
├── module/                 # CSV 유틸리티
├── data/vehicles/          # 차량 연비·가격 CSV
├── database/init/          # 정비 기준 SQL
├── examples/               # 개별 화면 예제
├── assets/                 # 앱 로고
├── images/                 # 화면 예시
└── docs/                   # 개발·구조·계산·검증 문서
```

## 문서 안내

- [개발 문서 전체 안내](docs/README.md)
- [개발 환경](docs/01-getting-started/development-environment.md) · [실행과 운영](docs/01-getting-started/run-and-operations.md)
- [시스템 구조](docs/02-architecture/system-architecture.md) · [DB 스키마](docs/05-database/schema-and-erd.md)
- [계산 모델](docs/07-ai-modeling/README.md) · [검증과 제한 사항](docs/10-quality/verification-and-limitations.md)

## 원본 저장소

[joy-riders/EDA_weather](https://github.com/joy-riders/EDA_weather)
