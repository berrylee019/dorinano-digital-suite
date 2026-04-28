import streamlit as st
import numpy as np
import plotly.graph_objects as go
import pandas as pd
import time

# 1. 페이지 및 테마 설정
st.set_page_config(
    page_title="DoriNano Digital Suite",
    page_icon="🧬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 화면 전환 및 데이터 관리를 위한 세션 상태 초기화
if 'view_mode' not in st.session_state:
    st.session_state.view_mode = 'internal'

def switch_to_sandbox():
    st.session_state.view_mode = 'sandbox'
    st.rerun()

def switch_to_internal():
    st.session_state.view_mode = 'internal'
    st.rerun()

# 커스텀 CSS (메디컬 테크 + 골드 버튼 + 리간드 리포트 스타일)
st.markdown("""
    <style>
    .main { background-color: #f8f9fa; }
    .stMetric { background-color: #ffffff; padding: 15px; border-radius: 10px; box-shadow: 0 2px 4px rgba(0,0,0,0.05); }
    .sidebar .sidebar-content { background-image: linear-gradient(#2e7bcf, #052b5e); color: white; }
    h1 { color: #0f3d7a; }
    h2 { color: #1a5fb4; border-left: 5px solid #1a5fb4; padding-left: 10px; }
    
    /* 샌드박스 진입 골드 버튼 */
    .gold-btn button {
        background-color: #D4AF37 !important;
        color: white !important;
        border: 2px solid #B8860B !important;
        font-size: 1.2em !important;
        font-weight: bold !important;
        height: 3.5em !important;
        width: 100% !important;
        border-radius: 12px !important;
        box-shadow: 0 4px 15px rgba(212, 175, 55, 0.4) !important;
    }
    
    /* 파트너 배너 스타일 */
    .partner-banner { 
        background-color: #ffffff; 
        padding: 25px; 
        border-radius: 15px; 
        border: 3px solid #ed1c24; 
        margin-bottom: 25px;
        box-shadow: 0 10px 20px rgba(0,0,0,0.1);
    }
    </style>
    """, unsafe_allow_html=True)

# =========================================================================
# 모드 1: [INTERNAL] 연구용 대시보드
# =========================================================================
if st.session_state.view_mode == 'internal':

    # 2. 사이드바 내비게이션
    st.sidebar.title("🚀 DoriVac OS v1.0")
    st.sidebar.markdown("---")
    menu = st.sidebar.radio(
        "Select Module",
        ["Executive Dashboard", "Antigen AI Link", "Nano-Spacing Optimizer", "Project Report"]
    )
    st.sidebar.markdown("---")
    st.sidebar.info("Developed by MisaTech\n\nPartner: DoriNano")

    # --- Module 1: Dashboard ---
    if menu == "Executive Dashboard":
        st.title("📊 Platform Executive Overview")
        st.markdown("도리나노 DNA 오리가미 백신의 상용화 및 가치 증명을 위한 통합 대시보드입니다.")
        
        col1, col2, col3 = st.columns(3)
        col1.metric("Current R&D Stage", "Pre-clinical", "Phase 1 Entry Ready")
        col2.metric("Optimal Spacing", "3.5 nm", "Targeted")
        col3.metric("Discovery Efficiency", "85% ↑", "vs Wet-lab")
        
        st.markdown("---")
        st.subheader("💡 Digital Twin Roadmap")
        st.write("""
        - **Step 1:** 카이스트 팀 AI 연동을 통한 개인 맞춤형 항원(Neoantigen) 확보
        - **Step 2:** 도리나노 '나노-스페이싱' 시뮬레이터를 통한 최적 면역 반응 설계
        - **Step 3:** 인실리코(In-silico) 검증 기반의 임상 가속화 및 비용 절감
        """)

        st.markdown("<br><br><br><hr>", unsafe_allow_html=True)
        st.markdown("### 🌐 Global Business Expansion")
        st.info("글로벌 제약사 전용 기술 시연 환경(PaaS Sandbox)으로 전환합니다.")
        
        col_l, col_m, col_r = st.columns([1, 2, 1])
        with col_m:
            st.markdown('<div class="gold-btn">', unsafe_allow_html=True)
            if st.button("🚀 Open Global Partner Sandbox (PaaS Demo)"):
                switch_to_sandbox()
            st.markdown('</div>', unsafe_allow_html=True)

    # --- Module 2: Antigen AI Link (시각화 및 신뢰감 강화 버전) ---
    elif menu == "Antigen AI Link":
        st.title("🧬 Antigen Discovery Integration")
        st.subheader("AI-Driven Neoantigen Identification & 3D Mapping")
        
        st.info("💡 **Speech Point:** 카이스트 AI가 '무엇(What)'을 찾으면, 저희는 그것을 '어떻게(How)' 배치할지 시각화합니다. 이 3D 뷰가 연구진 간의 '언어의 장벽'을 허물어 소통 비용을 낮춥니다.")

        col_up, col_info = st.columns([1, 1])
        with col_up:
            uploaded_file = st.file_uploader("카이스트 AI 분석 결과(CSV/JSON)를 업로드하세요.", type=['csv', 'json'])
        with col_info:
            st.markdown("""
            **연구 협업 최적화 포인트:**
            * **No-Code Visualization:** 복잡한 코딩 없이 데이터 즉시 시각화
            * **Communication Asset:** 마우스 클릭만으로 리간드 결합 상태 공유
            * **Data Pipeline:** AI 예측값 → 3D 구조체 자동 매핑
            """)
        
        if uploaded_file is not None:
            # 1. 신뢰감을 주는 스피너 효과
            with st.spinner('🧬 AI 엔진으로부터 리간드 결합 데이터를 수신하여 3D 구조를 생성 중입니다...'):
                time.sleep(2.0) 
                st.success("✅ 분석 완료: AI가 제안한 상위 항원의 리간드 결합 모델을 생성했습니다.")

                df_ai = pd.DataFrame({
                    "Antigen_ID": ["Neo-Ag-Alpha", "Neo-Ag-Beta", "Neo-Ag-Gamma"],
                    "Confidence": [0.98, 0.92, 0.85],
                    "X_Pos": [3.0, 6.0, 9.0],
                    "Linker_Length": [2.5, 2.5, 2.5]
                })

                tab1, tab2 = st.tabs(["📊 분석 데이터 요약", "🔬 3D 리간드 결합 시뮬레이션"])
                with tab1:
                    st.write("### AI Prediction Results")
                    st.table(df_ai)
                with tab2:
                    st.write("### 3D Ligand Binding Visualizer")
                    fig = go.Figure()
                    # DNA 베이스
                    fig.add_trace(go.Mesh3d(x=[0, 12, 12, 0], y=[0, 12, 12, 0], z=[0, 0, 0, 0], i=[0, 0], j=[1, 2], k=[2, 3], color='lightgray', opacity=0.3, name="Platform"))
                    # 리간드 수직 결합 시각화
                    for i, row in df_ai.iterrows():
                        # Linker (수직선)
                        fig.add_trace(go.Scatter3d(x=[row['X_Pos'], row['X_Pos']], y=[6, 6], z=[0, row['Linker_Length']], mode='lines', line=dict(color='#2e7bcf', width=6), name=f"{row['Antigen_ID']} Linker"))
                        # Antigen (다이아몬드)
                        fig.add_trace(go.Scatter3d(x=[row['X_Pos']], y=[6], z=[row['Linker_Length'] + 0.2], mode='markers+text', text=[row['Antigen_ID']], marker=dict(size=14, color='#ed1c24', symbol='diamond', line=dict(color='white', width=2)), name=row['Antigen_ID']))
                    
                    fig.update_layout(scene=dict(xaxis=dict(range=[0, 12]), yaxis=dict(range=[0, 12]), zaxis=dict(range=[0, 5]), aspectmode='manual', aspectratio=dict(x=1.5, y=1, z=0.6)), margin=dict(l=0, r=0, b=0, t=0), height=500)
                    st.plotly_chart(fig, use_container_width=True)
                    st.markdown("> **👨‍🔬 연구원 코멘트:** \"별도의 툴 없이 브라우저에서 리간드 간섭 여부를 즉시 확인하고 합의를 도출할 수 있어 소통 비용이 획기적으로 줄어듭니다.\"")
        else:
            st.warning("분석 결과를 시각화하려면 상단에 AI 결과 파일을 업로드해 주세요.")

    # --- Module 3: Nano-Spacing Optimizer (기존 유지) ---
    elif menu == "Nano-Spacing Optimizer":
        st.title("🔬 Nano-Spacing Optimizer")
        st.markdown("DNA 오리가미 구조체 위에서 항원의 배치를 0.1nm 단위로 시뮬레이션합니다.")
        c1, c2 = st.columns([1, 1])
        with c1: spacing = st.slider("📐 Antigen Spacing (nm)", 1.0, 10.0, 3.5, 0.1)
        with c2: antigen_count = st.number_input("🔢 Number of Antigens", 1, 20, 6)
        st.markdown("---")
        col_left, col_right = st.columns([1, 1])
        with col_left:
            st.subheader("🌐 3D Structure Twin")
            fig_3d = go.Figure()
            fig_3d.add_trace(go.Mesh3d(x=[0, 12, 12, 0], y=[0, 0, 12, 12], z=[0, 0, 0, 0], color='lightgray', opacity=0.3))
            x_pos = np.arange(antigen_count) * (spacing / 2)
            fig_3d.add_trace(go.Scatter3d(x=x_pos, y=[6]*antigen_count, z=[0.8]*antigen_count, mode='markers+text', text=[f"Ag {i+1}" for i in range(antigen_count)], marker=dict(size=12, color='red', symbol='circle', line=dict(color='white', width=2))))
            fig_3d.update_layout(margin=dict(l=0, r=0, b=0, t=0), scene=dict(aspectmode='manual', aspectratio=dict(x=2, y=1, z=0.5)))
            st.plotly_chart(fig_3d, use_container_width=True)
        with col_right:
            st.subheader("📈 Immune Efficacy Prediction")
            x_range = np.linspace(1, 10, 100)
            y_range = np.exp(-((x_range - 3.5)**2) / (2 * 1.2**2))
            current_val = np.exp(-((spacing - 3.5)**2) / (2 * 1.2**2))
            fig_line = go.Figure()
            fig_line.add_trace(go.Scatter(x=x_range, y=y_range, name="Efficiency Curve", line=dict(color='#1a5fb4', width=3)))
            fig_line.add_trace(go.Scatter(x=[spacing], y=[current_val], mode='markers+text', text=[f"Efficiency: {current_val:.1%}"], marker=dict(color='red', size=18, symbol='star')))
            st.plotly_chart(fig_line, use_container_width=True)
            if 3.3 <= spacing <= 3.7:
                st.balloons()
                st.success("🎯 Optimal Spacing Reached!")

    # --- Module 4: Report (기존 유지) ---
    elif menu == "Project Report":
        st.title("📋 Project Simulation Report")
        report_data = {"Parameter": ["Target Antigen", "Antigen Count", "Simulated Spacing", "Predicted Efficacy"], "Value": ["Patient-A-01", "6 units", "3.5 nm", "98.2%"]}
        st.table(pd.DataFrame(report_data))
        st.button("📥 Download PDF Report (Mockup)")
        st.button("🧪 Export DNA Sequence")

# =========================================================================
# 모드 2: [SANDBOX] 글로벌 파트너 전용 (기존 유지)
# =========================================================================
else:
    st.sidebar.title("🤝 Partner Portal")
    if st.sidebar.button("⬅️ Back to Internal R&D"):
        switch_to_internal()
    st.markdown("""<div class="partner-banner"><h1 style="color:#ed1c24; margin:0;">[🤝 Daiichi Sankyo Partner Portal]</h1><p style="font-weight:bold;">DoriVac™ Digital Showroom</p></div>""", unsafe_allow_html=True)
    c_in, c_sim = st.columns([1, 2])
    with c_in:
        cargo = st.selectbox("Cargo Modality", ["ADC", "mRNA", "Protein"])
        spacing_p = st.slider("Target Spacing (nm)", 1.0, 10.0, 3.5)
        sim_btn = st.button("▶️ Run Matching Simulation", type="primary")
    with c_sim:
        if sim_btn:
            with st.spinner("Analyzing..."):
                time.sleep(1.5)
                st.success("Compatibility Complete")
                fig_p = go.Figure(data=[go.Scatter3d(x=np.random.rand(6), y=[6]*6, z=[0.8]*6, mode='markers', marker=dict(size=12, color='#ed1c24'))])
                st.plotly_chart(fig_p, use_container_width=True)
