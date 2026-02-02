import streamlit as st
from datetime import datetime
import random

# ==================== CẤU HÌNH ====================
IMAGE_URL = "https://scontent.fdad3-6.fna.fbcdn.net/v/t1.15752-9/619246154_1621612339012038_4298887169126451992_n.jpg?stp=dst-jpg_s2048x2048_tt6&_nc_cat=110&ccb=1-7&_nc_sid=9f807c&_nc_eui2=AeEonldaM9u606F593lEnYDvrOQjkOLxWJKs5COQ4vFYkmLh6gXvoUZ7yW0_IrlvD38Q9zdDFyuo-3gAGmk5Zu_1&_nc_ohc=ImZZYNuS5u0Q7kNvwG74M0T&_nc_oc=AdnaIsR3FqUw-8tGdw3vI7kOw9oGPFQRaNyqOCUbqOJoYn3hhvbDoL-KXN2Bg7m7THo&_nc_zt=23&_nc_ht=scontent.fdad3-6.fna&oh=03_Q7cD4QEmk9v0lJZiUqvyjMOEBBt4uXSEV0qwUZuPuACA6Ioz6Q&oe=69A21933"

LOVE_MESSAGE = """
Hiii cậuu! 👋✨
Mình làm riêng trang web này cho cậu
Mong cậu sẽ thích món quà này 🥰
"""

# Các câu dễ thương khi bấm nút
SURPRISE_MESSAGES = [
    {
        "title": "🎉 Yayy!",
        "message": "Muốn nhận quà lắm rồi chứ gì! 😆",
        "emoji": "🥳",
        "color": "#ff6b9d"
    },
    {
        "title": "🌟 Wowww!",
        "message": "Lần thứ 2 rồi đó! Cậu đang nôn nóng lắm rồi đúng không? 😂",
        "emoji": "😜",
        "color": "#ffd93d"
    },
    {
        "title": "🎈 Ồ làaaa!",
        "message": "3 lần rồi nè! Mình đoán là cậu rất mất kiên nhẫn rồi nhỉ? Con người OCD 🤭",
        "emoji": "🤪",
        "color": "#6bcf7f"
    },
    {
        "title": "🍭 Ngọt ngàooo!",
        "message": "Thôi thì chuẩn bị nhận quà nhé! 🥰",
        "emoji": "😍",
        "color": "#ff9ff3"
    },
    {
        "title": "🎁 Quà tặngg!",
        "message": "Được đi chơi với cậu là món quà đối với mình! 🎀",
        "emoji": "🎁",
        "color": "#ff5252"
    },
    {
        "title": "⭐ Lấp lánhhh!",
        "message": "Mắt cậu lấp lánh như sao trời! ✨",
        "emoji": "🤩",
        "color": "#feca57"
    },
    {
        "title": "☀️ Tỏa sáng!",
        "message": "Nụ cười cậu tỏa nắng! 🙄",
        "emoji": "☀️",
        "color": "#ffbe76"
    },
    {
        "title": "🌸 Hoa hoa!",
        "message": "Cậu như bông hoa xinh đẹp!🌺✅",
        "emoji": "🌸",
        "color": "#ff7675"
    },
    {
        "title": "🎄 Hi hi!",
        "message": "Không phải con nghé 🐮⛔",
        "emoji": "🐄",
        "color": "#ff7675"
    },
    {
        "title": "🎨 Nghệ sĩiii!",
        "message": "Nếu có mình là họa sĩ! 🖌️",
        "emoji": "🎨",
        "color": "#74b9ff"
    },
    {
        "title": "🎨 Họa sĩiii!",
        "message": "Thì mình sẽ vẽ mãi nụ cười trên môi cậu! 😁",
        "emoji": "🎨",
        "color": "#74b9ff"
    },
    {
        "title": "🥰 Mong muốnnn!",
        "message": "Cười nhiều lên nhé cô gái 😍",
        "emoji": "😻",
        "color": "#e17055"
    },
   
]

