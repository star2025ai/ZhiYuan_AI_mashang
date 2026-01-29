import streamlit as st
import random
import time

# 1. 页面配置
st.set_page_config(page_title="2026马上有钱-财富马力体检", page_icon="🐎", layout="centered")

# 2. UI 强化：红包红 + 金色按钮
st.markdown("""
    <style>
    .stApp { background-color: #FDF5E6; }
    .result-popup {
        background: linear-gradient(135deg, #CF3C35 0%, #B22222 100%);
        color: white; padding: 30px; border-radius: 20px;
        text-align: center; border: 3px solid #FFD700;
        box-shadow: 0px 15px 40px rgba(178,34,34,0.5);
    }
    .score-font {
        font-size: 5.5rem; font-weight: bold; color: #FFD700;
        margin: 0; line-height: 1.1; text-shadow: 2px 4px 15px rgba(0,0,0,0.3);
    }
    .stButton>button {
        width: 100%; border-radius: 50px; 
        background: linear-gradient(90deg, #D32F2F 0%, #FF5252 100%);
        color: white; height: 4rem; font-size: 1.3rem; 
        border: 2px solid #FFD700; font-weight: 900;
        box-shadow: 0 4px 15px rgba(211,47,47,0.4);
    }
    .data-source {
        font-size: 0.8rem; color: #888; margin-bottom: 5px; font-style: italic;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. 认知库
COGNITION_BASE = [
    "钱是自由的工具，你是它的主人。",
    "底座稳，马力才足。理财的第一步是建立防御。",
    "2026马年：稳扎稳打，马上有钱！",
    "高息债是财富的黑洞，清债是最高效的投资。"
]

# 4. 主界面
st.title("🐎 2026 马上有钱")
st.subheader("测测你的“财富马力”报告卡")

# 5. 输入模块
with st.container(border=True):
    # --- 收入部分 ---
    st.markdown('<p class="data-source">参考：2025年国家统计局数据，全国城镇居民人均可支配收入约 4700 元/月</p>', unsafe_allow_html=True)
    income = st.number_input("您的月平均总收入 (元)", min_value=0, value=4700, step=100)
    
    # --- 支出部分 ---
    expense = st.number_input("平均每月固定支出 (元)", min_value=1, value=5000, step=100)
    
    # --- 备用金部分（直接显示定义） ---
    st.write("---")
    st.markdown("**手头现金及高流动资产 (元)**")
    st.caption("包括：现金、微信支付宝余额、股票、基金、债券等可随时变现的资产")
    cash = st.slider("滑动调整数额", 0, 500000, 10000, step=1000)
    
    # --- 负债部分（直接显示利息转换） ---
    st.write("---")
    st.markdown("**高息负债总额 (元)**")
    st.caption("指年化利率 >10% 或超过“1分利”的债务（1分利≈年化12%）")
    debt = st.number_input("输入负债金额", min_value=0, value=0, step=1000)
    
    # --- 保险部分 ---
    has_insurance = st.radio("是否配置了重疾/医疗等基础保障？", ["暂无", "已配置"], horizontal=True)

    st.write("")
    generate_btn = st.button("🚀 生成我的马年财富马力海报")

# 6. 结果生成逻辑
if generate_btn:
    with st.status("正在注入马力，开启好运...", expanded=False):
        time.sleep(1.2)
        
        # 计算逻辑
        months = cash / expense if expense > 0 else 0
        
        # 评分模型
        score = 65
        if months >= 6: score += 15
        elif months >= 3: score += 5
        if debt > 0: score -= 25
        if has_insurance == "已配置": score += 20
        # 加上收入对结余率的潜在贡献感
        if income > expense: score += 5
        
        score = max(8, min(100, score))

        # 结果海报卡片
        st.markdown(f"""
            <div class="result-popup">
                <p style="color: #FFD700; letter-spacing: 3px; font-weight: bold;">智远逻辑 · 2026新年特供</p>
                <div style="margin: 10px 0;">
                    <span style="font-size: 1.2rem; vertical-align: middle;">您的马力评分：</span>
                    <div class="score-font">{score}</div>
                </div>
                <div style="background: rgba(0,0,0,0.15); padding: 15px; border-radius: 15px; margin: 20px 0; border: 1px dashed rgba(255,215,0,0.5);">
                    <p style="margin:0; font-size: 1.1rem;">防御时长：<span style="color: #FFD700; font-size: 1.8rem; font-weight: bold;">{months:.1f}</span> 个月</p>
                    <p style="font-size: 0.8rem; margin-top:5px; color: #FDF5E6; opacity: 0.8;">（即使不工作，您也能稳坐钓鱼台的时间）</p>
                </div>
                <p style="font-style: italic; color: #FFD700; font-size: 0.95rem;">
                    “{random.choice(COGNITION_BASE)}”
                </p>
            </div>
        """, unsafe_allow_html=True)

        # 引导关注
        st.markdown(f"""
            <div style="background-color: #FFF3E0; border: 1px solid #FFB74D; padding: 15px; border-radius: 12px; text-align: center; margin-top: 15px;">
                <p style="color: #E65100; font-weight: bold; margin-bottom: 5px;">📥 想要在马年提升财富马力？</p>
                <p style="font-size: 0.85rem; color: #444;">截屏海报分享后，搜索并关注公众号<br><b>「智远逻辑」</b> 回复 <b>“马力”</b> 获取锦囊</p>
            </div>
        """, unsafe_allow_html=True)
        st.balloons()

# 7. 页脚
st.markdown("---")
st.markdown('<p style="text-align: center; color: #888; font-size: 0.8rem;">智远：自己的财，自己理。祝您马年马力十足！</p>', unsafe_allow_html=True)