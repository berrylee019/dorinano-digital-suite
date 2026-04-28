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

# 커스텀 CSS (기존 디자인 유지 + 골드 버튼 및 파트너 UI)
st.markdown("""
    <style>
    .main { background-color: #f8f9fa; }
    .stMetric { background-color: #ffffff; padding: 15px; border-radius: 10px; box-shadow: 0 2px 4px rgba(0,0,0,0.05); }
    .sidebar .sidebar-content { background-image: linear-gradient(#2e7bcf, #052b5e); color: white; }
    h1 { color: #0f3d7a; }
    h2 { color: #1a5fb4; border-left: 5px solid #1a5fb4; padding-left: 10px; }
    
    /* 골드 샌드박스 버튼 스타일 */
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
    
    /* 예측 리포트 박스 */
    .report-box {
        background-color: #f1f3f5; 
        padding: 20px; 
        border-radius: 10px; 
        border-left: 10px solid #ed1c24;
        margin-bottom: 20px;
    }
    </style>
    """, unsafe_allow_html=True)


# =========================================================================
# [모드 1] INTERNAL (연구용 대시보드)
# =========================================================================
if st.session_state.view_mode == 'internal':

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
        st.write("- **Step 1:** AI 연동 항원 확보 / **Step 2:** 나노-스페이싱 시뮬레이션 / **Step 3:** 임상 가속화")

        st.markdown("<br><br><br><hr>", unsafe_allow_html=True)
        st.markdown("### 🌐 Global Business Expansion")
        st.info("글로벌 파트너사 전용 기술 시연 환경(PaaS Sandbox)으로 전환합니다.")
        
        col_l, col_m, col_r = st.columns([1, 2, 1])
        with col_m:
            st.markdown('<div class="gold-btn">', unsafe_allow_html=True)
            if st.button("🚀 Open Global Partner Sandbox (Daiichi Sankyo Demo)"):
                switch_to_sandbox()
            st.markdown('</div>', unsafe_allow_html=True)

    # --- Module 2: Antigen AI Link (기존 유지) ---
    elif menu == "Antigen AI Link":
        st.title("🧬 Antigen Discovery Integration")
        uploaded_file = st.file_uploader("AI 분석 결과 파일 업로드", type=['csv', 'json'])
        if uploaded_file:
            st.success("데이터 로드 완료: 12개의 유효 항원 발견")

    # --- Module 3: Nano-Spacing Optimizer (기존 유지) ---
    elif menu == "Nano-Spacing Optimizer":
        st.title("🔬 Nano-Spacing Optimizer")
        c1, c2 = st.columns(2)
        with c1: spacing = st.slider("📐 Antigen Spacing (nm)", 1.0, 10.0, 3.5, 0.1)
        with c2: antigen_count = st.number_input("🔢 Number of Antigens", 1, 20, 6)
        
        col_left, col_right = st.columns(2)
        with col_left:
            fig_3d = go.Figure(data=[go.Scatter3d(x=np.arange(antigen_count)*(spacing/2), y=[6]*antigen_count, z=[0.8]*antigen_count, mode='markers', marker=dict(size=10, color='red'))])
            fig_3d.update_layout(margin=dict(l=0, r=0, b=0, t=0))
            st.plotly_chart(fig_3d, use_container_width=True)
        with col_right:
            st.write("면역 활성화 그래프 영역")
            if 3.4 <= spacing <= 3.6: st.balloons()

    # --- Module 4: Report (기존 유지) ---
    elif menu == "Project Report":
        st.title("📋 Project Simulation Report")
        st.table(pd.DataFrame({"Parameter": ["Target", "Spacing"], "Value": ["HNSCC", "3.5nm"]}))

