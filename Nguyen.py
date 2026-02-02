import streamlit as st
from datetime import datetime

# ==================== CẤU HÌNH ====================
IMAGE_URL = "https://scontent.fdad3-6.fna.fbcdn.net/v/t1.15752-9/619246154_1621612339012038_4298887169126451992_n.jpg?stp=dst-jpg_s2048x2048_tt6&_nc_cat=110&ccb=1-7&_nc_sid=9f807c&_nc_eui2=AeEonldaM9u606F593lEnYDvrOQjkOLxWJKs5COQ4vFYkmLh6gXvoUZ7yW0_IrlvD38Q9zdDFyuo-3gAGmk5Zu_1&_nc_ohc=ImZZYNuS5u0Q7kNvwG74M0T&_nc_oc=AdnaIsR3FqUw-8tGdw3vI7kOw9oGPFQRaNyqOCUbqOJoYn3hhvbDoL-KXN2Bg7m7THo&_nc_zt=23&_nc_ht=scontent.fdad3-6.fna&oh=03_Q7cD4QEmk9v0lJZiUqvyjMOEBBt4uXSEV0qwUZuPuACA6Ioz6Q&oe=69A21933"

# Các câu dễ thương khi bấm nút
SURPRISE_MESSAGES = [
    {"title": "Yayy!", "message": "Muốn nhận quà lắm rồi chứ gì!", "emoji": "🥳", "color": "#ff6b9d"},
    {"title": "Wowww!", "message": "Lần thứ 2 rồi đó! Cậu đang nôn nóng lắm rồi đúng không?", "emoji": "😜", "color": "#ffd93d"},
    {"title": "Ồ làaaa!", "message": "3 lần rồi nè! Mình đoán là cậu rất mất kiên nhẫn rồi nhỉ? Con người OCD", "emoji": "🤪", "color": "#6bcf7f"},
    {"title": "Ngọt ngàooo!", "message": "Thôi thì chuẩn bị nhận quà nhé!", "emoji": "😍", "color": "#ff9ff3"},
    {"title": "Quà tặngg!", "message": "Được đi chơi với cậu là món quà đối với mình!", "emoji": "🎁", "color": "#ff5252"},
    {"title": "Lấp lánhhh!", "message": "Mắt cậu lấp lánh như sao trời!", "emoji": "🤩", "color": "#feca57"},
    {"title": "Tỏa sáng!", "message": "Nụ cười cậu tỏa nắng!", "emoji": "☀️", "color": "#ffbe76"},
    {"title": "Hoa hoa!", "message": "Cậu như bông hoa xinh đẹp!", "emoji": "🌸", "color": "#ff7675"},
    {"title": "Hi hi!", "message": "Không phải con nghé", "emoji": "🐄", "color": "#ff7675"},
    {"title": "Nghệ sĩiii!", "message": "Nếu có mình là họa sĩ!", "emoji": "🎨", "color": "#74b9ff"},
    {"title": "Họa sĩiii!", "message": "Thì mình sẽ vẽ mãi nụ cười trên môi cậu!", "emoji": "🎨", "color": "#74b9ff"},
    {"title": "Mong muốnnn!", "message": "Cười nhiều lên nhé cô gái", "emoji": "😻", "color": "#e17055"},
]

