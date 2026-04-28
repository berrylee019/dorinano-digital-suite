import streamlit as st
import numpy as np
import plotly.graph_objects as go
import pandas as pd
import time

# 1. 페이지 및 테마 설정
st.set_page_config(
    page_title="DoriVac Digital Suite (PaaS Demo)",
    page_icon="🧬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 커스텀 CSS (파트너 전용 포털 느낌 연출)
st.markdown("""
    <style>
    .stApp { background-color: #f0f2f6; }
    .stMetric { background-color: #ffffff; padding: 15px; border-radius: 10px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); }
    .stSidebar .sidebar-content { background-image: linear-gradient(#002f6c, #0056a3); color: white; }
    h1 { color: #002f6c; font-family: 'Helvetica Neue', sans-serif; }
    h2 { color: #0056a3; border-bottom: 2px solid #0056a3; padding-bottom: 5px; }
    div[data-testid="stSidebarUserContent"] { color: white; }
    .partner-banner { 
        background-color: #ffffff; 
        padding: 20px; 
        border-radius: 15px; 
        border: 2px solid #ed1c24; 
        margin-bottom: 25px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    </style>
    """, unsafe_allow_html=True)

# 2. 사이드바 - 메인 OS 컨트롤
st.sidebar.title("🚀 DoriVac OS")
st.sidebar.markdown("---")
# 미팅 시연을 위해 'PaaS Sandbox'를 기본 메뉴로 설정
menu = st.sidebar.radio(
    "Select Operation Mode",
    ["Global Partner Sandbox (Demo)", "Internal R&D Dashboard", "Project Management"]
)

st.sidebar.markdown("---")
st.sidebar.caption("Secured by DoriNano Digital Division")

# 3. 메뉴별 기능 구현

# =========================================================================
# --- Module: Global Partner Sandbox (이 미팅의 핵심) ---
# [메커니즘 1. 파트너 전용 'Sandbox' 입장 (보안 접속)] 통합 구현
# =========================================================================
if menu == "Global Partner Sandbox (Demo)":
    
    # [메커니즘 1] 파트너 전용 배너 및 로고 (Daiichi Sankyo 시뮬레이션)
    st.markdown("""
        <div class="partner-banner">
            <h1 style="color:#ed1c24; margin:0;">[🤝 Daiichi Sankyo Partner Portal]</h1>
            <p style="color:#333; margin:10px 0 0 0; font-weight:bold;">Welcome to DoriVac™ PaaS Environment</p>
            <p style="color:#666; margin:0;">Status: Secure Session Active | Session ID: DS-RX-9912</p>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("글로벌 파트너사가 자사의 항원을 도리백 플랫폼에 탑재하고 결과를 실시간으로 예측해볼 수 있는 **'디지털 쇼룸'**입니다.")

    st.markdown("---")

    col_input, col_sim = st.columns([1, 2])

    with col_input:
        # =========================================================================
        # [메커니즘 2. 'Cargo-to-Vehicle' 매칭 시뮬레이션]
        # =========================================================================
        st.subheader("🛠️ Step 1: Input Partner Cargo")
        st.write("자사의 미공개 항원(Cargo) 특성을 입력하세요.")
        
        # 실제 데이터를 업로드하는 느낌을 주는 위젯
        cargo_type = st.selectbox("1. Cargo Modality", ["Nucleic Acid (mRNA/siRNA)", "Protein/Antigen", "Viral Vector", "Small Molecule"])
        
        if cargo_type == "Protein/Antigen":
            cargo_complex = st.select_slider("2. Cargo Molecular Complexity", options=["Low", "Mid", "High"], value="Mid")
            st.write("3. Cargo Sequence Data (Optional)")
            uploaded_file = st.file_uploader("sequence.csv (예시)", type=['csv', 'fasta'])
            if uploaded_file:
                st.success("Sequence Data Accepted")
        else:
            st.info("핵산 기반 화물은 표준 오리가미 패턴을 적용합니다.")
            cargo_complex = "Low" # 핵산은 상대적으로 단순하게 가정

        st.subheader("🔬 Step 2: DoriVac Design Parameter")
        st.write("도리백 플랫폼의 핵심 설계를 조절합니다.")
        
        # 형님의 핵심 로직인 '간격' 슬라이더를 파트너가 조절하게 유도
        spacing = st.slider("Target Nanolink Spacing (nm)", 1.0, 10.0, 3.5, 0.1, help="면역 반응 극대화를 위한 간격을 조절합니다. 최적치는 3.5nm입니다.")
        antigen_count = st.number_input("Cargo Capacity (Units)", 1, 12, 6)

        simulate_btn = st.button("▶️ Run Matching Simulation", type="primary")

    with col_sim:
        st.subheader("🌐 Step 3: Real-time Digital Twin View")
        if simulate_btn:
            with st.spinner("빅파마 파트너 화물과 도리백 플랫폼의 적합성을 분석 중..."):
                time.sleep(2) # 시뮬레이션 하는 느낌을 줌
                st.success("Matching Analysis Complete")

                c_metric1, c_metric2 = st.columns(2)
                
                # 가상의 적합성 수치 계산 로직 (형님 로직 반영)
                # 간격이 3.5에 가까울수록, complexity가 Mid 이하일수록 점수가 높게 설정
                spacing_score = np.exp(-((spacing - 3.5)**2) / (2 * 1.5**2))
                
                complex_mod = 1.0
                if cargo_complex == "High": complex_mod = 0.7
                elif cargo_complex == "Low": complex_mod = 1.2
                
                match_score = (spacing_score * 0.7 + complex_mod * 0.3) * 100
                if match_score > 100: match_score = 100

                c_metric1.metric("Cargo Compatibility", f"{match_score:.1f}%", f"vs Standard Platform")
                c_metric2.metric("Predicted Immune Activation", f"{(spacing_score * 100):.1f}%", f"{abs(3.5-spacing):.1f}nm to Opt.")

                # 3D 시각화 (도리백 판 위 항원 배치) - 이전 코드 활용
                fig_3d = go.Figure()
                
                # DNA 오리가미 베이스 판
                fig_3d.add_trace(go.Mesh3d(
                    x=[0, 12, 12, 0], y=[0, 0, 12, 12], z=[0, 0, 0, 0], 
                    color='lightgray', opacity=0.3, name="DoriVac Base"
                ))
                
                # 항원 배치 로직
                x_pos = np.arange(antigen_count) * (spacing / 2)
                fig_3d.add_trace(go.Scatter3d(
                    x=x_pos, y=[6]*antigen_count, z=[0.8]*antigen_count,
                    mode='markers+text',
                    text=[f"Cargo {i+1}" for i in range(antigen_count)],
                    marker=dict(size=12, color='#ed1c24', symbol='circle', line=dict(color='white', width=2)), # 색상을 다이이찌산쿄 레드로 설정
                    name="Partner Cargo"
                ))
                
                fig_3d.update_layout(
                    margin=dict(l=0, r=0, b=0, t=0),
                    scene=dict(
                        xaxis_title='X (nm)', yaxis_title='Y (nm)', zaxis_title='Z (nm)',
                        aspectmode='manual', aspectratio=dict(x=2, y=1, z=0.5),
                        camera=dict(eye=dict(x=1.5, y=1.5, z=1.2))
                    )
                )
                st.plotly_chart(fig_3d, use_container_width=True)
                
                # 3.5nm 도달 시 벌룬 이벤트
                if 3.3 <= spacing <= 3.7:
                    st.balloons()
                    st.info("면역 활성화 성적표가 극대화되는 황금 간격에 도달했습니다.")

        else:
            st.info("Step 1과 2를 설정하고 'Run Matching Simulation' 버튼을 눌러 시뮬레이션을 시작하세요.")

    st.markdown("---")
    
    # =========================================================================
    # [메커니즘 3. 예측 성적표 (Predictive Scorecard) 발급]
    # =========================================================================
    if simulate_btn:
        st.subheader("📋 [Efficacy Prediction Report] Generation")
        with st.expander("성적표 상세보기", expanded=True):
            st.write(f"본 리포트는 다이이찌산쿄의 입력 화물({cargo_type})과 도리백 플랫폼({spacing}nm 간격)의 가상 매칭 결과입니다.")
            
            c_rpt1, c_rpt2, c_rpt3 = st.columns(3)
            
            # 성적표 데이터 시뮬레이션
            efficiency = match_score / 100 * 0.95 + 0.03
            safety = 1.0 - (12-antigen_count)*0.01
            reduc_cost = 0.8
            
            c_rpt1.metric("Predicted Efficiency Score", f"{efficiency:.1%}", "vs Conventional LNP")
            c_rpt2.metric("Predicted Safety Profile", "High", "with Repeated Dosing")
            c_rpt3.metric("Cost Reduction (In-silico)", f"{reduc_cost:.0%}", "on R&D Phase")
            
            st.markdown(f"""
                **[전문가 분석 요약]**
                * 다이이찌산쿄의 화물 특성을 고려할 때, 도리백 플랫폼은 기존 LNP 대비 면역 원성을 **{(efficiency*100):.1f}%** 향상시킬 가능성이 높습니다.
                * {spacing}nm의 간격 설계는 면역 증강제의 조직화를 최적화하여 반복 투여 시에도 높은 안전성 프로파일을 유지할 것으로 예측됩니다.
                * CMC(제조 및 품질관리) 난이도는 '{cargo_complex}' 화물 특성상 **'Low-Mid'** 수준으로, 글로벌 상업화 공정 도입에 유리합니다.
            """)
            st.button("📥 Download PDF Report")

    # =========================================================================
    # [메커니즘 4. 실시간 기술 상담 (Communication Bridge)]
    # =========================================================================
    st.markdown("---")
    st.subheader("☎️ Step 4: Expert Bridge")
    st.write("시뮬레이션 결과를 바탕으로 도리나노 기술팀에게 구체적인 검토를 요청하세요.")
    
    st.text_area("문의 사항 (예: 위 조합으로 실제 NHP 실험이 가능한가요?)", height=100)
    col_ask1, col_ask2 = st.columns([1, 1])
    with col_ask1:
        st.button("[Request Expert Review]", type="secondary")
    with col_ask2:
        st.button("Request Wet-lab PoC Quotation")

# --- Module: Internal R&D Dashboard (기존 대시보드 - 간단히 유지) ---
elif menu == "Internal R&D Dashboard":
    st.title("📊 Internal R&D Dashboard")
    st.write("도리나노 내부 연구용 화면입니다.")
    st.metric("Total Active Programs", 4)

# --- Module: Project Management (가상 메뉴) ---
elif menu == "Project Management":
    st.title("📂 Project Management")
    st.write("진행 중인 파트너십 프로젝트를 관리합니다.")