# ==================== PAGE CONFIG ====================
st.set_page_config(
    page_title="💕 Dành cho Nguyên",
    page_icon="🥰",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# ==================== HIDE STREAMLIT UI ====================
hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
.stDeployButton {display:none;}
div[data-testid="stToolbar"] {display: none;}
div[data-testid="stDecoration"] {display: none;}
div[data-testid="stStatusWidget"] {display: none;}
section[data-testid="stSidebar"] {display: none;}
.block-container {
    padding: 0 !important;
    max-width: 100% !important;
}
div[data-testid="stVerticalBlock"] {
    gap: 0 !important;
}
</style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# ==================== INITIALIZE SESSION STATE ====================
if 'button_clicked' not in st.session_state:
    st.session_state.button_clicked = False
if 'click_count' not in st.session_state:
    st.session_state.click_count = 0
if 'current_message' not in st.session_state:
    st.session_state.current_message = None
if 'show_popup' not in st.session_state:
    st.session_state.show_popup = False

# ==================== RENDER FULL PAGE ====================
def render_full_page():
    click_count = st.session_state.click_count
    show_popup = st.session_state.show_popup
    current_message = st.session_state.current_message
    
    # Tăng cường độ hiệu ứng theo số lần click
    heart_count = min(click_count * 5 + 15, 60)
    heart_speed = max(5 - click_count * 0.2, 2)
    
    popup_html = ""
    if show_popup and current_message:
        popup_html = f"""
        <div class="popup-overlay" id="popupOverlay">
            <div class="popup-container" id="popupContainer">
                <div class="popup-emoji">{current_message['emoji']}</div>
                <h2 class="popup-title">{current_message['title']}</h2>
                <p class="popup-message">{current_message['message']}</p>
                <div class="popup-hearts">
                    <span style="animation-delay: 0s;">💖</span>
                    <span style="animation-delay: 0.2s;">✨</span>
                    <span style="animation-delay: 0.4s;">🌟</span>
                    <span style="animation-delay: 0.6s;">💕</span>
                    <span style="animation-delay: 0.8s;">🎀</span>
                </div>
                <div class="confetti-container" id="confettiContainer"></div>
            </div>
        </div>
        """
    
    full_html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=5.0">
        <link href="https://fonts.googleapis.com/css2?family=Quicksand:wght@400;600;700&family=Pacifico&display=swap" rel="stylesheet">
        <style>
            * {{
                margin: 0;
                padding: 0;
                box-sizing: border-box;
                -webkit-tap-highlight-color: transparent;
            }}
            
            html {{
                overflow-y: auto;
                overflow-x: hidden;
                height: 100%;
            }}
            
            body {{
                font-family: 'Quicksand', sans-serif;
                background: linear-gradient(135deg, #ffecd2 0%, #fcb69f 25%, #ff9a9e 50%, #fad0c4 75%, #ffecd2 100%);
                background-size: 400% 400%;
                animation: gradientShift 15s ease infinite;
                background-attachment: fixed;
                min-height: 100vh;
                padding-bottom: 100px;
            }}
            
            @keyframes gradientShift {{
                0% {{ background-position: 0% 50%; }}
                50% {{ background-position: 100% 50%; }}
                100% {{ background-position: 0% 50%; }}
            }}
            
            .container {{
                width: 100%;
                max-width: 700px;
                margin: 0 auto;
                padding: 20px 15px;
            }}
            
            .card {{
                background: rgba(255, 255, 255, 0.5);
                backdrop-filter: blur(20px);
                border-radius: 30px;
                padding: 30px 25px;
                box-shadow: 0 15px 40px rgba(255, 182, 193, 0.4);
                border: 3px solid rgba(255, 255, 255, 0.8);
                animation: fadeIn 1s ease-in;
            }}
            
            @keyframes fadeIn {{
                from {{ opacity: 0; transform: translateY(20px); }}
                to {{ opacity: 1; transform: translateY(0); }}
            }}
            
            .image-container {{
                text-align: center;
                margin-bottom: 30px;
                position: relative;
            }}
            
            .image-container img {{
                width: 100%;
                max-width: 350px;
                height: auto;
                aspect-ratio: 2/3;
                object-fit: cover;
                border-radius: 25px;
                box-shadow: 0 10px 30px rgba(255, 182, 193, 0.5);
                transition: transform 0.3s ease;
                border: 4px solid white;
            }}
            
            .image-container img:hover {{
                transform: scale(1.02) rotate(1deg);
            }}
            
            .message {{
                color: #ff6b9d;
                font-size: 17px;
                line-height: 1.9;
                text-align: center;
                text-shadow: 1px 1px 2px rgba(255, 255, 255, 0.8);
                white-space: pre-line;
                margin: 10px 0;
                font-weight: 600;
            }}
            
            .footer {{
                text-align: center;
                margin-top: 35px;
                color: #ff6b9d;
                font-size: 14px;
                font-weight: 600;
            }}
            
            .special-text {{
                font-family: 'Pacifico', cursive;
                font-size: 24px;
                margin: 15px 0;
                text-shadow: 2px 2px 4px rgba(255, 255, 255, 0.7);
                color: #ff4d7d;
            }}
            
            .time {{
                font-size: 13px;
                opacity: 0.85;
                margin-top: 10px;
                color: #ff8fab;
            }}
            
            @keyframes float {{
                0% {{ 
                    transform: translateY(0) translateX(0) rotate(0deg); 
                    opacity: 1; 
                }}
                100% {{ 
                    transform: translateY(-100vh) translateX(var(--drift)) rotate(360deg); 
                    opacity: 0; 
                }}
            }}
            
            .heart {{
                position: fixed;
                font-size: {30 + min(click_count * 2, 30)}px;
                animation: float {heart_speed}s ease-in forwards;
                pointer-events: none;
                z-index: 1000;
                will-change: transform, opacity;
            }}
            
            .counter-badge {{
                position: fixed;
                top: 15px;
                left: 15px;
                background: linear-gradient(135deg, #ff9a9e 0%, #fecfef 100%);
                backdrop-filter: blur(10px);
                padding: 12px 22px;
                border-radius: 30px;
                font-size: 18px;
                font-weight: bold;
                color: white;
                box-shadow: 0 6px 20px rgba(255, 154, 158, 0.4);
                z-index: 2000;
                animation: bounce 2s ease-in-out infinite;
                border: 3px solid white;
            }}
            
            @keyframes bounce {{
                0%, 100% {{ transform: translateY(0) scale(1) rotate(-3deg); }}
                50% {{ transform: translateY(-10px) scale(1.05) rotate(3deg); }}
            }}
            
            /* POPUP DỄ THƯƠNG */
            .popup-overlay {{
                position: fixed;
                top: 0;
                left: 0;
                width: 100%;
                height: 100%;
                background: rgba(255, 182, 193, 0.3);
                backdrop-filter: blur(10px);
                z-index: 9999;
                display: flex;
                align-items: center;
                justify-content: center;
                padding: 20px;
                animation: overlayFadeIn 0.3s ease-out;
            }}
            
            @keyframes overlayFadeIn {{
                from {{ opacity: 0; }}
                to {{ opacity: 1; }}
            }}
            
            .popup-container {{
                background: linear-gradient(135deg, {current_message['color'] if current_message else '#ff6b9d'} 0%, #ffffff 100%);
                border-radius: 35px;
                padding: 45px 35px;
                max-width: 450px;
                width: 100%;
                box-shadow: 0 25px 60px rgba(255, 107, 157, 0.5);
                text-align: center;
                position: relative;
                overflow: hidden;
                animation: popupBounceIn 0.7s cubic-bezier(0.68, -0.55, 0.265, 1.55);
                border: 5px solid white;
            }}
            
            @keyframes popupBounceIn {{
                0% {{ 
                    opacity: 0;
                    transform: scale(0.3) rotate(-20deg);
                }}
                50% {{
                    transform: scale(1.15) rotate(10deg);
                }}
                70% {{
                    transform: scale(0.95) rotate(-5deg);
                }}
                100% {{ 
                    opacity: 1;
                    transform: scale(1) rotate(0deg);
                }}
            }}
            
            .popup-emoji {{
                font-size: 90px;
                margin-bottom: 20px;
                animation: emojiJump 1s ease-out;
                display: inline-block;
            }}
            
            @keyframes emojiJump {{
                0%, 100% {{ transform: scale(1) rotate(0deg); }}
                25% {{ transform: scale(1.3) rotate(-15deg); }}
                50% {{ transform: scale(0.9) rotate(15deg); }}
                75% {{ transform: scale(1.2) rotate(-10deg); }}
            }}
            
            .popup-title {{
                font-family: 'Pacifico', cursive;
                font-size: 34px;
                color: white;
                margin-bottom: 15px;
                text-shadow: 3px 3px 6px rgba(0, 0, 0, 0.2);
                animation: titleWiggle 0.8s ease-out 0.2s both;
            }}
            
            @keyframes titleWiggle {{
                0%, 100% {{ transform: translateX(0) rotate(0deg); }}
                25% {{ transform: translateX(-10px) rotate(-5deg); }}
                75% {{ transform: translateX(10px) rotate(5deg); }}
            }}
            
            .popup-message {{
                font-size: 19px;
                color: white;
                line-height: 1.6;
                margin-bottom: 25px;
                text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.15);
                animation: messageSlideIn 0.8s ease-out 0.4s both;
                font-weight: 600;
            }}
            
            @keyframes messageSlideIn {{
                from {{ 
                    opacity: 0;
                    transform: translateY(30px);
                }}
                to {{ 
                    opacity: 1;
                    transform: translateY(0);
                }}
            }}
            
            .popup-hearts {{
                display: flex;
                justify-content: center;
                gap: 12px;
                margin-top: 20px;
            }}
            
            .popup-hearts span {{
                font-size: 35px;
                animation: heartDance 1s ease-in-out infinite;
                display: inline-block;
            }}
            
            @keyframes heartDance {{
                0%, 100% {{ transform: translateY(0) scale(1) rotate(0deg); }}
                25% {{ transform: translateY(-20px) scale(1.3) rotate(-15deg); }}
                75% {{ transform: translateY(-10px) scale(1.1) rotate(15deg); }}
            }}
            
            /* CONFETTI DỄ THƯƠNG */
            .confetti-container {{
                position: absolute;
                top: 0;
                left: 0;
                width: 100%;
                height: 100%;
                pointer-events: none;
                overflow: hidden;
            }}
            
            .confetti {{
                position: absolute;
                width: 12px;
                height: 12px;
                border-radius: 50%;
                background: white;
                animation: confettiFall 3s ease-out forwards;
            }}
            
            @keyframes confettiFall {{
                0% {{ 
                    transform: translateY(-20px) rotate(0deg) scale(1);
                    opacity: 1;
                }}
                100% {{ 
                    transform: translateY(450px) rotate(720deg) scale(0.5);
                    opacity: 0;
                }}
            }}
            
            @media (max-width: 768px) {{
                .container {{
                    padding: 15px 12px;
                }}
                .card {{
                    padding: 25px 20px;
                    border-radius: 25px;
                }}
                .image-container img {{
                    max-width: 280px;
                    border-radius: 20px;
                }}
                .message {{
                    font-size: 16px;
                }}
                .popup-container {{
                    padding: 40px 30px;
                    border-radius: 30px;
                }}
                .popup-emoji {{
                    font-size: 75px;
                }}
                .popup-title {{
                    font-size: 30px;
                }}
                .popup-message {{
                    font-size: 17px;
                }}
                .counter-badge {{
                    font-size: 16px;
                    padding: 10px 18px;
                }}
                .special-text {{
                    font-size: 22px;
                }}
            }}
            
            @media (max-width: 480px) {{
                .image-container img {{
                    max-width: 250px;
                }}
                .message {{
                    font-size: 15px;
                }}
            }}
        </style>
    </head>
    <body>
        {f'<div class="counter-badge">🥰 {click_count}</div>' if click_count > 0 else ''}
        
        <div id="heartsContainer"></div>
        
        {popup_html}
        
        <div class="container">
            <div class="card">
                <div class="image-container">
                    <img src="{IMAGE_URL}" alt="For You" />
                </div>
                
                <div class="message">
                    {LOVE_MESSAGE}
                </div>
                
                <div class="footer">
                    <div class="special-text">
                        Trang cute này dành riêng cho cậu đó! 🎀
                    </div>
                    <div class="time" id="currentTime"></div>
                </div>
            </div>
        </div>
        
        <script>
            // Hearts animation - DỄ THƯƠNG HỌA
            const container = document.getElementById('heartsContainer');
            const heartSymbols = ['💖', '🌸', '🎀', '✨', '🌟', '💕', '🦋', '🌈', '🍭', '🎈', '🧸', '🌺'];
            
            function createHeart() {{
                const heart = document.createElement('div');
                heart.className = 'heart';
                heart.textContent = heartSymbols[Math.floor(Math.random() * heartSymbols.length)];
                heart.style.left = Math.random() * 100 + '%';
                heart.style.bottom = '-50px';
                
                const drift = (Math.random() - 0.5) * 100;
                heart.style.setProperty('--drift', drift + 'px');
                
                container.appendChild(heart);
                
                setTimeout(() => heart.remove(), {heart_speed * 1000});
            }}
            
            // Continuous hearts
            setInterval(createHeart, {max(150, 600 - click_count * 40)});
            
            // Initial burst
            for (let i = 0; i < {heart_count}; i++) {{
                setTimeout(createHeart, i * 50);
            }}
            
            // Popup with confetti
            const popupOverlay = document.getElementById('popupOverlay');
            if (popupOverlay) {{
                // Create confetti dễ thương
                const confettiContainer = document.getElementById('confettiContainer');
                const colors = ['#ff9a9e', '#fecfef', '#ffecd2', '#fcb69f', '#fad0c4', '#white'];
                
                for (let i = 0; i < 60; i++) {{
                    setTimeout(() => {{
                        const confetti = document.createElement('div');
                        confetti.className = 'confetti';
                        confetti.style.left = Math.random() * 100 + '%';
                        confetti.style.background = colors[Math.floor(Math.random() * colors.length)];
                        confetti.style.animationDelay = Math.random() * 0.5 + 's';
                        confetti.style.animationDuration = (Math.random() * 2 + 2) + 's';
                        confettiContainer.appendChild(confetti);
                    }}, i * 25);
                }}
                
                // Auto close popup after 4 seconds
                setTimeout(() => {{
                    popupOverlay.style.animation = 'overlayFadeIn 0.3s ease-out reverse';
                    setTimeout(() => {{
                        popupOverlay.remove();
                    }}, 300);
                }}, 4500);
                
                // Click to close
                popupOverlay.addEventListener('click', (e) => {{
                    if (e.target === popupOverlay) {{
                        popupOverlay.style.animation = 'overlayFadeIn 0.3s ease-out reverse';
                        setTimeout(() => {{
                            popupOverlay.remove();
                        }}, 300);
                    }}
                }});
            }}
            
            // Update time
            function updateTime() {{
                const now = new Date();
                const options = {{ 
                    year: 'numeric', 
                    month: 'long', 
                    day: 'numeric', 
                    hour: '2-digit', 
                    minute: '2-digit',
                    second: '2-digit',
                    hour12: false
                }};
                const timeElement = document.getElementById('currentTime');
                if (timeElement) {{
                    timeElement.textContent = '🕐 ' + now.toLocaleDateString('vi-VN', options);
                }}
            }}
            updateTime();
            setInterval(updateTime, 1000);
        </script>
    </body>
    </html>
    """
    
    st.components.v1.html(full_html, height=900, scrolling=False)

# ==================== MAIN ====================
def main():
    # Render full page
    render_full_page()
    
    # Special button - DỄ THƯƠNG
    st.markdown("""
        <style>
        .stButton {
            position: fixed;
            bottom: 20px;
            left: 50%;
            transform: translateX(-50%);
            z-index: 10000;
            width: calc(100% - 40px);
            max-width: 400px;
        }
        .stButton > button {
            background: linear-gradient(135deg, #ff9a9e 0%, #fecfef 100%);
            color: white;
            font-size: 20px;
            font-weight: bold;
            padding: 18px 40px;
            border: 4px solid white;
            border-radius: 50px;
            cursor: pointer;
            box-shadow: 0 8px 25px rgba(255, 154, 158, 0.5);
            transition: all 0.3s ease;
            font-family: 'Quicksand', sans-serif;
            width: 100%;
            animation: buttonWiggle 2s ease-in-out infinite;
            -webkit-tap-highlight-color: transparent;
            touch-action: manipulation;
        }
        @keyframes buttonWiggle {
            0%, 100% { 
                transform: scale(1) rotate(-1deg); 
                box-shadow: 0 8px 25px rgba(255, 154, 158, 0.5); 
            }
            50% { 
                transform: scale(1.05) rotate(1deg); 
                box-shadow: 0 12px 35px rgba(255, 154, 158, 0.7); 
            }
        }
        .stButton > button:active {
            transform: scale(0.95) rotate(0deg);
            box-shadow: 0 5px 15px rgba(255, 154, 158, 0.8);
        }
        @media (max-width: 768px) {
            .stButton > button {
                font-size: 18px;
                padding: 16px 35px;
            }
        }
        </style>
    """, unsafe_allow_html=True)
    
    # Button text DỄ THƯƠNG
    button_texts = [
        "🎁 Nhấn lần lượt 12 lần để nhận quà"
    ]
    
    button_text = button_texts[min(st.session_state.click_count, len(button_texts) - 1)]
    
    if st.button(button_text, key="main_button"):
        st.session_state.click_count += 1
        msg_index = min(st.session_state.click_count - 1, len(SURPRISE_MESSAGES) - 1)
        st.session_state.current_message = SURPRISE_MESSAGES[msg_index]
        st.session_state.show_popup = True
        st.rerun()
    
    # Reset popup after showing
    if st.session_state.show_popup:
        st.session_state.show_popup = False

if __name__ == "__main__":
    main()