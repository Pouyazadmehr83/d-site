# 📝 d-site | Django Blog Project

A **blog web application** built with [Django](https://www.djangoproject.com/).  
این پروژه یک وب‌اپلیکیشن بلاگ است که با جنگو توسعه داده می‌شود.  
(⚠️ پروژه هنوز در حال توسعه است و کامل نشده است.)

---

## ✨ Features (Planned) | ویژگی‌ها (در حال توسعه)
- ✍️ ایجاد و مدیریت پست‌های وبلاگ
- 📂 دسته‌بندی و برچسب‌گذاری مطالب
- 👤 سیستم ثبت‌نام و ورود کاربران
- 💬 بخش نظرات
- 🎨 رابط کاربری ساده و کاربرپسند
- 🛠 داشبورد ادمین برای مدیریت کامل محتوا

---

## 🛠 Technologies Used | تکنولوژی‌های استفاده‌شده
- **Python 3**
- **Django Framework**
- **SQLite3 Database**
- **HTML / CSS / Bootstrap** برای قالب‌ها

---

## 📦 Installation & Run | نصب و اجرا

### Prerequisites | پیش‌نیازها
- Python 3.8 یا بالاتر
- pip
- (اختیاری) محیط مجازی `venv`

### Steps | مراحل
```bash
# 1. Clone the repository | کلون کردن ریپو
git clone https://github.com/Pouyazadmehr83/d-site.git
cd d-site

# 2. (Optional) Create virtual environment | محیط مجازی (اختیاری)
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows

# 3. Install dependencies | نصب وابستگی‌ها
pip install -r requirements.txt

# 4. Run migrations | اعمال مایگریشن‌ها
python manage.py migrate

# 5. Run the server | اجرای سرور
python manage.py runserver
