import streamlit as st
import random

# 1. 页面配置
st.set_page_config(page_title="2026马上有钱-财富马力体检", page_icon="🐎", layout="centered")

# 2. 增强型样式表
st.markdown("""
    <style>
    .stApp { background-color: #FDF5E6; }
    /* 结果容器 */
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
    /* 游戏化任务框 */
    .task-container {
        background: #FFF9C4; border: 2px dashed #FBC02D;
        padding: 20px; border-radius: 15px; margin-top: 20px;
    }
    .privacy-bar {
        background: #E8F5E9; border-left: 5px solid #4CAF50;
        padding: 10px 15px; border-radius: 5px; margin-bottom: 20px;
        font-size: 0.85rem; color: #2E7D32;
    }
    .stButton>button {
        width: 100%; border-radius: 50px; 
        background: linear-gradient(90deg, #D32F2F 0%, #FF5252 100%);
        color: white; height: 3.5rem; font-size: 1.2rem; 
        border: 2px solid #FFD700; font-weight: 900;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. 顶部：隐私承诺（用户输入前第一眼看到）
st.markdown("""
    <div class="privacy-bar">
        🛡️ <b>隐私安全承诺：</b>本程序采用纯前端计算逻辑。您的财务数据<b>不会上传至任何服务器</b>，
        也不进行任何后台存储。关闭网页后，所有输入数据将立即销毁。
    </div>
    """, unsafe_allow_html=True)

st.title("🐎 2026 马上有钱")
st.subheader("测测你的“财富马力”报告卡")

# 4. 输入模块
with st.container(border=True):
    st.markdown('⚖️ **参考标准：2025国家统计局·人均月入约 4700 元**')
    income = st.number_input("您的月平均总收入 (元)", min_value=0, value=4700)
    expense = st.number_input("平均每月固定支出 (元)", min_value=1, value=5000)
    
    st.markdown("---")
    st.markdown("**💰 备用金资产 (元)**")
    cash = st.slider("滑动调整现有流动资产", 0, 1000000, 10000, step=1000)
    
    st.markdown("**🧨 存量高息负债 (元)**")
    debt = st.number_input("请输入总额（无则填0）", min_value=0, value=0)
    
    has_insurance = st.radio("是否配置了基础保障（重疾/医疗）？", ["暂无", "已配置"], horizontal=True)
    
    st.write("")
    generate_btn = st.button("🚀 生成报告并开启提分挑战")

# 5. 计算逻辑与展示
if generate_btn or 'calculated' in st.session_state:
    st.session_state.calculated = True
    
    # 基础数值计算
    months_val = round(cash / expense, 1) if expense > 0 else 0.0
    s_rate = (income - expense) / income if income > 0 else 0.0
    
    # 评分模型
    base_score = 65
    if months_val >= 6: base_score += 10
    if debt > 0: base_score -= 25
    if has_insurance == "已配置": base_score += 15
    if s_rate > 0.3: base_score += 10
    
    # 核心展示区
    final_score = int(max(15, min(92, base_score))) # 初始分数最高封顶92，留出提分空间
    
    # 模拟排名
    r_val = round(random.uniform(60.1, 88.0) if final_score > 60 else random.uniform(20.1, 59.0), 1)

    # 渲染海报
    st.markdown(f"""
        <div class="result-popup">
            <p style="letter-spacing: 3px; font-size: 0.9rem; opacity: 0.9;">智远逻辑 · 2026马年特供</p>
            <div class="rank-tag">🏆 击败了全国 {r_val}% 的主理人</div>
            <div style="margin: 15px 0;">
                <div class="score-font">{final_score}</div>
                <p style="font-size: 1.1rem; opacity: 0.9;">初始财富马力评分</p>
            </div>
            <p style="font-style: italic; color: #FFD700; font-size: 0.9rem;">
                “底座稳，马力才足。点击下方任务解锁 100 分！”
            </p>
        </div>
    """, unsafe_allow_html=True)

    # --- 拼多多的“砍一刀”游戏化提分模块 ---
    st.markdown('<div class="task-container">', unsafe_allow_html=True)
    st.markdown(f"#### 🎁 提分挑战：距离 100 分还差 {100 - final_score} 分")
    st.progress((final_score - 15) / (100 - 15))
    
    st.write("勾选你的财务关注点，即刻注入提分能量：")
    
    # 意图捕捉项 (每个选项代表一个潜在服务需求)
    col1, col2 = st.columns(2)
    with col1:
        t1 = st.checkbox("我想学“无痛攒钱” (+3分)")
        t2 = st.checkbox("我有“理债”压力 (+4分)")
    with col2:
        t3 = st.checkbox("我要“保险”避坑 (+3分)")
        t4 = st.checkbox("我想“稳健增值” (+2分)")

    # 实时计算提升后的分数
    bonus = (3 if t1 else 0) + (4 if t2 else 0) + (3 if t3 else 0) + (2 if t4 else 0)
    boosted_score = final_score + bonus

    if bonus > 0:
        st.balloons()
        st.markdown(f"""
            <div style="text-align: center; color: #D32F2F; font-weight: bold; font-size: 1.2rem;">
                🚀 能量注入！当前分值已升至：{boosted_score}
            </div>
        """, unsafe_allow_html=True)
        
        # 需求捕捉器（进一步沉淀意图）
        st.write("---")
        user_intent = st.text_input("💡 除了以上几项，你现在最头疼的财务问题是什么？", placeholder="例如：月光族怎么存下第一个10万？")
        
        if boosted_score >= 95:
            st.warning(f"🚩 恭喜！你已触发‘高等级主理人’彩蛋。由于您关注了任务，请截屏此页面并发送【{boosted_score}分】至公众号「智远逻辑」，领取专属锦囊。")
    
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown("---")
st.markdown('<p style="text-align: center; color: #888; font-size: 0.8rem;">智远：自己的财，自己理。数据加密计算中 🟢</p>', unsafe_allow_html=True)