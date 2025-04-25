import streamlit as st
from PIL import Image
import base64

def img_to_base64(img_path):
    with open(img_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

def tampilkan_tentang_saya():
    # CSS dengan base64 dan !important
    st.markdown(f"""
    <style>
        .circle-image {{
            border-radius: 50% !important;
            width: 150px !important;
            height: 150px !important;
            object-fit: cover !important;
            display: block !important;
            margin: 0 auto 20px auto !important;
            box-shadow: 0 0 10px rgba(0,0,0,0.2);
        }}
        .main-title {{
            text-align: center;
            font-size: 48px;
            font-weight: 600;
        }}
        .subtitle {{
            text-align: center;
            font-size: 20px;
            color: #555;
            margin-top: -10px;
        }}
        .footer {{
            text-align: center;
            font-size: 18px;
            color: #888;
            margin-top: 30px;
        }}
    </style>
    """, unsafe_allow_html=True)

    # Header
    st.markdown('<h1 style="text-align: center;">📑 Tentang Saya</h1>', unsafe_allow_html=True)

    # Gambar dengan base64
    image_base64 = img_to_base64("IMG_1549.jpg")
    st.markdown(
        f'<img src="data:image/jpeg;base64,{image_base64}" class="circle-image">',
        unsafe_allow_html=True
    )

    # Konten
    st.markdown('<div class="main-title">Muhammad Gufril Firdaus</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">Data Analyst | Data Scientist | Lifelong Learner</div>', unsafe_allow_html=True)
    st.markdown('<div class="footer">Let’s build something awesome together 🚀</div>', unsafe_allow_html=True)

    # Konten markdown utama (tetap sama)
    st.markdown("""
    ---

    ### 👋 Tentang Saya

    Halo! Saya **Muhammad Gufril**, seorang *Logistics Administrator* dengan latar belakang pendidikan di bidang **Sistem Informasi** dan fokus dalam **analisis data** serta optimalisasi proses operasional.  

    Dengan pengalaman profesional lebih dari 5 tahun di **PT Paragon Technology and Innovation**, saya terbiasa mengelola alur logistik secara efisien, mulai dari pengecekan bahan kemasan, pengelolaan stok, hingga dokumentasi menggunakan sistem seperti **Odoo** dan **WMS**.

    📦 **Peran saya di logistik** membantu memastikan kelancaran proses produksi dan distribusi melalui koordinasi yang tepat, analisis data permintaan, serta pelaksanaan proyek perbaikan seperti *stock opname*, *relabeling*, dan *administrasi barang reject*.

    ---

    ### 🧠 Keahlian Saya

    - **Data Analysis:** Python, Pandas, NumPy, Matplotlib, Streamlit  
    - **Tools:** SQL, Power BI (DAX & Measure), Looker Studio, Google Tools  
    - **Logistics System:** Odoo, Warehouse Management System (WMS)  
    - **Others:** Git & GitHub, Microsoft Office, Visual Studio Code  

    ---

    ### 🏅 Pencapaian & Sertifikasi

    - 🥈 **Silver Grade - Quality Improvement Team (QIT)**
    - 📜 Dicoding Certified:
      - Analisis Data dengan Python  
      - Belajar Dasar Data Science  
      - SQL Dasar
    - 📜 Kelas.com – Microsoft Office  
    - 📜 Alison – Sourcing & Procurement Practices

    ---
    """)

tampilkan_tentang_saya()