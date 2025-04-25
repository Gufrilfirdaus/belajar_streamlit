import streamlit as st

def tampilkan_kontak():
    st.markdown("""
        <style>
            .contact-section {
                text-align: center;
                margin-bottom: 40px;
            }
            .contact-title {
                font-size: 38px;
                font-weight: bold;
                margin-bottom: 5px;
            }
            .contact-subtitle {
                font-size: 18px;
                color: #666;
                margin-bottom: 30px;
            }
            .contact-cards {
                display: flex;
                justify-content: center;
                flex-wrap: wrap;
                gap: 20px;
            }
            .contact-card {
                background: #f5f5f5;
                border-radius: 15px;
                padding: 25px;
                width: 250px;
                box-shadow: 0 4px 12px rgba(0,0,0,0.1);
                transition: transform 0.3s ease, box-shadow 0.3s ease;
            }
            .contact-card:hover {
                transform: translateY(-5px);
                box-shadow: 0 6px 18px rgba(0,0,0,0.15);
            }
            .contact-icon {
                font-size: 40px;
                margin-bottom: 10px;
            }
            .contact-method {
                font-size: 20px;
                font-weight: 600;
                margin-bottom: 5px;
            }
            .contact-link a {
                color: #0077cc;
                font-weight: 500;
                text-decoration: none;
                font-size: 16px;
            }
        </style>
        <div class="contact-section">
            <div class="contact-title">📬 Kontak Saya</div>
            <div class="contact-subtitle">Silakan hubungi saya melalui salah satu platform berikut:</div>
            <div class="contact-cards">
                <div class="contact-card">
                    <div class="contact-icon">📧</div>
                    <div class="contact-method">Email</div>
                    <div class="contact-link"><a href="mailto:Mgufrilfirdaus@email.com">mgufrilfirdaus@email.com</a></div>
                </div>
                <div class="contact-card">
                    <div class="contact-icon">💼</div>
                    <div class="contact-method">LinkedIn</div>
                    <div class="contact-link"><a href="https://www.linkedin.com/in/muhammad-gufril-firdaus" target="_blank">linkedin.com/in/muhammadgufril</a></div>
                </div>
                <div class="contact-card">
                    <div class="contact-icon">💬</div>
                    <div class="contact-method">WhatsApp</div>
                    <div class="contact-link"><a href="https://wa.me/6285215115852" target="_blank">+62 852-1511-5852</a></div>
                </div>
                <div class="contact-card">
                    <div class="contact-icon">🐙</div>
                    <div class="contact-method">GitHub</div>
                    <div class="contact-link"><a href="https://github.com/Gufrilfirdaus" target="_blank">github.com/Gufrilfirdaus</a></div>
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)