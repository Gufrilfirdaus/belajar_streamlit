import streamlit as st

def tampilkan_data_science_project():
    st.markdown("""
        <style>
            .project-grid {
                display: flex;
                flex-wrap: wrap;
                justify-content: space-between;
                gap: 20px;  /* Jarak antar kartu */
                margin-top: 30px;
            }
            .project-card {
                background: #f5f5f5;
                border-radius: 15px;
                padding: 20px;
                width: 48%;  /* Pastikan dua kartu muat dalam satu baris */
                box-shadow: 0 4px 10px rgba(0,0,0,0.1);
                transition: 0.3s ease;
                margin-bottom: 20px;  /* Jarak antar baris kartu */
            }
            .project-card:hover {
                transform: scale(1.02);
                box-shadow: 0 6px 15px rgba(0,0,0,0.15);
            }
            .project-title {
                font-size: 20px;
                font-weight: bold;
                margin-bottom: 10px;
            }
            .project-desc {
                font-size: 14px;
                color: #333;
                margin-bottom: 10px;
            }
            .project-tools {
                font-size: 13px;
                color: #888;
                margin-bottom: 8px;
            }
            .project-link a {
                text-decoration: none;
                font-size: 14px;
                color: #007acc;
                font-weight: bold;
            }
        </style>
    """, unsafe_allow_html=True)

    st.markdown("## 🧠 Data Science Projects")
    st.markdown("Berikut beberapa proyek data science yang saya kerjakan, mulai dari segmentasi pelanggan hingga prediksi churn dan analisis statistik:")

    projects = [
        {
            "title": "Customer Segmentation (RFM & Cohort)",
            "desc": "Segmentasi pelanggan Urban Mart dan analisis retensi menggunakan metode RFM dan Cohort.",
            "tools": "Python, Pandas, Matplotlib, Power BI",
            "link": "https://www.linkedin.com/posts/muhammad-gufril-firdaus_final-project-data-analyst-activity-7303218805126701057-6Ywi"
        },
        {
            "title": "Customer Satisfaction & Sentiment Analysis",
            "desc": "Analisis CSAT, NPS, CES dan klasifikasi sentimen ulasan pelanggan.",
            "tools": "Python, Power BI, Google Colab",
            "link": "https://docs.google.com/presentation/d/1XD6m38lUPIgdOmDt8CbNcIyFZj34LE5GaymDACbmK-I/edit?usp=sharing"
        },
        {
            "title": "Bike Sharing Dataset Analysis",
            "desc": "Analisis pengguna sepeda berdasarkan data musiman dan demografi.",
            "tools": "Pandas, Matplotlib, Streamlit",
            "link": "https://projectanalysisdatabikesharing.streamlit.app/"
        },
        {
            "title": "Hypothesis Testing - Personality Income",
            "desc": "Uji hipotesis perbedaan pendapatan berdasarkan gender, pendidikan, dll.",
            "tools": "Python, Scipy, Seaborn",
            "link": "https://github.com/Gufrilfirdaus/Hyphotesis-Testing-by-Using-Dataset-Customer-Personality-Analysis"
        },
        {
            "title": "Project Data Cleaning",
            "desc": "Membersihkan dataset California housing dari outlier dan distribusi tak normal.",
            "tools": "Python, Boxplot, IQR",
            "link": "https://github.com/Gufrilfirdaus/Project_data_cleaning"
        },
        {
            "title": "Project Data Manipulation",
            "desc": "Menerapkan teknik transformasi seperti filter, pivot, groupby dan crosstab.",
            "tools": "Python, Pandas",
            "link": "https://github.com/Gufrilfirdaus/Project_data_manipulation"
        },
    ]

    # Membuat container untuk grid proyek
    st.markdown('<div class="project-grid">', unsafe_allow_html=True)
    
    # Menampilkan proyek satu per satu
    for p in projects:
        st.markdown(f"""
            <div class="project-card">
                <div class="project-title">{p['title']}</div>
                <div class="project-desc">{p['desc']}</div>
                <div class="project-tools">🛠️ {p['tools']}</div>
                <div class="project-link"><a href="{p['link']}" target="_blank">🔗 Lihat Proyek</a></div>
            </div>
        """, unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)
