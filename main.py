import streamlit as st
import random

# 1. 页面配置
st.set_page_config(page_title="2026马上有钱-财富马力体检", page_icon="🐎", layout="centered")

# 2. 样式表 - 保持不动，这是核心视觉
st.markdown("""
    <style>
    .stApp { background-color: #FDF5E6; }
    .result-popup {
        background: linear-gradient(135deg, #CF3C35 0%, #B22222 100%);
        color: white; padding: 30px; border-radius: 20px;
        text-align: center; border: 3px solid #FFD700;
        box-shadow: 0px 15px 40px rgba(178,34,34,0.5);
        margin: 20px 0;
    }
    .score-font {
        font-size: 5.5rem; font-weight: bold; color: #FFD700;
        margin: 0; line-height: 1.1; text-shadow: 2px 4px 15px rgba(0,0,0,0.3);
    }
    .rank-tag {
        font-size: 1.2rem; color: #FFD700; font-weight: bold;
        background: rgba(0,0,0,0.2); padding: 8px 20px; border-radius: 50px;
        display: inline-block; margin-bottom: 15px;
    }
    .data-box {
        background: rgba(0,0,0,0.15); padding: 15px; border-radius: 15px; 
        margin: 20px 0; border: 1px dashed rgba(255,215,0,0.5);
    }
    .data-item { font-size: 1.1rem; margin: 10px 0; color: #FDF5E6; }
    .highlight-val { color: #FFD700; font-size: 1.8rem; font-weight: bold; margin: 0 5px; }
    .stButton>button {
        width: 100%; border-radius: 50px; 
        background: linear-gradient(90deg, #D32F2F 0%, #FF5252 100%);
        color: white; height: 4rem; font-size: 1.3rem; 
        border: 2px solid #FFD700; font-weight: 900;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🐎 2026 马上有钱")
st.subheader("测测你的“财富马力”报告卡")

# 3. 输入模块
with st.container(border=True):
    st.markdown('⚖️ **数据来源：国家统计局·2025年人均月收入约 4700 元**')
    income = st.number_input("您的月平均总收入 (元)", min_value=0, value=4700)
    expense = st.number_input("平均每月固定支出 (元)", min_value=1, value=5000)
    
    st.markdown("---")
    st.markdown("**💰 备用金资产 (元)**")
    st.caption("现金、余额、股票、基金等高流动资产")
    cash = st.slider("滑动调整", 0, 1000000, 10000, step=1000)
    
    st.markdown("**🧨 高息负债 (元)**")
    st.caption("年化利率 >10% 或超过“1分利”")
    debt = st.number_input("请输入总额", min_value=0, value=0)
    
    has_insurance = st.radio("是否配置了基础保障？", ["暂无", "已配置"], horizontal=True)
    generate_btn = st.button("🚀 生成我的马年财富马力海报")

# 4. 计算与结果展示
if generate_btn:
    # 提前算好所有数值，避免在 HTML 字符串里做运算
    months_val = round(cash / expense, 1) if expense > 0 else 0.0
    s_rate = (income - expense) / income if income > 0 else 0.0
    s_rate_pct = round(max(0, s_rate * 100), 1)
    
    # 算分逻辑
    score = 65
    if months_val >= 6: score += 15
    elif months_val >= 3: score += 5
    if debt > 0: score -= 25
    if has_insurance == "已配置": score += 20
    if s_rate > 0.3: score += 10
    final_score = int(max(12, min(100, score)))

    # 超越百分比
    if final_score >= 90: r_val = round(random.uniform(95.1, 99.9), 1)
    elif final_score >= 80: r_val = round(random.uniform(85.1, 95.0), 1)
    else: r_val = round(random.uniform(30.1, 85.0), 1)

    # 【关键修复点】把 HTML 模板拆解，确保渲染引擎不抽风
    html_content = f"""
    <div class="result-popup">
        <p style="letter-spacing: 3px; font-size: 0.9rem; opacity: 0.9;">智远逻辑 · 2026马年特供</p>
        <div class="rank-tag">🏆 击败了全国 {r_val}% 的主理人</div>
        <div style="margin: 15px 0;">
            <div class="score-font">{final_score}</div>
            <p style="font-size: 1.1rem; opacity: 0.9;">财富马力综合评分</p>
        </div>
        <div class="data-box">
            <div class="data-item">防御时长 <span class="highlight-val">{months_val}</span> 个月</div>
            <div class="data-item">马力储备 <span class="highlight-val">{s_rate_pct}%</span></div>
        </div>
        <p style="font-style: italic; color: #FFD700; font-size: 0.9rem; margin-top: 15px;">
            “底座稳，马力才足。2026 马上有钱！”
        </p>
    </div>
    """
    
    # 强制使用 markdown 渲染 HTML
    st.markdown(html_content, unsafe_allow_html=True)
    
    st.info("💡 **提分锦囊**：截屏分享海报后，关注公众号 **「智远逻辑」** 回复 **“马力”** 获取方案。")
    st.balloons()

st.markdown("---")
st.markdown('<p style="text-align: center; color: #888; font-size: 0.8rem;">智远：自己的财，自己理。</p>', unsafe_allow_html=True)