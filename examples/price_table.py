import streamlit as st
from API_Side.CarPrice import apicarprice

st.session_state["model_name"] = "기아"

# 여기서부터 아래를 사용하면 됨
price_list = apicarprice.getdata(st.session_state["model_name"])

option_list = []
for row in price_list:
    option_list.append(row[0])

    with st.container(border=True):
        col1, col2 = st.columns([1, 1])

        with col1:
            st.image(row[3], use_container_width=True)

        with col2:
            st.subheader(row[0])
            st.divider()

            # 가격 정보
            st.markdown(f"""
                    <div style="text-align: right;">
                        <p style="color: gray; margin: 0; font-size: 0.9rem;">최저가</p>
                        <h3 style="margin: 0; color: #1E1E1E;">{row[1]:,} 만원</h3>
                        <div style="margin: 10px 0;"></div>
                        <p style="color: gray; margin: 0; font-size: 0.9rem;">최고가</p>
                        <h3 style="margin: 0; color: #1E1E1E;">{row[2]:,} 만원</h3>
                    </div>
                """, unsafe_allow_html=True)

        st.caption("※ 위 가격은 선택 옵션 및 트림에 따라 달라질 수 있습니다.")

st.selectbox("당신의 차종을 골라주세요", option_list, key="in_price")
