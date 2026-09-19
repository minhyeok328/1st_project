# 배포

## 제공 구성

실행 진입점은 Streamlit `main.py`입니다. Dockerfile·Compose·호스팅 설정·자동 배포·고정 의존성 파일은 없습니다. 저장소만으로 공개 서비스의 현재 운영 상태를 확인할 수 없습니다.

## 실행 환경 조건

Python 3.12 이상, 필요한 Streamlit API를 지원하는 의존성, MySQL의 세 테이블, 로고·CSV 경로, 외부 이미지·유가 네트워크, 런타임 인증 설정이 필요합니다.

DB는 `localhost:3306`에 고정되어 있습니다. 앱을 컨테이너나 다른 서버로 옮기려면 DB 주소 설정 방식을 먼저 조정해야 합니다. 임의의 환경 변수만 추가해서 원격 DB에 연결할 수는 없습니다.

## 운영 전 확인

검색 SQL 문자열 조합, 수치 검증, 요청 timeout, 유가 대체값 표시, 버전 재현성을 해결하고 [검증 항목](../10-quality/verification-and-limitations.md)을 확인해야 합니다. 인증·접근 제어·모니터링·백업 복구 자동화는 현재 구현에 없습니다.

`package_loader.py`와 `DBsetup.sql`은 테이블을 재생성하므로 매 시작마다 실행하는 일반 운영 명령으로 사용하지 않습니다.

[실행과 운영](../01-getting-started/run-and-operations.md) · [문서 목록](../README.md)
