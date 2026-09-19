# 서버 내부 처리

별도 백엔드 서버는 없으며 Streamlit 서버 프로세스에서 DB와 유가 함수를 호출합니다.

## DB 접근

`DBLoader.sendquery(query)`는 연결·커서를 열고 SQL을 실행한 뒤 `fetchall()`을 반환합니다. MySQL 오류는 표준 출력에 기록하고 빈 목록으로 바꾸므로 조회 결과 없음과 DB 장애가 같은 형태로 전달됩니다.

`sendquerys_with_commit(querys)`는 한 연결에서 쿼리 목록을 실행하고 마지막 COMMIT을 수행합니다. 적재기는 INSERT 목록을 전달합니다. 테이블 삭제·생성은 별도 호출이므로 전체 적재가 하나의 원자적 교체는 아닙니다.

`db_search(table_name, user_input)`는 테이블명과 검색어를 SQL에 직접 넣습니다. 매개변수 바인딩이나 테이블 허용 목록 검사는 없습니다.

## 계산 연결

`get_maintenance_db(displacement, monthly_km)`는 부품 기준을 조회하여 배기량별 가격과 교체 예상 개월을 DataFrame으로 만듭니다. 캐시 키에는 입력이 포함되지만 DB 갱신 시각은 포함되지 않습니다.

최종 합산은 `main.py`의 결과 버튼 조건문 안에 있습니다. 독립된 계산 서비스나 결과 저장 테이블은 없습니다. 산식을 수정할 때 단위·요약·내역 표를 함께 확인합니다.

[인터페이스](../06-api/api-reference.md) · [계산 모델](../07-ai-modeling/README.md) · [문서 목록](../README.md)
