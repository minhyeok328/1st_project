# 인터페이스

외부 클라이언트에 제공하는 REST 엔드포인트는 없습니다. 아래는 Python 함수 인터페이스입니다.

| 함수 | 입력 | 반환·부작용 |
| --- | --- | --- |
| `DBLoader.sendquery(query)` | SQL | 튜플 목록; MySQL 오류 시 `[]` |
| `DBLoader.sendquerys_with_commit(querys)` | SQL 목록 | 행 목록; 마지막 COMMIT; 오류 시 `[]` |
| `DBLoader.db_search(table_name, user_input)` | 테이블·부분 모델명 | LIKE 검색 결과 |
| `CSVModule.csv_import(csv_name)` | UTF-8 경로 | 헤더 구분 없이 튜플 목록 |
| `CSVModule.csv_export(file_name, indata)` | 경로·행 | CSV 쓰기 |
| `CSVModule.csv_merge(file_path1, file_path2)` | 두 CSV | 첫 필드가 새로운 행만 병합 |
| `package_loader.export_table(...)` | 테이블·열 정의·행 | 테이블 재생성·적재 |
| `main.get_maintenance_db(...)` | 배기량·월 거리 | 부품 DataFrame |

## 외부 데이터 수집

`OilPrice.getdata(oil_type)`는 오피넷 `avgAllPrice.do`에 XML을 요청하고 `OIL/PRODNM`이 일치하는 `PRICE`를 float로 반환합니다. 키 없음·오류·일치 항목 없음은 -1.0입니다. 명시적 timeout과 재시도는 없습니다.

`CarPrice.getdata(model)`은 Carisyou 검색 HTML에서 모델명·최저가·최고가·이미지 주소를 추출합니다. `priceparser()`가 가격 문자열을 두 숫자로 분리합니다. HTML 선택자 변경·빈 결과에 대한 처리가 부족합니다. 메인 앱은 이 함수를 호출하지 않습니다.

`CarOil.getdata(model_name)`은 `CAR_ID` 헤더와 검색 파라미터를 구성하고 JSON에서 11개 제원 필드를 추출하도록 작성되었습니다. 요청 URL과 일부 인증 구성이 소스에 고정되어 있습니다. 비200 응답에서는 문자열과 정수 상태 코드의 연결이 실패할 수 있고 `res` 초기화도 보장되지 않습니다. DB CSV의 12번째 필드 `price_model`은 API 반환에 포함되지 않습니다.

인증 값이나 키가 포함된 실제 요청 URL은 문서·로그에 남기지 않습니다.

[서버 내부 처리](../04-backend/README.md) · [문서 목록](../README.md)