# =========================================================================
# [모드 2] SANDBOX (글로벌 파트너 전용 화면 - 3D 시각화 강화)
# =========================================================================
else:
    st.sidebar.title("🤝 Partner Portal")
    if st.sidebar.button("⬅️ Back to Internal R&D"):
        switch_to_internal()

    st.markdown(f"""
        <div class="partner-banner">
            <h1 style="color:#ed1c24; margin:0; font-size: 2.3em;">[🤝 Daiichi Sankyo Partner Portal]</h1>
            <p style="color:#333; margin:10px 0 0 0; font-weight:bold;">DoriVac™ Digital Showroom for Global Collaboration</p>
        </div>
    """, unsafe_allow_html=True)

    c_in, c_sim = st.columns([1, 2])
    
    with c_in:
        st.subheader("🛠️ Step 1: Input Your Cargo")
        cargo_type = st.selectbox("Cargo Modality", ["Antibody-Drug Conjugate", "mRNA/siRNA", "Protein Antigen"])
        st.file_uploader("Upload Molecule Data (.pdb / .csv)")
        
        st.subheader("🔬 Step 2: Virtual Assembly")
        spacing_p = st.slider("Target Nanolink Spacing (nm)", 1.0, 10.0, 3.5, 0.1)
        cargo_count = st.number_input("Cargo Units to Load", 1, 12, 6)
        sim_btn = st.button("▶️ Run Matching Simulation", type="primary")

    with c_sim:
        st.subheader("🌐 Step 3: Digital Twin Visualizer")
        
        if sim_btn:
            with st.spinner("Analyzing Partner Cargo Compatibility..."):
                time.sleep(1.5)
                st.success("Simulation Complete")
                
                # 1. 예측 성적표 (메커니즘 3)
                score = (np.exp(-((spacing_p - 3.5)**2) / 2) * 100)
                st.markdown(f"""
                    <div class="report-box">
                        <h3 style="margin-top:0; color:#ed1c24;">📋 Efficacy Prediction Report</h3>
                        <p><strong>Partner Cargo Type:</strong> {cargo_type}</p>
                        <p><strong>Target Matching Score:</strong> <span style="color:red; font-size:1.5em;">{score:.1f}%</span></p>
                        <p><strong>Predicted Efficacy:</strong> 면역 반응 활성도가 최적치 대비 우수함</p>
                    </div>
                """, unsafe_allow_html=True)
                
                # 2. 3D 시각화 (형님의 핵심 로직 이식)
                st.write("🔬 **3D Cargo-Vehicle Interaction View**")
                fig_3d_p = go.Figure()
                
                # DNA 오리가미 베이스 판
                fig_3d_p.add_trace(go.Mesh3d(
                    x=[0, 12, 12, 0], y=[0, 0, 12, 12], z=[0, 0, 0, 0],
                    color='lightgray', opacity=0.3, name="DoriVac Platform"
                ))
                
                # 파트너 화물 배치 (다이이찌산쿄 레드 컬러 적용)
                x_pos_p = np.arange(cargo_count) * (spacing_p / 2)
                fig_3d_p.add_trace(go.Scatter3d(
                    x=x_pos_p, y=[6]*cargo_count, z=[0.8]*cargo_count,
                    mode='markers+text',
                    text=[f"Cargo {i+1}" for i in range(cargo_count)],
                    marker=dict(size=12, color='#ed1c24', symbol='circle', line=dict(color='white', width=2)),
                    name="Partner Cargo"
                ))
                
                fig_3d_p.update_layout(
                    margin=dict(l=0, r=0, b=0, t=0),
                    scene=dict(
                        xaxis_title='X (nm)', yaxis_title='Y (nm)', zaxis_title='Z (nm)',
                        aspectmode='manual', aspectratio=dict(x=2, y=1, z=0.5)
                    ),
                    height=450
                )
                st.plotly_chart(fig_3d_p, use_container_width=True)
                
                if 3.4 <= spacing_p <= 3.6:
                    st.balloons()
        else:
            st.info("버튼을 누르면 파트너사 항원과 도리백의 매칭 시뮬레이션 결과가 생성됩니다.")

    st.markdown("---")
    st.subheader("☎️ Step 4: [Request Expert Review]")
    st.button("Submit Simulation Data to DoriNano Tech Team")
