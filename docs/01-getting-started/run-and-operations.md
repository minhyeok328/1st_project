# 실행과 운영

## 초기 데이터 준비

[개발 환경](development-environment.md)을 준비한 후 프로젝트 루트에서 실행합니다. 아래 초기화는 기존 테이블을 삭제하므로 보존할 데이터가 없는 개발 DB에서 수행합니다.

1. MySQL 클라이언트에 개발 계정으로 접속합니다. 비밀번호는 프롬프트에서 입력합니다.
2. MySQL 클라이언트에서 정비 SQL을 실행합니다. 경로는 실제 체크아웃 위치로 바꿉니다.

```sql
SOURCE C:/MinHyeok/skn26_projects/1st_project/database/init/DBsetup.sql;
```

`tco_system`을 생성하고 `parts`를 삭제·재생성하여 기준값 10개를 넣습니다.

3. 프로젝트 루트에서 차량 CSV를 적재합니다.

```powershell
.\.venv\Scripts\python.exe package_loader.py
```

적재기는 `car_oil` → `car_price` 순으로 삭제하고 가격 → 연비 순으로 생성·적재합니다. 헤더 없는 CSV의 열 순서를 그대로 사용합니다. 완료 메시지는 입력 행 수를 출력하므로 DB 결과를 별도로 확인합니다.

```sql
SELECT COUNT(*) FROM tco_system.parts;
SELECT COUNT(*) FROM tco_system.car_price;
SELECT COUNT(*) FROM tco_system.car_oil;
```

현재 파일 기준 예상치는 각각 10, 268, 506입니다. 수정 데이터가 있다면 재적재 전에 백업이 필요합니다.

## 화면 실행

```powershell
.\.venv\Scripts\python.exe -m streamlit run main.py
```

터미널에 표시되는 로컬 주소에 접속합니다. 프로젝트 루트 외의 위치에서 실행하면 로고 상대경로를 찾지 못할 수 있습니다. 종료는 실행 터미널의 Ctrl+C입니다.

## 장애 확인

| 증상 | 확인 내용 |
| --- | --- |
| 검색 결과 없음 | DB 연결 오류도 빈 목록이 되므로 로그·테이블·검색어를 함께 확인 |
| 일부 차량 적재 실패 | 중복 기본키, 작은따옴표, 가격 외래키와 로그 확인 |
| 부품 표 없음 | `parts` 테이블과 캐시 확인 |
| 유가 실패 | 키 설정·외부 연결 확인; 대체 단가로 계속 계산될 수 있음 |
| 수치 변환·나눗셈 오류 | 연비 문자열·0 연비·0 교체주기 확인 |
| 단가 변경 미반영 | `st.cache_data` 캐시 초기화 또는 앱 재시작 후 확인 |

이 문서 정리에서는 DB 초기화·적재·앱 실행·네트워크 요청을 수행하지 않았습니다.

[검증과 제한 사항](../10-quality/verification-and-limitations.md) · [문서 목록](../README.md)
