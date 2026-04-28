import streamlit as st
import numpy as np
import plotly.graph_objects as go
import pandas as pd
import time

# 1. 페이지 설정 및 초기화
st.set_page_config(
    page_title="DoriVac Digital Suite",
    page_icon="🧬",
    layout="wide"
)

# 화면 전환을 위한 상태 관리 (처음에는 'internal' 화면)
if 'view_mode' not in st.session_state:
    st.session_state.view_mode = 'internal'

# 버튼 클릭 시 모드 변경 함수
def switch_to_sandbox():
    st.session_state.view_mode = 'sandbox'

def switch_to_internal():
    st.session_state.view_mode = 'internal'

# 커스텀 스타일링
st.markdown("""
    <style>
    .stButton>button { width: 100%; border-radius: 10px; height: 3em; font-weight: bold; }
    .main-card { background-color: #ffffff; padding: 20px; border-radius: 15px; box-shadow: 0 4px 6px rgba(0,0,0,0.05); border: 1px solid #e0e0e0; margin-bottom: 20px; }
    .partner-banner { background-color: #ffffff; padding: 20px; border-radius: 15px; border: 2px solid #ed1c24; margin-bottom: 25px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); }
    </style>
    """, unsafe_allow_html=True)

# =========================================================================
# 화면 1: Internal R&D Dashboard (기존 연구용 화면)
# =========================================================================
if st.session_state.view_mode == 'internal':
    st.title("📊 DoriVac™ Internal R&D Dashboard")
    st.caption("Access Level: Administrator | Project: DoriVac-101 (HNSCC)")
    
    st.markdown("---")
    
    # 상단 지표
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Active Samples", "124", "+12%")
    c2.metric("Simulation Accuracy", "94.2%", "0.5%")
    c3.metric("MSK Collaboration", "Active", "Phase: IND")
    c4.metric("Last Update", "2h ago")

    # 중앙 분석 화면 (예시 그래프)
    st.subheader("🔬 Ongoing Nano-Spacing Analysis")
    chart_data = pd.DataFrame(np.random.randn(20, 3), columns=['3.5nm', '5.0nm', '7.0nm'])
    st.line_chart(chart_data)

    st.write("연구원들이 현재 진행 중인 실험 데이터와 시뮬레이션 결과가 연동되는 관리 화면입니다.")

    # 하단: 반전 카드 (Sandbox 진입 버튼)
    st.markdown("<br><br><br>", unsafe_allow_html=True)
    st.markdown("---")
    st.warning("⚠️ **[Business Development Notice]** 글로벌 파트너사(다이이찌산쿄 등) 전용 기술 시연 환경이 준비되었습니다.")
    
    col_btn_l, col_btn_m, col_btn_r = st.columns([1, 2, 1])
    with col_btn_m:
        st.button("🌐 Open Global Partner Sandbox (PaaS Demo)", on_click=switch_to_sandbox, type="primary")


# =========================================================================
# 화면 2: Global Partner Sandbox (업그레이드된 PaaS 버전)
# =========================================================================
else:
    # 파트너 포털 상단 배너
    st.markdown("""
        <div class="partner-banner">
            <h1 style="color:#ed1c24; margin:0;">[🤝 Daiichi Sankyo Partner Portal]</h1>
            <p style="color:#333; margin:10px 0 0 0; font-weight:bold;">Welcome to DoriVac™ PaaS Environment</p>
            <p style="color:#666; margin:0;">Status: Secure Session Active | Session ID: DS-RX-9912</p>
        </div>
    """, unsafe_allow_html=True)

    # 사이드바에 '돌아가기' 버튼 추가
    st.sidebar.title("🚀 DoriVac OS")
    if st.sidebar.button("⬅️ Back to Internal R&D"):
        st.session_state.view_mode = 'internal'
        st.rerun()

    st.markdown("글로벌 파트너사가 자사의 항원을 도리백 플랫폼에 탑재하고 결과를 실시간으로 예측해볼 수 있는 **'디지털 쇼룸'**입니다.")

    col_input, col_sim = st.columns([1, 2])

    with col_input:
        st.subheader("🛠️ Step 1: Input Partner Cargo")
        cargo_type = st.selectbox("Cargo Modality", ["Protein/Antigen", "Nucleic Acid", "Small Molecule"])
        cargo_complex = st.select_slider("Molecular Complexity", options=["Low", "Mid", "High"], value="Mid")
        st.subheader("🔬 Step 2: Design Parameter")
        spacing = st.slider("Target Spacing (nm)", 1.0, 10.0, 3.5, 0.1)
        antigen_count = st.number_input("Cargo Capacity", 1, 12, 6)
        simulate_btn = st.button("▶️ Run Matching Simulation", type="primary")

    with col_sim:
        st.subheader("🌐 Step 3: Digital Twin View")
        if simulate_btn:
            with st.spinner("빅파마 화물 적합성 분석 중..."):
                time.sleep(1.5)
                st.success("Analysis Complete")
                
                # 가상의 스코어 계산
                score = (np.exp(-((spacing - 3.5)**2) / 2) * 100)
                st.metric("Compatibility Score", f"{score:.1f}%")

                # 3D 시각화
                fig = go.Figure(data=[go.Scatter3d(
                    x=np.random.standard_normal(antigen_count),
                    y=np.random.standard_normal(antigen_count),
                    z=np.random.standard_normal(antigen_count),
                    mode='markers', marker=dict(size=10, color='#ed1c24')
                )])
                fig.update_layout(margin=dict(l=0, r=0, b=0, t=0), height=400)
                st.plotly_chart(fig, use_container_width=True)

    if simulate_btn:
        st.markdown("---")
        st.subheader("📋 [Efficacy Prediction Report]")
        st.info(f"선택하신 {spacing}nm 설계는 기존 대비 면역 원성을 극대화할 수 있는 것으로 분석되었습니다.")
        st.button("[Request Expert Review]")