# ==================== PAGE CONFIG ====================
st.set_page_config(
    page_title="Dành cho Nguyên",
    page_icon="🥰",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ==================== HIDE STREAMLIT UI & STYLING ====================
st.markdown("""
<style>
/* Hide Streamlit elements */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
.stDeployButton {display:none;}
div[data-testid="stToolbar"] {display: none;}
div[data-testid="stDecoration"] {display: none;}
div[data-testid="stStatusWidget"] {display: none;}
section[data-testid="stSidebar"] {display: none;}
.block-container {padding: 0 !important; max-width: 100% !important;}
div[data-testid="stVerticalBlock"] {gap: 0 !important;}

/* Background */
body, .stApp, [data-testid="stAppViewContainer"] {
    background: linear-gradient(135deg, #ffecd2 0%, #fcb69f 25%, #ff9a9e 50%, #fad0c4 75%, #ffecd2 100%) !important;
    background-size: 400% 400% !important;
    animation: gradientShift 15s ease infinite !important;
    background-attachment: fixed !important;
}

@keyframes gradientShift {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}

/* Main container */
.main-container {
    max-width: 700px;
    margin: 20px auto;
    padding: 0 15px 120px 15px;
}

/* Card styling */
.cute-card {
    background: rgba(255, 255, 255, 0.6) !important;
    backdrop-filter: blur(20px);
    border-radius: 30px;
    padding: 35px 30px;
    box-shadow: 0 15px 40px rgba(255, 182, 193, 0.5);
    border: 4px solid rgba(255, 255, 255, 0.9);
    text-align: center;
}

.cute-card img {
    max-width: 350px;
    width: 100%;
    height: auto;
    aspect-ratio: 2/3;
    object-fit: cover;
    border-radius: 25px;
    box-shadow: 0 10px 30px rgba(255, 182, 193, 0.6);
    border: 4px solid white;
    margin-bottom: 15px;
}

/* Message text - FIX MÀU */
.cute-message {
    color: #ff1493 !important;
    font-size: 19px;
    line-height: 2;
    text-align: center;
    text-shadow: 2px 2px 4px rgba(255, 255, 255, 0.9);
    margin: 15px 0 25px 0;
    font-weight: 700;
    font-family: 'Quicksand', sans-serif;
}

/* Footer text - FIX MÀU */
.cute-footer {
    font-family: 'Pacifico', cursive;
    font-size: 26px;
    color: #ff1493 !important;
    text-shadow: 2px 2px 6px rgba(255, 255, 255, 0.9);
    margin: 25px 0 15px 0;
    font-weight: bold;
}

/* Time text */
.cute-time {
    font-size: 14px;
    color: #ff4d7d !important;
    opacity: 1;
    font-weight: 600;
}

/* Counter badge */
.counter-badge {
    position: fixed;
    top: 15px;
    left: 15px;
    background: linear-gradient(135deg, #ff1493 0%, #ff69b4 100%);
    backdrop-filter: blur(10px);
    padding: 14px 24px;
    border-radius: 30px;
    font-size: 20px;
    font-weight: bold;
    color: white;
    box-shadow: 0 8px 25px rgba(255, 20, 147, 0.5);
    z-index: 2000;
    animation: bounce 2s ease-in-out infinite;
    border: 3px solid white;
}

@keyframes bounce {
    0%, 100% { transform: translateY(0) scale(1) rotate(-3deg); }
    50% { transform: translateY(-10px) scale(1.08) rotate(3deg); }
}

/* Popup overlay */
.popup-overlay {
    position: fixed;
    top: 0;
    left: 0;
    width: 100vw;
    height: 100vh;
    background: rgba(255, 182, 193, 0.4);
    backdrop-filter: blur(15px);
    z-index: 9999;
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 20px;
    animation: fadeIn 0.3s ease-out;
}

.popup-box {
    border-radius: 35px;
    padding: 50px 40px;
    max-width: 450px;
    width: 100%;
    box-shadow: 0 30px 70px rgba(255, 107, 157, 0.6);
    text-align: center;
    position: relative;
    overflow: hidden;
    animation: popupBounce 0.7s cubic-bezier(0.68, -0.55, 0.265, 1.55);
    border: 5px solid white;
}

.popup-emoji {
    font-size: 95px;
    margin-bottom: 20px;
    animation: emojiJump 1s ease-out;
    display: inline-block;
}

.popup-title {
    font-family: 'Pacifico', cursive;
    font-size: 36px;
    color: white;
    margin-bottom: 15px;
    text-shadow: 4px 4px 8px rgba(0, 0, 0, 0.3);
}

.popup-message {
    font-size: 20px;
    color: white;
    line-height: 1.7;
    margin-bottom: 25px;
    text-shadow: 3px 3px 6px rgba(0, 0, 0, 0.2);
    font-weight: 700;
}

.popup-hearts span {
    font-size: 38px;
    margin: 0 6px;
    animation: heartDance 1s ease-in-out infinite;
    display: inline-block;
}

/* Animations */
@keyframes fadeIn { 
    from {opacity: 0;} 
    to {opacity: 1;} 
}

@keyframes popupBounce {
    0% { opacity: 0; transform: scale(0.3) rotate(-20deg); }
    50% { transform: scale(1.15) rotate(10deg); }
    70% { transform: scale(0.95) rotate(-5deg); }
    100% { opacity: 1; transform: scale(1) rotate(0deg); }
}

@keyframes emojiJump {
    0%, 100% { transform: scale(1) rotate(0deg); }
    25% { transform: scale(1.4) rotate(-15deg); }
    50% { transform: scale(0.9) rotate(15deg); }
    75% { transform: scale(1.3) rotate(-10deg); }
}

@keyframes heartDance {
    0%, 100% { transform: translateY(0) scale(1) rotate(0deg); }
    25% { transform: translateY(-20px) scale(1.4) rotate(-15deg); }
    75% { transform: translateY(-10px) scale(1.2) rotate(15deg); }
}

/* Button styling */
.stButton {
    position: fixed;
    bottom: 20px;
    left: 50%;
    transform: translateX(-50%);
    z-index: 10000;
    width: calc(100% - 40px);
    max-width: 450px;
}

.stButton > button {
    background: linear-gradient(135deg, #ff1493 0%, #ff69b4 100%) !important;
    color: white !important;
    font-size: 22px !important;
    font-weight: bold !important;
    padding: 20px 45px !important;
    border: 5px solid white !important;
    border-radius: 50px !important;
    box-shadow: 0 10px 30px rgba(255, 20, 147, 0.6) !important;
    width: 100% !important;
    font-family: 'Quicksand', sans-serif !important;
    cursor: pointer !important;
    transition: all 0.3s ease !important;
}

.stButton > button:hover {
    transform: scale(1.05) !important;
    box-shadow: 0 15px 40px rgba(255, 20, 147, 0.8) !important;
}

.stButton > button:active {
    transform: scale(0.98) !important;
}

/* Responsive */
@media (max-width: 768px) {
    .cute-card { padding: 28px 22px; }
    .cute-card img { max-width: 280px; margin-bottom: 12px; }
    .cute-message { font-size: 17px; }
    .cute-footer { font-size: 24px; }
    .popup-box { padding: 40px 32px; }
    .popup-emoji { font-size: 80px; }
    .popup-title { font-size: 32px; }
    .popup-message { font-size: 18px; }
    .counter-badge { font-size: 18px; padding: 12px 20px; }
    .stButton > button { font-size: 20px !important; padding: 18px 40px !important; }
}

@media (max-width: 480px) {
    .cute-card img { max-width: 250px; }
    .cute-message { font-size: 16px; }
    .cute-footer { font-size: 22px; }
}
</style>
<link href="https://fonts.googleapis.com/css2?family=Quicksand:wght@400;600;700&family=Pacifico&display=swap" rel="stylesheet">
""", unsafe_allow_html=True)

# ==================== SESSION STATE ====================
if 'click_count' not in st.session_state:
    st.session_state.click_count = 0
if 'show_popup' not in st.session_state:
    st.session_state.show_popup = False
if 'current_msg' not in st.session_state:
    st.session_state.current_msg = None

# ==================== RENDER ====================
# Counter badge
if st.session_state.click_count > 0:
    st.markdown(f'<div class="counter-badge">🥰 {st.session_state.click_count}</div>', unsafe_allow_html=True)

# Popup
if st.session_state.show_popup and st.session_state.current_msg:
    msg = st.session_state.current_msg
    st.markdown(f"""
    <div class="popup-overlay" onclick="this.style.display='none'">
        <div class="popup-box" style="background: linear-gradient(135deg, {msg['color']} 0%, #ffffff 100%);">
            <div class="popup-emoji">{msg['emoji']}</div>
            <div class="popup-title">{msg['title']}</div>
            <div class="popup-message">{msg['message']}</div>
            <div class="popup-hearts">
                <span>💖</span><span>✨</span><span>🌟</span><span>💕</span><span>🎀</span>
            </div>
        </div>
    </div>
    <script>
        setTimeout(() => {{
            const popup = document.querySelector('.popup-overlay');
            if (popup) popup.style.display = 'none';
        }}, 4500);
    </script>
    """, unsafe_allow_html=True)
    st.session_state.show_popup = False

# Main content
st.markdown(f"""
<div class="main-container">
    <div class="cute-card">
        <img src="{IMAGE_URL}" alt="For You" />
        <div class="cute-message">
            Hiii cậuu! 👋✨<br><br>
            Mình làm riêng trang web này cho cậu<br><br>
            Mong cậu sẽ thích món quà này 🥰
        </div>
        <div class="cute-footer">
            Trang cute này dành riêng cho cậu đó! 🎀
        </div>
        <div class="cute-time" id="timeDisplay"></div>
    </div>
</div>

<script>
    function updateTime() {{
        const now = new Date();
        const options = {{ year: 'numeric', month: 'long', day: 'numeric', hour: '2-digit', minute: '2-digit', second: '2-digit', hour12: false }};
        const timeEl = document.getElementById('timeDisplay');
        if (timeEl) timeEl.textContent = '🕐 ' + now.toLocaleDateString('vi-VN', options);
    }}
    updateTime();
    setInterval(updateTime, 1000);
</script>
""", unsafe_allow_html=True)

# Button
if st.button("🎁 Nhấn lần lượt 12 lần để nhận quà", key="main_btn"):
    st.session_state.click_count += 1
    idx = min(st.session_state.click_count - 1, len(SURPRISE_MESSAGES) - 1)
    st.session_state.current_msg = SURPRISE_MESSAGES[idx]
    st.session_state.show_popup = True
    st.rerun()