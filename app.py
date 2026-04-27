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

# 커스텀 CSS (전문적인 메디컬 테크 느낌 연출)
st.markdown("""
    <style>
    .main { background-color: #f8f9fa; }
    .stMetric { background-color: #ffffff; padding: 15px; border-radius: 10px; box-shadow: 0 2px 4px rgba(0,0,0,0.05); }
    .sidebar .sidebar-content { background-image: linear-gradient(#2e7bcf, #052b5e); color: white; }
    h1 { color: #0f3d7a; }
    h2 { color: #1a5fb4; border-left: 5px solid #1a5fb4; padding-left: 10px; }
    </style>
    """, unsafe_allow_html=True)

# 2. 사이드바 내비게이션
st.sidebar.title("🚀 DoriVac OS v1.0")
st.sidebar.markdown("---")
menu = st.sidebar.radio(
    "Select Module",
    ["Executive Dashboard", "Antigen AI Link", "Nano-Spacing Optimizer", "Project Report"]
)

st.sidebar.markdown("---")
st.sidebar.info("Developed by MisaTech\n\nPartner: DoriNano")

# 3. 메뉴별 기능 구현

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

# --- Module 3: Nano-Spacing Optimizer (핵심 시뮬레이터) ---
elif menu == "Nano-Spacing Optimizer":
    st.title("🔬 Nano-Spacing Optimizer")
    st.markdown("DNA 오리가미 구조체 위에서 항원의 배치를 0.1nm 단위로 시뮬레이션합니다.")
    
    # 조절 영역 (사이드바가 아닌 메인 상단에 배치하여 박사님이 집중하게 함)
    c1, c2 = st.columns([1, 1])
    with c1:
        spacing = st.slider("📐 Antigen Spacing (nm)", 1.0, 10.0, 3.5, 0.1)
    with c2:
        antigen_count = st.number_input("🔢 Number of Antigens", 1, 20, 6)
    
    st.markdown("---")
    
    col_left, col_right = st.columns([1, 1])
    
    with col_left:
        st.subheader("🌐 3D Structure Twin")
        # 3D 시각화 (도리백 판 위 항원 배치)
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
            text=[f"Ag {i+1}" for i in range(antigen_count)],
            # symbol을 'sphere'에서 'circle'로 변경했습니다.
            marker=dict(size=12, color='red', symbol='circle', line=dict(color='white', width=2)),
            name="Neoantigens"
        ))
        
        fig_3d.update_layout(
            margin=dict(l=0, r=0, b=0, t=0),
            scene=dict(
                xaxis_title='X (nm)', yaxis_title='Y (nm)', zaxis_title='Z (nm)',
                aspectmode='manual', aspectratio=dict(x=2, y=1, z=0.5)
            )
        )
        st.plotly_chart(fig_3d, use_container_width=True)

    with col_right:
        st.subheader("📈 Immune Efficacy Prediction")
        # 가우시안 곡선 (3.5nm에서 피크)
        x_range = np.linspace(1, 10, 100)
        y_range = np.exp(-((x_range - 3.5)**2) / (2 * 1.2**2)) 
        current_val = np.exp(-((spacing - 3.5)**2) / (2 * 1.2**2))
        
        fig_line = go.Figure()
        fig_line.add_trace(go.Scatter(x=x_range, y=y_range, name="Efficiency Curve", line=dict(color='#1a5fb4', width=3)))
        fig_line.add_trace(go.Scatter(
            x=[spacing], y=[current_val], 
            mode='markers+text', 
            text=[f"Efficiency: {current_val:.1%}"],
            textposition="top right",
            marker=dict(color='red', size=18, symbol='star'),
            name="Current Setting"
        ))
        
        fig_line.update_layout(
            xaxis_title="Spacing (nm)", 
            yaxis_title="Immune Activation Score",
            hovermode="x unified"
        )
        st.plotly_chart(fig_line, use_container_width=True)
        
        if 3.3 <= spacing <= 3.7:
            st.balloons()
            st.success("🎯 Optimal Spacing (3.5nm) Reached! 면역 반응이 극대화되는 지점입니다.")
        else:
            st.warning(f"최적 간격(3.5nm)까지 {abs(3.5-spacing):.1f}nm 조정이 필요합니다.")

# --- Module 4: Report ---
elif menu == "Project Report":
    st.title("📋 Project Simulation Report")
    st.write("분석된 데이터를 기반으로 합성 공정 가이드라인을 생성합니다.")
    
    report_data = {
        "Parameter": ["Target Antigen", "Antigen Count", "Simulated Spacing", "Predicted Efficacy", "Complexity Score"],
        "Value": ["Patient-A-01 (Neoantigen)", "6 units", "3.5 nm (Optimal)", "98.2%", "Low (Standardized)"]
    }
    st.table(pd.DataFrame(report_data))
    
    st.button("📥 Download PDF Report (Mockup)")
    st.button("🧪 Export DNA Sequence for Synthesis")
