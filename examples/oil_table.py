import streamlit as st
import pandas as pd
from API_Side.CarOil import apicar

st.session_state["model_name"] = "테슬라"
st.session_state["use_grade"] = True
st.session_state["in_grade"] = "3등급"
st.session_state["use_year"] = True
st.session_state["in_year"] = "2020"

##############################################################################

# 2. API 데이터 호출
# ApiCar 내부의 keys 리스트와 순서가 일치해야 합니다.
columns = [
    "모델명", "제조사", "연료", "표시효율", "도심효율",
    "고속도로효율", "1회충전주행거리", "예상연료비", "등급", "배기량", "연식"
]

search_result = apicar.getdata(st.session_state["model_name"])

#-----------------------------------------------------------------------------------------------------

if not search_result:
    st.warning(f"'{st.session_state['model_name']}'에 대한 검색 결과가 API에 존재하지 않습니다.")
    st.stop() # 이후 코드 실행을 중단합니다.

#-----------------------------------------------------------------------------------------------------

# 3. 데이터 필터링 및 리스트 생성
filtered_data = []
for row in search_result:
    # row[8]이 '등급', row[10]이 '연식' (ApiCar 클래스의 keys 순서 기준)
    if st.session_state["use_grade"] and row[8] != st.session_state["in_grade"]:
        continue
    if st.session_state["use_year"] and str(row[10]) != st.session_state["in_year"]:
        continue

    filtered_data.append(row)

# 4. 표 출력 및 상세 선택
if filtered_data:
    # Pandas DataFrame으로 변환
    df = pd.DataFrame(filtered_data, columns=columns)

    st.subheader(f"'{st.session_state['model_name']}' 검색 결과")

    # 전체 결과를 표로 먼저 보여주기
    st.dataframe(df, use_container_width=True)

    # 셀렉트박스로 특정 모델 상세 선택
    selected_model = st.selectbox(
        "상세 정보를 확인할 모델을 선택하세요",
        df["모델명"].unique()
    )

    # 선택한 모델의 정보만 추출해서 보여주기
    detail_info = df[df["모델명"] == selected_model]
    st.write(f"### 🔍 {selected_model} 상세 정보")
    st.table(detail_info)  # 혹은 st.json(detail_info.to_dict('records')[0])
else:
    st.warning("검색 결과가 없습니다. 필터 조건을 확인해주세요.")