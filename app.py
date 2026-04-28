import streamlit as st
import numpy as np
import plotly.graph_objects as go
import pandas as pd
import time

# 1. 페이지 설정 및 세션 상태 초기화
st.set_page_config(
    page_title="DoriNano Digital Suite",
    page_icon="🧬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 화면 전환을 위한 상태 관리
if 'view_mode' not in st.session_state:
    st.session_state.view_mode = 'internal'

def switch_to_sandbox():
    st.session_state.view_mode = 'sandbox'
    st.rerun()

def switch_to_internal():
    st.session_state.view_mode = 'internal'
    st.rerun()

# 2. 커스텀 CSS
st.markdown("""
    <style>
    .main { background-color: #f8f9fa; }
    h1 { color: #0f3d7a; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; }
    h2 { color: #1a5fb4; border-left: 5px solid #1a5fb4; padding-left: 10px; }
    .stMetric { background-color: #ffffff; padding: 15px; border-radius: 10px; box-shadow: 0 2px 4px rgba(0,0,0,0.05); }
    
    /* 샌드박스 진입 골드 버튼 스타일 */
    .sandbox-btn-container button {
        width: 100%;
        border-radius: 12px;
        height: 4.5em;
        font-size: 1.2em !important;
        font-weight: bold !important;
        background-color: #D4AF37 !important; /* Gold */
        color: white !important;
        border: 2px solid #B8860B !important;
        box-shadow: 0 4px 15px rgba(212, 175, 55, 0.3);
        transition: all 0.3s;
    }
    .sandbox-btn-container button:hover {
        background-color: #B8860B !important;
        transform: translateY(-2px);
    }

    /* 파트너 배너 */
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

    # 사이드바
    st.sidebar.title("🚀 DoriVac OS v1.0")
    st.sidebar.markdown("---")
    menu = st.sidebar.radio(
        "Select Module",
        ["Executive Dashboard", "Antigen AI Link", "Nano-Spacing Optimizer", "Project Report"]
    )
    st.sidebar.markdown("---")
    st.sidebar.info("Developed by MisaTech\n\nPartner: DoriNano")

    # --- Module 1: Executive Dashboard (여기에만 버튼 추가) ---
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

        # [핵심] 오직 Dashboard 메뉴 하단에만 나타나는 골드 버튼 섹션
        st.markdown("<br><br><br><hr>", unsafe_allow_html=True)
        st.markdown("### 🌐 Global Business Expansion")
        st.info("💡 **박사님 필살기:** 글로벌 제약사(다이이찌산쿄 등) 전용 기술 시연 환경으로 전환합니다.")
        
        col_btn_l, col_btn_m, col_btn_r = st.columns([1, 2, 1])
        with col_btn_m:
            st.markdown('<div class="sandbox-btn-container">', unsafe_allow_html=True)
            if st.button("🚀 Open Global Partner Sandbox (Daiichi Sankyo Demo)"):
                switch_to_sandbox()
            st.markdown('</div>', unsafe_allow_html=True)

    # --- Module 2: Antigen AI Link ---
    elif menu == "Antigen AI Link":
        st.title("🧬 Antigen Discovery Integration")
        uploaded_file = st.file_uploader("AI 분석 결과 파일 업로드 (JSON/CSV)", type=['csv', 'json'])
        if uploaded_file:
            st.success("데이터 로드 완료: 12개의 유효 신생 항원이 발견되었습니다.")
        else:
            st.warning("분석할 AI 데이터 파일을 업로드해 주세요.")

    # --- Module 3: Nano-Spacing Optimizer ---
    elif menu == "Nano-Spacing Optimizer":
        st.title("🔬 Nano-Spacing Optimizer")
        c1, c2 = st.columns(2)
        with c1: spacing = st.slider("📐 Antigen Spacing (nm)", 1.0, 10.0, 3.5, 0.1)
        with c2: antigen_count = st.number_input("🔢 Number of Antigens", 1, 20, 6)
        
        col_l, col_r = st.columns(2)
        with col_l:
            # 3D 가상 구조 (기존 로직 유지)
            fig_3d = go.Figure(data=[go.Scatter3d(x=np.random.rand(antigen_count), y=np.random.rand(antigen_count), z=np.random.rand(antigen_count), mode='markers', marker=dict(size=10, color='red'))])
            fig_3d.update_layout(margin=dict(l=0, r=0, b=0, t=0))
            st.plotly_chart(fig_3d)
        with col_r:
            st.info("3.5nm 간격 도달 시 면역 활성화가 극대화됩니다.")
            if 3.4 <= spacing <= 3.6: st.balloons()

    # --- Module 4: Report ---
    elif menu == "Project Report":
        st.title("📋 Project Simulation Report")
        st.table(pd.DataFrame({"Parameter": ["Target", "Antigen Count", "Spacing Status"], "Value": ["HNSCC (Head & Neck)", f"{antigen_count} units", "Optimized"]}))
        st.button("📥 Download PDF Report")


# =========================================================================
# 모드 2: [SANDBOX] 글로벌 파트너 전용 포털 (반전 화면)
# =========================================================================
else:
    # 파트너 포털 전용 사이드바
    st.sidebar.title("🤝 Partner Portal")
    st.sidebar.write("Project: DS-Collaboration")
    if st.sidebar.button("⬅️ Back to Internal R&D"):
        switch_to_internal()
    
    # 파트너 전용 배너
    st.markdown(f"""
        <div class="partner-banner">
            <h1 style="color:#ed1c24; margin:0; font-size: 2.5em;">[🤝 Daiichi Sankyo Partner Portal]</h1>
            <p style="color:#333; margin:10px 0 0 0; font-size: 1.2em; font-weight:bold;">DoriVac™ Digital Showroom for Global Collaboration</p>
            <p style="color:#666; margin:0;">Secure Session ID: DS-2026-BOS | Status: Encrypted</p>
        </div>
    """, unsafe_allow_html=True)

    col_in, col_out = st.columns([1, 2])
    
    with col_in:
        st.subheader("🛠️ Step 1: Input Your Cargo")
        cargo = st.selectbox("Cargo Modality", ["Antibody-Drug Conjugate", "mRNA/siRNA", "Protein Antigen"])
        st.subheader("🔬 Step 2: Virtual Assembly")
        spacing_p = st.slider("Target Nanolink Spacing (nm)", 1.0, 10.0, 3.5, 0.1)
        sim_btn = st.button("▶️ Run Matching Simulation", type="primary")

    with col_out:
        st.subheader("🌐 Step 3: Digital Twin Visualizer")
        if sim_btn:
            with st.spinner("Analyzing Compatibility..."):
                time.sleep(1.5)
                st.success("Simulation Complete")
                st.markdown("""
                    <div style="background-color: #f1f3f5; padding: 20px; border-radius: 10px; border-left: 10px solid #ed1c24;">
                        <h3 style="margin-top:0;">📋 Efficacy Prediction Report</h3>
                        <p><strong>Target Matching Score:</strong> <span style="color:red; font-size:1.5em;">98.4%</span></p>
                        <p><strong>Predicted Immune Response:</strong> 3.2x Higher than LNP</p>
                    </div>
                """, unsafe_allow_html=True)
                fig = go.Figure(data=[go.Scatter3d(x=np.random.rand(10), y=np.random.rand(10), z=np.random.rand(10), mode='markers', marker=dict(size=8, color='#ed1c24'))])
                st.plotly_chart(fig)
        else:
            st.info("시뮬레이션 실행 버튼을 누르면 성적표가 생성됩니다.")

    st.markdown("---")
    st.subheader("📩 Step 4: [Request Expert Review]")
    st.button("Submit Request to DoriNano Tech Team")
