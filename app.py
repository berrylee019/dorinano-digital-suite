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

# 2. 커스텀 CSS (버튼 색상 및 디자인 튜닝)
st.markdown("""
    <style>
    /* 메인 배경 및 폰트 */
    .main { background-color: #f8f9fa; }
    h1 { color: #0f3d7a; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; }
    h2 { color: #1a5fb4; border-left: 5px solid #1a5fb4; padding-left: 10px; }
    
    /* 카드 스타일 */
    .stMetric { background-color: #ffffff; padding: 15px; border-radius: 10px; box-shadow: 0 2px 4px rgba(0,0,0,0.05); }
    
    /* 샌드박스 전환 버튼 (골드 & 다크블루 조합) */
    .stButton>button {
        width: 100%;
        border-radius: 12px;
        height: 4em;
        font-size: 1.2em !important;
        font-weight: bold !important;
        transition: all 0.3s;
    }
    
    /* 연구용 화면 내 버튼 색상 (Deep Blue) */
    div[data-testid="stButton"] > button {
        background-color: #0f3d7a;
        color: white;
        border: none;
    }
    
    /* 샌드박스 전용 버튼 (Deep Gold / Global Business) */
    .sandbox-btn-container button {
        background-color: #D4AF37 !important; /* Gold */
        color: #000 !important;
        border: 2px solid #B8860B !important;
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
# 모드 1: [INTERNAL] 연구용 대시보드 (기존 코드 유지)
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

    elif menu == "Antigen AI Link":
        st.title("🧬 Antigen Discovery Integration")
        uploaded_file = st.file_uploader("AI 분석 결과 파일 업로드 (JSON/CSV)", type=['csv', 'json'])
        if uploaded_file:
            st.success("데이터 로드 완료: 12개의 유효 신생 항원이 발견되었습니다.")

    elif menu == "Nano-Spacing Optimizer":
        st.title("🔬 Nano-Spacing Optimizer")
        c1, c2 = st.columns(2)
        with c1: spacing = st.slider("📐 Antigen Spacing (nm)", 1.0, 10.0, 3.5, 0.1)
        with c2: antigen_count = st.number_input("🔢 Number of Antigens", 1, 20, 6)
        
        col_l, col_r = st.columns(2)
        with col_l:
            fig_3d = go.Figure(data=[go.Scatter3d(x=np.random.rand(antigen_count), y=np.random.rand(antigen_count), z=np.random.rand(antigen_count), mode='markers', marker=dict(size=10, color='red'))])
            st.plotly_chart(fig_3d)
        with col_r:
            st.write("이미지 및 그래프 시뮬레이션 영역")
            if 3.4 <= spacing <= 3.6: st.balloons()

    elif menu == "Project Report":
        st.title("📋 Project Simulation Report")
        st.table(pd.DataFrame({"Parameter": ["Target", "Spacing"], "Value": ["HNSCC", "3.5nm"]}))

    # [하단 반전 카드 섹션]
    st.markdown("<br><br><hr>", unsafe_allow_html=True)
    st.markdown("### 🌐 Global Business Expansion")
    st.info("박사님, 이 기술을 글로벌 제약사(다이이찌산쿄 등)가 직접 체험하게 하려면 어떤 인터페이스가 필요할까요?")
    
    c_btn1, c_btn2, c_btn3 = st.columns([1, 2, 1])
    with c_btn2:
        # 샌드박스 전환 버튼 (골드 색상 적용)
        st.markdown('<div class="sandbox-btn-container">', unsafe_allow_html=True)
        if st.button("🚀 Open Global Partner Sandbox (Daiichi Sankyo Demo)"):
            switch_to_sandbox()
        st.markdown('</div>', unsafe_allow_html=True)


# =========================================================================
# 모드 2: [SANDBOX] 글로벌 파트너 전용 포털 (반전 화면)
# =========================================================================
else:
    # 파트너 포털 전용 사이드바
    st.sidebar.title("🤝 Partner Portal")
    if st.sidebar.button("⬅️ Back to Internal R&D"):
        switch_to_internal()
    
    # [메커니즘 1. 파트너 전용 'Sandbox' 배너]
    st.markdown(f"""
        <div class="partner-banner">
            <h1 style="color:#ed1c24; margin:0; font-size: 2.5em;">[🤝 Daiichi Sankyo Partner Portal]</h1>
            <p style="color:#333; margin:10px 0 0 0; font-size: 1.2em; font-weight:bold;">DoriVac™ Digital Showroom for Global Collaboration</p>
            <p style="color:#666; margin:0;">Secure Session ID: DS-2026-BOS | Status: Encrypted</p>
        </div>
    """, unsafe_allow_html=True)

    # [메커니즘 2. 'Cargo-to-Vehicle' 매칭]
    col_in, col_out = st.columns([1, 2])
    
    with col_in:
        st.subheader("🛠️ Step 1: Input Your Cargo")
        cargo = st.selectbox("Cargo Modality", ["Antibody-Drug Conjugate", "mRNA/siRNA", "Protein Antigen"])
        st.file_uploader("Upload Molecule Data (.pdb / .csv)")
        
        st.subheader("🔬 Step 2: Virtual Assembly")
        spacing_p = st.slider("Target Nanolink Spacing (nm)", 1.0, 10.0, 3.5, 0.1)
        sim_btn = st.button("▶️ Run Matching Simulation", type="primary")

    with col_out:
        st.subheader("🌐 Step 3: Digital Twin Visualizer")
        if sim_btn:
            with st.spinner("Analyzing Compatibility..."):
                time.sleep(1.5)
                st.success("Simulation Complete")
                
                # 예측 성적표 발급 (메커니즘 3)
                st.markdown("""
                    <div style="background-color: #f1f3f5; padding: 20px; border-radius: 10px; border-left: 10px solid #ed1c24;">
                        <h3 style="margin-top:0;">📋 Efficacy Prediction Report</h3>
                        <p><strong>Target Matching Score:</strong> <span style="color:red; font-size:1.5em;">98.4%</span></p>
                        <p><strong>Predicted Immune Response:</strong> 3.2x Higher than LNP</p>
                        <p><strong>Manufacturing Complexity:</strong> Low (Optimal for Scalability)</p>
                    </div>
                """, unsafe_allow_html=True)
                
                # 가상 3D 그래프
                fig = go.Figure(data=[go.Scatter3d(x=np.random.rand(10), y=np.random.rand(10), z=np.random.rand(10), mode='markers', marker=dict(size=8, color='#ed1c24'))])
                st.plotly_chart(fig)
        else:
            st.info("위의 시뮬레이션 실행 버튼을 누르면 예측 성적표와 3D 모델이 생성됩니다.")

    # [메커니즘 4. 실시간 기술 상담]
    st.markdown("---")
    st.subheader("☎️ Step 4: Communication Bridge")
    c_ask1, c_ask2 = st.columns([2, 1])
    with c_ask1:
        st.text_area("Request specific technical details or Wet-lab PoC scheduling:")
    with c_ask2:
        st.markdown("<br>", unsafe_allow_html=True)
        st.button("📩 [Request Expert Review]")
