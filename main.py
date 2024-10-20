import streamlit as st
import DSSV
import appsen
import f
import cuano

st.set_page_config(layout="wide", page_title="Ứng dụng Tổng hợp")

# CSS để tạo kiểu cho ứng dụng
st.markdown("""
<style>
    .main {
        padding: 0rem 1rem;
    }
    .sidebar .sidebar-content {
        width: 300px;
    }
</style>
""", unsafe_allow_html=True)

PAGES = {
    "Danh sách Sinh viên": DSSV,
    "Đánh giá SIFT và ORB": appsen,
    "So sánh Ảnh Chân dung và Thẻ Sinh viên": f,
    "Nhận diện khuôn mặt trong ảnh lớp học": cuano
}

st.sidebar.title('Chọn Ứng dụng')
selection = st.sidebar.radio("Chuyển đến", list(PAGES.keys()))

# Xóa nội dung cũ
st.empty()

# Chạy ứng dụng được chọn
if selection == "Danh sách Sinh viên":
    DSSV.main()
elif selection == "Đánh giá SIFT và ORB":
    appsen.main()
elif selection == "So sánh Ảnh Chân dung và Thẻ Sinh viên":
    f.main()
elif selection == "Nhận diện khuôn mặt trong ảnh lớp học":
    cuano.main()