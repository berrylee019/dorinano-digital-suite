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

# 화면 전환을 위한 세션 상태 초기화
if 'view_mode' not in st.session_state:
    st.session_state.view_mode = 'internal'

def switch_to_sandbox():
    st.session_state.view_mode = 'sandbox'
    st.rerun()

def switch_to_internal():
    st.session_state.view_mode = 'internal'
    st.rerun()

# 커스텀 CSS (기존 디자인 유지 + 골드 버튼 추가)
st.markdown("""
    <style>
    .main { background-color: #f8f9fa; }
    .stMetric { background-color: #ffffff; padding: 15px; border-radius: 10px; box-shadow: 0 2px 4px rgba(0,0,0,0.05); }
    .sidebar .sidebar-content { background-image: linear-gradient(#2e7bcf, #052b5e); color: white; }
    h1 { color: #0f3d7a; }
    h2 { color: #1a5fb4; border-left: 5px solid #1a5fb4; padding-left: 10px; }
    
    /* 골드 샌드박스 버튼 스타일 */
    .sandbox-container {
        text-align: center;
        padding: 40px 0;
    }
    div.stButton > button:first-child {
        background-color: #0f3d7a;
        color: white;
    }
    /* 특정 클래스 내의 버튼을 골드로 설정 */
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
# [모드 1] INTERNAL (기존 연구용 대시보드 구조)
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

        # 하단 샌드박스 전환 섹션 (Executive Dashboard에만 표시)
        st.markdown("<br><br><br><hr>", unsafe_allow_html=True)
        st.markdown("### 🌐 Global Business Expansion")
        st.info("글로벌 제약사(다이이찌산쿄 등) 전용 기술 시연 환경을 확인하시겠습니까?")
        
        col_l, col_m, col_r = st.columns([1, 2, 1])
        with col_m:
            st.markdown('<div class="gold-btn">', unsafe_allow_html=True)
            if st.button("🚀 Open Global Partner Sandbox (PaaS Demo)"):
                switch_to_sandbox()
            st.markdown('</div>', unsafe_allow_html=True)

    # --- Module 2: Antigen AI Link ---
    elif menu == "Antigen AI Link":
        st.title("🧬 Antigen Discovery Integration")
        st.subheader("AI-Driven Neoantigen Identification")
        st.info("카이스트 AI 모델(T세포/B세포 동시 예측) 데이터를 수신하는 게이트웨이입니다.")
        uploaded_file = st.file_uploader("AI 분석 결과 파일 업로드 (JSON/CSV)", type=['csv', 'json'])
        if uploaded_file is not None:
            with st.spinner('AI 데이터를 분석 중...'):
                time.sleep(1.5)
                st.success("데이터 로드 완료: 12개의 유효 신생 항원이 발견되었습니다.")
                df_sample = pd.DataFrame({
                    "Antigen_ID": [f"AG-{i:03d}" for i in range(1, 7)],
                    "Binding_Affinity": [0.98, 0.95, 0.88, 0.82, 0.79, 0.75],
                    "Priority": ["High", "High", "Mid", "Mid", "Low", "Low"]
                })
                st.table(df_sample)
        else:
            st.warning("분석할 AI 데이터 파일을 업로드해 주세요.")

    # --- Module 3: Nano-Spacing Optimizer ---
    elif menu == "Nano-Spacing Optimizer":
        st.title("🔬 Nano-Spacing Optimizer")
        st.markdown("DNA 오리가미 구조체 위에서 항원의 배치를 0.1nm 단위로 시뮬레이션합니다.")
        c1, c2 = st.columns([1, 1])
        with c1:
            spacing = st.slider("📐 Antigen Spacing (nm)", 1.0, 10.0, 3.5, 0.1)
        with c2:
            antigen_count = st.number_input("🔢 Number of Antigens", 1, 20, 6)
        st.markdown("---")
        col_left, col_right = st.columns([1, 1])
        with col_left:
            st.subheader("🌐 3D Structure Twin")
            fig_3d = go.Figure()
            fig_3d.add_trace(go.Mesh3d(x=[0, 12, 12, 0], y=[0, 0, 12, 12], z=[0, 0, 0, 0], color='lightgray', opacity=0.3))
            x_pos = np.arange(antigen_count) * (spacing / 2)
            fig_3d.add_trace(go.Scatter3d(x=x_pos, y=[6]*antigen_count, z=[0.8]*antigen_count, mode='markers+text', text=[f"Ag {i+1}" for i in range(antigen_count)], marker=dict(size=12, color='red', symbol='circle', line=dict(color='white', width=2))))
            fig_3d.update_layout(margin=dict(l=0, r=0, b=0, t=0), scene=dict(xaxis_title='X (nm)', yaxis_title='Y (nm)', zaxis_title='Z (nm)', aspectmode='manual', aspectratio=dict(x=2, y=1, z=0.5)))
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
                st.success("🎯 Optimal Spacing (3.5nm) Reached!")
            else:
                st.warning(f"최적 간격(3.5nm)까지 {abs(3.5-spacing):.1f}nm 조정 필요")

    # --- Module 4: Report ---
    elif menu == "Project Report":
        st.title("📋 Project Simulation Report")
        report_data = {"Parameter": ["Target Antigen", "Antigen Count", "Simulated Spacing", "Predicted Efficacy"], "Value": ["Patient-A-01", "6 units", "3.5 nm", "98.2%"]}
        st.table(pd.DataFrame(report_data))
        st.button("📥 Download PDF Report (Mockup)")

# =========================================================================
# [모드 2] SANDBOX (글로벌 파트너 전용 화면)
# =========================================================================
else:
    st.sidebar.title("🤝 Partner Portal")
    if st.sidebar.button("⬅️ Back to Internal R&D"):
        switch_to_internal()

    st.markdown(f"""
        <div class="partner-banner">
            <h1 style="color:#ed1c24; margin:0; font-size: 2.3em;">[🤝 Daiichi Sankyo Partner Portal]</h1>
            <p style="color:#333; margin:10px 0 0 0; font-weight:bold;">Welcome to DoriVac™ Digital Showroom</p>
            <p style="color:#666; margin:0;">Status: Secure Session Active | Session ID: DS-RX-9912</p>
        </div>
    """, unsafe_allow_html=True)

    c_in, c_sim = st.columns([1, 2])
    with c_in:
        st.subheader("🛠️ Step 1: Input Cargo")
        cargo_type = st.selectbox("Cargo Modality", ["Protein/Antigen", "Nucleic Acid", "Small Molecule"])
        st.subheader("🔬 Step 2: Design")
        spacing_p = st.slider("Target Spacing (nm)", 1.0, 10.0, 3.5, 0.1)
        sim_btn = st.button("▶️ Run Matching Simulation", type="primary")

    with c_sim:
        st.subheader("🌐 Step 3: Digital Twin")
        if sim_btn:
            with st.spinner("Analyzing..."):
                time.sleep(1.5)
                st.success("Compatibility Analysis Complete")
                st.metric("Predicted Efficacy Score", f"{(np.exp(-((spacing_p - 3.5)**2) / 2) * 100):.1f}%")
                st.info("📋 [Efficacy Prediction Report]가 생성되었습니다. 아래에서 상담을 요청하세요.")
        else:
            st.info("시뮬레이션을 실행하여 최적 적합성을 확인하세요.")

    st.markdown("---")
    st.subheader("☎️ Step 4: Expert Bridge")
    st.button("📩 [Request Expert Review]")
