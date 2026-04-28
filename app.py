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

# 세션 상태 초기화
if 'view_mode' not in st.session_state:
    st.session_state.view_mode = 'internal'

def switch_to_sandbox():
    st.session_state.view_mode = 'sandbox'
    st.rerun()

def switch_to_internal():
    st.session_state.view_mode = 'internal'
    st.rerun()

# 커스텀 CSS
st.markdown("""
    <style>
    .main { background-color: #f8f9fa; }
    .stMetric { background-color: #ffffff; padding: 15px; border-radius: 10px; box-shadow: 0 2px 4px rgba(0,0,0,0.05); }
    .sidebar .sidebar-content { background-image: linear-gradient(#2e7bcf, #052b5e); color: white; }
    h1 { color: #0f3d7a; }
    h2 { color: #1a5fb4; border-left: 5px solid #1a5fb4; padding-left: 10px; }
    
    /* 골드 샌드박스 버튼 */
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

    /* 파트너용 리포트 박스 */
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
# 모드 1: [INTERNAL] 연구용 대시보드
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

    # --- Module 1: Executive Dashboard ---
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
        st.info("글로벌 제약사 전용 기술 시연 환경(PaaS Sandbox)으로 전환합니다.")
        
        col_l, col_m, col_r = st.columns([1, 2, 1])
        with col_m:
            st.markdown('<div class="gold-btn">', unsafe_allow_html=True)
            if st.button("🚀 Open Global Partner Sandbox (Daiichi Sankyo Demo)"):
                switch_to_sandbox()
            st.markdown('</div>', unsafe_allow_html=True)

    # --- Module 2: Antigen AI Link ---
    elif menu == "Antigen AI Link":
        st.title("🧬 Antigen Discovery Integration")
        st.subheader("AI-Driven Neoantigen Identification & 3D Mapping")
        st.info("💡 **Speech Point:** 카이스트 AI가 '무엇'을 찾으면, 저희는 그것을 '어떻게' 배치할지 시각화합니다.")

        col_up, col_info = st.columns([1, 1])
        with col_up:
            uploaded_file = st.file_uploader("카이스트 AI 결과 업로드", type=['csv', 'json'])
        
        if uploaded_file:
            with st.spinner('3D 구조 생성 중...'):
                time.sleep(2.0)
                st.success("✅ 리간드 결합 모델 생성 완료")
                df_ai = pd.DataFrame({"Antigen_ID": ["Neo-Ag-A", "Neo-Ag-B"], "X_Pos": [3.0, 8.0], "Linker": [2.5, 2.5]})
                
                # 3D 뷰어
                fig = go.Figure()
                fig.add_trace(go.Mesh3d(x=[0, 12, 12, 0], y=[0, 12, 12, 0], z=[0, 0, 0, 0], color='lightgray', opacity=0.3))
                for i, row in df_ai.iterrows():
                    fig.add_trace(go.Scatter3d(x=[row['X_Pos'], row['X_Pos']], y=[6, 6], z=[0, row['Linker']], mode='lines', line=dict(color='#2e7bcf', width=6)))
                    fig.add_trace(go.Scatter3d(x=[row['X_Pos']], y=[6], z=[row['Linker']+0.2], mode='markers', marker=dict(size=14, color='#ed1c24', symbol='diamond')))
                fig.update_layout(scene=dict(aspectmode='manual', aspectratio=dict(x=1.5, y=1, z=0.6)), margin=dict(l=0, r=0, b=0, t=0))
                st.plotly_chart(fig, use_container_width=True)

    # --- Module 3: Nano-Spacing Optimizer ---
    elif menu == "Nano-Spacing Optimizer":
        st.title("🔬 Nano-Spacing Optimizer")
        c1, c2 = st.columns(2)
        with c1: spacing = st.slider("📐 Antigen Spacing (nm)", 1.0, 10.0, 3.5, 0.1)
        with c2: count = st.number_input("🔢 Number of Antigens", 1, 20, 6)
        
        if 3.3 <= spacing <= 3.7:
            st.balloons()
            st.success("🎯 최적 범위(Golden Zone) 진입!")

    # --- Module 4: Report ---
    elif menu == "Project Report":
        st.title("📋 Project Simulation Report")
        st.table(pd.DataFrame({"Parameter": ["Target", "Status"], "Value": ["HNSCC", "Optimized"]}))

# =========================================================================
# 모드 2: [SANDBOX] 글로벌 파트너 전용 (수정 완료)
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
                
                # [복구 포인트 1] 성적표 박스
                score = (np.exp(-((spacing_p - 3.5)**2) / 2) * 100)
                st.markdown(f"""
                    <div class="report-box">
                        <h3 style="margin-top:0; color:#ed1c24;">📋 Efficacy Prediction Report</h3>
                        <p><strong>Partner Cargo Type:</strong> {cargo_type}</p>
                        <p><strong>Target Matching Score:</strong> <span style="color:red; font-size:1.5em;">{score:.1f}%</span></p>
                        <p><strong>Predicted Efficacy:</strong> 면역 반응 활성도가 최적치 대비 우수함</p>
                    </div>
                """, unsafe_allow_html=True)
                
                # [복구 포인트 2] 3D 시각화
                fig_p = go.Figure()
                fig_p.add_trace(go.Mesh3d(x=[0, 12, 12, 0], y=[0, 12, 12, 0], z=[0, 0, 0, 0], color='lightgray', opacity=0.3))
                x_p = np.arange(cargo_count) * (spacing_p / 2)
                fig_p.add_trace(go.Scatter3d(x=x_p, y=[6]*cargo_count, z=[0.8]*cargo_count, mode='markers', marker=dict(size=12, color='#ed1c24', symbol='circle', line=dict(color='white', width=2))))
                fig_p.update_layout(margin=dict(l=0, r=0, b=0, t=0), scene=dict(aspectmode='manual', aspectratio=dict(x=2, y=1, z=0.5)), height=400)
                st.plotly_chart(fig_p, use_container_width=True)
                
                if 3.3 <= spacing_p <= 3.7:
                    st.balloons()
        else:
            st.info("버튼을 누르면 시뮬레이션 결과와 리포트가 생성됩니다.")

    # [복구 포인트 3] 하단 문의 버튼 영역
    st.markdown("---")
    st.subheader("☎️ Step 4: [Request Expert Review]")
    st.write("상기 시뮬레이션 데이터를 바탕으로 도리나노 기술팀과 상세 협의를 시작하시겠습니까?")
    if st.button("📩 Submit Simulation Data for Review"):
        st.success("데이터가 성공적으로 전송되었습니다. 24시간 이내에 담당자가 연락드립니다.")
