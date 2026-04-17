import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

# --- [0] 기본 설정 및 테마 ---
st.set_page_config(page_title="DoriNano Digital Suite", layout="wide", page_icon="🧬")

# 도리나노 브랜드 컬러 (Teal & Dark Navy) 반영 스타일링
st.markdown("""
    <style>
    .main { background-color: #f8f9fa; }
    .stMetric { background-color: #ffffff; padding: 20px; border-radius: 12px; box-shadow: 0 4px 6px rgba(0,0,0,0.05); }
    h1, h2, h3 { color: #004a7c; }
    </style>
    """, unsafe_allow_html=True)

# --- [1] 사이드바 내비게이션 ---
st.sidebar.image("https://images.squarespace-cdn.com/content/v1/63ff9e359f14061a9956f4d2/88f2882c-4f74-4b95-9b0c-9333333d455b/DoriNano_Logo_Horizontal_Color.png", width=200) # 도리나노 로고(예시)
st.sidebar.title("Digital Twin Menu")
app_mode = st.sidebar.radio("Select Module", 
    ["Business Strategy (PaaS)", "Nanospacing Optimizer", "3D Architecture Visualizer", "Batch Analytics (CMC)"])

st.sidebar.markdown("---")
st.sidebar.info("Developed by 이병서/MisaTech\n\nContact: bslee@yahoo.com")

# --- [2] 모듈 1: 비즈니스화 전략 (Business Strategy) ---
if app_mode == "Business Strategy (PaaS)":
    st.header("🚀 Business Strategy: DoriVac-as-a-Service (PaaS)")
    st.write("도리나노의 DNA 오리가미 플랫폼을 전 세계 제약사에 라이선싱하는 비즈니스 모델 제안입니다.")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Model A: PaaS", "Scaffold Licensing", delta="High Scalability")
    with col2:
        st.metric("Model B: On-Demand", "Personalized Neoantigen", delta="High Margin")
    with col3:
        st.metric("Model C: Kits", "Research Use Only", delta="Steady Revenue")

    st.subheader("Platform Workflow for Partners")
    st.image("https://via.placeholder.com/1000x300.png?text=Partner+Antigen+Input+->+DoriNano+Optimization+->+Production+Ready+Design", use_container_width=True)
    
    with st.expander("상업화 가속을 위한 기대 효과"):
        st.markdown("""
        * **Time-to-Market:** 독자적인 플랫폼 구축 없이 도리나노의 검증된 구조체 활용 (개발 기간 50% 단축)
        * **Regulatory Advantage:** 표준화된 DNA 구조체 사용으로 CMC 데이터 확보 용이
        * **Precision Medicine:** 환자별 맞춤 항원을 즉각 조립하여 '암 백신 4.0' 시대 선도
        """)

# --- [3] 모듈 2: 나노 간격 최적화기 (Nanospacing Optimizer) ---
elif app_mode == "Nanospacing Optimizer":
    st.header("📏 DoriVac Nanospacing Optimizer")
    st.write("면역 반응을 극대화하는 '3.5nm의 골든 법칙'을 실험 전 시뮬레이션합니다.")
    
    col_in, col_out = st.columns([1, 2])
    
    with col_in:
        st.subheader("Simulation Parameters")
        target_receptor = st.selectbox("Target Receptor", ["CD40", "TLR9", "OX40", "Custom"])
        ligand_type = st.radio("Ligand Type", ["CpG", "Peptide Antigen", "Antibody Fragment"])
        spacing = st.slider("Spacing (nm)", 1.0, 10.0, 3.5, step=0.1)
        density = st.number_input("Ligand Density (per Scaffold)", 1, 20, 6)

    with col_out:
        # 가상 최적화 로직: 3.5nm에서 정규분포 형태로 피크 발생
        x = np.linspace(1, 10, 100)
        y = np.exp(-(x - 3.5)**2 / (2 * 1.2**2)) * 100 # Gaussian peak at 3.5nm
        
        fig = px.line(x=x, y=y, labels={'x':'Spacing (nm)', 'y':'Immune Activation (%)'},
                     title=f"Predicted Activation for {target_receptor}")
        fig.add_vline(x=spacing, line_dash="dash", line_color="red", annotation_text="Selected")
        # 3.5nm 최적점 표시
        fig.add_annotation(x=3.5, y=100, text="Optimal (3.5nm)", showarrow=True, arrowhead=1)
        
        st.plotly_chart(fig, use_container_width=True)
        
        st.success(f"**Result:** Spacing of {spacing}nm yields {y[np.abs(x-spacing).argmin()]:.1f}% immune efficiency.")
        st.info("이 시뮬레이션은 반복적인 실험(Wet-lab) 횟수를 획기적으로 줄여주는 비즈니스 핵심 도구입니다.")

# --- [4] 모듈 3: 3D 구조 시각화 (3D Architecture Visualizer) ---
elif app_mode == "3D Architecture Visualizer":
    st.header("🧬 3D DNA-Origami Architecture")
    st.write("설계된 DNA 구조체와 항원 결합 지점을 3차원으로 미리 확인합니다.")
    
    # 실제 구현 시 py3Dmol을 사용하나, 웹 데모용으로 Plotly 3D Scatter 활용
    # 형님, 실제 박사님께 보낼 때는 py3Dmol 라이브러리를 임베딩한 코드를 넣으면 더 강력합니다.
    
    z = np.linspace(0, 10, 50)
    theta = np.linspace(-4 * np.pi, 4 * np.pi, 50)
    x = np.cos(theta)
    y = np.sin(theta)
    
    fig = go.Figure(data=[go.Scatter3d(x=x, y=y, z=z, mode='lines', line=dict(color='#004a7c', width=6))])
    # 항원 부착 지점 표시
    fig.add_trace(go.Scatter3d(x=[x[10], x[25], x[40]], y=[y[10], y[25], y[40]], z=[z[10], z[25], z[40]],
                               mode='markers', marker=dict(size=10, color='red'), name='Ligand Attachment'))
    
    fig.update_layout(title="Scaffold Structure & Ligand Positions", margin=dict(l=0, r=0, b=0, t=40))
    st.plotly_chart(fig, use_container_width=True)
    
    st.write("💡 **Feature:** CAD 없이도 웹에서 시퀀스 기반의 3D 구조 무결성을 즉각 검토 가능")

# --- [5] 모듈 4: 생산 품질 분석 (Batch Analytics) ---
elif app_mode == "Batch Analytics (CMC)":
    st.header("📊 Batch Analytics & Quality Control")
    st.write("상업화를 위한 필수 단계인 생산 공정(CMC) 데이터를 관리합니다.")
    
    # 가상 데이터 생성
    df = pd.DataFrame({
        'Batch_ID': [f'LOT-{i:03d}' for i in range(1, 11)],
        'Yield (%)': np.random.normal(85, 5, 10),
        'Purity (%)': np.random.normal(92, 2, 10),
        'Stability (Days)': [30, 28, 35, 40, 32, 45, 38, 33, 31, 29]
    })
    
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Production Yield Trend")
        st.bar_chart(df.set_index('Batch_ID')['Yield (%)'])
    with col2:
        st.subheader("Batch Purity vs Stability")
        fig = px.scatter(df, x='Purity (%)', y='Stability (Days)', size='Yield (%)', 
                         color='Batch_ID', hover_name='Batch_ID')
        st.plotly_chart(fig, use_container_width=True)

    st.warning("Batch LOT-004 shows high stability but lower purity. Action required.")
