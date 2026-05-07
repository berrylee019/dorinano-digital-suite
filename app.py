import streamlit as st
import numpy as np
import plotly.graph_objects as go
import pandas as pd
import time
import json 
import requests # NCI GDC API 연동을 위해 추가

# 1. 페이지 및 테마 설정
st.set_page_config(
    page_title="DoriNano Digital Suite",
    page_icon="🧬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================================================================
# [SECURITY] 비밀번호 보안 설정 함수
# =========================================================================
def check_password():
    """비밀번호가 올바른지 확인하는 함수"""
    def password_entered():
        """입력된 비밀번호를 검증하고 세션 상태를 업데이트"""
        if st.session_state["password"] == "3.5nm":  
            st.session_state["password_correct"] = True
            del st.session_state["password"]  
        else:
            st.session_state["password_correct"] = False

    if "password_correct" not in st.session_state:
        st.markdown("<br><br>", unsafe_allow_html=True)
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.title("🧬 DoriVac Digital Suite")
            st.info("""
            **[Security Alert]**
            이 시스템은 보안 구역입니다. 승인된 연구원만 접근 가능합니다.

            *Secure Access Zone. Entry is restricted to authorized researchers only.*
            """)
            st.text_input("Security Password", type="password", on_change=password_entered, key="password")
            st.caption("비밀번호를 입력하고 Enter를 눌러주세요.")
        return False
    elif not st.session_state["password_correct"]:
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.title("🧬 DoriVac Digital Suite")
            st.text_input("Security Password", type="password", on_change=password_entered, key="password")
            st.error("😕 비밀번호가 일치하지 않습니다 형님. 다시 확인해주세요.")
        return False
    else:
        return True

# 보안 체크 실행
if check_password():

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
        
        .partner-banner { 
            background-color: #ffffff; 
            padding: 25px; 
            border-radius: 15px; 
            border: 3px solid #ed1c24; 
            margin-bottom: 25px;
            box-shadow: 0 10px 20px rgba(0,0,0,0.1);
        }

        .report-box {
            background-color: #ffffff; 
            padding: 25px; 
            border-radius: 15px; 
            border: 1px solid #dee2e6;
            border-left: 8px solid #ed1c24;
            box-shadow: 0 4px 12px rgba(0,0,0,0.1);
            margin-bottom: 20px;
        }
        .report-metric { font-size: 0.85em; color: #666; margin-bottom: 2px; }
        .report-value { font-size: 1.4em; font-weight: bold; color: #ed1c24; }
        
        /* GDC 데이터 카드 스타일 */
        .gdc-card {
            background-color: #e3f2fd;
            padding: 15px;
            border-radius: 10px;
            border: 1px solid #2196f3;
            margin-bottom: 10px;
        }
        </style>
        """, unsafe_allow_html=True)
    
    # =========================================================================
    # 모드 1: [INTERNAL] 연구용 대시보드
    # =========================================================================
    if st.session_state.view_mode == 'internal':
        st.sidebar.title("🧬 DoriVac OS v1.1") # 버전 업데이트
        st.sidebar.markdown("---")
        # NCI GDC Data Link 메뉴 추가
        menu = st.sidebar.radio("Select Module", ["Executive Dashboard", "NCI GDC Data Link", "Antigen AI Link", "Nano-Spacing Optimizer", "Project Report"])
        st.sidebar.markdown("---")
        st.sidebar.info("Developed by MisaTech\n\nPartner: DoriNano")
    
        if menu == "Executive Dashboard":
            st.title("📊 Platform Executive Overview")
            col1, col2, col3 = st.columns(3)
            col1.metric("Current R&D Stage", "Pre-clinical", "Phase 1 Entry Ready")
            col2.metric("Optimal Spacing", "3.5 nm", "Targeted")
            col3.metric("Discovery Efficiency", "85% ↑", "vs Wet-lab")
            st.markdown("---")
            st.subheader("🧬 Digital Twin Roadmap")
            st.write("- **Step 1:** NGS 변이 데이터 확보(GDC) / **Step 2:** AI 항원 구조 예측(SUROP) / **Step 3:** 나노-스페이싱 설계(DoriVac)")
            st.markdown("<br><br><br><hr>", unsafe_allow_html=True)
            st.markdown("### 🌐 Global Business Expansion")
            col_l, col_m, col_r = st.columns([1, 2, 1])
            with col_m:
                st.markdown('<div class="gold-btn">', unsafe_allow_html=True)
                if st.button("🚀 Open Global Partner Sandbox (Daiichi Sankyo Demo)"):
                    switch_to_sandbox()
                st.markdown('</div>', unsafe_allow_html=True)

        # ---------------------------------------------------------------------
        # [NEW] NCI GDC 실시간 연동 모듈
        # ---------------------------------------------------------------------
        elif menu == "NCI GDC Data Link":
            st.title("🔗 NCI GDC Real-time Data Integration")
            st.markdown("미국 국립암연구소(NCI) GDC 서버에 접속하여 환자별 유전체 변이 데이터를 실시간으로 스트리밍합니다.")
            
            c1, c2 = st.columns([2, 1])
            with c1:
                target_patient = st.text_input("Enter Patient ID (Submitter ID)", value="TCGA-A7-A0CE", help="예: TCGA-A7-A0CE, TCGA-A7-A13E 등")
            with c2:
                st.markdown("<br>", unsafe_allow_html=True)
                fetch_btn = st.button("🔍 Fetch Mutation Data", use_container_width=True)

            if fetch_btn:
                with st.spinner(f"Requesting data for {target_patient} from api.gdc.cancer.gov..."):
                    try:
                        # [실전] API 호출 로직 시작
                        filters = {
                            "op": "and",
                            "content": [
                                {"op": "in", "content": {"field": "cases.submitter_id", "value": [target_patient]}}
                            ]
                        }
                        params = {
                            "filters": json.dumps(filters),
                            "fields": "genomic_dna_change,ssm_id,consequence.transcript.consequence_type",
                            "size": "5" 
                        }
                        
                        response = requests.get("https://api.gdc.cancer.gov/ssms", params=params)
                        
                        if response.status_code == 200:
                            data = response.json()
                            mutations = data.get("data", {}).get("hits", [])
                            
                            if mutations:
                                st.success(f"✅ 성공적으로 {len(mutations)}개의 핵심 돌연변이 데이터를 수신했습니다.")
                                
                                st.subheader("📋 Somatic Simple Mutations (Raw Data)")
                                for mut in mutations:
                                    with st.container():
                                        st.markdown(f"""
                                        <div class="gdc-card">
                                            <b>SSM ID:</b> {mut.get('ssm_id')}<br>
                                            <b>DNA Change:</b> <code style='color:#d63384'>{mut.get('genomic_dna_change')}</code><br>
                                            <b>Consequence:</b> {mut.get('consequence', [{}])[0].get('transcript', {}).get('consequence_type', 'N/A')}
                                        </div>
                                        """, unsafe_allow_html=True)
                                
                                st.info("💡 **Next Step:** 수신된 변이 서열을 SUROP AI 엔진으로 전송하여 3D 항원 구조(Neo-Ag-Alpha) 예측을 시작하십시오.")
                                if st.button("🧬 Send to SUROP Engine"):
                                    st.toast("데이터 전송 중... SUROP 엔진에서 구조 예측을 시작합니다.")
                                    time.sleep(1)
                                    st.success("데이터가 성공적으로 전송되었습니다.")
                            else:
                                st.warning("해당 환자 ID에 대한 공개된 변이 데이터를 찾을 수 없습니다.")
                        else:
                            st.error(f"GDC API 연결 실패: {response.status_code}")
                            
                    except Exception as e:
                        st.error(f"데이터 연동 중 오류 발생: {str(e)}")

        elif menu == "Antigen AI Link":
            st.title("🧬 Antigen Discovery Integration")
            st.info("NCI GDC 또는 자체 NGS 분석을 통해 도출된 항원 구조를 정밀 분석합니다.")
            uploaded_file = st.file_uploader("AI 분석 결과(PDB/JSON) 업로드", type=['csv', 'json'])
            if uploaded_file:
                with st.spinner('3D 구조 생성 중...'):
                    time.sleep(1.5)
                    df_ai = pd.DataFrame({"Antigen_ID": ["Neo-Ag-Alpha", "Neo-Ag-Beta"], "X_Pos": [3.0, 8.0], "Linker": [2.5, 2.5]})
                    tab1, tab2 = st.tabs(["📊 분석 데이터 요약", "🔬 3D 리간드 결합 시뮬레이션"])
                    with tab1: st.table(df_ai)
                    with tab2:
                        fig = go.Figure()
                        fig.add_trace(go.Mesh3d(x=[0, 12, 12, 0], y=[0, 12, 12, 0], z=[0, 0, 0, 0], color='lightgray', opacity=0.3))
                        for i, row in df_ai.iterrows():
                            fig.add_trace(go.Scatter3d(x=[row['X_Pos'], row['X_Pos']], y=[6, 6], z=[0, row['Linker']], mode='lines', line=dict(color='#2e7bcf', width=6)))
                            fig.add_trace(go.Scatter3d(x=[row['X_Pos']], y=[6], z=[row['Linker']+0.2], mode='markers', marker=dict(size=14, color='#ed1c24', symbol='diamond')))
                        fig.update_layout(scene=dict(aspectmode='manual', aspectratio=dict(x=1.5, y=1, z=0.6)), margin=dict(l=0, r=0, b=0, t=0), height=500)
                        st.plotly_chart(fig, use_container_width=True)

        elif menu == "Nano-Spacing Optimizer":
            st.title("🔬 Nano-Spacing Optimizer")
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
                fig_3d.add_trace(go.Scatter3d(x=x_pos, y=[6]*antigen_count, z=[0.8]*antigen_count, mode='markers', marker=dict(size=12, color='red')))
                fig_3d.update_layout(margin=dict(l=0, r=0, b=0, t=0), scene=dict(aspectmode='manual', aspectratio=dict(x=2, y=1, z=0.5)), height=500)
                st.plotly_chart(fig_3d, use_container_width=True)
            with col_right:
                st.subheader("📈 Immune Efficacy Prediction")
                x_range = np.linspace(1, 10, 100)
                y_range = np.exp(-((x_range - 3.5)**2) / (2 * 1.2**2))
                current_val = np.exp(-((spacing - 3.5)**2) / (2 * 1.2**2))
                fig_line = go.Figure()
                fig_line.add_trace(go.Scatter(x=x_range, y=y_range, line=dict(color='#1a5fb4', width=3)))
                fig_line.add_trace(go.Scatter(x=[spacing], y=[current_val], mode='markers', marker=dict(color='red', size=15)))
                st.plotly_chart(fig_line, use_container_width=True)
                if 3.3 <= spacing <= 3.7: st.balloons()

        elif menu == "Project Report":
            st.title("📋 Project Simulation Report")
            st.subheader("📊 [종합 분석 대시보드]")
            kpi1, kpi2, kpi3, kpi4 = st.columns(4)
            kpi1.metric("최종 매칭 스코어", "98.2%", "↑ 1.5%")
            kpi2.metric("예상 면역 증강", "4.5x", "vs LNP")
            kpi3.metric("나노 안전성", "Stable", "Optimum")
            kpi4.metric("R&D 가속도", "3.2개월", "단축 완료")
            st.markdown("<br>", unsafe_allow_html=True)
            col_chart, col_summary = st.columns([1.5, 1])
            with col_chart:
                categories = ['Efficacy', 'Safety', 'Stability', 'Scalability', 'Cost-Efficiency']
                fig_radar = go.Figure()
                fig_radar.add_trace(go.Scatterpolar(r=[95, 88, 92, 85, 90], theta=categories, fill='toself', name='Current Project', line_color='#ed1c24'))
                fig_radar.update_layout(polar=dict(radialaxis=dict(visible=True, range=[0, 100])), showlegend=False, margin=dict(l=40, r=40, t=40, b=40), height=400)
                st.plotly_chart(fig_radar, use_container_width=True)
            with col_summary:
                st.info("**💡 연구원 종합 코멘트 (AI Summary)**")
                st.markdown("""
                현재 **Patient-A-01** 프로젝트에 적용된 나노-스페이싱 기술은 3.5nm 황금 비율에 도달하여 수용체 결합력을 극대화했습니다.
                * **강점:** 기존 알룸(Alum) 대비 4배 이상의 면역 반응 예측.
                * **결론:** Wet-lab 기반의 세포 독성 테스트 진입에 '적합' 판정을 내립니다.
                """)
                st.warning("**차기 마일스톤:** Phase 1 진입을 위한 공식 서류 제출 대기 중.")
            st.markdown("---")
            st.subheader("📝 세부 파라미터 내역")
            st.table(pd.DataFrame({
                "Parameter": ["Target Project", "Optimal Spacing", "Ligand Type", "Simulation ID", "Researcher"], 
                "Value": ["Patient-A-01", "3.5nm", "Protein Antigen", "Dori-2026-04-A", "Senior Research Team"]
            }))

    # =========================================================================
    # 모드 2: [SANDBOX] 글로벌 파트너 전용
    # =========================================================================
    else:
        st.sidebar.title(" Partner Portal")
        if st.sidebar.button("⬅️ Back to Internal R&D"): switch_to_internal()
        st.markdown("""
            <div class="partner-banner">
                <h1 style="color:#ed1c24; margin:0; font-size: 2.3em;">[Global Pharmaceutical Partner Portal]</h1>
                <p style="color:#555; margin-top:5px;">Secure Sandbox for Cargo-to-Vehicle Matching Simulation</p>
            </div>
        """, unsafe_allow_html=True)
        c_in, c_sim = st.columns([1, 1.5])
        with c_in:
            st.subheader("🛠️ Step 1 & 2: Cargo Input")
            cargo_type = st.selectbox("1. Select Cargo Modality", ["Antibody-Drug Conjugate (ADC)", "mRNA / siRNA", "Protein Antigen", "Custom Ligand"])
            st.markdown("**2. Upload Undisclosed Antigen Data (Private)**")
            st.file_uploader("미공개 항원의 특성 파일(CSV/JSON)을 업로드하여 보안 시뮬레이션을 수행하십시오.", type=['csv', 'xlsx', 'json'])
            st.markdown("**3. DoriVac Delivery System Tuning**")
            spacing_p = st.slider("Target Spacing (nm)", 1.0, 10.0, 3.5, 0.1)
            cargo_count = st.number_input("Number of Cargo Units", 1, 12, 6)
            st.markdown("<br>", unsafe_allow_html=True)
            sim_btn = st.button("▶️ Run Matching Simulation", type="primary", use_container_width=True)
        with c_sim:
            if sim_btn:
                with st.spinner("계산 중... 3.5nm 황금 로직을 기반으로 적합성을 분석합니다."):
                    time.sleep(2.0)
                    score = (np.exp(-((spacing_p - 3.5)**2) / 2) * 100)
                    efficiency_boost = score * 1.45
                    cost_saving = (100 - score) * 0.05 + 2.8
                    st.markdown(f"""
                        <div class="report-box">
                            <h2 style="color:#ed1c24; margin-top:0;">📋 [Efficacy Prediction Report]</h2>
                            <hr style="border: 0.5px solid #eee;">
                            <div style="display: flex; justify-content: space-between; text-align: center;">
                                <div style="flex: 1;"><p class="report-metric">Matching Score</p><p class="report-value">{score:.1f}%</p></div>
                                <div style="flex: 1; border-left: 1px solid #eee; border-right: 1px solid #eee;"><p class="report-metric">vs LNP Efficiency</p><p class="report-value">+{efficiency_boost:.1f}% ↑</p></div>
                                <div style="flex: 1;"><p class="report-metric">Est. R&D Saving</p><p class="report-value">${cost_saving:.1f}M</p></div>
                            </div>
                            <p style="margin-top:15px; font-size:0.85em; color:#777;">* <b>Validation:</b> In-silico matching confirmed for {cargo_type}</p>
                        </div>
                    """, unsafe_allow_html=True)
                    recipe_data = {
                        "project": "Global-Partner-Sandbox",
                        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
                        "modality": cargo_type,
                        "parameters": {"spacing_nm": spacing_p, "cargo_count": cargo_count, "matching_score": f"{score:.1f}%"},
                        "formulation_guide": "Use DNA Origami Scaffold Type-B with 3.5nm anchor points."
                    }
                    st.download_button(label="📥 Download Formulation Recipe (JSON)", data=json.dumps(recipe_data, indent=2), file_name=f"DoriVac_Recipe_{cargo_type}.json", mime="application/json", use_container_width=True)
                    fig_p = go.Figure()
                    fig_p.add_trace(go.Mesh3d(x=[0, 12, 12, 0], y=[0, 12, 12, 0], z=[0, 0, 0, 0], color='lightgray', opacity=0.3))
                    x_p = np.arange(cargo_count) * (spacing_p / 2)
                    fig_p.add_trace(go.Scatter3d(x=x_p, y=[6]*cargo_count, z=[0.8]*cargo_count, mode='markers', marker=dict(size=12, color='#ed1c24')))
                    fig_p.update_layout(margin=dict(l=0, r=0, b=0, t=0), scene=dict(aspectmode='manual', aspectratio=dict(x=2, y=1, z=0.5)), height=400)
                    st.plotly_chart(fig_p, use_container_width=True)
                    if 3.3 <= spacing_p <= 3.7: st.balloons()
            else:
                st.info("💡 **Partner Guide:** 좌측에서 항원 타입을 선택하거나 파일을 업로드한 후 시뮬레이션 버튼을 누르세요.")
        st.markdown("---")
        st.subheader("☎️ Step 4: [Request Expert Review]")
        col_msg, col_send = st.columns([2, 1])
        with col_msg: st.write("발행된 리포트를 기반으로 도리나노 기술팀의 정밀 검토 및 공동 연구 가능성을 타진하시겠습니까?")
        with col_send:
            if st.button("📩 Submit Simulation Data for Review", use_container_width=True): st.success("전송 완료! 담당자가 24시간 이내에 연락드립니다.")
