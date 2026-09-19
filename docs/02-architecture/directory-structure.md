# 디렉터리 구조

| 경로 | 역할 |
| --- | --- |
| `main.py` | 실제 진입점; 화면과 계산 전체 |
| `package_loader.py` | 차량 열 정의와 `export_table` |
| `DB_Side/DBLoader.py` | SQL 조회·일괄 실행·모델명 검색 |
| `database/init/DBsetup.sql` | `parts` 스키마와 10개 기준 행 |
| `data/vehicles/car_oil.csv` | 차량 제원 12필드 |
| `data/vehicles/car_price.csv` | 가격·이미지 4필드 |
| `API_Side/CarOil.py` | 차량 API 응답의 11개 제원 필드 추출 |
| `API_Side/CarPrice.py` | Carisyou 검색 페이지 파싱 |
| `API_Side/OilPrice.py` | 오피넷 XML 처리 |
| `module/CSVModule.py` | CSV 읽기·쓰기·첫 필드 기준 병합 |
| `examples/oil_table.py`, `examples/price_table.py` | 개별 표·선택 화면 예제 |
| `assets/logo.png`, `images/` | 앱 로고와 문서 화면 예시 |
| `docs/` | 공통 분류의 개발 문서 |

예제의 `apicar`/`apicarprice` import는 현재 모듈의 정의와 맞지 않습니다. 예제 파일들을 완성된 실행 진입점으로 안내하지 않습니다. 이전 설명의 `physical_file_loader.py`, `DB_Side/CSVModule.py`는 현재 파일 구조에 없습니다. 관계 참고 파일은 [relation_key.xlsx](../references/relation_key.xlsx)에 보관합니다.

[시스템 구조](system-architecture.md) · [문서 목록](../README.md)
