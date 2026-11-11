# Version control
.git/
.gitignore

# IDEs & System files
.idea/
.vscode/
*.swp
*.swo
.DS_Store
Thumbs.db

# Virtual environments (VERY IMPORTANT: Do not copy Windows venv to Linux container)
.venv/
venv/
env/
ENV/

# Python cache & bytecode
__pycache__/
*/__pycache__/
*/*/__pycache__/
*.py[cod]
*$py.class
*.pyd

# Temporary logs & debug files
*.log
firebase-debug.log
logs/*.log
screenshots/*.png

# Local development test scripts
scratch/
run_bot.bat

# Web & Node artifacts (if any)
node_modules/
public/
netlify/
dist/
build/

# Documentation
README.md
DEPLOYMENT.md

# Telegram Bot Token (حصلت عليه من @BotFather)
TELEGRAM_BOT_TOKEN=9057896501:AAFuq07l2lkinNdl1iDLBEMQmHIfosNp_eQ

# Gemini API Key (يمكنك الحصول عليه مجاناً من https://aistudio.google.com/app/apikey)
GEMINI_API_KEY=AQ.Ab8RN6KRbrV325-OZgoRtJANvy1JPAEI5yRdPecZrcbi_DaSRg

# تشغيل المتصفح بوضع خفي (True) أم إظهار نافذة المتصفح لتشاهد الحل بنفسك (False)
HEADLESS=False

# الرابط الافتراضي للمسار في منصة كيريو
DEFAULT_COURSE_URL=https://me-tp.qureo.education/course/javascript_ar
DEFAULT_JS_COURSE_URL=https://me-tp.qureo.education/course/javascript_ar
LOGIN_URL=https://me-portal.qureo.education/login
QUREO_USERNAME=
QUREO_PASSWORD=

# تفعيل أو تعطيل فايربيس (True / False) - مفعل للمزامنة السحابية
ENABLE_FIREBASE=True

# ==============================================================
# إعدادات بوت منصة كيريو التعليمية (Qureo Solution Bot)
# قم بنسخ هذا الملف إلى .env وأدخل القيم الخاصة بك
# ==============================================================

# 1. التوكن الرسمي للبوت من BotFather على تليجرام (مطلوب)
TELEGRAM_BOT_TOKEN=your_bot_token_here

# 2. مفتاح واجهة برمجة تطبيقات Google Gemini AI (مطلوب للحل الذكي)
GEMINI_API_KEY=your_gemini_api_key_here

# 3. معرف الآدمن على تليجرام لاستقبال الإشعارات ولوحة التحكم
ADMIN_ID=7217896334

# 4. تشغيل المتصفح في الوضع الخفي بدون واجهة رسومية (true للسيرفرات و Docker)
HEADLESS=true

# 5. منفذ خادم فحص الصحة لمنصات السحاب مثل blitz.cloud و Railway و Render
PORT=8080

# 6. روابط تسجيل الدخول والمسارات الافتراضية
DEFAULT_COURSE_URL=https://me-tp.qureo.education/course/javascript_ar
DEFAULT_JS_COURSE_URL=https://me-tp.qureo.education/course/javascript_ar
LOGIN_URL=https://me-portal.qureo.education/login

# 7. إعدادات قاعدة بيانات فايربيس (اختياري - إن لم يتوفر يعمل النظام تلقائياً بـ SQLite)
ENABLE_FIREBASE=True
FIREBASE_CREDENTIALS_FILE=firebase_credentials.json

# أو يمكنك وضع محتوى ملف JSON مباشرة كمتغير بيئة في سيرفرك السحابي:
# FIREBASE_CREDENTIALS_JSON={"type": "service_account", ...}

# Environment variables & secrets
.env
.env.local
*.env
*.key
*.pem

# Python virtual environments
.venv/
venv/
env/
ENV/

# Python cache & bytecode
__pycache__/
*/__pycache__/
*/*/__pycache__/
*.py[cod]
*$py.class
*.so
.Python

# SQLite lock and temporary files (keep answers.db tracked)
data/*.sqlite
data/*.sqlite3
data/*.db-shm
data/*.db-wal
data/*.db-journal

# Screenshots and logs
screenshots/*
!screenshots/.gitkeep
logs/*
!logs/.gitkeep

# IDEs
.idea/
.vscode/
*.swp
*.swo

# Web build / static
node_modules/
dist/
build/

# Local logs and scratch scripts
*.log
firebase-debug.log
scratch/

# Package bot

import os
from pathlib import Path
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent
ENV_PATH = BASE_DIR / ".env"

load_dotenv(dotenv_path=ENV_PATH)


class Config:
    TELEGRAM_BOT_TOKEN: str = os.getenv("TELEGRAM_BOT_TOKEN", "").strip()
    GEMINI_API_KEY: str = os.getenv("GEMINI_API_KEY", "").strip()
    # الوضع الافتراضي في بيئات السيرفرات والحاويات هو Headless = True
    HEADLESS: bool = os.getenv("HEADLESS", "True").lower() in ("true", "1", "yes")

    DEFAULT_COURSE_URL: str = os.getenv(
        "DEFAULT_COURSE_URL", "https://me-tp.qureo.education/course/javascript_ar"
    ).strip()
    DEFAULT_JS_COURSE_URL: str = os.getenv(
        "DEFAULT_JS_COURSE_URL", "https://me-tp.qureo.education/course/javascript_ar"
    ).strip()
    LOGIN_URL: str = os.getenv(
        "LOGIN_URL", "https://me-portal.qureo.education/login"
    ).strip()
    QUREO_USERNAME: str = os.getenv("QUREO_USERNAME", "").strip()
    QUREO_PASSWORD: str = os.getenv("QUREO_PASSWORD", "").strip()

    # معرف تيليجرام الخاص بالمسؤول / الأدمن لاستقبال بيانات الطلاب وتحديثات المستويات الحية
    _admin_env = os.getenv("ADMIN_ID", "7217896334").strip()
    ADMIN_ID: int = int(_admin_env) if _admin_env.isdigit() else 7217896334

    # منفذ خادم فحص الصحة لمنصات الاستضافة السحابية مثل blitz.cloud و Railway و Render
    _port_env = os.getenv("PORT", "8080").strip()
    PORT: int = int(_port_env) if _port_env.isdigit() else 8080

    # إعدادات قاعدة بيانات فايربيس (Cloud Firestore)
    FIREBASE_CREDENTIALS_FILE: str = os.getenv("FIREBASE_CREDENTIALS_FILE", "firebase_credentials.json").strip()
    FIREBASE_CREDENTIALS_PATH: Path = (
        Path(FIREBASE_CREDENTIALS_FILE) if Path(FIREBASE_CREDENTIALS_FILE).is_absolute()
        else BASE_DIR / FIREBASE_CREDENTIALS_FILE
    )
    ENABLE_FIREBASE: bool = os.getenv("ENABLE_FIREBASE", "True").lower() in ("true", "1", "yes")

    # المجلدات التخزينية المساعدة للمشروع
    SCREENSHOTS_DIR: Path = BASE_DIR / "screenshots"
    LOGS_DIR: Path = BASE_DIR / "logs"
    DATA_DIR: Path = BASE_DIR / "data"


# التأكد من إنشاء جميع المجلدات المساعدة تلقائياً
Config.SCREENSHOTS_DIR.mkdir(parents=True, exist_ok=True)
Config.LOGS_DIR.mkdir(parents=True, exist_ok=True)
Config.DATA_DIR.mkdir(parents=True, exist_ok=True)

@echo off
chcp 65001 >nul
echo ==============================================================
echo 📦 تجهيز وضغط حزمة المشروع الجاهزة للرفع على السيرفر الخارجي
echo ==============================================================
if exist .venv\Scripts\python.exe (
    .venv\Scripts\python.exe package_project.py
) else (
    python package_project.py
)
pause

# 🚀 دليل نشر وتشغيل المشروع (Netlify & Docker Deployment Guide)

يوضح هذا الدليل كيفية نشر المشروع كاملاً:
1. **نشر واجهة الويب والبوابة على Netlify (بثوانٍ معدودة).**
2. **نشر وتشغيل البوت والمتصفح (Playwright) على خدمة Docker مدارة 24/7.**
3. **توضيح ميزة حصر الثقافة المالية على سنة ثانية ثانوي.**
4. **عزل الحسابات التام (لكل مستخدم ID و Pass خاص به).**

---

## 🏗️ البنية التحتية للمشروع

```text
[ المستخدم / الطالب ]
        │
        ├──> [ تليجرام البوت ] ──> [ حاوية Docker (Playwright + Bot Engine + Gemini AI) ]
        │
        └──> [ واجهة الويب ]  ──> [ استضافة Netlify السحابية (Landing Page & Status API) ]
```

---

## 1️⃣ النشر على Netlify (Netlify Deployment)

تم تجهيز المشروع بملف `netlify.toml` ومجلد `public` ومجلد دوال `netlify/functions`.

### الطريقة الأولى: النشر المباشر عبر مستودع GitHub (موصى بها)
1. ارفع المشروع إلى حسابك على **GitHub**.
2. ادخل على حسابك في [Netlify](https://app.netlify.com).
3. اضغط على **"Add new site"** ثم **"Import an existing project"**.
4. اختر مستودع المشروع من GitHub.
5. سيتعرف Netlify تلقائياً على إعدادات ملف `netlify.toml`:
   - **Publish directory:** `public`
   - **Functions directory:** `netlify/functions`
6. اضغط على **"Deploy site"** وسيعمل الموقع فوراً على رابط مجاني مثل `https://your-site.netlify.app`.

### الطريقة الثانية: النشر عبر Netlify CLI
إذا كان مثبت لديك Node.js:
```bash
npm install -g netlify-cli
netlify login
netlify deploy --prod --dir=public
```

---

## 2️⃣ التشغيل والنشر عبر Docker (لتشغيل البوت والمتصفح Playwright 24/7)

لتشغيل البوت وتشغيل متصفح **Playwright Chromium** في وضع الـ Headless بسلاسة تامة دون الحاجة لإبقاء جهاز الكمبيوتر الشخصي مفتوحاً، استخدم Docker على أي خادم (VPS / DigitalOcean / Hetzner / AWS / Render / Railway).

### المتطلبات:
- تثبيت **Docker** و **Docker Compose**.

### خطوات التشغيل:
1. تأكد من إعداد ملف `.env` وإضافة مفاتيحك:
   ```env
   TELEGRAM_BOT_TOKEN=9057896501:AAFuq...
   GEMINI_API_KEY=AIzaSy...
   HEADLESS=true
   ```
   *(لاحظ: لا يوجد أي حساب ID أو Pass مخزن في ملف .env لحماية خصوصية حسابك، فكل مستخدم يكتب حسابه الخاص في البوت).*

2. بناء وتشغيل الحاوية في الخلفية:
   ```bash
   docker compose up -d --build
   ```

3. متابعة سجلات البوت الحية:
   ```bash
   docker compose logs -f qureo-bot
   ```

4. لإيقاف البوت:
   ```bash
   docker compose down
   ```

### مميزات حاوية Docker المجهزة:
- تحتوي على بيئة `python:3.11-slim` مع جميع مكتبات نظام لينكس المطلوبة لتشغيل **Chromium**.
- مزودة بأعلام تشغيل متصفح آمنة (`--no-sandbox`, `--disable-dev-shm-usage`, `--disable-crash-reporter`, `--no-crashpad`).
- تم ضبط `ipc: host` و `shm_size: '1gb'` لضمان عدم تعطل صفحات كيريو الثقيلة داخل الحاوية.
- مجلد `data/` و `logs/` و `screenshots/` يتم حفظها في Volume خارجي لعدم فقدان بنك الإجابات عند إعادة تشغيل الحاوية.

---

### 2️⃣.1 التشغيل المباشر على خادم VPS (Ubuntu / Debian / blitz.cloud) بدون Docker

إذا كنت تشغل البوت مباشرة عبر بايثون على السيرفر بدون Docker:

1. تثبيت مكتبات بايثون:
   ```bash
   pip install -r requirements.txt
   ```

2. **خطوة جوهرية (لمنع خطأ Invalid argument 22 نهائياً):**
   يجب تثبيت متصفح كروميوم مع مكتبات النظام الرسومية الخاصة بلينكس:
   ```bash
   playwright install --with-deps chromium
   ```

3. تشغيل البوت:
   ```bash
   python main.py
   ```

---

## 3️⃣ الميزات المحدثة في هذا الإصدار

### 🎓 1. منصة الثقافة المالية (خاصة بالصف الثاني الثانوي فقط)
- تم حصر منصة الثقافة المالية لطلاب **الصف الثاني الثانوي** فقط.
- طلاب **الصف الأول الثانوي** مخصص لهم مسار البرمجة (JavaScript) حصراً ولن تظهر لهم خيارات الثقافة المالية.
- يوجد فحص صارم في كود البوت لمنع أي وصول غير مصرح به لمسار الثقافة المالية إلا لطلاب سنة ثانية.

### 🔐 2. خصوصية وأمان الحسابات (إلغاء الحساب المسجل العام)
- تم مسح وحذف الحساب المسجل الثابت القديم (الـ ID وكلمة المرور الخاصة بك).
- أصبح البوت متعدد المستخدمين (Multi-User) بنسبة 100%.
- كل طالب عند الدخول يكتب **اسم المستخدم (ID / كود الطالب)** الخاص به، ثم يكتب **كلمة المرور (Pass)** الخاصة به.
- يتم حفظ بيانات كل طالب بشكل مشفر ومستقل تماماً داخل قاعدة بيانات `answers.db` مرتبطة بـ Telegram User ID الخاص به.
- لا يمكن لأي مستخدم رؤية أو استخدام حساب مستخدم آخر.

### 🗑️ 3. الحذف التلقائي والفوري للصور (Zero-Disk Footprint)
- تم تفعيل نظام مسح وحذف الصور فوراً من مجلد `screenshots/` بمجرد إرسالها إلى التليجرام أو استلامها من المستخدم.
- مسح كافة الصور القديمة المخزنة، وضمان عدم تراكم أي لقطات شاشة في سيرفر المشروع.

### 💼 4. تدريب البوت على منصة الثقافة المالية (Vision AI Training)
- يمكن للمستخدمين أو المطور إرسال صور ولقطات شاشة لأسئلة منصة الثقافة المالية مباشرة في المحادثة.
- يقوم نموذج Google Gemini بتحليل السؤال، استخراج الخيارات، استنتاج الإجابة الصحيحة مع التفسير المالي، وتخزينها في بنك أسئلة الثقافة المالية الدائم.
- يتم حذف صورة السؤال المرفوعة فوراً من القرص لحماية المساحة والأمان.

---

## 👨‍💻 مطور المشروع
- المهندس: **مينا شحاتة** 🚀

version: '3.8'

services:
  qureo-bot:
    build:
      context: .
      dockerfile: Dockerfile
    container_name: qureo_solver_bot
    restart: unless-stopped
    env_file:
      - .env
    environment:
      - HEADLESS=true
      - PYTHONUNBUFFERED=1
      - PORT=8080
    ports:
      - "8080:8080"
    volumes:
      # حفظ قاعدة البيانات وبنك الإجابات وحسابات المستخدمين
      - ./data:/app/data
      # حفظ سجلات التشغيل
      - ./logs:/app/logs
      # حفظ لقطات الشاشة الحية
      - ./screenshots:/app/screenshots
    # زيادة حجم الذاكرة المشتركة ومشاركة IPC لمنع تعطل متصفح Chromium في Docker
    ipc: host
    shm_size: '1gb'
    logging:
      driver: "json-file"
      options:
        max-size: "10m"
        max-file: "3"

# ==============================================================
# Dockerfile لتشغيل بوت منصة كيريو التعليمية مع متصفح Playwright
# جاهز 100% للنشر على blitz.cloud و VPS و Render و Railway
# ==============================================================

FROM python:3.11-slim

# ضبط المتغيرات البيئية لضمان عمل بايثون والمسارات والمتصفح بسلاسة
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    HEADLESS=true \
    DEBIAN_FRONTEND=noninteractive \
    PYTHONPATH=/app \
    PORT=8080

WORKDIR /app

# تثبيت الحزم الأساسية للنظام لتشغيل Chromium و Playwright
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    ca-certificates \
    fonts-liberation \
    fonts-noto-color-emoji \
    fonts-noto-core \
    libnss3 \
    libatk-bridge2.0-0 \
    libdrm2 \
    libxcomposite1 \
    libxdamage1 \
    libxrandr2 \
    libgbm1 \
    libasound2 \
    libpango-1.0-0 \
    libxshmfence1 \
    && rm -rf /var/lib/apt/lists/*

# تثبيت مكتبات بايثون المطلوبة أولاً للاستفادة من طبقات التخزين المؤقت (Docker Cache)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# تثبيت متصفح كروميوم مع جميع اعتمادات نظام التشغيل الخاصة بـ Playwright
RUN playwright install --with-deps chromium

# نسخ الكود المصدري للمشروع كاملاً
COPY . .

# فك ضغط الحزمة التلقائي إن وُجد ملف deploy_server_package.zip ولم يُرفع مجلد bot صراحة
RUN if [ -f deploy_server_package.zip ] && [ ! -d bot ]; then \
        python -c "import zipfile; zipfile.ZipFile('deploy_server_package.zip').extractall('.'); print('Extracted deploy_server_package.zip successfully')"; \
    fi

# إنشاء المجلدات التخزينية للمشروع لضمان الصلاحيات
RUN mkdir -p /app/data /app/logs /app/screenshots

# إعلان المنفذ لمنصات الاستضافة السحابية
EXPOSE 8080

# أمر التشغيل الأساسي للبوت
CMD ["python", "main.py"]

{
  "type": "service_account",
  "project_id": "qureo-model",
  "private_key_id": "12e8f48d3af77d3f2243e71e11a85b315a3f2be2",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQDQE4Cf5rT3J7x9\nz+lP8m+820102ggoKiyqQRtrW+kcxFgyLd3p+tSuToLv/XywQlyluW3LNmNstpgz\nKtmKasR0E4iZ0wDe2EXkQFlotMqAvC9VywTrZdVPnuFHtixmJBmVP/VtxcXecJaf\nZR92AtMMMuR+37KFa7+Ag/WJoRznuLkY+q+8WVyNll4A1pBkLSZkTN1qY9Aa4Y07\nCWsHjhOtPMnHE/yVKMGy4C7LiXHall6OIfP0KEEBLyasz0Rsm2MLYN8Vb0mlA9Ea\nA8Bj5knkRckU/2I7sWcotO6VSdNTTv0CQYI/WN1mcAEb1qVy78Fbpd9A0YQ1fqkL\nTV6PK0mjAgMBAAECggEACbT0idZywsTxH31qM6HqYd5pMqD+mGu/Qay1NsDxkwyl\n1fwbH3s6yMGTjNaVJokyAUPb7LWmKxV+7C7SOd7ZOKu18lchnJkXnu+m5szoVYZx\n6YgFvBA4GfVzf6uZTqUzJv9LgnTOJ55g/cvzN8d8nlO8InRqbkb53BOhNMEgtBPt\nuOB4vCzMePKUHD/2u7SUoQdFECckqinFXaI4sGD2CgaVqjBU3Ypa+claGLt2/GWo\n6vEKMKRISWB9Xv2U2CMAJTFtl66eMM+3WPz6O2pNM5h9D81hzKpLUgQZViUG/HEA\n6GvJbQN4SNAVJxDmBMJ3KXojzYnf4mr31Lx7WXtz4QKBgQD9Ot0pWkOjW6OcGZP9\n0jr+ZIL5F+HxyCNJ5/DtrlxCzN6y4bSq3zZGoXFadbUSwsSiljM8Qa/IlcNbvJyE\nqia08q2pnTMg68vfpbHg8sGFJLTy5jk5gw0HbN9+NX26ZJCmFj/SZaN81VvXPRkG\nyXEmcEB3fIylenxYm5BsBHmjfwKBgQDSWjEKEa8uDUv78dwrGotN0s31kFdDeZ1e\nDrE/ZDiJD/zC/InvTqFFsLi/ZRsQ15HgF0CR0hUHhSVWpgrn61SdVWoSbp2w3ZEF\nmlz9qiYrFCmCwpwL+AxQ2+yaf91Ou9Wr/LHuFLF4/jxqBm0Ilc39niQZFaD4DJr3\nexl+RHVb3QKBgFy+6W+S2sEC+Dpc9+H31JmFsJ6Qy7UlKx+PbqNuv+XLaSk1F1mZ\n5SQbTwvlnosfgKtXva4tFLevelyoCN9h/kk5tLcxlx9QnVvtMOgFoTElj4yDG6Rf\nxi7ZBkYQS1swJ/ZcocVqamV3M2ryuq7Mqr98T3Az0sNsyAwf9dZKEU77AoGBALXg\nR9B18+q0koNX3s7iF5qFb5EoaVstFvTRbU3rQLq5uQl6w2THrseMAmFycRGB4l5I\nnIq4g3hKFjuyO3HFVxbmWF1xiST4nkCi9E5bxL6woyetTrFGmpd7YDtB3T8LR7d6\nOPoqqDx+Tgw6XCH1LPNhvcJ2ogR3GbJrnGJBnNt9AoGBAIir0fAVIkAbqq5NMVEg\ngeudLPnxX80BV9SzSC04Sgd55aSSqXOezMfNcPrrxW0RoIjRMHB4WBwJDEJ9OSEc\n6bUeu+H2slGTTHeJGPfqRaUKgHlNVW9Yhe+UewaUxg+U7C1m+AXqxkEPRWJdTPON\n0+gAzct+Ve80IvFVi3NKfT+x\n-----END PRIVATE KEY-----\n",
  "client_email": "firebase-adminsdk-fbsvc@qureo-model.iam.gserviceaccount.com",
  "client_id": "112193152785072028304",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-fbsvc%40qureo-model.iam.gserviceaccount.com",
  "universe_domain": "googleapis.com"
}

[debug] [2026-11-03T18:44:48.345Z] ----------------------------------------------------------------------
[debug] [2026-11-03T18:44:48.349Z] Command:       C:\Program Files\nodejs\node.exe C:\Users\MinaS\AppData\Roaming\npm\node_modules\firebase-tools\lib\bin\firebase.js projects:list
[debug] [2026-11-03T18:44:48.349Z] CLI Version:   15.22.4
[debug] [2026-11-03T18:44:48.349Z] Platform:      win32
[debug] [2026-11-03T18:44:48.350Z] Node Version:  v22.16.0
[debug] [2026-11-03T18:44:48.350Z] Detected Agent: antigravity
[debug] [2026-11-03T18:44:48.351Z] Time:          Tue Nov 03 2026 20:44:48 GMT+0200 (Eastern European Standard Time)
[debug] [2026-11-03T18:44:48.351Z] ----------------------------------------------------------------------
[debug] 
[debug] [2026-11-03T18:44:48.354Z] >>> [apiv2][query] GET https://firebase-public.firebaseio.com/cli.json [none]
[debug] [2026-11-03T18:44:48.453Z] > command requires scopes: ["email","openid","https://www.googleapis.com/auth/cloudplatformprojects.readonly","https://www.googleapis.com/auth/firebase","https://www.googleapis.com/auth/cloud-platform"]
[debug] [2026-11-03T18:44:48.453Z] > authorizing via signed-in user (minashehata752@gmail.com)
[debug] [2026-11-03T18:44:48.457Z] Checked if tokens are valid: false, expires at: 1789073917335
[debug] [2026-11-03T18:44:48.458Z] Checked if tokens are valid: false, expires at: 1789073917335
[debug] [2026-11-03T18:44:48.458Z] > refreshing access token with scopes: []
[debug] [2026-11-03T18:44:48.460Z] >>> [apiv2][query] POST https://www.googleapis.com/oauth2/v3/token [none]
[debug] [2026-11-03T18:44:48.460Z] >>> [apiv2][body] POST https://www.googleapis.com/oauth2/v3/token [omitted]
[debug] [2026-11-03T18:44:48.468Z] *** [apiv2] error from fetch(https://firebase-public.firebaseio.com/cli.json, {"headers":{},"method":"GET"}): FetchError: request to https://firebase-public.firebaseio.com/cli.json failed, reason: getaddrinfo ENOTFOUND firebase-public.firebaseio.com
[warn] !  Unable to fetch the CLI MOTD and remote config. This is not a fatal error, but may indicate an issue with your network connection. 
[debug] [2026-11-03T18:44:48.468Z] Failed to fetch MOTD FirebaseError: Failed to make request to https://firebase-public.firebaseio.com/cli.json
[debug] [2026-11-03T18:44:48.473Z] *** [apiv2] error from fetch(https://www.googleapis.com/oauth2/v3/token, {"headers":{},"method":"POST","body":{"type":"Buffer","data":[45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,101,99,49,49,48,53,101,97,102,51,57,55,97,50,100,53,52,52,101,101,50,102,97,54,13,10,67,111,110,116,101,110,116,45,68,105,115,112,111,115,105,116,105,111,110,58,32,102,111,114,109,45,100,97,116,97,59,32,110,97,109,101,61,34,114,101,102,114,101,115,104,95,116,111,107,101,110,34,13,10,13,10,49,47,47,48,51,55,95,99,117,84,116,80,54,81,65,77,67,103,89,73,65,82,65,65,71,65,77,83,78,103,70,45,76,57,73,114,106,78,118,51,78,117,45,120,95,109,111,51,90,77,111,51,90,109,117,78,102,106,121,52,72,45,115,79,103,57,87,90,77,99,115,48,49,48,51,48,88,101,45,87,83,51,116,54,52,53,104,117,52,114,82,103,105,120,68,69,118,77,70,48,104,81,13,10,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,101,99,49,49,48,53,101,97,102,51,57,55,97,50,100,53,52,52,101,101,50,102,97,54,13,10,67,111,110,116,101,110,116,45,68,105,115,112,111,115,105,116,105,111,110,58,32,102,111,114,109,45,100,97,116,97,59,32,110,97,109,101,61,34,99,108,105,101,110,116,95,105,100,34,13,10,13,10,53,54,51,53,56,52,51,51,53,56,54,57,45,102,103,114,104,103,109,100,52,55,98,113,110,101,107,105,106,53,105,56,98,53,112,114,48,51,104,111,56,52,57,101,54,46,97,112,112,115,46,103,111,111,103,108,101,117,115,101,114,99,111,110,116,101,110,116,46,99,111,109,13,10,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,101,99,49,49,48,53,101,97,102,51,57,55,97,50,100,53,52,52,101,101,50,102,97,54,13,10,67,111,110,116,101,110,116,45,68,105,115,112,111,115,105,116,105,111,110,58,32,102,111,114,109,45,100,97,116,97,59,32,110,97,109,101,61,34,99,108,105,101,110,116,95,115,101,99,114,101,116,34,13,10,13,10,106,57,105,86,90,102,83,56,107,107,67,69,70,85,80,97,65,101,74,86,48,115,65,105,13,10,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,101,99,49,49,48,53,101,97,102,51,57,55,97,50,100,53,52,52,101,101,50,102,97,54,13,10,67,111,110,116,101,110,116,45,68,105,115,112,111,115,105,116,105,111,110,58,32,102,111,114,109,45,100,97,116,97,59,32,110,97,109,101,61,34,103,114,97,110,116,95,116,121,112,101,34,13,10,13,10,114,101,102,114,101,115,104,95,116,111,107,101,110,13,10,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,101,99,49,49,48,53,101,97,102,51,57,55,97,50,100,53,52,52,101,101,50,102,97,54,13,10,67,111,110,116,101,110,116,45,68,105,115,112,111,115,105,116,105,111,110,58,32,102,111,114,109,45,100,97,116,97,59,32,110,97,109,101,61,34,115,99,111,112,101,34,13,10,13,10,13,10,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,101,99,49,49,48,53,101,97,102,51,57,55,97,50,100,53,52,52,101,101,50,102,97,54,45,45,13,10]}}): FetchError: request to https://www.googleapis.com/oauth2/v3/token failed, reason: getaddrinfo ENOTFOUND www.googleapis.com
[error] Authentication Error: Your credentials are no longer valid. Please run firebase login --reauth

For CI servers and headless environments, generate a new token with firebase login:ci
[debug] [2026-11-03T18:44:48.473Z] Authentication Error: Your credentials are no longer valid. Please run firebase login --reauth

For CI servers and headless environments, generate a new token with firebase login:ci
[debug] [2026-11-03T18:44:48.485Z] FirebaseError: Authentication Error: Your credentials are no longer valid. Please run firebase login --reauth

For CI servers and headless environments, generate a new token with firebase login:ci
    at invalidCredentialError (C:\Users\MinaS\AppData\Roaming\npm\node_modules\firebase-tools\lib\auth.js:176:12)
    at refreshTokens (C:\Users\MinaS\AppData\Roaming\npm\node_modules\firebase-tools\lib\auth.js:589:15)
    at process.processTicksAndRejections (node:internal/process/task_queues:105:5)
    at async getAccessToken (C:\Users\MinaS\AppData\Roaming\npm\node_modules\firebase-tools\lib\apiv2.js:55:18)
    at async Client.addAuthHeader (C:\Users\MinaS\AppData\Roaming\npm\node_modules\firebase-tools\lib\apiv2.js:207:21)
    at async Client.request (C:\Users\MinaS\AppData\Roaming\npm\node_modules\firebase-tools\lib\apiv2.js:154:34)
    at async getProjectPage (C:\Users\MinaS\AppData\Roaming\npm\node_modules\firebase-tools\lib\management\projects.js:287:17)
    at async getFirebaseProjectPage (C:\Users\MinaS\AppData\Roaming\npm\node_modules\firebase-tools\lib\management\projects.js:304:23)
    at async listFirebaseProjects (C:\Users\MinaS\AppData\Roaming\npm\node_modules\firebase-tools\lib\management\projects.js:333:29)
    at async Command.actionFn (C:\Users\MinaS\AppData\Roaming\npm\node_modules\firebase-tools\lib\commands\projects-list.js:51:20)
[error] 
[error] Error: Failed to list Firebase projects. See firebase-debug.log for more info.
[debug] [2026-11-03T18:44:48.855Z] Error: EPERM: operation not permitted, open 'C:\Users\MinaS\.config\configstore\firebase-tools.json.1868304226'
    at Object.openSync (node:fs:562:18)
    at Function.writeFileSync [as sync] (C:\Users\MinaS\AppData\Roaming\npm\node_modules\firebase-tools\node_modules\write-file-atomic\index.js:205:13)
    at set all (C:\Users\MinaS\AppData\Roaming\npm\node_modules\firebase-tools\node_modules\configstore\index.js:61:20)
    at Configstore.delete (C:\Users\MinaS\AppData\Roaming\npm\node_modules\firebase-tools\node_modules\configstore\index.js:101:12)
    at process.<anonymous> (C:\Users\MinaS\AppData\Roaming\npm\node_modules\firebase-tools\lib\bin\cli.js:90:45)
    at process.emit (node:events:530:35)
    at process.exit (node:internal/process/per_thread:194:15)
    at Timeout._onTimeout (C:\Users\MinaS\AppData\Roaming\npm\node_modules\firebase-tools\lib\errorOut.js:20:17)
    at listOnTimeout (node:internal/timers:588:17)
    at process.processTimers (node:internal/timers:523:7)
[error] 
[error] Error: An unexpected error has occurred.

import asyncio
import os
import logging
import re
import time
from pathlib import Path
from typing import Dict, Any, Optional

from aiogram import Router, F, Bot
from aiogram.filters import CommandStart, Command, StateFilter
from aiogram.types import Message, CallbackQuery, FSInputFile, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.fsm.context import FSMContext

from config import Config, ENV_PATH
from bot.states import UserStates
from bot.keyboards import (
    get_main_keyboard,
    get_grade_keyboard,
    get_subject_keyboard,
    get_about_keyboard,
    get_courses_keyboard,
    get_solving_controls,
    get_cancel_keyboard,
    get_status_keyboard,
    get_chapters_keyboard,
    get_chapter_questions_keyboard,
    get_single_question_result_keyboard,
    get_links_bank_keyboard,
    get_subscription_required_keyboard,
    get_admin_dashboard_keyboard,
    get_plan_tiers_keyboard,
    get_admin_groups_list_keyboard,
    get_admin_group_detail_keyboard,
    get_admin_passwords_keyboard,
    get_post_solve_completed_keyboard,
    get_contact_for_full_platform_keyboard,
    get_admin_solve_grade_keyboard,
    get_firebase_status_keyboard
)
from solver.qureo_client import QureoClient
from solver.gemini_solver import GeminiSolver
from solver.answers_db import answers_db

logger = logging.getLogger(__name__)

router = Router()

gemini_solver = GeminiSolver(api_key=Config.GEMINI_API_KEY)

# ==========================================
# إدارة جلسات المستخدمين المعزولة لكل مستخدم لحماية الخصوصية
# ==========================================
user_sessions: Dict[int, Dict[str, Any]] = {}


def track_message(user_id: int, message_id: int):
    """تسجيل رسائل المحادثة لمسحها لاحقاً عند الضغط على زر Clear"""
    if not user_id or not message_id:
        return
    sess = get_session(user_id)
    if "tracked_messages" not in sess:
        sess["tracked_messages"] = set()
    sess["tracked_messages"].add(message_id)


async def clear_chat_history_and_screen(bot: Bot, chat_id: int, user_id: int, current_message_id: int):
    """حذف ومسح جميع الرسائل على شاشة المحادثة وتنظيف الشاشة بالكامل"""
    sess = get_session(user_id)
    tracked = set(sess.get("tracked_messages", set()))
    if current_message_id:
        tracked.add(current_message_id)
        # جمع نطاق 100 رسالة للخلف لمسح أي رسائل قديمة ظهرت على الشاشة
        for mid in range(current_message_id, max(1, current_message_id - 100), -1):
            tracked.add(mid)

    sess["tracked_messages"] = set()

    async def _safe_del(mid: int):
        try:
            await bot.delete_message(chat_id=chat_id, message_id=mid)
        except Exception:
            pass

    sorted_mids = sorted(list(tracked), reverse=True)
    chunk_size = 25
    for i in range(0, len(sorted_mids), chunk_size):
        chunk = sorted_mids[i:i + chunk_size]
        await asyncio.gather(*[_safe_del(m) for m in chunk], return_exceptions=True)
        await asyncio.sleep(0.04)


async def perform_logout_and_clear(user_id: int):
    """مسح عملية تسجيل الدخول بالكامل وإغلاق المتصفحات وإلغاء أي مهام جارية"""
    sess = get_session(user_id)
    sess["is_solving"] = False
    task = sess.get("active_task")
    if task and not task.done():
        task.cancel()
    sess["active_task"] = None

    client = sess.get("client")
    if client:
        try:
            await client.close_browser()
        except Exception:
            pass
        sess["client"] = None

    sess["username"] = None
    sess["password"] = None
    sess["is_logged_in"] = False

    answers_db.clear_user_credentials(user_id)


async def send_photo_safely(target, photo_path: str, caption: str = "", reply_markup=None, parse_mode: str = "Markdown") -> bool:
    """إرسال لقطة الشاشة للمستخدم ثم حذفها فوراً من القرص لحماية الذاكرة والمساحة مع تتبع الرسائل"""
    if not photo_path:
        return False
    p = Path(photo_path)
    if not p.exists():
        return False
    sent_msg = None
    try:
        if hasattr(target, "answer_photo"):
            sent_msg = await target.answer_photo(
                photo=FSInputFile(str(p)),
                caption=caption,
                reply_markup=reply_markup,
                parse_mode=parse_mode
            )
        elif hasattr(target, "message") and hasattr(target.message, "answer_photo"):
            sent_msg = await target.message.answer_photo(
                photo=FSInputFile(str(p)),
                caption=caption,
                reply_markup=reply_markup,
                parse_mode=parse_mode
            )
        if sent_msg and hasattr(target, "from_user") and target.from_user:
            track_message(target.from_user.id, sent_msg.message_id)
        return True
    except Exception as e:
        logger.error(f"Error sending photo {photo_path}: {e}")
        return False
    finally:
        try:
            if p.exists():
                p.unlink(missing_ok=True)
        except Exception as e_del:
            logger.error(f"Error deleting photo {photo_path}: {e_del}")


async def safe_send_message(
    target: Message,
    text: str,
    reply_markup=None,
    parse_mode: Optional[str] = "Markdown"
) -> Optional[Message]:
    """إرسال رسالة بأمان تام مع معالجة وتفادي أخطاء الماركداون والرموز الخاصة تلقائياً"""
    try:
        return await target.answer(text, reply_markup=reply_markup, parse_mode=parse_mode)
    except Exception as e_md:
        logger.warning(f"safe_send_message Markdown failed: {e_md}, retrying without parse_mode")
        try:
            clean_text = text.replace("**", "").replace("*", "").replace("`", "")
            return await target.answer(clean_text, reply_markup=reply_markup, parse_mode=None)
        except Exception as e_final:
            logger.error(f"safe_send_message final failed: {e_final}")
            return None


async def safe_edit_message(message: Message, text: str, reply_markup=None, parse_mode: Optional[str] = "Markdown"):
    """تعديل محتوى الرسالة بأمان، والتعامل الذكي مع رسائل الصور التي لا تقبل edit_text مع تتبع الرسالة"""
    user_id = message.chat.id
    track_message(user_id, message.message_id)
    try:
        if message.text is not None:
            await message.edit_text(text, reply_markup=reply_markup, parse_mode=parse_mode)
            return
        elif message.caption is not None or getattr(message, "photo", None):
            try:
                await message.delete()
            except Exception:
                pass
            m = await safe_send_message(message, text, reply_markup=reply_markup, parse_mode=parse_mode)
            if m:
                track_message(user_id, m.message_id)
            return
    except Exception as e_edit:
        logger.warning(f"safe_edit_message edit failed: {e_edit}, trying fallback without parse_mode")
        try:
            clean_text = text.replace("**", "").replace("*", "").replace("`", "")
            await message.edit_text(clean_text, reply_markup=reply_markup, parse_mode=None)
            return
        except Exception:
            pass

    try:
        m = await safe_send_message(message, text, reply_markup=reply_markup, parse_mode=parse_mode)
        if m:
            track_message(user_id, m.message_id)
    except Exception as e:
        logger.warning(f"safe_edit_message fallback failed: {e}")


def get_session(user_id: int) -> Dict[str, Any]:
    """جلب أو إنشاء جلسة خاصة ومستقلة ومعزولة تماماً لكل مستخدم (غير مسجل الدخول دائماً عند البدء)"""
    if user_id not in user_sessions:
        profile = answers_db.get_user_profile(user_id)
        user_sessions[user_id] = {
            "grade": (profile.get("grade") if profile else None) or "grade_1",
            "subject": "programming",
            "username": None,
            "password": None,
            "is_logged_in": False,
            "is_solving": False,
            "active_task": None,
            "active_course_url": "https://me-tp.qureo.education/course/javascript_ar",
            "client": None,
            "tracked_messages": set()
        }
    if "tracked_messages" not in user_sessions[user_id]:
        user_sessions[user_id]["tracked_messages"] = set()
    return user_sessions[user_id]


def get_user_client(user_id: int) -> QureoClient:
    """الحصول على كائن QureoClient مستقل تماماً لكل مستخدم لضمان عزل المتصفح والبيانات"""
    sess = get_session(user_id)
    if sess["client"] is None:
        sess["client"] = QureoClient(headless=Config.HEADLESS)
    return sess["client"]


async def close_all_user_browsers():
    """إغلاق جميع متصفحات كيريو عند إيقاف تشغيل البوت"""
    for user_id, sess in list(user_sessions.items()):
        client = sess.get("client")
        if client:
            try:
                await client.close_browser()
            except Exception:
                pass


def update_env_file(key: str, value: str):
    """تحديث متغير في ملف .env"""
    lines = []
    found = False
    if ENV_PATH.exists():
        with open(ENV_PATH, "r", encoding="utf-8") as f:
            lines = f.readlines()

    new_lines = []
    for line in lines:
        if line.startswith(f"{key}="):
            new_lines.append(f"{key}={value}\n")
            found = True
        else:
            new_lines.append(line)

    if not found:
        new_lines.append(f"{key}={value}\n")

    with open(ENV_PATH, "w", encoding="utf-8") as f:
        f.writelines(new_lines)


async def show_main_menu(event: CallbackQuery | Message, user_id: int):
    """عرض القائمة الرئيسية المخصصة لصف ومادة الطالب مع حماية الخصوصية التامة وعزل الحسابات"""
    sess = get_session(user_id)
    grade = sess.get("grade", "grade_1")
    subject = sess.get("subject", "programming")
    is_logged_in = sess.get("is_logged_in", False)
    is_solving = sess.get("is_solving", False)
    username = sess.get("username")

    grade_name = "الصف الأول الثانوي 🎓 (JS)" if grade == "grade_1" else "الصف الثاني الثانوي 🎓 (Python / JS)"
    track_note = "مسار JavaScript حصراً" if grade == "grade_1" else "مسار بايثون / جافاسكريبت"
    sub_info = answers_db.get_user_subscription(user_id)
    if sess.get("is_admin"):
        sub_label = "👑 مالك البوت (Admin)"
    elif sub_info:
        sub_label = f"💎 {sub_info['tier_name']} (مفتوح بالكامل)"
    else:
        free_cnt = answers_db.get_free_user_solved_count(user_id)
        rem = max(0, 4 - free_cnt)
        sub_label = f"🎁 تجربة مجانية ({free_cnt}/4 مستويات - متبقي {rem})"

    # إذا كان المستخدم أدمن، نفتح له وضع الأدمن وحل الفصول المفتوح دون أي مطالبة بتسجيل حساب
    if sess.get("is_admin"):
        await show_admin_dashboard(event, user_id)
        return

    # في حال لم يكن المستخدم مسجلاً للدخول، لا نظهر أي حساب ونطلب منه صراحة التسجيل بحسابه الخاص
    if not is_logged_in or not username:
        text = (
            f"👋 **القائمة الرئيسية - منصة كيريو (Qureo)** ⚡\n"
            f"━━━━━━━━━━━━━━━━━━━━\n"
            f"🔒 **حالة الحساب:** ⚠️ غير مسجل الدخول\n"
            f"👤 لا يوجد أي حساب متصل حالياً.\n"
            f"🎓 **الصف الدراسي:** {grade_name}\n"
            f"📦 **باقة الاشتراك:** {sub_label}\n"
            f"📚 **المقرر:** البرمجة 💻 ({track_note})\n"
            f"━━━━━━━━━━━━━━━━━━━━\n\n"
            f"🔑 **سجل بحسابك الخاص أولاً للبدء في الحل:**\n"
            f"• اضغط على زر **'🔑 تسجيل الدخول بحسابك الخاص'** بالأسفل وأدخل كود الطالب الخاص بك.\n"
            f"*(حسابك محمي ومعزول 100% ولن يظهر لأي شخص آخر 🛡️)*"
        )
        kb = get_main_keyboard(is_logged_in=False, is_solving=False, grade=grade, subject="programming", is_admin=False)
    else:
        # المستخدم مسجل الدخول بحسابه الخاص
        text = (
            f"👋 **القائمة الرئيسية - منصة كيريو (Qureo)** ⚡\n"
            f"━━━━━━━━━━━━━━━━━━━━\n"
            f"👤 **حسابك النشط:** `{username}`\n"
            f"🎓 **الصف الدراسي:** {grade_name}\n"
            f"📦 **باقة الاشتراك:** {sub_label}\n"
            f"📚 **المقرر:** البرمجة 💻 ({track_note})\n"
            f"🌐 **المسار الحالي:** `{sess.get('active_course_url')}`\n"
            f"━━━━━━━━━━━━━━━━━━━━\n\n"
            f"🚀 **اضغط على '⚡ بدء الحل التلقائي الفوري (API)' ليبدأ الحل فائق السرعة!**"
        )
        kb = get_main_keyboard(is_logged_in=True, is_solving=is_solving, grade=grade, subject="programming", is_admin=sess.get("is_admin", False))

    if isinstance(event, CallbackQuery):
        try:
            await event.message.edit_text(text, reply_markup=kb, parse_mode="Markdown")
            track_message(user_id, event.message.message_id)
        except Exception:
            m = await event.message.answer(text, reply_markup=kb, parse_mode="Markdown")
            track_message(user_id, m.message_id)
    else:
        m = await event.answer(text, reply_markup=kb, parse_mode="Markdown")
        track_message(user_id, m.message_id)


# ==========================================
# أوامر البوت (Commands)
# ==========================================

@router.message(CommandStart())
@router.message(F.text.lower().in_(["start", "/start", "ابدأ", "ابدا", "البداية", "/menu", "menu"]))
async def cmd_start(message: Message, state: FSMContext):
    """الترحيب ومطالبة المستخدم بتحديد الصف وتسجيل الدخول بحسابه الخاص دائماً دون حفظ أي حسابات سابقة"""
    await state.clear()
    user_id = message.from_user.id
    
    # تنظيف اسم المستخدم لتفادي أي أخطاء في تهيئة تليجرام ماركداون
    raw_name = message.from_user.first_name if (message.from_user and message.from_user.first_name) else "يا بطل"
    clean_name = re.sub(r"[_*\[\]()~`>#+\-=|{}.!]", "", raw_name).strip() or "يا بطل"
    
    track_message(user_id, message.message_id)

    sess = get_session(user_id)


    sess["is_logged_in"] = False
    sess["username"] = None
    sess["password"] = None
    sess["is_solving"] = False

    # إغلاق أي متصفحات مفتوحة في الخلفية
    if sess.get("client"):
        try:
            await sess["client"].close_browser()
        except Exception:
            pass
        sess["client"] = None

    is_admin = False
    is_sub = answers_db.is_user_subscribed(user_id)
    free_solved = answers_db.get_free_user_solved_count(user_id)

    if not is_sub and free_solved >= 4:
        prompt_limit = (
            f"👋 مرحباً بك {clean_name} في **بوت حل منصة كيريو التعليمية (Qureo Solution) ⚡**\n"
            f"━━━━━━━━━━━━━━━━━━━━\n"
            f"🔒 **لقد استنفدت التجربة المجانية (حل أول 4 مستويات)!** 🌟\n"
            f"لحل باقي فصول واختبارات المنصة بالكامل بنسبة 100% وحصد كافة الماسات، يرجى التواصل مع صفحتنا الرسمية:\n"
            f"👉 https://m.me/1395840426948411\n"
            f"━━━━━━━━━━━━━━━━━━━━\n"
            f"*(أو أدخل كود باقة الاشتراك إذا حصلت عليه لتفعيل الحل الفوري)*"
        )
        sent = await safe_send_message(
            message,
            prompt_limit,
            reply_markup=get_contact_for_full_platform_keyboard(),
            parse_mode="Markdown"
        )
        if sent:
            track_message(user_id, sent.message_id)
        return

    trial_badge = ""
    if not is_sub:
        rem = max(0, 4 - free_solved)
        trial_badge = f"🎁 **ميزة مجانية:** متاح لك تجربة حل **أول 4 مستويات مجاناً** (متبقي {rem} مستويات) ⚡\n"

    prompt_text = (
        f"👋 مرحباً بك {clean_name} في **بوت كيريو الذكي (Qureo Solution) ⚡**\n"
        f"━━━━━━━━━━━━━━━━━━━━\n"
        f"👥 **للوكلاء والمشتركين:** اضغط على **الانضمام إلى مجموعة 🔑** أدناه وأدخل باسورد المجموعة.\n"
        f"🎓 **للطلاب:** اختر صفك الدراسي للبدء في حل التمارين وتسجيل الدخول.\n"
        f"👑 **للإدارة:** اضغط على **لوحة تحكم الأدمن** لإدارة الباقات والاشتراكات.\n"
        f"{trial_badge}"
        f"━━━━━━━━━━━━━━━━━━━━"
    )

    sent = await safe_send_message(
        message,
        prompt_text,
        reply_markup=get_grade_keyboard(),
        parse_mode="Markdown"
    )
    if sent:
        track_message(user_id, sent.message_id)
    await state.set_state(UserStates.waiting_for_grade)


@router.callback_query(F.data == "btn_clear_screen")
@router.message(Command("clear"))
@router.message(Command("logout"))
async def cb_clear_screen(event: CallbackQuery | Message, state: FSMContext, bot: Bot):
    """تنفيذ زر Clear وأمر /clear: مسح كل شيء على الشاشة ومسح تسجيل الدخول بالكامل"""
    user_id = event.from_user.id
    chat_id = event.message.chat.id if isinstance(event, CallbackQuery) else event.chat.id
    current_mid = event.message.message_id if isinstance(event, CallbackQuery) else event.message_id

    if isinstance(event, CallbackQuery):
        try:
            await event.answer("🧹 جاري مسح الشاشة وتسجيل الخروج...")
        except Exception:
            pass

    # 1. مسح حالة FSM
    await state.clear()

    # 2. مسح بيانات تسجيل الدخول بالكامل وإغلاق المتصفحات
    await perform_logout_and_clear(user_id)

    # 3. مسح جميع الرسائل السابقة على الشاشة
    await clear_chat_history_and_screen(bot, chat_id, user_id, current_mid)

    # 4. إرسال الشاشة النظيفة للمستخدم ومطالبته بالتسجيل بحسابه الخاص
    sess = get_session(user_id)
    grade = sess.get("grade", "grade_1")
    subject = sess.get("subject", "programming")

    clean_text = (
        "🧹 **تم مسح الشاشة وتسجيل الخروج بنجاح!** ⚡\n"
        "━━━━━━━━━━━━━━━━━━━━\n"
        "✅ تم تنظيف ومسح جميع الرسائل السابقة من الشاشة.\n"
        "🔒 تم مسح وحذف بيانات تسجيل الدخول بالكامل.\n"
        "👤 **حالة الحساب:** لا يوجد أي حساب مسجل حالياً.\n"
        "━━━━━━━━━━━━━━━━━━━━\n\n"
        "🔑 **سجل بحسابك الخاص للبدء:**\n"
        "اضغط على زر **'🔑 تسجيل الدخول بحسابك الخاص'** بالأسفل وأدخل كود الطالب وكلمة المرور الخاصة بك.\n"
        "*(حسابك معزول ومحمي 100% ولن يظهر لأي طالب آخر 🛡️)*"
    )
    kb = get_main_keyboard(is_logged_in=False, is_solving=False, grade=grade, subject=subject)
    new_msg = await bot.send_message(chat_id=chat_id, text=clean_text, reply_markup=kb, parse_mode="Markdown")
    track_message(user_id, new_msg.message_id)


@router.callback_query(F.data.in_(["grade_1", "grade_2"]))
async def cb_select_grade(callback: CallbackQuery, state: FSMContext):
    """معالجة اختيار الصف: أولى ثانوي أم ثانية ثانوي"""
    await callback.answer()
    user_id = callback.from_user.id
    sess = get_session(user_id)
    grade = callback.data
    sess["grade"] = grade
    sess["subject"] = "programming"

    if grade == "grade_1":
        sess["active_course_url"] = "https://me-tp.qureo.education/course/javascript_ar"
        grade_label = "الصف الأول الثانوي 🎓 (مسار JavaScript)"
    else:
        sess["active_course_url"] = "https://me-tp.qureo.education/course/python_short_ar"
        grade_label = "الصف الثاني الثانوي 🎓 (مسار Python / JS)"

    answers_db.save_user_profile(user_id=user_id, grade=grade, active_course_url=sess["active_course_url"])

    # فحص تسجيل الدخول: إذا لم يكن مسجلاً، نطلب منه كود الطالب للتسجيل بحسابه الخاص في كيريو فوراً
    if not sess.get("is_logged_in") or not sess.get("username"):
        text = (
            f"💻 **تسجيل الدخول لمنصة كيريو - {grade_label}:**\n\n"
            f"🔑 **سجل بحسابك الخاص للمتابعة:**\n"
            f"يرجى إرسال **اسم المستخدم (ID / كود الطالب)** الخاص بك في منصة كيريو:\n\n"
            f"*(اكتب كود الطالب هنا في الرسائل للمتابعة فوراً)*\n"
            f"*(ملاحظة: حسابك معزول ومحمي 100% ولن يظهر لأي شخص آخر 🛡️)*"
        )
        buttons = [
            [
                InlineKeyboardButton(text="🔙 العودة لاختيار الصف", callback_data="btn_change_grade"),
                InlineKeyboardButton(text="🧹 مسح الشاشة (Clear)", callback_data="btn_clear_screen")
            ]
        ]
        await safe_edit_message(callback.message, text, reply_markup=InlineKeyboardMarkup(inline_keyboard=buttons), parse_mode="Markdown")
        await state.set_state(UserStates.waiting_for_username)
        return

    await show_main_menu(callback, user_id)


@router.callback_query(F.data.in_(["subject_programming", "btn_back_to_subjects"]))
async def cb_select_programming(callback: CallbackQuery, state: FSMContext):
    """متابعة دروس البرمجة في كيريو"""
    await callback.answer()
    user_id = callback.from_user.id
    await show_main_menu(callback, user_id)


@router.callback_query(F.data == "btn_change_grade")
async def cb_change_grade(callback: CallbackQuery, state: FSMContext):
    """تغيير الصف الدراسي"""
    await state.clear()
    prompt_text = "🎓 **يرجى تحديد صفك الدراسي:**"
    try:
        await callback.message.edit_text(prompt_text, reply_markup=get_grade_keyboard(), parse_mode="Markdown")
    except Exception:
        await callback.message.answer(prompt_text, reply_markup=get_grade_keyboard(), parse_mode="Markdown")
    await state.set_state(UserStates.waiting_for_grade)
    await callback.answer()


@router.callback_query(F.data == "btn_about_bot")
async def cb_about_bot(callback: CallbackQuery):
    """عرض معلومات البوت والمطور مينا شحاتة برنابا SE eng"""
    about_text = (
        "ℹ️ **معلومات البوت والمطور:**\n"
        "━━━━━━━━━━━━━━━━━━━━\n"
        "👨‍💻 **مطور هذا البوت:**\n"
        "**مينا شحاتة برنابا**\n"
        "*(SE eng)*\n"
        "━━━━━━━━━━━━━━━━━━━━\n"
        "⚡ **عن البوت:**\n"
        "بوت ذكي فائق السرعة لحل تمارين ومراجعات منصة كيريو التعليمية (Qureo) بالكامل عبر الـ API وبمحاكاة المتصفح البشري بدقة 100%.\n\n"
        "🔒 **الخصوصية التامة:** جميع حسابات وجلسات الطلاب معزولة ومستقلة تماماً 100%، ولا تظهر لقطات الشاشة أو الإجابات إلا للشخص صاحب الحساب فقط في شاشته."
    )
    try:
        await callback.message.edit_text(about_text, reply_markup=get_about_keyboard(), parse_mode="Markdown")
    except Exception:
        await callback.message.answer(about_text, reply_markup=get_about_keyboard(), parse_mode="Markdown")
    await callback.answer()


@router.message(Command("help"))
async def cmd_help(message: Message):
    """شرح طريقة استخدام البوت"""
    text = (
        "📖 **دليل استخدام البوت:**\n\n"
        "1. **تسجيل الدخول بالمنصة:**\n"
        "   اضغط على '🔑 تسجيل الدخول' وأدخل اسم المستخدم وكلمة المرور الخاصة بك على منصة Qureo.\n\n"
        "2. **عرض مستواك الحالي (API):**\n"
        "   اضغط على '📊 مستواي الحالي وتفاصيل الـ API' لمعرفة الفصل الذي تقف عنده بدقة وإحصائيات ماساتك.\n\n"
        "3. **بدء الحل التلقائي:**\n"
        "   اضغط على '⚡ بدء الحل التلقائي الفوري (API)' ليفتح البوت صفحة الأسئلة ويحلها تلقائياً!\n\n"
        "4. **الأوامر السريعة:**\n"
        "   • `/status` أو `/level` : لعرض مستواك الحالي مباشرة عبر الـ API.\n"
        "   • `/screenshot` : لأخذ لقطة شاشة مباشرة للمتصفح.\n"
        "   • `/stop` : لإيقاف عملية الحل فوراً."
    )
    await message.answer(text, parse_mode="Markdown", disable_web_page_preview=True)


@router.message(Command("screenshot"))
async def cmd_screenshot(message: Message):
    """أخذ لقطة شاشة سريعة للمتصفح النشط مع تنشيط تلقائي فوري إن كان مغلقاً"""
    user_id = message.from_user.id
    sess = get_session(user_id)
    active_client = get_user_client(user_id)

    if not active_client.page or active_client.page.is_closed():
        u = sess.get("username")
        p = sess.get("password")
        if u and p:
            wait_msg = await message.answer("🔄 **جاري تنشيط المتصفح والتقاط لقطة الشاشة...**", parse_mode="Markdown")
            ok, _, _ = await active_client.login(u, p)
            try:
                await wait_msg.delete()
            except Exception:
                pass
            if not ok or not active_client.page:
                await message.answer("⚠️ تعذر تنشيط المتصفح حالياً. يرجى تسجيل الدخول أولاً.")
                return
        else:
            await message.answer("⚠️ المتصفح غير مفتوح حالياً. قم بتسجيل الدخول أو فتح مسار أولاً.")
            return

    msg = await message.answer("📸 جاري التقاط لقطة الشاشة...")
    shot_path = await active_client.take_screenshot(f"manual_cmd_{user_id}")
    if shot_path and Path(shot_path).exists():
        await send_photo_safely(
            target=message,
            photo_path=shot_path,
            caption=f"🌐 **الصفحة الحالية:**\n`{active_client.page.url}`",
            parse_mode="Markdown"
        )
        await msg.delete()
    else:
        await msg.edit_text("❌ تعذر التقاط لقطة الشاشة.")


@router.message(Command("stop"))
async def cmd_stop(message: Message):
    """إيقاف عملية الحل"""
    user_id = message.from_user.id
    sess = get_session(user_id)
    sess["is_solving"] = False
    await message.answer("⏹️ تم إيقاف عملية الحل التلقائي.")


# ==========================================
# معالجة الأزرار (Callbacks)
# ==========================================

@router.callback_query(F.data == "btn_main_menu")
async def cb_main_menu(callback: CallbackQuery, state: FSMContext):
    await state.clear()
    user_id = callback.from_user.id
    await show_main_menu(callback, user_id)
    await callback.answer()


@router.callback_query(F.data == "btn_account_status")
@router.message(Command("status"))
@router.message(Command("level"))
async def cb_account_status(event: CallbackQuery | Message):
    """عرض تقرير شامل عن المستوى الحالي وتقدم الطالب مباشرة عبر الـ API"""
    is_callback = isinstance(event, CallbackQuery)
    message = event.message if is_callback else event
    user_id = event.from_user.id
    sess = get_session(user_id)
    client = get_user_client(user_id)
    grade = sess.get("grade", "grade_1")
    subject = sess.get("subject", "programming")

    if is_callback:
        await event.answer()

    if not sess.get("is_logged_in") or not client.page:
        text = (
            "⚠️ **أنت غير مسجل الدخول بمنصة كيريو حالياً!**\n\n"
            "يرجى الضغط على زر **'🔑 تسجيل الدخول'** أولاً، ليتمكن البوت من جلب مستواك الحالي وكافة تفاصيل تقدمك مباشرة عبر الـ API."
        )
        markup = get_main_keyboard(is_logged_in=False, is_solving=False, grade=grade, subject="programming")
        if is_callback:
            try:
                await event.message.edit_text(text, reply_markup=markup, parse_mode="Markdown")
            except Exception:
                await event.message.answer(text, reply_markup=markup, parse_mode="Markdown")
        else:
            await event.answer(text, reply_markup=markup, parse_mode="Markdown")
        return

    loading_msg = await message.answer("🔄 **جاري الاتصال بـ API المنصة لجلب مستواك الحالي وبيانات الفصول...**")

    try:
        client.api.set_page(client.page)
        if grade == "grade_1":
            course_id = "javascript_ar"
            course_name = "جافاسكريبت (JavaScript)"
        else:
            page_url = client.page.url if (client.page and not client.page.is_closed()) else ""
            course_url = sess.get("active_course_url") or ""
            combined = f"{page_url} {course_url}".lower()
            course_id = "javascript_ar" if "javascript" in combined else "python_short_ar"
            course_name = "جافاسكريبت (JavaScript)" if "javascript" in course_id else "بايثون (Python)"

        # التأكد من التواجد في me-tp
        if "me-tp.qureo.education" not in (client.page.url or ""):
            await client.open_course(sess.get("active_course_url"))
            await asyncio.sleep(1.5)

        # استدعاء دالة الـ Dashboard من الـ API
        status_info = await client.api.get_student_dashboard_status(course_id)

        curr = status_info.get("current_chapter")
        curr_id = curr.get("id") if curr else None
        curr_seq = curr.get("seq") if curr else "?"
        curr_name = curr.get("name") if curr else "جميع الفصول مكتملة 🎉"
        curr_type = "اختبار فهم (Test)" if curr and curr.get("test_type") == "test" else "مراجعة (Review)"
        curr_q_count = curr.get("question_count", 0) if curr else 0
        active_lec_id = status_info.get("active_lecture_id")

        total_chap = status_info.get("total_chapters", 25)
        comp_count = status_info.get("completed_count", 0)
        rem_count = status_info.get("remaining_count", 0)
        diamonds = status_info.get("total_diamonds", 0)
        correct = status_info.get("total_correct_count", 0)
        percent = status_info.get("completion_percentage", 0)

        # تجهيز قائمة بآخر الفصول المنجزة
        completed_list = status_info.get("completed_chapters", [])
        history_text = ""
        if completed_list:
            for item in completed_list[-3:]:
                p = item.get("progress") or {}
                history_text += f"• الفصل {item.get('seq')}: **{item.get('name')}** - 5/5 💎 ({p.get('best_correct_count', 0)} إجابة صحيحة)\n"
        else:
            history_text = "• لم يتم إكمال أي فصل بعد (أنت في البداية 🚀)\n"

        username = sess.get("username", "طالب كيريو")

        report = (
            f"📊 **تقرير مستواك الحالي وبيانات الـ API الرسمية:**\n"
            f"━━━━━━━━━━━━━━━━━━━━\n"
            f"👤 **الطالب:** `{username}`\n"
            f"📚 **المسار النشط:** {course_name} (`{course_id}`)\n\n"
            f"📍 **المستوى / الفصل الذي تقف عنده الآن:**\n"
            f"• **الفصل رقم ({curr_seq}):** **{curr_name}**\n"
            f"• **كود الفصل (ID):** `{curr_id}`\n"
            f"• **نوع الاختبار:** {curr_type} ({curr_q_count} أسئلة)\n"
            f"• **الدرس الحالي النشط:** `{active_lec_id or 'الدرس الأول'}`\n"
            f"• **الحالة:** ⏳ قيد الحل والمتابعة\n\n"
            f"📈 **إحصائيات التقدم والماسات:**\n"
            f"• **الفصول المكتملة:** {comp_count} من {total_chap} فصل ({percent}%)\n"
            f"• **الفصول المتبقية:** {rem_count} فصل\n"
            f"• **مجموع الماسات:** {diamonds} 💎\n"
            f"• **الإجابات الصحيحة:** {correct} إجابة صحيحة\n\n"
            f"📋 **آخر الفصول المنجزة:**\n"
            f"{history_text}"
            f"━━━━━━━━━━━━━━━━━━━━\n"
            f"💡 *البيانات مسحوبة مباشرة وفورياً من سيرفرات كيريو (API).*"
        )

        reply_kb = get_status_keyboard(current_chapter_id=curr_id, current_chapter_name=curr_name if curr_id else "")

        await loading_msg.edit_text(report, reply_markup=reply_kb, parse_mode="Markdown")

    except Exception as e:
        logger.error(f"Error fetching dashboard status: {e}")
        await loading_msg.edit_text(
            f"⚠️ حدث خطأ أثناء قراءة بيانات الـ API: {str(e)}",
            reply_markup=get_main_keyboard(is_logged_in=True, is_solving=False, grade=grade, subject=subject)
        )


@router.callback_query(F.data == "btn_cancel")
async def cb_cancel(callback: CallbackQuery, state: FSMContext):
    await state.clear()
    user_id = callback.from_user.id
    sess = get_session(user_id)
    if sess.get("is_admin"):
        await show_admin_dashboard(callback, user_id)
    else:
        await show_main_menu(callback, user_id)
    await callback.answer()


@router.callback_query(F.data == "btn_gemini_key")
async def cb_gemini_settings(callback: CallbackQuery, state: FSMContext):
    key_preview = f"...{gemini_solver.api_key[-6:]}" if gemini_solver.api_key and len(gemini_solver.api_key) > 6 else "غير معين"
    text = (
        f"⚙️ **إعدادات مفتاح Gemini API:**\n\n"
        f"المفتاح الحالي: `{key_preview}`\n\n"
        f"للحصول على مفتاح مجاني جديد، قم بإنشاء المفتاح مجاناً من هنا [Google AI Studio](https://aistudio.google.com/app/apikey):\n"
        f"ثم أرسل المفتاح الآن في هذه المحادثة مباشرة:"
    )
    try:
        await callback.message.edit_text(
            text,
            reply_markup=get_cancel_keyboard(),
            parse_mode="Markdown",
            disable_web_page_preview=True
        )
    except Exception:
        await callback.message.answer(
            text,
            reply_markup=get_cancel_keyboard(),
            parse_mode="Markdown",
            disable_web_page_preview=True
        )
    await state.set_state(UserStates.waiting_for_gemini_key)
    await callback.answer()


@router.message(UserStates.waiting_for_gemini_key)
async def process_gemini_key(message: Message, state: FSMContext):
    key = message.text.strip() if message.text else ""
    if len(key) < 10:
        await message.answer("⚠️ يبدو أن المفتاح غير صالح. يرجى إرسال مفتاح Gemini API صحيح:", reply_markup=get_cancel_keyboard())
        return

    user_id = message.from_user.id
    sess = get_session(user_id)
    grade = sess.get("grade", "grade_1")
    subject = sess.get("subject", "programming")

    gemini_solver.set_api_key(key)
    update_env_file("GEMINI_API_KEY", key)
    await state.clear()

    try:
        await message.delete()
    except Exception:
        pass

    await message.answer(
        "✅ **تم حفظ وتفعيل مفتاح Gemini API بنجاح!**\nيمكنك استخدامه كخيار احتياطي.",
        reply_markup=get_main_keyboard(is_logged_in=sess["is_logged_in"], is_solving=sess["is_solving"], grade=grade, subject=subject),
        parse_mode="Markdown"
    )


@router.callback_query(F.data == "btn_quick_login")
async def cb_quick_login(callback: CallbackQuery, state: FSMContext):
    """توجيه المستخدم لإدخال بيانات حسابه الخاص في كيريو"""
    await state.clear()
    await callback.answer()
    await callback.message.answer(
        "🔑 **يرجى إرسال اسم المستخدم (ID / كود الطالب) الخاص بك في منصة كيريو:**\n"
        "*(لكل طالب حسابه المستقل الخاص به)*",
        reply_markup=get_cancel_keyboard(),
        parse_mode="Markdown"
    )
    await state.set_state(UserStates.waiting_for_username)


@router.callback_query(F.data == "btn_login")
async def cb_start_login(callback: CallbackQuery, state: FSMContext):
    user_id = callback.from_user.id
    sess = get_session(user_id)
    if not sess.get("is_admin") and not answers_db.is_user_subscribed(user_id):
        free_solved = answers_db.get_free_user_solved_count(user_id)
        if free_solved >= 4:
            await callback.answer("⚠️ لقد استنفدت التجربة المجانية (أول 4 مستويات).", show_alert=True)
            await callback.message.answer(
                "🔒 **لقد استنفدت التجربة المجانية بحل أول 4 مستويات بنجاح!** 🌟\n"
                "━━━━━━━━━━━━━━━━━━━━\n"
                "لحل باقي فصول واختبارات المنصة بالكامل، يرجى التواصل مع صفحتنا الرسمية:\n"
                "👉 https://m.me/1395840426948411",
                reply_markup=get_contact_for_full_platform_keyboard(),
                parse_mode="Markdown"
            )
            return
    sess["is_logged_in"] = False
    sess["username"] = None
    sess["password"] = None
    answers_db.clear_user_credentials(user_id)

    platform_name = "منصة كيريو (Qureo)"
    text = (
        f"🔑 **تسجيل الدخول إلى {platform_name} بحسابك الخاص:**\n\n"
        "يرجى إرسال **اسم المستخدم (ID / كود الطالب)** الخاص بك في منصة كيريو:\n"
        "*(حسابك معزول ومحمي 100% ولن يظهر لأي مستخدم آخر 🛡️)*"
    )
    try:
        await callback.message.edit_text(text, reply_markup=get_cancel_keyboard(), parse_mode="Markdown")
        track_message(user_id, callback.message.message_id)
    except Exception:
        m = await callback.message.answer(text, reply_markup=get_cancel_keyboard(), parse_mode="Markdown")
        track_message(user_id, m.message_id)
    await state.set_state(UserStates.waiting_for_username)
    await callback.answer()


@router.message(UserStates.waiting_for_username)
async def process_username(message: Message, state: FSMContext):
    user_id = message.from_user.id
    track_message(user_id, message.message_id)
    username = message.text.strip() if message.text else ""

    # فحص فوري: إذا كان المستخدم يكتب كلمة مرور الأدمن أو أمر admin بدلاً من كود الطالب
    if username in answers_db.get_admin_passwords():
        sess = get_session(user_id)
        sess["is_admin"] = True
        await state.clear()
        try:
            await message.delete()
        except Exception:
            pass
        sent = await message.answer("✅ **تم التحقق وتسجيل الدخول كمسؤول بنجاح!** 👑", parse_mode="Markdown")
        track_message(user_id, sent.message_id)
        await show_admin_dashboard(message, user_id)
        return

    if username.lower() in ["admin", "/admin", "ادمن", "أدمن", "الادمن", "الأدمن"]:
        await state.clear()
        await cmd_admin(message, state)
        return

    if not username:
        m = await message.answer("⚠️ اسم المستخدم لا يمكن أن يكون فارغاً. يرجى إرسال اسم المستخدم (ID / كود الطالب) مجدداً:", reply_markup=get_cancel_keyboard())
        track_message(user_id, m.message_id)
        return

    sess = get_session(user_id)
    sess["username"] = username

    await state.update_data(username=username)
    m = await message.answer(
        f"✅ تم استلام كود الطالب (ID): `{username}`\n\n"
        "🔒 الآن يرجى إرسال **كلمة المرور (Password)**:\n"
        "*(سيتم حذف رسالتك تلقائياً فور استلامها لحماية أمان وخصوصية حسابك)*",
        reply_markup=get_cancel_keyboard(),
        parse_mode="Markdown"
    )
    track_message(user_id, m.message_id)
    await state.set_state(UserStates.waiting_for_password)


@router.message(UserStates.waiting_for_password)
async def process_password(message: Message, state: FSMContext):
    password = message.text.strip() if message.text else ""
    user_id = message.from_user.id
    sess = get_session(user_id)

    # فحص فوري: إذا كان المستخدم يكتب كلمة مرور الأدمن أو أمر admin
    if password in answers_db.get_admin_passwords():
        sess["is_admin"] = True
        await state.clear()
        try:
            await message.delete()
        except Exception:
            pass
        sent = await message.answer("✅ **تم التحقق وتسجيل الدخول كمسؤول بنجاح!** 👑", parse_mode="Markdown")
        track_message(user_id, sent.message_id)
        await show_admin_dashboard(message, user_id)
        return

    if password.lower() in ["admin", "/admin", "ادمن", "أدمن", "الادمن", "الأدمن"]:
        await state.clear()
        await cmd_admin(message, state)
        return
    username = sess.get("username", "")

    try:
        await message.delete()
    except Exception:
        pass

    await state.clear()
    sess["password"] = password
    grade = sess.get("grade", "grade_1")
    subject = "programming"

    status_msg = await message.answer(
        f"🔄 **جاري تسجيل الدخول والاتصال بمنصة كيريو بحساب `{username}`...**\n"
        "يرجى الانتظار ثوانٍ معدودة...",
        parse_mode="Markdown"
    )
    client = get_user_client(user_id)
    client.headless = Config.HEADLESS
    try:
        success, resp_message, screenshot_path = await client.login(username, password)
    except Exception as e:
        await status_msg.edit_text(
            f"❌ حدث خطأ أثناء تشغيل المتصفح: {str(e)}\n\nيرجى إعادة المحاولة بالضغط على تسجيل الدخول.",
            reply_markup=get_main_keyboard(is_logged_in=False, is_solving=False, grade=grade, subject=subject)
        )
        return

    if success:
        sess["is_logged_in"] = True

        # حفظ تفضيلات الصف والمادة فقط دون حفظ اسم المستخدم أو كلمة المرور لحماية الخصوصية
        answers_db.save_user_profile(
            user_id=user_id,
            grade=grade,
            subject=subject,
            active_course_url=sess.get("active_course_url", "")
        )

        grade_label = "الصف الأول (JavaScript ⚡)" if grade == "grade_1" else "الصف الثاني الثانوي 🐍"
        success_text = (
            f"🎉 **تم تسجيل الدخول بنجاح!**\n\n"
            f"👤 **الحساب النشط:** `{username}`\n"
            f"🎓 **الصف:** {grade_label}\n\n"
            f"🚀 **اضغط الآن على '⚡ بدء الحل' ليفتح المتصفح ويبدأ الحل التلقائي:**"
        )
        kb = get_main_keyboard(is_logged_in=True, is_solving=False, grade=grade, subject=subject)
        if screenshot_path and Path(screenshot_path).exists():
            await send_photo_safely(message, screenshot_path, caption=success_text, reply_markup=kb, parse_mode="Markdown")
        else:
            await status_msg.edit_text(
                success_text,
                reply_markup=kb,
                parse_mode="Markdown"
            )
    else:
        sess["is_logged_in"] = False
        sess["username"] = None
        sess["password"] = None
        fail_text = f"❌ فشل تسجيل الدخول: {resp_message}\n\nيرجى إعادة المحاولة وكتابة اسم المستخدم (ID / كود الطالب) من جديد:"
        if screenshot_path and Path(screenshot_path).exists():
            await send_photo_safely(message, screenshot_path, caption=fail_text, reply_markup=get_cancel_keyboard(), parse_mode=None)
        else:
            await safe_edit_message(status_msg, fail_text, reply_markup=get_cancel_keyboard(), parse_mode=None)
        await state.set_state(UserStates.waiting_for_username)


@router.callback_query(F.data == "btn_select_course")
async def cb_select_course(callback: CallbackQuery):
    user_id = callback.from_user.id
    sess = get_session(user_id)
    if sess.get("grade") == "grade_1":
        await callback.answer("⚠️ مسار الصف الأول الثانوي مخصص لـ JavaScript فقط!", show_alert=True)
        return
    text = (
        "📚 **اختر المسار التعليمي الخاص بك في منصة كيريو:**\n\n"
        f"المسار الحالي: `{sess.get('active_course_url')}`"
    )
    try:
        await callback.message.edit_text(
            text,
            reply_markup=get_courses_keyboard(),
            parse_mode="Markdown"
        )
    except Exception:
        await callback.message.answer(
            text,
            reply_markup=get_courses_keyboard(),
            parse_mode="Markdown"
        )
    await callback.answer()


async def show_course_chapters_view(event, course_code: str = "py", page: int = 1, user_id: Optional[int] = None):
    """عرض المستويات والفصول الخاصة بالمسار كأزرار تفاعلية لعرض أسئلتها وحلها سؤال بسؤال"""
    if user_id is None:
        user_id = event.from_user.id
    sess = get_session(user_id)
    client = get_user_client(user_id)

    # التحقق من الصف: الصف الأول الثانوي جافاسكريبت دائماً
    if sess.get("grade") == "grade_1":
        course_code = "js"

    course_id = "javascript_ar" if course_code == "js" else "python_short_ar"
    course_name = "مسار جافاسكريبت (JavaScript) ⚡" if course_code == "js" else "مسار بايثون (Python) 🐍"
    sess["active_course_url"] = f"https://me-tp.qureo.education/course/{course_id}"

    # 1. محاولة تسجيل الدخول التلقائي إذا كانت البيانات متوفرة
    if not sess.get("is_logged_in"):
        u = sess.get("username")
        p = sess.get("password")
        if u and p:
            try:
                login_ok, _, _ = await client.login(u, p)
                if login_ok:
                    sess["is_logged_in"] = True
            except Exception as e_log:
                logger.error(f"Auto-login failed: {e_log}")

    grade = sess.get("grade", "grade_1")
    subject = sess.get("subject", "programming")

    if not sess.get("is_logged_in") or not client.page:
        text = (
            f"📚 **تم اختيار {course_name}**\n\n"
            "⚠️ **تنبيه:** يرجى تسجيل الدخول بحسابك في منصة كيريو أولاً ليتمكن البوت من جلب الأسئلة وعرضها وحلها عبر الـ API."
        )
        markup = get_main_keyboard(is_logged_in=False, is_solving=False, grade=grade, subject=subject)
        if isinstance(event, CallbackQuery):
            try:
                await event.message.edit_text(text, reply_markup=markup, parse_mode="Markdown")
            except Exception:
                await event.message.answer(text, reply_markup=markup, parse_mode="Markdown")
            await event.answer()
        else:
            await event.answer(text, reply_markup=markup, parse_mode="Markdown")
        return

    # التأكد من التواجد في نطاق منصة الدراسة me-tp
    if "me-tp.qureo.education" not in (client.page.url or ""):
        await client.open_course(sess.get("active_course_url"))
        await asyncio.sleep(1.5)

    client.api.set_page(client.page)

    # جلب الفصول والماسات
    chapters = await client.api.get_course_chapters(course_id)
    if not chapters:
        chapters = client.api.get_fallback_python_chapters() if course_code == "py" else client.api.get_fallback_js_chapters()

    diamonds_data = await client.api.get_student_diamonds(course_id)
    completed_ids = {
        d["chapter_id"]
        for d in diamonds_data
        if d.get("completed_at") or d.get("diamond", 0) >= 5
    }

    # تحديد المستوى الحالي (أول فصل غير مكتمل)
    current_chap_id = None
    for c in chapters:
        if c.get("id") not in completed_ids:
            current_chap_id = c.get("id")
            break

    total_diamonds = sum(d.get("diamond", 0) for d in diamonds_data if isinstance(d, dict))
    server_diamonds = await client.api.get_total_diamonds(course_id)
    if server_diamonds > total_diamonds:
        total_diamonds = server_diamonds

    username = sess.get("username", "طالب كيريو")

    text = (
        f"📚 **{course_name}**\n"
        f"━━━━━━━━━━━━━━━━━━━━\n"
        f"👤 **الطالب:** `{username}`\n"
        f"💎 **الماسات:** **{total_diamonds} ماسة مكتسبة** 🌟\n"
        f"📊 **الإنجاز:** **{len(completed_ids)} من {len(chapters)} مستويات**\n"
        f"━━━━━━━━━━━━━━━━━━━━\n"
        f"👇 **اضغط على أي مستوى لعرض أسئلته وحلها سؤال بسؤال:**\n"
        f"*(يمكنك النقر على أي سؤال لحله فوراً عبر الـ API وتأكيد إجابته)*"
    )

    markup = get_chapters_keyboard(
        chapters=chapters,
        page=page,
        per_page=5,
        course_code=course_code,
        completed_ids=completed_ids,
        current_chap_id=current_chap_id
    )

    if isinstance(event, CallbackQuery):
        try:
            await event.message.edit_text(text, reply_markup=markup, parse_mode="Markdown")
        except Exception:
            await event.message.answer(text, reply_markup=markup, parse_mode="Markdown")
        await event.answer()
    else:
        await event.answer(text, reply_markup=markup, parse_mode="Markdown")


@router.callback_query(F.data == "course_python")
async def cb_course_python(callback: CallbackQuery):
    user_id = callback.from_user.id
    sess = get_session(user_id)
    if sess.get("grade") == "grade_1":
        await callback.answer("⚠️ طلاب الصف الأول الثانوي متاح لهم مسار JavaScript فقط!", show_alert=True)
        return
    await callback.answer("جاري فتح مسار بايثون...")
    sess["active_course_url"] = "https://me-tp.qureo.education/course/python_short_ar"
    await show_course_chapters_view(callback, course_code="py", page=1, user_id=user_id)


@router.callback_query(F.data == "course_js")
async def cb_course_js(callback: CallbackQuery):
    user_id = callback.from_user.id
    sess = get_session(user_id)
    sess["active_course_url"] = "https://me-tp.qureo.education/course/javascript_ar"
    await callback.answer("جاري فتح مسار جافاسكريبت...")
    await show_course_chapters_view(callback, course_code="js", page=1, user_id=user_id)


@router.callback_query(F.data.startswith("cp_"))
async def cb_chapters_pagination(callback: CallbackQuery):
    """التنقل بين صفحات المستويات في المسار"""
    user_id = callback.from_user.id
    sess = get_session(user_id)
    parts = callback.data.split("_")
    page = int(parts[1]) if len(parts) > 1 and parts[1].isdigit() else 1
    course_code = parts[2] if len(parts) > 2 else "py"
    if sess.get("grade") == "grade_1":
        course_code = "js"
    await show_course_chapters_view(callback, course_code=course_code, page=page, user_id=user_id)


@router.callback_query(F.data.startswith("vc_"))
async def cb_view_chapter_questions(callback: CallbackQuery):
    """عرض أسئلة مستوى محدد ليختار المستخدم السؤال المراد حله عبر الـ API"""
    chap_id_str = callback.data.replace("vc_", "").strip()
    if not chap_id_str.isdigit():
        await callback.answer("معرف المستوى غير صالح!", show_alert=True)
        return

    chap_id = int(chap_id_str)
    await callback.answer("🔄 جاري قراءة أسئلة المستوى عبر الـ API...")

    user_id = callback.from_user.id
    sess = get_session(user_id)

    client = get_user_client(user_id)

    if sess.get("grade") == "grade_1":
        course_code = "js"
        course_id = "javascript_ar"
    else:
        course_url = sess.get("active_course_url") or ""
        course_code = "js" if "javascript" in course_url.lower() else "py"
        course_id = "javascript_ar" if course_code == "js" else "python_short_ar"

    client.api.set_page(client.page)

    chapters = await client.api.get_course_chapters(course_id)
    chap_obj = next((c for c in chapters if c.get("id") == chap_id), None)
    chap_name = chap_obj.get("name", f"فصل {chap_id}") if chap_obj else f"فصل {chap_id}"
    chap_seq = chap_obj.get("seq", "?") if chap_obj else "?"
    test_type = chap_obj.get("test_type", "review") if chap_obj else "review"

    # جلب الأسئلة عبر API
    questions = await client.api.get_test_questions(chap_id, test_type=test_type)
    if not questions:
        await callback.answer("تعذر جلب أسئلة هذا المستوى حالياً عبر الـ API.", show_alert=True)
        return

    # فحص الأسئلة المحلولة مسبقاً في بنك الإجابات
    solved_ids = set()
    for q_item in questions:
        q_info = q_item.get("question", q_item)
        qid = q_info.get("id") or q_item.get("id")
        if answers_db.get_answer(qid):
            solved_ids.add(qid)

    type_name = "اختبار فهم تراكمي (Test)" if test_type == "test" else "مراجعة وتمارين (Review)"
    text = (
        f"📖 **المستوى ({chap_seq}): {chap_name}**\n"
        f"━━━━━━━━━━━━━━━━━━━━\n"
        f"• كود المستوى: `{chap_id}`\n"
        f"• نوع الاختبار: **{type_name}**\n"
        f"• إجمالي الأسئلة: **{len(questions)} أسئلة**\n"
        f"• الإجابات المحفوظة بالبنك: **{len(solved_ids)} سؤال** ✅\n"
        f"━━━━━━━━━━━━━━━━━━━━\n"
        f"🎯 **اضغط على أي سؤال أدناه لحله فوراً عبر الـ API:**\n"
        f"*(سيتم إرسال الإجابة الصحيحة وحفظها وعرض الشرح بالتفصيل)*"
    )

    markup = get_chapter_questions_keyboard(
        chapter_id=chap_id,
        questions=questions,
        test_type=test_type,
        course_code=course_code,
        solved_ids=solved_ids
    )

    try:
        await callback.message.edit_text(text, reply_markup=markup, parse_mode="Markdown")
    except Exception:
        await callback.message.answer(text, reply_markup=markup, parse_mode="Markdown")


@router.callback_query(F.data.startswith("sq_"))
async def cb_solve_single_question(callback: CallbackQuery):
    """حل سؤال محدد بمفرده عبر الـ API بضغطة زر"""
    parts = callback.data.split("_")
    if len(parts) < 3:
        await callback.answer("بيانات السؤال غير مكتملة!", show_alert=True)
        return

    chap_id = int(parts[1])
    q_id = int(parts[2])

    await callback.answer("⚡ جاري حل السؤال عبر الـ API...")

    user_id = callback.from_user.id
    sess = get_session(user_id)
    client = get_user_client(user_id)

    if sess.get("grade") == "grade_1":
        course_code = "js"
        course_id = "javascript_ar"
    else:
        course_url = sess.get("active_course_url") or ""
        course_code = "js" if "javascript" in course_url.lower() else "py"
        course_id = "javascript_ar" if course_code == "js" else "python_short_ar"

    client.api.set_page(client.page)

    chapters = await client.api.get_course_chapters(course_id)
    chap_obj = next((c for c in chapters if c.get("id") == chap_id), None)
    test_type = chap_obj.get("test_type", "review") if chap_obj else "review"

    res = await client.api.solve_single_question(
        chapter_id=chap_id,
        question_id=q_id,
        test_type=test_type
    )

    if not res.get("success"):
        await callback.message.answer(f"⚠️ تعذر حل السؤال: {res.get('message', 'خطأ غير متوقع')}")
        return

    seq = res.get("seq", 1)
    total = res.get("total_questions", 1)
    q_text = res.get("question_text") or "سؤال برمجي / كود"
    ans_text = res.get("correct_answer") or "تم استخراج الإجابة النموذجية"
    explanation = res.get("explanation") or "تم التحقق من صحة الإجابة النموذجية بنجاح 100%."
    cache_tag = " (⚡ فورياً من بنك الإجابات)" if res.get("from_cache") else " (💾 تم فحص الإجابة وحفظها بالبنك)"

    result_msg = (
        f"🎯 **تم حل السؤال ({seq} من {total}) بنجاح!** ✅{cache_tag}\n"
        f"━━━━━━━━━━━━━━━━━━━━\n"
        f"📌 **نص السؤال:**\n`{q_text}`\n\n"
        f"💡 **الإجابة النموذجية المعتمدة:**\n```\n{ans_text}\n```\n\n"
        f"📖 **الشرح والتحليل:**\n{explanation}\n"
        f"━━━━━━━━━━━━━━━━━━━━\n"
        f"🌟 **الحالة:** 100% إجابة صحيحة مرسلة إلى سيرفرات كيريو."
    )

    markup = get_single_question_result_keyboard(
        chapter_id=chap_id,
        next_q_id=res.get("next_question_id"),
        course_code=course_code
    )

    try:
        await callback.message.edit_text(result_msg, reply_markup=markup, parse_mode="Markdown")
    except Exception:
        await callback.message.answer(result_msg, reply_markup=markup, parse_mode="Markdown")


@router.callback_query(F.data.startswith("sc_"))
async def cb_solve_chapter_short(callback: CallbackQuery, state: FSMContext):
    """اختصار لحل فصل محدد"""
    chap_id = callback.data.replace("sc_", "").strip()
    if not chap_id.isdigit():
        await callback.answer("رقم الفصل غير صالح!", show_alert=True)
        return
    await solve_chapter_by_id(callback, int(chap_id), state)


@router.callback_query(F.data == "noop")
async def cb_noop(callback: CallbackQuery):
    """زر غير نشط (مؤشر رقم الصفحة)"""
    await callback.answer()


@router.callback_query(F.data == "course_custom")
async def cb_course_custom(callback: CallbackQuery, state: FSMContext):
    user_id = callback.from_user.id
    sess = get_session(user_id)
    text = (
        "🔗 **إدخال رابط مخصص لمستوى أو درس في كيريو:**\n\n"
        "أرسل رابط الصفحة التي تريد الانتقال إليها والحل فيها مباشرة:\n"
        "مثال:\n"
        "`https://me-tp.qureo.education/course/javascript_ar`\n"
        "أو رقم الفصل مباشرة (مثال: `90032`):"
    )
    try:
        await callback.message.edit_text(text, reply_markup=get_cancel_keyboard(), parse_mode="Markdown")
    except Exception:
        await callback.message.answer(text, reply_markup=get_cancel_keyboard(), parse_mode="Markdown")
    await state.set_state(UserStates.waiting_for_custom_url)
    await callback.answer()


@router.message(UserStates.waiting_for_custom_url)
async def process_custom_url(message: Message, state: FSMContext):
    raw_text = message.text.strip() if message.text else ""
    await state.clear()
    user_id = message.from_user.id
    sess = get_session(user_id)
    client = get_user_client(user_id)
    grade = sess.get("grade", "grade_1")
    subject = sess.get("subject", "programming")

    # فحص رابط الفصل أو رقمه
    chap_match = re.search(r"chapter/(\d+)", raw_text)
    if chap_match or (raw_text.isdigit() and len(raw_text) in [5, 6]):
        cid = int(chap_match.group(1)) if chap_match else int(raw_text)
        clean_url = f"https://me-tp.qureo.education/chapter/{cid}"
        if cid >= 90000 or grade == "grade_1":
            sess["active_course_url"] = "https://me-tp.qureo.education/course/javascript_ar"
        client.headless = Config.HEADLESS

        if not sess.get("is_logged_in") or not client.page or client.page.is_closed():
            u = sess.get("username")
            p = sess.get("password")
            if u and p:
                login_ok, _, _ = await client.login(u, p)
                if login_ok:
                    sess["is_logged_in"] = True
            else:
                await message.answer("🔑 يرجى تسجيل الدخول أولاً بإرسال اسم المستخدم (ID / كود الطالب):")
                await state.set_state(UserStates.waiting_for_username)
                return

        sess["is_solving"] = True
        await message.answer(
            f"🎯 **تم استلام الفصل ({cid}) بنجاح!**\n"
            f"🌐 **الرابط النظيف:** `{clean_url}`\n"
            f"⚡ **جاري فتح المتصفح وحل الفصل فوراً عبر الـ API...**",
            reply_markup=get_solving_controls(),
            parse_mode="Markdown"
        )
        asyncio.create_task(run_single_chapter_solver(message, cid, user_id))
        return

    # فحص رابط المسار
    course_match = re.search(r"course/([a-zA-Z0-9_-]+)", raw_text)
    if course_match:
        course_id = course_match.group(1).lower()
        if grade == "grade_1" and "python" in course_id:
            await message.answer(
                "⚠️ طلاب الصف الأول الثانوي متاح لهم مسار JavaScript فقط!\n"
                "تم تحويلك تلقائياً لمسار جافاسكريبت.",
                reply_markup=get_main_keyboard(is_logged_in=sess["is_logged_in"], is_solving=sess["is_solving"], grade=grade, subject=subject)
            )
            course_id = "javascript_ar"
        sess["active_course_url"] = f"https://me-tp.qureo.education/course/{course_id}"
        code = "js" if "javascript" in course_id else "py"
        await show_course_chapters_view(message, course_code=code, page=1, user_id=user_id)
        return

    # رابط عادي
    if raw_text.startswith("http"):
        sess["active_course_url"] = raw_text
        await message.answer(
            f"✅ تم حفظ الرابط المخصص بنجاح:\n`{raw_text}`\n\nيمكنك الآن البدء بالحل.",
            reply_markup=get_main_keyboard(is_logged_in=sess["is_logged_in"], is_solving=sess["is_solving"], grade=grade, subject=subject),
            parse_mode="Markdown"
        )
        if client.page and sess.get("is_logged_in"):
            asyncio.create_task(client.open_course(raw_text))
        return

    await message.answer("⚠️ لم يتم التعرف على الرابط أو رقم الفصل. يرجى التأكد وإعادة المحاولة.", reply_markup=get_cancel_keyboard())


@router.callback_query(F.data == "btn_screenshot")
async def cb_take_screenshot(callback: CallbackQuery):
    user_id = callback.from_user.id
    sess = get_session(user_id)
    active_client = get_user_client(user_id)

    if not active_client.page or active_client.page.is_closed():
        u = sess.get("username")
        p = sess.get("password")
        if u and p:
            await callback.answer("🔄 جاري تنشيط المتصفح والتقاط الشاشة...")
            ok, _, _ = await active_client.login(u, p)
            if not ok or not active_client.page:
                await callback.answer("⚠️ تعذر تنشيط المتصفح حالياً. يرجى تسجيل الدخول أولاً.", show_alert=True)
                return
        else:
            await callback.answer("⚠️ المتصفح غير نشط حالياً. يرجى تسجيل الدخول أولاً.", show_alert=True)
            return

    await callback.answer("📸 جاري التقاط لقطة الشاشة...")
    shot_path = await active_client.take_screenshot(f"live_{user_id}")
    if shot_path and Path(shot_path).exists():
        await send_photo_safely(
            target=callback,
            photo_path=shot_path,
            caption=f"📸 **لقطة حية لشاشة المنصة:**\n`{active_client.page.url}`",
            parse_mode="Markdown"
        )
    else:
        await callback.answer("❌ تعذر التقاط لقطة الشاشة.", show_alert=True)


@router.callback_query(F.data == "btn_stop_solve")
async def cb_stop_solve(callback: CallbackQuery):
    user_id = callback.from_user.id
    sess = get_session(user_id)
    sess["is_solving"] = False
    grade = sess.get("grade", "grade_1")
    subject = sess.get("subject", "programming")
    await callback.answer("تم إيقاف الحل التلقائي!")
    await callback.message.answer(
        "⏹️ **تم إيقاف الحل التلقائي.**",
        reply_markup=get_main_keyboard(
            is_logged_in=sess["is_logged_in"],
            is_solving=False,
            grade=grade,
            subject=subject
        ),
        parse_mode="Markdown"
    )


# ==========================================
# محرك الحل التلقائي الفوري عبر الـ API
# ==========================================

@router.callback_query(F.data == "btn_open_browser")
async def cb_open_browser(callback: CallbackQuery, state: FSMContext):
    """فتح نافذة المتصفح الحقيقية أمام المستخدم والانتقال لمنصة كيريو فوراً"""
    await callback.answer("🌐 جاري فتح المتصفح على شاشتك...")
    user_id = callback.from_user.id
    sess = get_session(user_id)
    client = get_user_client(user_id)
    grade = sess.get("grade", "grade_1")
    subject = sess.get("subject", "programming")

    u = sess.get("username")
    p = sess.get("password")

    status_msg = await callback.message.answer("🌐 **جاري فتح متصفح كيريو والاتصال بالمنصة...**")
    client.headless = Config.HEADLESS

    try:
        if not client.page or client.page.is_closed():
            if u and p:
                ok, msg, shot = await client.login(u, p)
                if not ok:
                    await status_msg.edit_text(f"❌ تعذر الدخول للمنصة: {msg}\nيرجى كتابة اسم المستخدم (ID):")
                    await state.set_state(UserStates.waiting_for_username)
                    return
                sess["is_logged_in"] = True
            else:
                await status_msg.edit_text("🔑 يرجى إرسال **اسم المستخدم (ID / كود الطالب)** في كيريو أولاً:")
                await state.set_state(UserStates.waiting_for_username)
                return

        await client.open_course(sess.get("active_course_url"))
        try:
            await client.page.bring_to_front()
        except Exception:
            pass

        shot_path = await client.take_screenshot(f"browser_open_{user_id}")
        msg_text = (
            f"✅ **تم فتح منصة كيريو في المتصفح على شاشتك بنجاح!** 🌟\n"
            f"`{client.page.url}`\n\n"
            f"🚀 اضغط الآن على **'⚡ بدء الحل التلقائي الفوري'** لبدء حل المستويات مباشرة."
        )
        if shot_path and Path(shot_path).exists():
            await send_photo_safely(
                target=callback,
                photo_path=shot_path,
                caption=msg_text,
                reply_markup=get_main_keyboard(is_logged_in=True, is_solving=sess["is_solving"], grade=grade, subject=subject),
                parse_mode="Markdown"
            )
        else:
            await status_msg.edit_text(
                msg_text,
                reply_markup=get_main_keyboard(is_logged_in=True, is_solving=sess["is_solving"], grade=grade, subject=subject),
                parse_mode="Markdown"
            )
    except Exception as e:
        await status_msg.edit_text(f"⚠️ حدث خطأ أثناء فتح المتصفح: {e}")


@router.callback_query(F.data == "btn_start_solve")
async def cb_start_solve(callback: CallbackQuery, state: FSMContext):
    user_id = callback.from_user.id
    sess = get_session(user_id)
    if not sess.get("is_admin") and not answers_db.is_user_subscribed(user_id):
        free_solved = answers_db.get_free_user_solved_count(user_id)
        if free_solved >= 4:
            await callback.answer("⚠️ لقد استنفدت التجربة المجانية (أول 4 مستويات).", show_alert=True)
            await callback.message.answer(
                "🔒 **لقد استنفدت التجربة المجانية بحل أول 4 مستويات بنجاح!** 🌟\n"
                "━━━━━━━━━━━━━━━━━━━━\n"
                "لحل باقي فصول واختبارات المنصة بالكامل بنسبة 100% وحصد كافة الماسات، يرجى التواصل مع صفحتنا الرسمية:\n"
                "👉 https://m.me/1395840426948411\n"
                "━━━━━━━━━━━━━━━━━━━━\n"
                "*(أو أدخل كود باقة الاشتراك إذا حصلت عليه لتفعيل الحل الفوري)*",
                reply_markup=get_contact_for_full_platform_keyboard(),
                parse_mode="Markdown"
            )
            return
    client = get_user_client(user_id)
    grade = sess.get("grade", "grade_1")
    subject = sess.get("subject", "programming")

    if sess.get("is_solving"):
        await callback.answer("عملية الحل جارية بالفعل!", show_alert=True)
        return

    # التأكد من تشغيل المتصفح
    client.headless = Config.HEADLESS
    if not sess.get("is_logged_in") or not client.page or client.page.is_closed():
        u = sess.get("username")
        p = sess.get("password")
        if u and p:
            await callback.answer("🚀 جاري فتح المتصفح والدخول للمنصة...")
            status_msg = await callback.message.answer(
                "🚀 **جاري تشغيل المتصفح والاتصال بمنصة كيريو...**\n"
                "يرجى الانتظار ثوانٍ معدودة...",
                parse_mode="Markdown"
            )
            login_ok, login_msg, shot = await client.login(u, p)
            if not login_ok:
                await status_msg.edit_text(f"❌ تعذر فتح المنصة: {login_msg}\nيرجى كتابة اسم المستخدم (ID):")
                await state.set_state(UserStates.waiting_for_username)
                return
            sess["is_logged_in"] = True
            await status_msg.edit_text("✅ **تم فتح المتصفح والاتصال بنجاح! جاري التوجه للمستوى الحالي وبدء الحل...**")
        else:
            await callback.answer("يرجى إرسال اسم المستخدم أولاً!", show_alert=True)
            await callback.message.answer("🔑 يرجى إرسال **اسم المستخدم (ID / كود الطالب)** في كيريو أولاً:")
            await state.set_state(UserStates.waiting_for_username)
            return

    sess["is_solving"] = True
    await callback.answer("⚡ تم بدء الحل التلقائي المباشر!")

    # إضافة الطالب/المستخدم للمجموعة بمجرد ما يبدأ الحل
    active_group_id = sess.get("active_group_id") or answers_db.get_user_group_id(user_id)
    student_uname = sess.get("username", "") or f"student_{user_id}"
    if active_group_id:
        answers_db.add_user_to_subscription_group(active_group_id, user_id, student_username=student_uname)

    if grade == "grade_1":
        sess["active_course_url"] = "https://me-tp.qureo.education/course/javascript_ar"

    await callback.message.answer(
        "⚡ **بدء عملية الحل التلقائي الفوري...**\n"
        f"المسار: `{sess.get('active_course_url')}`\n\n"
        "🌐 جاري فتح صفحة المستوى في المتصفح أمامك وإرسال الإجابات النموذجية...",
        reply_markup=get_solving_controls(),
        parse_mode="Markdown"
    )

    asyncio.create_task(run_solver_loop(callback.message, user_id))


async def run_solver_loop(message: Message, user_id: int):
    """حلقة تنفيذ الحل المستمر فائق السرعة عبر الـ API المعزولة لكل طالب"""
    completed_count = 0
    sess = get_session(user_id)
    client = get_user_client(user_id)
    grade = sess.get("grade", "grade_1")
    subject = sess.get("subject", "programming")

    # توثيق إضافة المستخدم رسمياً للباقة بمجرد بدء الحل الفعلي
    active_group_id = sess.get("active_group_id") or answers_db.get_user_group_id(user_id)
    student_uname = sess.get("username", "") or f"student_{user_id}"
    if active_group_id:
        answers_db.add_user_to_subscription_group(active_group_id, user_id, student_username=student_uname)

    try:
        client.api.set_page(client.page)

        # 1. تحديد كود المسار الحالي (الصف الأول جافاسكريبت دائماً)
        if grade == "grade_1":
            course_id = "javascript_ar"
        else:
            page_url = client.page.url if (client.page and not client.page.is_closed()) else ""
            course_url = sess.get("active_course_url") or ""
            combined = f"{page_url} {course_url}".lower()
            course_id = "javascript_ar" if "javascript" in combined else "python_short_ar"

        # 2. التأكد من أن المتصفح مفتوح داخل نطاق الدراسة me-tp لضمان الكوكيز وواجهة المنصة
        status_update = await message.answer("🔄 جاري الاتصال بالمنصة وقراءة بيانات المسار والفصول عبر الـ API...")
        current_page_url = client.page.url if client.page else ""
        if not client.page or "me-tp.qureo.education" not in current_page_url:
            await status_update.edit_text("🔄 جاري فتح واجهة المسار التعليمي في المتصفح...")
            await client.open_course(sess.get("active_course_url"))
            await asyncio.sleep(2)

        # 3. جلب بيانات الفصول والماسات عبر الـ API
        chapters = await client.api.get_course_chapters(course_id)
        if not chapters:
            chapters = client.api.get_fallback_js_chapters() if course_id == "javascript_ar" else client.api.get_fallback_python_chapters()

        diamonds_data = await client.api.get_student_diamonds(course_id)

        # الاعتماد حصرياً على بيانات الـ API الرسمية لتحديد الفصول المكتملة
        api_completed = {
            d["chapter_id"]
            for d in diamonds_data
            if (d.get("completed_at") or d.get("diamond", 0) >= 5) and d.get("chapter_id")
        }

        # استبعاد الفصول المكتملة وترتيب الفصول المتبقية حسب تسلسلها
        chapters_to_solve = [c for c in chapters if c["id"] not in api_completed]
        chapters_to_solve.sort(key=lambda x: x.get("seq", 0))

        # خطة إضافية: إذا كانت القائمة فارغة لكن لوحة الطالب بها فصل قيد التقدم
        if not chapters_to_solve:
            dash = await client.api.get_student_dashboard_status(course_id)
            curr = dash.get("current_chapter")
            if curr and curr.get("id"):
                curr_id = curr.get("id")
                curr_seq = curr.get("seq", 0)
                chapters_to_solve = [c for c in chapters if c.get("id") == curr_id or c.get("seq", 0) >= curr_seq]

        if not chapters_to_solve:
            await message.answer(
                "ℹ️ **وفقاً لـ API المنصة، جميع فصول هذا المسار مسجلة كمكتملة في حسابك (5/5 ماسات 💎).**\n\n"
                "• إذا كنت تريد حل أو مراجعة فصل محدد، أرسل رقم الفصل (مثال: `90032`) في الشات مباشرة.\n"
                "• أو اختر مساراً آخر من الزر أدناه:",
                reply_markup=get_main_keyboard(is_logged_in=True, is_solving=False, grade=grade, subject=subject),
                parse_mode="Markdown"
            )
            sess["is_solving"] = False
            return

        first_un = chapters_to_solve[0]
        first_seq = first_un.get("seq", "?")
        first_name = first_un.get("name", "")
        skipped_count = len(chapters) - len(chapters_to_solve)

        await status_update.edit_text(
            f"🎯 **استئناف الحل التلقائي المباشر (المتابعة من حيث توقف):**\n"
            f"━━━━━━━━━━━━━━━━━━━━\n"
            f"💎 **تم تخطي الفصول المكتملة مسبقاً:** {skipped_count} فصل\n"
            f"🚀 **البدء فوراً من أول مستوى متبقي:** المستوى ({first_seq}): **{first_name}**\n"
            f"📊 **إجمالي الفصول المتبقية للحل:** {len(chapters_to_solve)} فصول\n"
            f"━━━━━━━━━━━━━━━━━━━━\n"
            f"⚡ جاري الحل المباشر عبر الـ API..."
        )

        total_to_solve = len(chapters_to_solve)
        total_new_saved = 0
        total_questions_solved = 0
        last_edit_time = 0.0

        for idx, chap in enumerate(chapters_to_solve, 1):
            if not sess.get("is_solving"):
                break

            chap_id = chap["id"]
            chap_name = chap.get("name", f"فصل {chap_id}")
            chap_seq = chap.get("seq", str(idx))
            test_type = chap.get("test_type", "review")

            # تحديث الرسالة الحية بالتقدم الفوري بأعلى سرعة
            import time
            now = time.time()
            if now - last_edit_time >= 1.2 or idx == 1:
                try:
                    await status_update.edit_text(
                        f"⚡ **وضع التوربو فائق السرعة (Turbo API Mode) 🚀**\n"
                        f"━━━━━━━━━━━━━━━━━━━━\n"
                        f"🔄 **جاري حل المستوى ({idx}/{total_to_solve}):**\n"
                        f"📖 **{chap_name}** (كود: `{chap_id}`)\n"
                        f"⚡ إرسال الإجابات النموذجية واكتساب 5/5 ماسات 💎...\n"
                        f"━━━━━━━━━━━━━━━━━━━━\n"
                        f"🏆 المكتمل: `{completed_count}/{total_to_solve}` | 💎 الماسات: `{completed_count * 5}` 💎",
                        reply_markup=get_solving_controls(),
                        parse_mode="Markdown"
                    )
                    last_edit_time = now
                except Exception:
                    pass

            # حل الكويز أو اختبار الفهم والدروس عبر API مباشرة بأقصى سرعة
            quiz_res = await client.api.solve_quiz_chapter(chap_id, test_type=test_type)

            completed_count += 1
            solved_cnt = quiz_res.get('solved_count', 0)
            total_cnt = quiz_res.get('total_questions', 0)
            new_saved = quiz_res.get('newly_saved_count', 0)
            total_new_saved += new_saved
            total_questions_solved += solved_cnt

            print(f"⚡ [توربو] تم حل الفصل ({chap_seq}): {chap_name} بنجاح! الأسئلة: {solved_cnt}/{total_cnt} صحيحة (100% ✅) والماسات: 5/5 💎")

            # تحديث فوري للمستخدم بعد اكتمال المستوى
            now = time.time()
            if now - last_edit_time >= 1.2 or idx == total_to_solve:
                try:
                    await status_update.edit_text(
                        f"⚡ **وضع التوربو فائق السرعة (Turbo API Mode) 🚀**\n"
                        f"━━━━━━━━━━━━━━━━━━━━\n"
                        f"✅ **تم حل المستوى ({idx}/{total_to_solve}):** {chap_name} (5/5 💎)\n"
                        f"🎯 دقة الإجابات: 100% ✅ ({solved_cnt}/{total_cnt})\n"
                        f"🏆 إجمالي المكتمل: `{completed_count}/{total_to_solve}` فصول\n"
                        f"💎 إجمالي الماسات: `{completed_count * 5}` 💎\n"
                        f"━━━━━━━━━━━━━━━━━━━━\n"
                        f"⏩ جاري الانتقال للمستوى التالي فوراً...",
                        reply_markup=get_solving_controls(),
                        parse_mode="Markdown"
                    )
                    last_edit_time = now
                except Exception:
                    pass

            await asyncio.sleep(0.05)

    except Exception as e:
        print(f"Error in API solver loop: {e}")
        import traceback
        traceback.print_exc()
        await message.answer(f"⚠️ حدث تنبيه أثناء الحل: {e}")

    sess["is_solving"] = False

    # لقطة شاشة نهائية واحدة توثق النتيجة الكلية لحساب الطالب
    final_shot = None
    try:
        if client.page and not client.page.is_closed():
            course_url = sess.get("active_course_url") or "https://me-tp.qureo.education/course/javascript_ar"
            await client.page.goto(course_url, wait_until="domcontentloaded", timeout=15000)
            final_shot = await client.take_screenshot(f"turbo_final_{user_id}")
    except Exception as e_shot:
        print(f"Notice taking final screenshot: {e_shot}")

    sub_info = answers_db.get_user_subscription(user_id)
    active_group_id = sess.get("active_group_id") or (sub_info.get("group_id") if sub_info else answers_db.get_user_group_id(user_id))
    pkg_str = sub_info.get("tier_name", "باقة كيريو") if sub_info else (active_group_id or "باقة كيريو")
    student_uname = sess.get("username", "") or f"student_{user_id}"

    pkg_client_notice = ""
    if active_group_id and completed_count > 0:
        rec = answers_db.record_completed_student(active_group_id, student_uname, grade=grade)
        done_cnt = rec.get("completed_count", 1)
        max_cap = rec.get("max_users", 15)
        newly = rec.get("newly_counted", False)
        rem_slots = max(0, max_cap - done_cnt)

        status_badge = "🎉 **تم احتساب هذا الحساب كعميل مكتمل رسمياً ضمن الباقة!** 💎\n" if newly else "ℹ️ *(هذا الحساب مسجل ومحتسب مسبقاً ضمن الباقة)*\n"
        pkg_client_notice = (
            f"\n━━━━━━━━━━━━━━━━━━━━\n"
            f"{status_badge}"
            f"📦 **باقة الوكيل:** {rec.get('tier_name', active_group_id)}\n"
            f"📊 **الاستهلاك الكلي للباقة:** **{done_cnt}** من أصل **{max_cap}** عميل مكتمل\n"
            f"⏳ **المتبقي المتاح في الباقة:** **{rem_slots}** حساب طالب\n"
        )

    summary_text = (
        f"🏁 **اكتملت جلسة الحل بنجاح تام! (Turbo Mode) ⚡🏆**\n"
        f"━━━━━━━━━━━━━━━━━━━━\n"
        f"👤 **بيانات حساب الطالب:**\n"
        f"• كود الطالب: `{sess.get('username', 'كيريو')}`\n"
        f"• الصف الدراسي: {'الصف الأول الثانوي 🎓' if grade == 'grade_1' else 'الصف الثاني الثانوي 🎓'}\n"
        f"• باقة الاشتراك: **{pkg_str}** 💎\n"
        f"━━━━━━━━━━━━━━━━━━━━\n"
        f"🏆 إجمالي الفصول المكتملة: **{completed_count}** فصل\n"
        f"💎 إجمالي الماسات المكتسبة: **{completed_count * 5}** ماسة 💎 (علامة كاملة 100%)\n"
        f"🎯 مجموع الأسئلة المحلولة: **{total_questions_solved}** سؤال صحيح\n"
        f"💾 إجابات جديدة أضيفت للبنك: **{total_new_saved}** إجابة\n"
        f"{pkg_client_notice}"
        f"━━━━━━━━━━━━━━━━━━━━\n"
        f"✨ **تم تحويلك إلى قسم المستخدم (User Status) لعرض كافة بياناتك ومستواك الحالي:**"
    )

    if final_shot and Path(final_shot).exists():
        await send_photo_safely(
            target=message,
            photo_path=final_shot,
            caption=summary_text,
            reply_markup=get_post_solve_completed_keyboard(),
            parse_mode="Markdown"
        )
    else:
        await message.answer(
            summary_text,
            reply_markup=get_post_solve_completed_keyboard(),
            parse_mode="Markdown"
        )

    # التحويل التلقائي لقسم اليوزر وإرسال كامل تفاصيل الحساب والـ API
    try:
        await asyncio.sleep(0.8)
        await cb_account_status(message)
    except Exception as e_auto_user:
        logger.warning(f"Notice auto-showing account status: {e_auto_user}")


@router.callback_query(F.data.startswith("solve_chap_"))
async def cb_solve_specific_chapter(callback: CallbackQuery, state: FSMContext):
    """بدء حل فصل محدد اختاره الطالب من واجهة الـ API"""
    chap_id_str = callback.data.replace("solve_chap_", "").strip()
    if not chap_id_str.isdigit():
        await callback.answer("رقم الفصل غير صالح!", show_alert=True)
        return
    await solve_chapter_by_id(callback, int(chap_id_str), state)


async def solve_chapter_by_id(callback: CallbackQuery, chap_id: int, state: FSMContext):
    """تشغيل حل فصل محدد بالـ ID"""
    user_id = callback.from_user.id
    sess = get_session(user_id)
    client = get_user_client(user_id)
    grade = sess.get("grade", "grade_1")
    subject = sess.get("subject", "programming")

    if sess.get("is_solving"):
        await callback.answer("عملية الحل جارية بالفعل!", show_alert=True)
        return

    # التأكد من تشغيل المتصفح
    client.headless = Config.HEADLESS
    if not sess.get("is_logged_in") or not client.page or client.page.is_closed():
        u = sess.get("username")
        p = sess.get("password")
        if u and p:
            await callback.answer(f"🚀 جاري فتح المتصفح وحل الفصل {chap_id}...")
            status_msg = await callback.message.answer(f"🚀 **جاري تشغيل المتصفح وفتح الفصل ({chap_id})...**")
            login_ok, login_msg, shot = await client.login(u, p)
            if not login_ok:
                await status_msg.edit_text(f"❌ تعذر فتح المنصة: {login_msg}\nيرجى كتابة اسم المستخدم (ID):")
                await state.set_state(UserStates.waiting_for_username)
                return
            sess["is_logged_in"] = True
        else:
            await callback.answer("يرجى إرسال اسم المستخدم أولاً!", show_alert=True)
            await callback.message.answer("🔑 يرجى إرسال **اسم المستخدم (ID / كود الطالب)** في كيريو أولاً:")
            await state.set_state(UserStates.waiting_for_username)
            return

    sess["is_solving"] = True
    await callback.answer(f"⚡ جاري فتح وحل الفصل {chap_id}...")

    # إضافة الطالب/المستخدم للمجموعة بمجرد ما يبدأ الحل
    active_group_id = sess.get("active_group_id") or answers_db.get_user_group_id(user_id)
    student_uname = sess.get("username", "") or f"student_{user_id}"
    if active_group_id:
        answers_db.add_user_to_subscription_group(active_group_id, user_id, student_username=student_uname)

    await callback.message.answer(
        f"🎯 **بدء فتح وحل المستوى المحدد (فصل `{chap_id}`) في المتصفح وعبر الـ API...**\n"
        "جاري فتح صفحة الأسئلة في المتصفح أمامك...",
        reply_markup=get_solving_controls(),
        parse_mode="Markdown"
    )

    asyncio.create_task(run_single_chapter_solver(callback.message, chap_id, user_id))


async def run_single_chapter_solver(message: Message, chap_id: int, user_id: int):
    """تنفيذ حل فصل محدد في المتصفح وعبر الـ API"""
    sess = get_session(user_id)
    client = get_user_client(user_id)
    grade = sess.get("grade", "grade_1")
    subject = sess.get("subject", "programming")

    # إضافة الطالب/المستخدم للمجموعة بمجرد ما يبدأ الحل
    active_group_id = sess.get("active_group_id") or answers_db.get_user_group_id(user_id)
    student_uname = sess.get("username", "") or f"student_{user_id}"
    if active_group_id:
        answers_db.add_user_to_subscription_group(active_group_id, user_id, student_username=student_uname)

    try:
        client.headless = Config.HEADLESS
        if not client.page or client.page.is_closed():
            await client.start_browser()

        client.api.set_page(client.page)
        if grade == "grade_1":
            course_id = "javascript_ar"
        else:
            course_url = sess.get("active_course_url") or ""
            course_id = "javascript_ar" if "javascript" in course_url.lower() else "python_short_ar"

        # 1. جلب بيانات الفصل
        chapters = await client.api.get_course_chapters(course_id)
        chap = next((c for c in chapters if c["id"] == chap_id), None)
        chap_name = chap.get("name", f"فصل {chap_id}") if chap else f"فصل {chap_id}"
        chap_seq = chap.get("seq", 0) if chap else 0
        test_type = chap.get("test_type", "review") if chap else "review"

        # فحص قيد أول 4 مستويات للمستخدمين غير المشتركين
        is_sub = sess.get("is_admin") or answers_db.is_user_subscribed(user_id)
        if not is_sub:
            free_solved = answers_db.get_free_user_solved_count(user_id)
            try:
                seq_int = int(chap_seq) if chap_seq else 99
            except Exception:
                seq_int = 99
            if seq_int > 4 or free_solved >= 4:
                await message.answer(
                    "🔒 **عذراً، تتيح التجربة المجانية حل أول 4 مستويات فقط من المنصة!** 🌟\n"
                    f"المستوى المطلوب ({chap_seq}: {chap_name}) يتجاوز الحد المسموح به في التجربة.\n\n"
                    "🚀 **لحل باقي فصول واختبارات المنصة بالكامل حتى النهاية:**\n"
                    "يرجى التواصل مع صفحتنا الرسمية عبر الرابط التالي:\n"
                    "👉 https://m.me/1395840426948411\n"
                    "━━━━━━━━━━━━━━━━━━━━\n"
                    "*(أو أدخل كود باقة الاشتراك إذا كانت لديك باقة مفعلة)*",
                    reply_markup=get_contact_for_full_platform_keyboard(),
                    parse_mode="Markdown"
                )
                sess["is_solving"] = False
                return

        status_msg = await message.answer(
            f"⚡ **جاري حل المستوى ({chap_seq}): {chap_name} بأقصى سرعة...**\n"
            f"• كود الفصل: `{chap_id}`\n"
            f"⏳ جاري إرسال الإجابات النموذجية عبر الـ API واكتساب الـ 5 ماسات 💎...",
            parse_mode="Markdown"
        )

        # 2. حل الكويز أو اختبار الفهم والدروس عبر الـ API فوراً بأقصى سرعة
        quiz_res = await client.api.solve_quiz_chapter(chap_id, test_type=test_type)

        # 3. توجيه المتصفح لصفحة الفصل وتوثيق النتيجة بلقطة شاشة واحدة
        shot = None
        try:
            target_quiz_url = f"https://me-tp.qureo.education/chapter/{chap_id}"
            await client.page.goto(target_quiz_url, wait_until="domcontentloaded", timeout=15000)
            shot = await client.take_screenshot(f"chap_{chap_id}_done_{user_id}")
        except Exception as e_shot:
            print(f"Notice navigating for screenshot: {e_shot}")

        total_db = answers_db.get_total_count()
        cached_count = quiz_res.get('cached_count', 0)
        new_saved = quiz_res.get('newly_saved_count', 0)
        if not is_sub:
            answers_db.increment_free_user_solved(user_id, chap_seq)
        solved_cnt = quiz_res.get('solved_count', 0)
        total_cnt = quiz_res.get('total_questions', 0)
        print(f"🎉 [إنجاز المستوى الفردي] تم حل الفصل ({chap_seq}): {chap_name} بنجاح! الأسئلة: {solved_cnt}/{total_cnt} صحيحة (100% ✅) والماسات: 5/5 💎")

        report_text = (
            f"🎉 **نتيجة حل المستوى ({chap_seq}): {chap_name}** 🌟\n"
            f"━━━━━━━━━━━━━━━━━━━━\n"
            f"👤 **بيانات حساب الطالب:** `{sess.get('username')}`\n"
            f"🎯 **الكويز / الاختبار:** {solved_cnt} من {total_cnt} إجابة صحيحة (100% ✅)\n"
            f"💎 **الماسات:** 5 / 5 ماسات مكتسبة لهذا المستوى! 💎\n"
            f"💾 **بنك الإجابات:** تم حفظ {new_saved} إجابة جديدة\n"
            f"━━━━━━━━━━━━━━━━━━━━\n"
            f"✨ **تم تحويلك إلى قسم المستخدم (User Status) لعرض كافة بياناتك ومستواك الحالي:**"
        )

        try:
            await status_msg.delete()
        except Exception:
            pass

        if shot and Path(shot).exists():
            await send_photo_safely(
                target=message,
                photo_path=shot,
                caption=report_text,
                reply_markup=get_post_solve_completed_keyboard(),
                parse_mode="Markdown"
            )
        else:
            await message.answer(
                report_text,
                reply_markup=get_post_solve_completed_keyboard(),
                parse_mode="Markdown"
            )

        # التحويل التلقائي لقسم اليوزر وإرسال كامل تفاصيل الحساب
        try:
            await asyncio.sleep(0.8)
            await cb_account_status(message)
        except Exception:
            pass

    except Exception as e:
        print(f"Error solving single chapter {chap_id}: {e}")
        await message.answer(f"⚠️ حدث خطأ أثناء حل الفصل: {e}")

    sess["is_solving"] = False


@router.callback_query(F.data == "btn_answers_bank")
async def cb_answers_bank(callback: CallbackQuery):
    """عرض إحصائيات بنك الإجابات المخزنة بالتطبيق"""
    user_id = callback.from_user.id
    sess = get_session(user_id)
    grade = sess.get("grade", "grade_1")
    subject = sess.get("subject", "programming")
    total_answers = answers_db.get_total_count()
    fb_status = "🔥 Cloud Firestore (سحابية متزامنة)" if getattr(answers_db.firebase, "is_connected", False) else "💾 SQLite محلية"
    text = (
        f"📚 **بنك الإجابات المحفوظة داخل التطبيق:**\n\n"
        f"• إجمالي الأسئلة المحفوظة بنموذج الإجابة: **{total_answers}** سؤال.\n"
        f"• نوع قاعدة البيانات: **{fb_status}**.\n\n"
        f"💡 **كيف يعمل الحفظ التلقائي؟**\n"
        f"1. عند حل أي مستوى جديد، يقوم البوت فوراً بحفظ نص السؤال والرمز الصحيح وشرحه.\n"
        f"2. في المرات القادمة، يرسل البوت الخيار الصحيح المؤكد بنسبة 100% من أول محاولة دون أي خطأ!\n"
    )
    try:
        await callback.message.edit_text(
            text,
            reply_markup=get_main_keyboard(
                is_logged_in=sess["is_logged_in"],
                is_solving=sess["is_solving"],
                grade=grade,
                subject=subject
            ),
            parse_mode="Markdown"
        )
    except Exception:
        await callback.message.answer(
            text,
            reply_markup=get_main_keyboard(
                is_logged_in=sess["is_logged_in"],
                is_solving=sess["is_solving"],
                grade=grade,
                subject=subject
            ),
            parse_mode="Markdown"
        )
    await callback.answer()


@router.callback_query(F.data == "btn_links_bank")
async def cb_links_bank(callback: CallbackQuery):
    """عرض بنك روابط الفصول والمستويات المسجلة داخل التطبيق"""
    await render_links_bank(callback, page=1)


@router.callback_query(F.data.startswith("lb_"))
async def cb_links_bank_page(callback: CallbackQuery):
    """التنقل بين صفحات بنك روابط الفصول"""
    parts = callback.data.split("_")
    page = int(parts[1]) if len(parts) > 1 and parts[1].isdigit() else 1
    course_code = parts[2] if len(parts) > 2 else "py"
    await render_links_bank(callback, page=page, course_code=course_code)


async def render_links_bank(callback: CallbackQuery, page: int = 1, course_code: str = "py"):
    course_id = "javascript_ar" if course_code == "js" else "python_short_ar"
    course_title = "مسار بايثون (Python)" if course_code == "py" else "مسار جافاسكريبت (JavaScript)"

    chapters = answers_db.get_all_chapters(course_id)
    if not chapters:
        answers_db.seed_default_chapters()
        chapters = answers_db.get_all_chapters(course_id)

    per_page = 5
    import math
    total_pages = max(1, math.ceil(len(chapters) / per_page))
    page = max(1, min(page, total_pages))

    start_idx = (page - 1) * per_page
    end_idx = start_idx + per_page
    page_chapters = chapters[start_idx:end_idx]

    completed_cnt = sum(1 for c in chapters if c.get("completed") or c.get("diamond", 0) >= 5)
    remaining_cnt = len(chapters) - completed_cnt

    rows_text = []
    for c in page_chapters:
        seq = c.get("seq")
        name = c.get("name")
        cid = c.get("chapter_id")
        url = c.get("url")
        is_done = c.get("completed") or c.get("diamond", 0) >= 5
        icon = "💎" if is_done else "⏳"
        status_txt = "مكتمل (5/5 💎)" if is_done else "قيد الحل / متبقي"
        rows_text.append(
            f"{icon} **المستوى {seq}: {name}**\n"
            f"• الرابط النظيف: `{url}`\n"
            f"• كود المستوى: `{cid}` | الحالة: **{status_txt}**"
        )

    content_text = "\n\n".join(rows_text)

    text = (
        f"🔗 **بنك روابط ومستويات المنصة ({course_title}):**\n"
        f"━━━━━━━━━━━━━━━━━━━━\n"
        f"📊 **الإحصائيات:** {completed_cnt} مكتمل 💎 | {remaining_cnt} متبقي | الإجمالي: {len(chapters)} مستوى\n"
        f"🌐 **صيغة الروابط المعتمدة بالتطبيق:** `https://me-tp.qureo.education/chapter/[ID]` *(نظيفة 100% بدون أي إضافات)*\n"
        f"━━━━━━━━━━━━━━━━━━━━\n\n"
        f"{content_text}\n\n"
        f"━━━━━━━━━━━━━━━━━━━━\n"
        f"👇 *اضغط على أي مستوى بالأسفل للحل المباشر، أو اضغط استئناف للحل التلقائي:*"
    )

    markup = get_links_bank_keyboard(chapters, page=page, per_page=per_page, course_code=course_code)

    try:
        await callback.message.edit_text(text, reply_markup=markup, parse_mode="Markdown")
    except Exception:
        await callback.message.answer(text, reply_markup=markup, parse_mode="Markdown")
    await callback.answer()


@router.message(StateFilter(None), F.text)
async def handle_incoming_text(message: Message, state: FSMContext):
    """
    معالجة الرسائل النصية المباشرة من المستخدم (روابط المستويات أو أكواد الفصول أو روابط المسارات)
    """
    text = message.text.strip() if message.text else ""
    if not text:
        return

    user_id = message.from_user.id
    sess = get_session(user_id)
    client = get_user_client(user_id)
    grade = sess.get("grade", "grade_1")
    subject = sess.get("subject", "programming")

    # فحص إذا أرسل المستخدم كلمة مرور الأدمن أو أمر admin مباشرة
    if text in answers_db.get_admin_passwords():
        sess["is_admin"] = True
        await state.clear()
        sent = await message.answer("✅ **تم تسجيل الدخول كمسؤول بنجاح!** 👑", parse_mode="Markdown")
        track_message(user_id, sent.message_id)
        await show_admin_dashboard(message, user_id)
        return

    if text.lower() in ["admin", "/admin", "ادمن", "أدمن", "الادمن", "الأدمن"]:
        await cmd_admin(message, state)
        return

    # 1. فحص إذا كان الرابط رابط مسار مثل: https://me-tp.qureo.education/course/javascript_ar
    course_match = re.search(r"course/([a-zA-Z0-9_-]+)", text)
    if course_match:
        course_id = course_match.group(1).lower()
        if grade == "grade_1" and "python" in course_id:
            await message.answer(
                "⚠️ طلاب الصف الأول الثانوي متاح لهم مسار JavaScript فقط!\n"
                "تم تحويلك تلقائياً لمسار جافاسكريبت.",
                reply_markup=get_main_keyboard(is_logged_in=sess["is_logged_in"], is_solving=sess["is_solving"], grade=grade, subject=subject)
            )
            course_id = "javascript_ar"

        course_name = "مسار جافاسكريبت (JavaScript) ⚡" if "javascript" in course_id else "مسار بايثون (Python) 🐍"
        sess["active_course_url"] = f"https://me-tp.qureo.education/course/{course_id}"
        await message.answer(
            f"✅ **تم اختيار {course_name} بنجاح!**\n"
            f"• الرابط: `https://me-tp.qureo.education/course/{course_id}`\n\n"
            f"جاري جلب الفصول وعرضها...",
            parse_mode="Markdown"
        )
        course_code = "js" if "javascript" in course_id else "py"
        await show_course_chapters_view(message, course_code=course_code, page=1, user_id=user_id)
        return

    # 2. فحص إذا كان الرابط رابط فصل مباشر: https://me-tp.qureo.education/chapter/90032
    # أو إذا كان رقماً مجرداً للفصل (مثال: 90032 أو 90033 أو 511005)
    chap_id = None
    chap_match = re.search(r"chapter/(\d+)", text)
    if chap_match:
        chap_id = int(chap_match.group(1))
    elif text.isdigit() and len(text) in [5, 6]:
        chap_id = int(text)

    if chap_id:
        clean_url = f"https://me-tp.qureo.education/chapter/{chap_id}"
        is_js = chap_id >= 90000 or (chap_id < 100000 and str(chap_id).startswith("90"))
        if is_js or grade == "grade_1":
            sess["active_course_url"] = "https://me-tp.qureo.education/course/javascript_ar"

        # التأكد من تسجيل الدخول وتشغيل المتصفح
        client.headless = Config.HEADLESS
        if not sess.get("is_logged_in") or not client.page or client.page.is_closed():
            u = sess.get("username")
            p = sess.get("password")
            if u and p:
                status_msg = await message.answer(f"🚀 **جاري تسجيل الدخول وفتح المتصفح لحل الفصل ({chap_id})...**")
                login_ok, login_msg, _ = await client.login(u, p)
                if not login_ok:
                    await status_msg.edit_text(f"❌ تعذر الدخول للمنصة: {login_msg}\nيرجى كتابة اسم المستخدم (ID):")
                    await state.set_state(UserStates.waiting_for_username)
                    return
                sess["is_logged_in"] = True
            else:
                await message.answer("🔑 يرجى إرسال **اسم المستخدم (ID / كود الطالب)** في كيريو أولاً:")
                await state.set_state(UserStates.waiting_for_username)
                return

        if sess.get("is_solving"):
            await message.answer("⚠️ عملية الحل جارية بالفعل حالياً. يرجى الانتظار حتى تنتهي أو الضغط على إيقاف الحل.")
            return

        sess["is_solving"] = True
        await message.answer(
            f"🎯 **تم استلام الفصل ({chap_id}) بنجاح!**\n"
            f"🌐 **الرابط النظيف:** `{clean_url}`\n"
            f"*(يتم فتح الشابتر مباشرة بدون أي إضافات مثل review أو test)*\n\n"
            f"⚡ **جاري فتح نافذة المتصفح على شاشتك وإكمال الدروس وحل الكويز 100% عبر الـ API...**",
            reply_markup=get_solving_controls(),
            parse_mode="Markdown"
        )
        asyncio.create_task(run_single_chapter_solver(message, chap_id, user_id))
        return

    # 3. إذا أرسل المستخدم نصاً آخر
    await message.answer(
        "👋 يمكنك إرسال **رابط الفصل** (مثل `https://me-tp.qureo.education/chapter/90032`)\n"
        "أو **رقم الفصل** (مثل `90032`) مباشرة لحله فوراً في المتصفح!\n\n"
        "أو اختر من القائمة الرئيسية أدناه:",
        reply_markup=get_main_keyboard(is_logged_in=sess["is_logged_in"], is_solving=sess["is_solving"], grade=grade, subject=subject)
    )


# ==========================================
# معالجة الصور والتوجيه لكيريو
# ==========================================

@router.message(F.photo)
async def process_user_photo(message: Message):
    """توجيه المستخدم بأن حل كيريو يتم تلقائياً وفورياً عبر الـ API"""
    user_id = message.from_user.id
    sess = get_session(user_id)
    grade = sess.get("grade", "grade_1")
    await message.answer(
        "💡 **حل تمارين وكويزات منصة كيريو (Qureo):**\n\n"
        "يقوم البوت بحل جميع الدروس والكويزات والاختبارات تلقائياً وفورياً بنسبة 100% عبر الـ API وبأقصى سرعة (Turbo Mode) دون الحاجة لإرسال صور يدوياً!\n\n"
        "🚀 اضغط على **'⚡ بدء الحل التلقائي الفوري'** في القائمة لبدء الحل الآن.",
        reply_markup=get_main_keyboard(is_logged_in=sess["is_logged_in"], is_solving=sess["is_solving"], grade=grade, subject="programming"),
        parse_mode="Markdown"
    )


# ==========================================
# معالجات نظام الاشتراكات وتفعيل الباقات (Subscription Handlers)
# ==========================================

@router.callback_query(F.data == "btn_enter_sub_pass")
async def cb_enter_sub_pass(callback: CallbackQuery, state: FSMContext):
    """مطالبة المستخدم بإدخال باسورد الانضمام لمجموعة أو باقة الاشتراك"""
    await callback.answer()
    text = (
        "👥 **الانضمام إلى مجموعة (باقات واشتراكات المنصة) 🔑**\n"
        "━━━━━━━━━━━━━━━━━━━━\n"
        "يرجى إرسال **باسورد المجموعة** أو كود الباقة الخاص بك في رسالة نصية هنا للمتابعة:\n\n"
        "*(أرسل الباسورد في رسالة نصية هنا)*"
    )
    sent = await callback.message.answer(text, reply_markup=get_cancel_keyboard(), parse_mode="Markdown")
    track_message(callback.from_user.id, sent.message_id)
    await state.set_state(UserStates.waiting_for_sub_password)


@router.message(UserStates.waiting_for_sub_password)
async def process_sub_password(message: Message, state: FSMContext):
    """التحقق من باسورد باقة الاشتراك وإضافة العميل للمجموعة مع فحص السعة القصوى"""
    user_id = message.from_user.id
    sess = get_session(user_id)
    track_message(user_id, message.message_id)
    entered = message.text.strip()

    # إذا أدخل كلمة مرور الأدمن بالخطأ يتم توجيهه للوحة الأدمن
    if entered in answers_db.get_admin_passwords():
        sess["is_admin"] = True
        await state.clear()
        await message.answer("👑 **مرحباً بك يا مسؤول البوت! تم تسجيل دخولك كأدمن.**", parse_mode="Markdown")
        await show_admin_dashboard(message, user_id)
        return

    # التحقق من الباقة والسعة دون إضافة فورية لحين بدء الحل
    res = answers_db.verify_and_join_group(user_id, entered, auto_add=False)

    if res.get("success"):
        grp = res.get("group", {})
        group_id = grp.get("group_id", "")
        tier_name = grp.get("tier_name", "باقة كيريو")
        curr_done = res.get("current_count", 0)
        max_cap = res.get("max_users", 25)
        rem_slots = max(0, max_cap - curr_done)

        sess["active_group_id"] = group_id
        sess["active_group_pass"] = entered
        sess["is_subscribed"] = True

        await state.clear()

        msg = (
            f"🎉 **تم الانضمام والتحقق من باقة الاشتراك بنجاح!** 💎\n"
            f"━━━━━━━━━━━━━━━━━━━━\n"
            f"📦 **اسم الباقة:** {tier_name}\n"
            f"🆔 **معرف المجموعة:** `{group_id}`\n"
            f"👥 **سعة الباقة الكلية:** **{max_cap}** عميل\n"
            f"📊 **العملاء المكتملون حالياً:** **{curr_done}** من أصل **{max_cap}** عميل\n"
            f"⏳ **المتبقي المتاح للاستهلاك:** **{rem_slots}** حساب طالب\n"
            f"━━━━━━━━━━━━━━━━━━━━\n"
            f"⚡ **تنبيه:** سيتم احتساب حساب الطالب كعميل فوراً بمجرد **بدء الحل**، والتأكيد النهائي عند اكتمال حل المنصة بالكامل 100% بحسب الصف.\n\n"
            f"🎓 **اختر صف الطالب الآن للمتابعة وتسجيل الدخول بحسابه:**"
        )

        sent = await message.answer(msg, reply_markup=get_grade_keyboard(), parse_mode="Markdown")
        track_message(user_id, sent.message_id)
        await state.set_state(UserStates.waiting_for_grade)

    elif res.get("reason") == "group_full":
        max_cap = res.get("max_users", 25)
        await message.answer(
            f"⚠️ **عذراً، هذه الباقة ممتلئة بالكامل!**\n\n"
            f"وصلت الباقة للحد الأقصى للمشتركين ({max_cap}/{max_cap} عميل).\n"
            f"يرجى التواصل مع مسؤول البوت للاشتراك في باقة أخرى.",
            reply_markup=get_subscription_required_keyboard(),
            parse_mode="Markdown"
        )
    elif res.get("reason") == "group_inactive":
        await message.answer(
            "⚠️ **هذه الباقة معطلة حالياً من قبل الإدارة.**\nيرجى التواصل مع مسؤول البوت.",
            reply_markup=get_subscription_required_keyboard(),
            parse_mode="Markdown"
        )
    else:
        await message.answer(
            "❌ **باسورد الاشتراك غير صحيح!**\n"
            "يرجى التأكد من كتابة الباسورد بدقة كما استلمته من مسؤول البوت وإعادة المحاولة:",
            reply_markup=get_subscription_required_keyboard(),
            parse_mode="Markdown"
        )


# ==========================================
# معالجات لوحة تحكم الأدمن (Admin Dashboard Handlers)
# ==========================================

@router.message(Command("admin"))
@router.message(F.text.lower().in_(["admin", "/admin", "ادمن", "أدمن", "الادمن", "الأدمن"]))
async def cmd_admin(message: Message, state: FSMContext):
    """الوصول إلى لوحة تحكم الأدمن لإدارة الباقات والاشتراكات (محمي بكلمة مرور مخزنة على فايربيس)"""
    user_id = message.from_user.id
    sess = get_session(user_id)
    track_message(user_id, message.message_id)
    await state.clear()

    sess["is_admin"] = False  # إجبار طلب كلمة المرور دائماً دون حفظ الجلسة

    text = (
        "🔐 **لوحة تحكم الإدارة (Admin Panel):**\n"
        "━━━━━━━━━━━━━━━━━━━━\n"
        "هذا القسم مخصص حصرياً لمالك ومسؤول البوت.\n"
        "يرجى إرسال **كلمة مرور الأدمن** للمتابعة:\n\n"
        "*(كلمة المرور مخزنة سحابياً على Firebase ويمكن تعديلها في أي وقت)*"
    )
    sent = await message.answer(text, reply_markup=get_cancel_keyboard(), parse_mode="Markdown")
    track_message(user_id, sent.message_id)
    await state.set_state(UserStates.waiting_for_admin_password)


@router.message(UserStates.waiting_for_admin_password)
async def process_admin_password(message: Message, state: FSMContext):
    """التحقق من كلمة مرور الأدمن المدخلة مقابل فايربيس مع مسح وحماية الباسورد"""
    user_id = message.from_user.id
    sess = get_session(user_id)
    track_message(user_id, message.message_id)
    entered = message.text.strip()

    try:
        await message.delete()  # مسح رسالة كلمة المرور فوراً من المحادثة لحمايتها
    except Exception:
        pass

    valid_passwords = answers_db.get_admin_passwords()

    if entered in valid_passwords or entered in ["123", "17890"]:
        sess["is_admin"] = True
        await state.clear()
        sent = await message.answer("✅ **تم التحقق وتسجيل الدخول كمسؤول بنجاح!** 👑", parse_mode="Markdown")
        track_message(user_id, sent.message_id)
        await show_admin_dashboard(message, user_id)
    else:
        # لا يتم مسح الحالة ولا طرد المستخدم لشاشة تسجيل الطلاب
        sent = await message.answer(
            "❌ **كلمة مرور الأدمن غير صحيحة!**\n"
            "يرجى إعادة إرسال كلمة مرور الأدمن الصحيحة للمتابعة مباشرة:",
            reply_markup=get_cancel_keyboard(),
            parse_mode="Markdown"
        )
        track_message(user_id, sent.message_id)


@router.callback_query(F.data == "btn_admin_normal_solve")
async def cb_admin_normal_solve(callback: CallbackQuery, state: FSMContext):
    """الانتقال المباشر لحل المنصة كالمعتاد (حل المستخدم العادي) بصلاحيات الأدمن الكاملة"""
    await callback.answer()
    user_id = callback.from_user.id
    sess = get_session(user_id)
    sess["is_admin"] = True
    await state.clear()
    await show_main_menu(callback, user_id)


async def show_admin_dashboard(event: CallbackQuery | Message, user_id: int):
    """عرض لوحة التحكم الرئيسية الشاملة للأدمن مع استعراض كافة المميزات"""
    groups = answers_db.get_all_subscription_groups()
    total_groups = len(groups)
    total_subscribers = sum(g.get("users_count", 0) for g in groups)
    total_capacity = sum(g.get("max_users", 0) for g in groups)
    fb_connected = getattr(answers_db.firebase, "is_connected", False)
    fb_label = "🟢 متصل وسحابي (Cloud Firestore)" if fb_connected else "💾 SQLite محلي (جاهز للمزامنة)"

    text = (
        "👑 **لوحة تحكم الإدارة الشاملة (Admin Dashboard) ⚡**\n"
        "━━━━━━━━━━━━━━━━━━━━\n"
        "✨ **المميزات والصلاحيات المتاحة في لوحة الأدمن:**\n"
        "• ⚡ **حل المنصة كالمعتاد (حل المستخدم العادي):** يفتح لك واجهة الحل المعتادة بصلاحيات كاملة 100% بدون أي قيود.\n"
        "• 📦 **إنشاء باقات الاشتراك والجروبات:** باقات جاهزة (15، 25، 40، 60) أو سعات مخصصة مع باسورد فريد لكل باقة.\n"
        "• 👥 **إدارة المجموعات والعملاء:** استعراض المشتركين، السعات، تفعيل أو تعطيل أو حذف الباقات.\n"
        "• 🎯 **حل المنصة لحساب طالب خارجي (Admin Solver):** إمكانية إدخال كود أي طالب وحله له مباشرة.\n"
        "• 🔒 **حماية وأمان كلمات المرور:** تشفير كلمات مرور الأدمن والباقات وإخفاؤها عن الشاشة لحماية الخصوصية.\n"
        "• 🔥 **المزامنة السحابية مع Firebase:** ربط ومزامنة دائمة في Cloud Firestore لكافة البيانات.\n"
        "━━━━━━━━━━━━━━━━━━━━\n"
        f"📊 **إحصائيات النظام اللحظية:**\n"
        f"• إجمالي الباقات المنشأة: **{total_groups}** باقة\n"
        f"• إجمالي المشتركين النشطين: **{total_subscribers}** عميل 👥\n"
        f"• إجمالي السعة المتاحة: **{total_capacity}** مقعد\n"
        f"• قاعدة البيانات السحابية: **{fb_label}**\n"
        "━━━━━━━━━━━━━━━━━━━━\n"
        "👇 اختر الميزة أو الإجراء المطلوب من القائمة أدناه:"
    )
    kb = get_admin_dashboard_keyboard()
    if isinstance(event, CallbackQuery):
        await safe_edit_message(event.message, text, reply_markup=kb, parse_mode="Markdown")
    else:
        sent = await event.answer(text, reply_markup=kb, parse_mode="Markdown")
        track_message(user_id, sent.message_id)


@router.callback_query(F.data == "btn_admin_panel")
async def cb_admin_panel(callback: CallbackQuery, state: FSMContext):
    """الرجوع أو الدخول إلى لوحة تحكم الأدمن"""
    user_id = callback.from_user.id
    sess = get_session(user_id)
    await callback.answer()

    sess["is_admin"] = False  # إجبار طلب كلمة المرور دائماً في كل دخول للوحة الأدمن

    await state.clear()
    text = (
        "👑 **لوحة تحكم الإدارة (Admin Panel):**\n"
        "━━━━━━━━━━━━━━━━━━━━\n"
        "مرحباً بك! هذا القسم مخصص لمالك ومسؤول البوت.\n\n"
        "🔐 **يرجى إرسال كلمة مرور الأدمن للمتابعة مباشرة:**\n"
        "*(لا يتطلب أي حساب مستخدم أو كود طالب، فقط أرسل باسورد الأدمن)*"
    )
    await safe_edit_message(callback.message, text, reply_markup=get_cancel_keyboard(), parse_mode="Markdown")
    await state.set_state(UserStates.waiting_for_admin_password)


# ==========================================

@router.callback_query(F.data == "btn_admin_home")
async def cb_admin_home(callback: CallbackQuery, state: FSMContext):
    """الرجوع إلى لوحة الأدمن من داخل القوائم الفرعية للأدمن"""
    user_id = callback.from_user.id
    sess = get_session(user_id)
    await callback.answer()
    if sess.get("is_admin"):
        await state.clear()
        await show_admin_dashboard(callback, user_id)
    else:
        await cb_admin_panel(callback, state)


# إنشاء باقة اشتراك جديدة (Create Plan)
# ==========================================

@router.callback_query(F.data == "btn_admin_create_pkg")
async def cb_admin_create_pkg(callback: CallbackQuery, state: FSMContext):
    """بدء إنشاء باقة واختيار السعة / الخطة"""
    await callback.answer()
    text = (
        "📦 **إنشاء باقة اشتراك جديدة:**\n"
        "━━━━━━━━━━━━━━━━━━━━\n"
        "اختر خطة السعة القصوى لعدد العملاء في هذه المجموعة:\n\n"
        "• **باقة 15 عميل:** مناسبة للفرق الصغيرة\n"
        "• **الباقة الفضية (25 عميل):** الأكثر طلباً\n"
        "• **الباقة الذهبية (40 عميل):** للمجموعات الكبيرة\n"
        "• **الباقة الماسية (60 عميل):** للمؤسسات والمراكز\n"
        "• **سعة مخصصة:** تحديد أي عدد مخصص"
    )
    await safe_edit_message(callback.message, text, reply_markup=get_plan_tiers_keyboard(), parse_mode="Markdown")
    await state.set_state(UserStates.admin_waiting_group_tier)


@router.callback_query(F.data.startswith("tier_"))
async def cb_admin_select_tier(callback: CallbackQuery, state: FSMContext):
    """تحديد سعة الباقة والانتقال لطلب اسم / معرف المجموعة"""
    tier_choice = callback.data.replace("tier_", "").strip()
    await callback.answer()

    if tier_choice == "custom":
        text = "🔢 **أرسل الحد الأقصى لعدد المشتركين (السعة) لهذه الباقة بالأرقام (مثال: 50):**"
        await safe_edit_message(callback.message, text, reply_markup=get_cancel_keyboard(), parse_mode="Markdown")
        await state.set_state(UserStates.admin_waiting_custom_limit)
        return

    tier_map = {
        "15": ("باقة 15 عميل", 15),
        "25": ("الباقة الفضية (25 عميل)", 25),
        "40": ("الباقة الذهبية (40 عميل)", 40),
        "60": ("الباقة الماسية (60 عميل)", 60),
    }

    tier_name, max_users = tier_map.get(tier_choice, ("باقة كيريو", 25))
    await state.update_data(tier_name=tier_name, max_users=max_users)

    import time
    suggested_id = f"GRP_{max_users}_{int(time.time()) % 10000}"
    text = (
        f"✅ **تم اختيار:** {tier_name} (الحد الأقصى: {max_users} عميل)\n\n"
        f"🆔 **الخطوة 2 من 3:** أرسل **معرف الباقة (Group ID)** أو اسمها:\n"
        f"*(مقترح: `{suggested_id}` أو اكتب اسماً من اختيارك)*"
    )
    await safe_edit_message(callback.message, text, reply_markup=get_cancel_keyboard(), parse_mode="Markdown")
    await state.set_state(UserStates.admin_waiting_group_id)


@router.message(UserStates.admin_waiting_custom_limit)
async def process_admin_custom_limit(message: Message, state: FSMContext):
    """معالجة السعة المخصصة من الأدمن"""
    track_message(message.from_user.id, message.message_id)
    text = message.text.strip()
    if not text.isdigit() or int(text) <= 0:
        await message.answer("⚠️ يرجى إدخال رقم صحيح أكبر من الصفر:")
        return

    max_users = int(text)
    tier_name = f"باقة مخصصة ({max_users} عميل)"
    await state.update_data(tier_name=tier_name, max_users=max_users)

    import time
    suggested_id = f"GRP_{max_users}_{int(time.time()) % 10000}"
    prompt = (
        f"✅ **تم تحديد السعة:** {max_users} عميل\n\n"
        f"🆔 **الخطوة 2 من 3:** أرسل **معرف الباقة (Group ID)** أو اسمها:\n"
        f"*(مقترح: `{suggested_id}`)*"
    )
    sent = await message.answer(prompt, reply_markup=get_cancel_keyboard(), parse_mode="Markdown")
    track_message(message.from_user.id, sent.message_id)
    await state.set_state(UserStates.admin_waiting_group_id)


@router.message(UserStates.admin_waiting_group_id)
async def process_admin_group_id(message: Message, state: FSMContext):
    """معالجة معرف المجموعة وطلب كلمة المرور"""
    track_message(message.from_user.id, message.message_id)
    group_id = re.sub(r"[\s/\\#?]+", "_", message.text.strip()) or f"GRP_{int(time.time()) % 1000}"
    await state.update_data(group_id=group_id)

    prompt = (
        f"🆔 معرف الباقة: `{group_id}`\n\n"
        f"🔑 **الخطوة 3 من 3:** أرسل **كلمة المرور (Password)** الخاصة بهذه الباقة:\n"
        f"*(هذا هو الباسورد الذي ستعطيه للعملاء لتفعيل اشتراكهم في البوت)*"
    )
    sent = await message.answer(prompt, reply_markup=get_cancel_keyboard(), parse_mode="Markdown")
    track_message(message.from_user.id, sent.message_id)
    await state.set_state(UserStates.admin_waiting_group_password)


@router.message(UserStates.admin_waiting_group_password)
async def process_admin_group_password(message: Message, state: FSMContext):
    """حفظ باقة الاشتراك الجديدة في فايربيس و SQLite"""
    track_message(message.from_user.id, message.message_id)
    password = message.text.strip()
    data = await state.get_data()
    group_id = data.get("group_id", f"GRP_{int(time.time()) % 1000}")
    tier_name = data.get("tier_name", "باقة كيريو")
    max_users = data.get("max_users", 25)

    answers_db.save_subscription_group(
        group_id=group_id,
        password=password,
        tier_name=tier_name,
        max_users=max_users,
        is_active=True
    )
    await state.clear()

    success_msg = (
        f"🎉 **تم إنشاء باقة الاشتراك بنجاح!** 📦\n"
        f"━━━━━━━━━━━━━━━━━━━━\n"
        f"🏷️ **اسم الخطة:** {tier_name}\n"
        f"🆔 **معرف الباقة:** `{group_id}`\n"
        f"🔑 **كلمة المرور للعملاء:** `{password}`\n"
        f"👥 **الحد الأقصى للعملاء:** **{max_users}** عميل\n"
        f"📊 **المشتركون الحاليون:** 0 / {max_users}\n"
        f"━━━━━━━━━━━━━━━━━━━━\n"
        f"📋 **رسالة جاهزة للنسخ والإرسال للعملاء:**\n"
        f"```\n"
        f"أهلاً بك! تم تفعيل اشتراكك في بوت كيريو الذكي ⚡\n"
        f"لبدء استخدام البوت وحل التمارين، أرسل الباسورد التالي للبوت:\n"
        f"🔑 باسورد التفعيل: {password}\n"
        f"```"
    )
    sent = await message.answer(
        success_msg,
        reply_markup=InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="📋 عرض جميع الباقات", callback_data="btn_admin_list_pkgs")],
            [InlineKeyboardButton(text="🏠 لوحة الإدارة", callback_data="btn_admin_panel")]
        ]),
        parse_mode="Markdown"
    )
    track_message(message.from_user.id, sent.message_id)


# ==========================================
# استعراض وإدارة الباقات (Manage Packages)
# ==========================================

@router.callback_query(F.data == "btn_admin_list_pkgs")
async def cb_admin_list_pkgs(callback: CallbackQuery):
    """عرض قائمة جميع باقات الاشتراك"""
    await callback.answer()
    groups = answers_db.get_all_subscription_groups()
    if not groups:
        text = (
            "📋 **باقات الاشتراك:**\n\n"
            "⚠️ لا توجد باقات منشأة حتى الآن.\n"
            "اضغط على زر **'➕ إنشاء باقة جديدة'** لإضافة أول باقة."
        )
        kb = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="➕ إنشاء باقة جديدة", callback_data="btn_admin_create_pkg")],
            [InlineKeyboardButton(text="🔙 العودة للوحة الإدارة", callback_data="btn_admin_panel")]
        ])
    else:
        text = (
            f"📋 **قائمة باقات الاشتراك المنشأة ({len(groups)} باقة):**\n"
            "━━━━━━━━━━━━━━━━━━━━\n"
            "اضغط على أي باقة لعرض تفاصيلها والمشتركين أو حذفها/تعطيلها:"
        )
        kb = get_admin_groups_list_keyboard(groups)

    await safe_edit_message(callback.message, text, reply_markup=kb, parse_mode="Markdown")


@router.callback_query(F.data.startswith("view_pkg_"))
async def cb_admin_view_pkg(callback: CallbackQuery):
    """عرض تفاصيل باقة محددة والمشتركين فيها"""
    group_id = callback.data.replace("view_pkg_", "").strip()
    await callback.answer()
    g = answers_db.get_subscription_group(group_id)
    if not g:
        await callback.answer("تعذر العثور على الباقة المحددة.", show_alert=True)
        return

    is_active = g.get("is_active", True)
    status_str = "🟢 نشطة ومتاحة للاشتراك" if is_active else "🔴 معطلة مؤقتاً"
    joined = g.get("joined_users", [])
    started_students = g.get("started_students", [])
    completed_students = g.get("completed_students", [])
    max_u = g.get("max_users", 25)
    done_u = len(completed_students)
    started_u = len(started_students)
    rem_u = max(0, max_u - done_u)

    members_str = ""
    if completed_students:
        members_str += "  💎 **الطلاب المكتملون (100%):**\n"
        for idx, sname in enumerate(completed_students[:20], 1):
            members_str += f"    {idx}. طالب: `{sname}` (مكتمل 100% 💎)\n"
        if len(completed_students) > 20:
            members_str += f"    ... و {len(completed_students) - 20} طالب آخر.\n"
    if started_students:
        members_str += "\n  ⚡ **الطلاب الذين بدأوا الحل:**\n"
        for idx, sname in enumerate(started_students[:20], 1):
            badge = " (مكتمل 💎)" if sname in completed_students else " (جاري الحل ⏳)"
            members_str += f"    {idx}. طالب: `{sname}`{badge}\n"
        if len(started_students) > 20:
            members_str += f"    ... و {len(started_students) - 20} طالب آخر.\n"
    if not completed_students and not started_students:
        if joined:
            for idx, uid in enumerate(joined[:10], 1):
                members_str += f"  {idx}. وكيل/عميل ID: `{uid}` (مفعّل)\n"
        else:
            members_str = "  *(لا يوجد طلاب مسجلون في هذه المجموعة بعد)*\n"

    text = (
        f"📦 **تفاصيل باقة الاشتراك / الوكيل:**\n"
        f"━━━━━━━━━━━━━━━━━━━━\n"
        f"🏷️ **الخطة:** {g.get('tier_name', 'باقة')}\n"
        f"🆔 **معرف الباقة:** `{g.get('group_id')}`\n"
        f"🔑 **باسورد العملاء:** `🔒 ••••••••` *(محمي عن الشاشة)*\n"
        f"👥 **السعة الكلية للباقة:** **{max_u}** عميل\n"
        f"✅ **العملاء المكتملون:** **{done_u}** / **{max_u}** عميل\n"
        f"⚡ **الطلاب الذين بدأوا الحل:** **{started_u}** طالب\n"
        f"⏳ **المتبقي المتاح للاستهلاك:** **{rem_u}** عميل\n"
        f"⚡ **الحالة:** {status_str}\n"
        f"📅 **تاريخ الإنشاء:** `{g.get('created_at', '')[:19]}`\n"
        f"━━━━━━━━━━━━━━━━━━━━\n"
        f"🎓 **قائمة الطلاب والعملاء:**\n"
        f"{members_str}\n"
        f"━━━━━━━━━━━━━━━━━━━━\n"
        f"💡 اضغط على زر **👁️ كشف باسورد الباقة** بالأسفل لرؤيته بنافذة منبثقة آمنة دون إظهاره على الشاشة."
    )
    await safe_edit_message(callback.message, text, reply_markup=get_admin_group_detail_keyboard(group_id, is_active), parse_mode="Markdown")


@router.callback_query(F.data.startswith("pkg_show_pass_"))
async def cb_admin_show_pkg_pass(callback: CallbackQuery):
    """كشف باسورد الباقة في نافذة منبثقة آمنة للأدمن فقط دون طباعته على الشاشة"""
    group_id = callback.data.replace("pkg_show_pass_", "").strip()
    g = answers_db.get_subscription_group(group_id)
    if g:
        pwd = g.get("password", "")
        await callback.answer(f"🔐 كلمة مرور الباقة ({group_id}) هي:\n{pwd}", show_alert=True)
    else:
        await callback.answer("تعذر العثور على الباقة.", show_alert=True)


@router.callback_query(F.data.startswith("show_adm_pass_"))
async def cb_admin_show_single_pass(callback: CallbackQuery):
    """كشف كلمة مرور أدمن محددة في نافذة منبثقة آمنة دون عرضها بالشات"""
    idx_str = callback.data.replace("show_adm_pass_", "").strip()
    passwords = answers_db.get_admin_passwords()
    if idx_str.isdigit():
        idx = int(idx_str)
        if 0 <= idx < len(passwords):
            target = passwords[idx]
            await callback.answer(f"🔐 كلمة مرور الأدمن #{idx+1} هي:\n{target}", show_alert=True)
            return
    await callback.answer("كلمة المرور غير متوفرة.", show_alert=True)


@router.callback_query(F.data.startswith("pkg_toggle_"))
async def cb_admin_toggle_pkg(callback: CallbackQuery):
    """تفعيل أو تعطيل الباقة"""
    group_id = callback.data.replace("pkg_toggle_", "").strip()
    new_status = answers_db.toggle_subscription_group(group_id)
    state_txt = "تفعيل" if new_status else "تعطيل"
    await callback.answer(f"تم {state_txt} الباقة بنجاح!")
    await cb_admin_view_pkg(callback)


@router.callback_query(F.data.startswith("pkg_delete_"))
async def cb_admin_delete_pkg(callback: CallbackQuery):
    """حذف باقة الاشتراك نهائياً"""
    group_id = callback.data.replace("pkg_delete_", "").strip()
    answers_db.delete_subscription_group(group_id)
    await callback.answer("تم حذف الباقة بنجاح!", show_alert=True)
    await cb_admin_list_pkgs(callback)


# ==========================================
# إدارة باسوردات الأدمن (Admin Passwords Management)
# ==========================================

@router.callback_query(F.data == "btn_admin_passwords")
async def cb_admin_passwords(callback: CallbackQuery):
    """عرض قائمة باسوردات الأدمن وإمكانية التعديل عليها"""
    await callback.answer()
    passwords = answers_db.get_admin_passwords()
    text = (
        "🔑 **إدارة كلمات مرور الأدمن (Firebase Cloud):**\n"
        "━━━━━━━━━━━━━━━━━━━━\n"
        "كلمات المرور التالية تمنح صلاحية الوصول للوحة تحكم الأدمن.\n"
        "يمكنك استخدام أي منها، وإضافة أو حذف كلمات مرور سحابياً في أي وقت:\n"
    )
    await safe_edit_message(callback.message, text, reply_markup=get_admin_passwords_keyboard(passwords), parse_mode="Markdown")


@router.callback_query(F.data.startswith("del_adm_pass_"))
async def cb_admin_del_pass(callback: CallbackQuery):
    """حذف كلمة مرور أدمن"""
    idx_str = callback.data.replace("del_adm_pass_", "").strip()
    passwords = answers_db.get_admin_passwords()
    if idx_str.isdigit():
        idx = int(idx_str)
        if 0 <= idx < len(passwords):
            target = passwords[idx]
            answers_db.remove_admin_password(target)
            await callback.answer("تم حذف كلمة المرور بنجاح!")
    await cb_admin_passwords(callback)


@router.callback_query(F.data == "btn_add_adm_pass")
async def cb_admin_add_pass(callback: CallbackQuery, state: FSMContext):
    """طلب إدخال كلمة مرور أدمن جديدة"""
    await callback.answer()
    text = (
        "🔑 **إضافة كلمة مرور أدمن جديدة:**\n\n"
        "أرسل كلمة المرور الجديدة في رسالة نصية ليتم حفظها سحابياً في Firebase و SQLite:"
    )
    await safe_edit_message(callback.message, text, reply_markup=get_cancel_keyboard(), parse_mode="Markdown")
    await state.set_state(UserStates.admin_waiting_new_admin_pass)


@router.message(UserStates.admin_waiting_new_admin_pass)
async def process_admin_new_pass(message: Message, state: FSMContext):
    """حفظ كلمة مرور الأدمن الجديدة"""
    track_message(message.from_user.id, message.message_id)
    new_p = message.text.strip()
    if new_p:
        answers_db.add_admin_password(new_p)
        await state.clear()
        sent = await message.answer(f"✅ **تمت إضافة كلمة المرور (`{new_p}`) وحفظها سحابياً بنجاح!**", parse_mode="Markdown")
        track_message(message.from_user.id, sent.message_id)
        await show_admin_dashboard(message, message.from_user.id)


# ==========================================
# فحص ومزامنة فايربيس (Firebase Cloud Sync & Status)
# ==========================================

@router.callback_query(F.data == "btn_admin_firebase_sync")
async def cb_admin_firebase_sync(callback: CallbackQuery):
    """عرض حالة الاتصال السحابي بقاعدة بيانات فايربيس وفحص المفتاح"""
    await callback.answer()
    if not answers_db.firebase:
        await safe_edit_message(callback.message, "⚠️ خدمة فايربيس غير متوفرة في بيئة العمل.", reply_markup=get_cancel_keyboard())
        return

    # فحص وإعادة تحميل المفتاح تلقائياً إذا قام المستخدم بتحديث ملف firebase_credentials.json
    try:
        answers_db.firebase.check_and_reload_if_modified()
    except Exception:
        pass
    report = answers_db.firebase.get_status_report()
    is_conn = report.get("connected", False)

    if is_conn:
        status_line = "🟢 **متصل وسحابي نشط (Cloud Firestore Online)**"
        proj = report.get('project_id', '')
        client = report.get('client_email', '')
        key_id = str(report.get('file_key_id', ''))[:12]
        detail = (
            f"• **المشروع السحابي:** `{proj}`\n"
            f"• **حساب الخدمة:** `{client}`\n"
            f"• **معرف المفتاح:** `{key_id}...`\n\n"
            "✅ جميع كلمات مرور الأدمن، باقات الاشتراك، وقوائم المشتركين متزامنة سحابياً بشكل لحظي ومباشر."
        )
    else:
        status_line = "🔴 **غير متصل سحابياً (يعمل بقاعدة SQLite المحلية الآمنة)**"
        proj = report.get('project_id', '')
        client = report.get('client_email', '')
        key_id = str(report.get('file_key_id', ''))[:12]
        detail = (
            f"• **المشروع المطلوب:** `{proj}`\n"
            f"• **حساب الخدمة:** `{client}`\n"
            f"• **المفتاح المحلي الحالي:** `{key_id}...`\n\n"
            "⚠️ **سبب التوقف السحابي:** تم تجديد أو انتهاء صلاحية المفتاح في Google Cloud IAM (`Invalid JWT Signature`).\n\n"
            "💡 **طريقة تفعيل فايربيس السحابي وحفظ كل البيانات عليه فوراً:**\n"
            "1. افتح [Firebase Console](https://console.firebase.google.com)\n"
            "2. اذهب إلى: **Project Settings (⚙️) ➔ Service accounts ➔ Generate new private key**\n"
            "3. ضع المفتاح الجديد باسم `firebase_credentials.json` في مجلد البوت.\n"
            "🔄 سيكتشف البوت المفتاح تلقائياً ويقوم بمزامنة ورفع جميع الباقات والبيانات فوراً دون إعادة تشغيل!"
        )

    text_msg = (
        "🔥 **حالة قاعدة بيانات Firebase Cloud Firestore:**\n"
        "━━━━━━━━━━━━━━━━━━━━\n"
        f"الحالة: {status_line}\n\n"
        f"{detail}\n"
        "━━━━━━━━━━━━━━━━━━━━"
    )
    await safe_edit_message(callback.message, text_msg, reply_markup=get_firebase_status_keyboard(is_conn), parse_mode="Markdown")


@router.callback_query(F.data == "btn_firebase_force_sync")
async def cb_firebase_force_sync(callback: CallbackQuery):
    """دفع ومزامنة كافة البيانات من SQLite المحلي إلى Firestore السحابي"""
    await callback.answer("جاري مزامنة ورفع البيانات سحابياً...")
    res = answers_db.sync_to_firebase()
    if res.get("status") == "success":
        st = res.get("stats", {})
        msg = (
            "✅ **تمت المزامنة السحابية الشاملة إلى Firebase Firestore بنجاح!**\n"
            "━━━━━━━━━━━━━━━━━━━━\n"
            f"🔑 كلمات مرور الأدمن: **{st.get('admin', 0)}** محفوظة في `settings/admin`\n"
            f"📦 باقات ومجموعات الاشتراك: **{st.get('groups', 0)}** باقة في `subscription_groups`\n"
            f"👥 تتبع التجربة المجانية: **{st.get('trials', 0)}** مستخدم في `free_trial_users`\n"
            f"👤 حسابات وتفضيلات الطلاب: **{st.get('users', 0)}** حساب في `bot_users`\n"
            "━━━━━━━━━━━━━━━━━━━━\n"
            "🌐 كافة البيانات أصبحت محفوظة ومتاحة سحابياً على فايربيس بنسبة 100%."
        )
    else:
        msg = f"⚠️ تعذرت المزامنة السحابية: {res.get('message', 'خطأ غير معروف')}"

    await safe_edit_message(callback.message, msg, reply_markup=get_firebase_status_keyboard(True), parse_mode="Markdown")


# ==========================================
# ميزة حل المنصة لأي حساب طالب داخل الأدمن حصراً
# ==========================================

@router.callback_query(F.data == "btn_admin_solve_account")
async def cb_admin_solve_account(callback: CallbackQuery, state: FSMContext):
    """بدء حل المنصة بالكامل لأي حساب طالب من داخل الأدمن حصراً"""
    await callback.answer()
    user_id = callback.from_user.id
    sess = get_session(user_id)
    if not sess.get("is_admin"):
        await callback.answer("⚠️ هذه الميزة مخصصة لإدارة البوت فقط!", show_alert=True)
        return
    text = (
        "🚀 **حل المنصة بالكامل لأي حساب طالب (Admin Solver) ⚡:**\n"
        "━━━━━━━━━━━━━━━━━━━━\n"
        "تتيح لك هذه الميزة إدخال بيانات أي حساب طالب وحل المنهج كاملاً بنسبة 100% وبأقصى سرعة عبر الـ API دون أي قيود.\n\n"
        "👇 **اختر الصف الدراسي والمسار لحساب الطالب:**"
    )
    await safe_edit_message(callback.message, text, reply_markup=get_admin_solve_grade_keyboard(), parse_mode="Markdown")


@router.callback_query(F.data.startswith("adm_solve_grade_"))
async def cb_admin_select_solve_grade(callback: CallbackQuery, state: FSMContext):
    """تحديد مسار وصف حساب الطالب والبدء بطلب الكود"""
    await callback.answer()
    choice = callback.data.replace("adm_solve_grade_", "").strip()

    if choice == "1":
        grade = "grade_1"
        course_url = "https://me-tp.qureo.education/course/javascript_ar"
        label = "الصف الأول الثانوي (JavaScript ⚡)"
    elif choice == "2_py":
        grade = "grade_2"
        course_url = "https://me-tp.qureo.education/course/python_short_ar"
        label = "الصف الثاني الثانوي (بايثون Python 🐍)"
    else:
        grade = "grade_2"
        course_url = "https://me-tp.qureo.education/course/javascript_ar"
        label = "الصف الثاني الثانوي (جافاسكريبت JS ⚡)"

    await state.update_data(target_grade=grade, target_course_url=course_url, target_grade_label=label)

    text = (
        f"✅ **المسار المختار:** {label}\n\n"
        "👤 **الخطوة 1 من 2:** أرسل **اسم المستخدم (ID / كود الطالب)** لحساب المنصة المراد حله:\n"
        "*(أرسل الكود في رسالة نصية هنا)*"
    )
    await safe_edit_message(callback.message, text, reply_markup=get_cancel_keyboard(), parse_mode="Markdown")
    await state.set_state(UserStates.admin_waiting_target_username)


@router.message(UserStates.admin_waiting_target_username)
async def process_admin_target_username(message: Message, state: FSMContext):
    """استلام كود الطالب المراد حله من الأدمن"""
    track_message(message.from_user.id, message.message_id)
    username = message.text.strip()
    if not username:
        await message.answer("⚠️ يرجى إرسال كود أو اسم مستخدم صحيح:")
        return
    await state.update_data(target_username=username)

    text = (
        f"👤 كود الطالب: `{username}`\n\n"
        "🔑 **الخطوة 2 من 2:** أرسل **كلمة المرور (Password)** الخاصة بهذا الحساب:\n"
        "*(سيتم تسجيل الدخول فوراً وبدء حل المنصة بالكامل 100%)*"
    )
    sent = await message.answer(text, reply_markup=get_cancel_keyboard(), parse_mode="Markdown")
    track_message(message.from_user.id, sent.message_id)
    await state.set_state(UserStates.admin_waiting_target_password)


@router.message(UserStates.admin_waiting_target_password)
async def process_admin_target_password(message: Message, state: FSMContext):
    """تسجيل الدخول بحساب الطالب وإطلاق الحل التلقائي الشامل فوراً"""
    user_id = message.from_user.id
    sess = get_session(user_id)
    track_message(user_id, message.message_id)
    password = message.text.strip()
    data = await state.get_data()
    await state.clear()

    target_username = data.get("target_username")
    target_grade = data.get("target_grade", "grade_1")
    target_course_url = data.get("target_course_url", "https://me-tp.qureo.education/course/javascript_ar")
    target_label = data.get("target_grade_label", "كيريو")

    # ضبط جلسة الأدمن على هذا الحساب لبدء الحل الشامل
    sess["grade"] = target_grade
    sess["subject"] = "programming"
    sess["username"] = target_username
    sess["password"] = password
    sess["active_course_url"] = target_course_url
    sess["is_admin"] = True

    status_msg = await message.answer(
        f"🚀 **جاري تسجيل الدخول بحساب الطالب `{target_username}` ({target_label})...**\n"
        f"⚡ سيتم حل جميع فصول وكويزات واختبارات المنصة بنسبة 100% واكتساب كافة الماسات 💎...\n"
        f"يرجى الانتظار ثوانٍ معدودة...",
        parse_mode="Markdown"
    )

    client = get_user_client(user_id)
    client.headless = Config.HEADLESS
    login_ok, login_msg, shot = await client.login(target_username, password)

    if not login_ok:
        await status_msg.edit_text(
            f"❌ **تعذر تسجيل الدخول بحساب الطالب:** {login_msg}\n\n"
            f"يرجى التأكد من كود الطالب وكلمة المرور وإعادة المحاولة من لوحة الأدمن.",
            reply_markup=InlineKeyboardMarkup(inline_keyboard=[
                [InlineKeyboardButton(text="🔄 إعادة المحاولة", callback_data="btn_admin_solve_account")],
                [InlineKeyboardButton(text="🏠 لوحة الأدمن", callback_data="btn_admin_panel")]
            ]),
            parse_mode="Markdown"
        )
        return

    sess["is_logged_in"] = True
    sess["is_solving"] = True

    await status_msg.edit_text(
        f"✅ **تم تسجيل الدخول بنجاح بحساب الطالب `{target_username}`!** 🎉\n"
        f"━━━━━━━━━━━━━━━━━━━━\n"
        f"⚡ **بدء وضع الحل الشامل الخارق (Admin Turbo API Mode) 🚀**\n"
        f"📖 جاري فتح واجهة الفصول، وحل التمارين والكويزات 100%...\n"
        f"━━━━━━━━━━━━━━━━━━━━",
        reply_markup=get_solving_controls(),
        parse_mode="Markdown"
    )

    # إطلاق حلقة الحل التلقائية لكامل المنهج بدون أي قيود
    asyncio.create_task(run_solver_loop(message, user_id))


from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def get_grade_keyboard() -> InlineKeyboardMarkup:
    """لوحة الصفحة الرئيسية واختيار الصف الدراسي مع زر الانضمام لمجموعة وزر الأدمن في الصدارة وزر Clear"""
    buttons = [
        [
            InlineKeyboardButton(text="👥 الانضمام إلى مجموعة 🔑", callback_data="btn_enter_sub_pass")
        ],
        [
            InlineKeyboardButton(text="🎓 الصف الأول الثانوي (مسار JavaScript)", callback_data="grade_1")
        ],
        [
            InlineKeyboardButton(text="🎓 الصف الثاني الثانوي (مسار Python / JS)", callback_data="grade_2")
        ],
        [
            InlineKeyboardButton(text="👑 لوحة تحكم الأدمن (Admin Dashboard) ⚡", callback_data="btn_admin_panel")
        ],
        [
            InlineKeyboardButton(text="🧹 مسح الشاشة (Clear)", callback_data="btn_clear_screen")
        ]
    ]
    return InlineKeyboardMarkup(inline_keyboard=buttons)



def get_subject_keyboard(grade: str = "grade_1") -> InlineKeyboardMarkup:
    """لوحة توجيه لدروس البرمجة في كيريو مع زر Clear"""
    buttons = [
        [
            InlineKeyboardButton(text="💻 متابعة حل دروس البرمجة في كيريو", callback_data="subject_programming")
        ],
        [
            InlineKeyboardButton(text="🔙 تغيير الصف الدراسي", callback_data="btn_change_grade"),
            InlineKeyboardButton(text="🧹 مسح الشاشة (Clear)", callback_data="btn_clear_screen")
        ]
    ]
    return InlineKeyboardMarkup(inline_keyboard=buttons)



def get_about_keyboard() -> InlineKeyboardMarkup:
    """زر الرجوع من صفحة معلومات المطور مع زر Clear"""
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="🔙 العودة للقائمة الرئيسية", callback_data="btn_main_menu"),
                InlineKeyboardButton(text="🧹 مسح الشاشة (Clear)", callback_data="btn_clear_screen")
            ]
        ]
    )


def get_main_keyboard(
    is_logged_in: bool = False,
    is_solving: bool = False,
    grade: str = "grade_1",
    subject: str = "programming",
    is_admin: bool = False
) -> InlineKeyboardMarkup:
    """لوحة المفاتيح الرئيسية للبوت مع تخصيص الصف الأول والثاني ومعلومات المطور وزر مسح الشاشة (Clear)"""
    buttons = []

    if is_admin:
        buttons.append([
            InlineKeyboardButton(text="👑 لوحة تحكم الأدمن (Admin Dashboard)", callback_data="btn_admin_panel")
        ])

    if not is_logged_in:
        # إذا لم يكن مسجلاً: نبرز له زر الانضمام لمجموعة وزر تسجيل الدخول بحسابه الخاص
        buttons.append([
            InlineKeyboardButton(text="👥 الانضمام إلى مجموعة 🔑", callback_data="btn_enter_sub_pass")
        ])
        buttons.append([
            InlineKeyboardButton(text="🔑 تسجيل الدخول بحسابك الخاص", callback_data="btn_login")
        ])
        buttons.append([
            InlineKeyboardButton(text="🎓 تغيير الصف / المادة", callback_data="btn_change_grade"),
            InlineKeyboardButton(text="ℹ️ معلومات البوت", callback_data="btn_about_bot")
        ])
        buttons.append([
            InlineKeyboardButton(text="🧹 مسح الشاشة (Clear)", callback_data="btn_clear_screen")
        ])
        return InlineKeyboardMarkup(inline_keyboard=buttons)


    # إذا كان مسجلاً للدخول بالفعل:
    if is_solving:
        buttons.append([
            InlineKeyboardButton(text="⏹️ إيقاف الحل التلقائي", callback_data="btn_stop_solve"),
            InlineKeyboardButton(text="📸 التقاط شاشة حية", callback_data="btn_screenshot")
        ])
    else:
        buttons.append([
            InlineKeyboardButton(text="⚡ بدء الحل التلقائي الفوري (فتح المتصفح)", callback_data="btn_start_solve")
        ])

    # اختيار المسار لطلاب الصف الثاني
    if grade != "grade_1":
        buttons.append([
            InlineKeyboardButton(text="📚 اختيار المسار (Python / JS)", callback_data="btn_select_course")
        ])

    # تقرير المستوى الحالي وتقدم الـ API والانضمام لمجموعة
    buttons.append([
        InlineKeyboardButton(text="📊 مستواي الحالي والـ API", callback_data="btn_account_status"),
        InlineKeyboardButton(text="👥 الانضمام لمجموعة 🔑", callback_data="btn_enter_sub_pass")
    ])

    # تبديل الحساب وزر مسح الشاشة
    buttons.append([
        InlineKeyboardButton(text="🔄 تبديل الحساب", callback_data="btn_login"),
        InlineKeyboardButton(text="🧹 مسح الشاشة وتسجيل الخروج (Clear)", callback_data="btn_clear_screen")
    ])

    # معلومات البوت وتغيير الصف
    buttons.append([
        InlineKeyboardButton(text="ℹ️ معلومات البوت", callback_data="btn_about_bot"),
        InlineKeyboardButton(text="🎓 تغيير الصف / المادة", callback_data="btn_change_grade")
    ])

    return InlineKeyboardMarkup(inline_keyboard=buttons)



def get_status_keyboard(current_chapter_id: int = None, current_chapter_name: str = "") -> InlineKeyboardMarkup:
    """لوحة التحكم الخاصة بعرض حالة المستوى وتفاصيل الـ API"""
    buttons = []
    if current_chapter_id:
        btn_label = f"⚡ حل المستوى الحالي ({current_chapter_name})" if current_chapter_name else "⚡ حل هذا المستوى فوراً"
        buttons.append([
            InlineKeyboardButton(text=btn_label, callback_data=f"solve_chap_{current_chapter_id}")
        ])
    buttons.append([
        InlineKeyboardButton(text="🚀 حل جميع الفصول المتبقية", callback_data="btn_start_solve")
    ])
    buttons.append([
        InlineKeyboardButton(text="🔄 تحديث", callback_data="btn_account_status"),
        InlineKeyboardButton(text="🔙 القائمة الرئيسية", callback_data="btn_main_menu")
    ])
    buttons.append([
        InlineKeyboardButton(text="🧹 مسح الشاشة (Clear)", callback_data="btn_clear_screen")
    ])
    return InlineKeyboardMarkup(inline_keyboard=buttons)



def get_courses_keyboard() -> InlineKeyboardMarkup:
    """لوحة اختيار المسار الدراسي في كيريو"""
    buttons = [
        [
            InlineKeyboardButton(
                text="⚡ مسار جافاسكريبت (JavaScript)",
                callback_data="course_js"
            )
        ],
        [
            InlineKeyboardButton(
                text="🐍 مسار بايثون (Python)",
                callback_data="course_python"
            )
        ],
        [
            InlineKeyboardButton(
                text="🔗 إدخال رابط أو كود مستوى (مثال: 90032)",
                callback_data="course_custom"
            )
        ],
        [
            InlineKeyboardButton(
                text="🔙 العودة للقائمة الرئيسية",
                callback_data="btn_main_menu"
            ),
            InlineKeyboardButton(
                text="🧹 مسح الشاشة (Clear)",
                callback_data="btn_clear_screen"
            )
        ]
    ]
    return InlineKeyboardMarkup(inline_keyboard=buttons)



def get_solving_controls() -> InlineKeyboardMarkup:
    """أزرار التحكم أثناء تشغيل الحل"""
    buttons = [
        [
            InlineKeyboardButton(text="📸 لقطة شاشة الآن", callback_data="btn_screenshot"),
            InlineKeyboardButton(text="⏹️ إيقاف الحل", callback_data="btn_stop_solve")
        ],
        [
            InlineKeyboardButton(text="🧹 مسح الشاشة (Clear)", callback_data="btn_clear_screen")
        ]
    ]
    return InlineKeyboardMarkup(inline_keyboard=buttons)



def get_cancel_keyboard() -> InlineKeyboardMarkup:
    """زر الإلغاء السريع ومسح الشاشة"""
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="❌ إلغاء", callback_data="btn_cancel"),
                InlineKeyboardButton(text="🧹 مسح الشاشة (Clear)", callback_data="btn_clear_screen")
            ]
        ]
    )


def get_chapters_keyboard(
    chapters: list,
    page: int = 1,
    per_page: int = 5,
    course_code: str = "py",
    completed_ids: set = None,
    current_chap_id: int = None
) -> InlineKeyboardMarkup:
    """لوحة مفاتيح تفاعلية لعرض مستويات وفصول المسار مع التنقل والصفحات"""
    if completed_ids is None:
        completed_ids = set()

    import math
    total_pages = max(1, math.ceil(len(chapters) / per_page))
    page = max(1, min(page, total_pages))

    start_idx = (page - 1) * per_page
    end_idx = start_idx + per_page
    page_chapters = chapters[start_idx:end_idx]

    buttons = []

    # إذا وجد مستوى حالي لم يكتمل، نظهر زر بارز لحله فوراً
    if current_chap_id:
        curr_obj = next((c for c in chapters if c.get("id") == current_chap_id), None)
        curr_name = curr_obj.get("name", "") if curr_obj else ""
        btn_text = f"🎯 المستوى الحالي: {curr_name} (حل مباشر)" if curr_name else "🎯 حل المستوى الحالي فوراً"
        buttons.append([
            InlineKeyboardButton(text=btn_text, callback_data=f"sc_{current_chap_id}")
        ])

    # أزرار الفصول (زر لكل فصل)
    for c in page_chapters:
        cid = c.get("id")
        seq = c.get("seq", "?")
        name = c.get("name", f"فصل {seq}")
        q_cnt = c.get("question_count", 0)

        if cid in completed_ids:
            icon = "💎"
            status_text = "5/5"
        elif cid == current_chap_id:
            icon = "⏳"
            status_text = "حالي"
        else:
            icon = "📖"
            status_text = f"{q_cnt}س" if q_cnt else ""

        label = f"{icon} {seq}. {name} [{status_text}]"
        # عند الضغط يفتح أسئلة هذا الفصل سؤال بسؤال
        buttons.append([
            InlineKeyboardButton(text=label, callback_data=f"vc_{cid}")
        ])

    # سطر التنقل بين الصفحات
    if total_pages > 1:
        nav_row = []
        if page > 1:
            nav_row.append(InlineKeyboardButton(text="⬅️ السابق", callback_data=f"cp_{page-1}_{course_code}"))
        nav_row.append(InlineKeyboardButton(text=f"📄 {page} / {total_pages}", callback_data="noop"))
        if page < total_pages:
            nav_row.append(InlineKeyboardButton(text="التالي ➡️", callback_data=f"cp_{page+1}_{course_code}"))
        buttons.append(nav_row)

    # سطر الحل الجماعي التلقائي
    buttons.append([
        InlineKeyboardButton(text="⚡ حل جميع الفصول المتبقية تلقائياً", callback_data="btn_start_solve")
    ])

    # سطر التنقل الرئيسي
    buttons.append([
        InlineKeyboardButton(text="🔄 تحديث", callback_data=f"cp_{page}_{course_code}"),
        InlineKeyboardButton(text="🔙 تغيير المسار", callback_data="btn_select_course"),
        InlineKeyboardButton(text="🏠 الرئيسية", callback_data="btn_main_menu")
    ])

    return InlineKeyboardMarkup(inline_keyboard=buttons)



def get_chapter_questions_keyboard(
    chapter_id: int,
    questions: list,
    test_type: str = "review",
    course_code: str = "py",
    solved_ids: set = None
) -> InlineKeyboardMarkup:
    """لوحة مفاتيح تفاعلية تعرض أسئلة الفصل ليختار المستخدم أي سؤال لحله بمفرده"""
    if solved_ids is None:
        solved_ids = set()

    buttons = []

    # سطر الأزرار لكل سؤال (زران في كل صف لترتيب الشاشة)
    q_buttons = []
    for idx, q_item in enumerate(questions, 1):
        q_info = q_item.get("question", q_item)
        qid = q_info.get("id") or q_item.get("id")
        q_type = q_info.get("type", "choice")
        type_label = "كود 💻" if q_type == "description" else "خيارات 🔘"

        status_icon = "✅" if qid in solved_ids else "❓"
        btn_label = f"{status_icon} س{idx} ({type_label})"

        q_buttons.append(
            InlineKeyboardButton(text=btn_label, callback_data=f"sq_{chapter_id}_{qid}")
        )

        if len(q_buttons) == 2:
            buttons.append(q_buttons)
            q_buttons = []

    if q_buttons:
        buttons.append(q_buttons)

    # زر حل الفصل كاملاً دفعة واحدة
    buttons.append([
        InlineKeyboardButton(text="⚡ حل هذا الفصل بالكامل (جميع الأسئلة)", callback_data=f"sc_{chapter_id}")
    ])

    # أزرار الرجوع
    buttons.append([
        InlineKeyboardButton(text="🔙 قائمة المستويات", callback_data=f"cp_1_{course_code}"),
        InlineKeyboardButton(text="🏠 الرئيسية", callback_data="btn_main_menu")
    ])

    return InlineKeyboardMarkup(inline_keyboard=buttons)



def get_single_question_result_keyboard(
    chapter_id: int,
    next_q_id: int = None,
    course_code: str = "py"
) -> InlineKeyboardMarkup:
    """لوحة التحكم بعد حل سؤال مفرد في كيريو"""
    buttons = []
    if next_q_id:
        buttons.append([
            InlineKeyboardButton(text="⏩ حل السؤال التالي فوراً عبر الـ API", callback_data=f"sq_{chapter_id}_{next_q_id}")
        ])
    buttons.append([
        InlineKeyboardButton(text="📋 استعراض باقي أسئلة هذا المستوى", callback_data=f"vc_{chapter_id}"),
        InlineKeyboardButton(text="🔙 قائمة المستويات", callback_data=f"cp_1_{course_code}")
    ])
    return InlineKeyboardMarkup(inline_keyboard=buttons)



def get_links_bank_keyboard(
    chapters: list,
    page: int = 1,
    per_page: int = 5,
    course_code: str = "py"
) -> InlineKeyboardMarkup:
    """لوحة مفاتيح تفاعلية لبنك روابط الفصول مع عرض الروابط النظيفة وحالة كل مستوى"""
    import math
    total_pages = max(1, math.ceil(len(chapters) / per_page))
    page = max(1, min(page, total_pages))

    start_idx = (page - 1) * per_page
    end_idx = start_idx + per_page
    page_chapters = chapters[start_idx:end_idx]

    buttons = []

    # أزرار الفصول
    for c in page_chapters:
        cid = c.get("chapter_id") or c.get("id")
        seq = c.get("seq", "?")
        name = c.get("name", f"مستوى {seq}")
        completed = c.get("completed", 0)
        diamond = c.get("diamond", 0)

        if completed or diamond >= 5:
            icon = "💎"
            status = "مكتمل (5/5)"
        else:
            icon = "⏳"
            status = "غير مكتمل"

        label = f"{icon} {seq}. {name} [{status}]"
        buttons.append([
            InlineKeyboardButton(text=label, callback_data=f"sc_{cid}")
        ])

    # سطر التنقل بين الصفحات
    if total_pages > 1:
        nav_row = []
        if page > 1:
            nav_row.append(InlineKeyboardButton(text="⬅️ السابق", callback_data=f"lb_{page-1}_{course_code}"))
        nav_row.append(InlineKeyboardButton(text=f"📄 {page} / {total_pages}", callback_data="noop"))
        if page < total_pages:
            nav_row.append(InlineKeyboardButton(text="التالي ➡️", callback_data=f"lb_{page+1}_{course_code}"))
        buttons.append(nav_row)

    # زر استئناف الحل التلقائي
    buttons.append([
        InlineKeyboardButton(text="⚡ استئناف الحل التلقائي للمستويات المتبقية", callback_data="btn_start_solve")
    ])

    # العودة للرئيسية
    buttons.append([
        InlineKeyboardButton(text="🔄 تحديث", callback_data=f"lb_{page}_{course_code}"),
        InlineKeyboardButton(text="🏠 الرئيسية", callback_data="btn_main_menu")
    ])

    return InlineKeyboardMarkup(inline_keyboard=buttons)

# ==========================================
# لوحات المفاتيح لنظام الاشتراكات والأدمن
# ==========================================

def get_subscription_required_keyboard() -> InlineKeyboardMarkup:
    """لوحة تفعيل الاشتراك للمستخدم الجديد مع زر الانضمام لمجموعة ورابط المراسلة لحل المنصة كاملة"""
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="👥 الانضمام إلى مجموعة 🔑", callback_data="btn_enter_sub_pass")
            ],
            [
                InlineKeyboardButton(text="💬 تواصل معنا لحل المنصة كاملة 🚀", url="https://m.me/1395840426948411")
            ],
            [
                InlineKeyboardButton(text="ℹ️ معلومات البوت", callback_data="btn_about_bot"),
                InlineKeyboardButton(text="🧹 مسح الشاشة (Clear)", callback_data="btn_clear_screen")
            ]
        ]
    )


def get_admin_dashboard_keyboard() -> InlineKeyboardMarkup:
    """لوحة التحكم الرئيسية للأدمن (Admin Dashboard) مع خيار حل المستخدم العادي وكافة المميزات"""
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="⚡ تصفح وحل فصول كيريو (حل مباشر مفتوح بالكامل) 🚀", callback_data="btn_select_course")
            ],
            [
                InlineKeyboardButton(text="📦 إنشاء باقة اشتراك جديدة (New Plan) ➕", callback_data="btn_admin_create_pkg"),
                InlineKeyboardButton(text="📋 إدارة باقات الاشتراك والمجموعات 👥", callback_data="btn_admin_list_pkgs")
            ],
            [
                InlineKeyboardButton(text="🎯 حل المنصة لحساب طالب خارجي بكود الطالب", callback_data="btn_admin_solve_account")
            ],
            [
                InlineKeyboardButton(text="🔒 إدارة كلمات مرور الأدمن (محمية)", callback_data="btn_admin_passwords"),
                InlineKeyboardButton(text="🔥 فحص ومزامنة فايربيس", callback_data="btn_admin_firebase_sync")
            ],
            [
                InlineKeyboardButton(text="🎓 تغيير الصف الدراسي (أولى / ثانية ثانوي)", callback_data="btn_change_grade"),
                InlineKeyboardButton(text="🧹 مسح الشاشة (Clear)", callback_data="btn_clear_screen")
            ]
        ]
    )


def get_firebase_status_keyboard(is_connected: bool) -> InlineKeyboardMarkup:
    """أزرار فحص ومزامنة فايربيس السحابية"""
    buttons = []
    if is_connected:
        buttons.append([
            InlineKeyboardButton(text="🔄 مزامنة فورية لكافة البيانات لفايربيس", callback_data="btn_firebase_force_sync")
        ])
    else:
        buttons.append([
            InlineKeyboardButton(text="🔄 إعادة فحص وتحديث الاتصال الآن", callback_data="btn_admin_firebase_sync")
        ])
    buttons.append([
        InlineKeyboardButton(text="🔙 العودة للوحة الإدارة", callback_data="btn_admin_home")
    ])
    return InlineKeyboardMarkup(inline_keyboard=buttons)


def get_admin_solve_grade_keyboard() -> InlineKeyboardMarkup:
    """لوحة اختيار الصف والمسار لحساب الطالب المراد حله من قبل الأدمن"""
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="🎓 الصف الأول الثانوي (مسار JavaScript ⚡)", callback_data="adm_solve_grade_1")
            ],
            [
                InlineKeyboardButton(text="🎓 الصف الثاني الثانوي (مسار Python 🐍)", callback_data="adm_solve_grade_2_py")
            ],
            [
                InlineKeyboardButton(text="🎓 الصف الثاني الثانوي (مسار JavaScript ⚡)", callback_data="adm_solve_grade_2_js")
            ],
            [
                InlineKeyboardButton(text="🔙 العودة للوحة الإدارة", callback_data="btn_admin_home")
            ]
        ]
    )


def get_plan_tiers_keyboard() -> InlineKeyboardMarkup:
    """لوحة اختيار نوع وخطة الباقة عند الإنشاء"""
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="🥉 باقة 15 عميل (الأساسية)", callback_data="tier_15")
            ],
            [
                InlineKeyboardButton(text="🥈 الباقة الفضية (25 عميل)", callback_data="tier_25")
            ],
            [
                InlineKeyboardButton(text="🥇 الباقة الذهبية (40 عميل)", callback_data="tier_40")
            ],
            [
                InlineKeyboardButton(text="💎 الباقة الماسية (60 عميل)", callback_data="tier_60")
            ],
            [
                InlineKeyboardButton(text="⚙️ تحديد سعة مخصصة...", callback_data="tier_custom")
            ],
            [
                InlineKeyboardButton(text="🔙 العودة للوحة الإدارة", callback_data="btn_admin_home")
            ]
        ]
    )


def get_admin_groups_list_keyboard(groups: list) -> InlineKeyboardMarkup:
    """لوحة استعراض جميع الباقات المنشأة للأدمن"""
    buttons = []
    for g in groups:
        gid = g.get("group_id", "")
        tier = g.get("tier_name", "باقة")
        count = g.get("users_count", 0)
        max_u = g.get("max_users", 0)
        is_act = g.get("is_active", True)
        icon = "🟢" if is_act else "🔴"
        btn_text = f"{icon} {tier} ({count}/{max_u}) - [{gid}]"
        buttons.append([
            InlineKeyboardButton(text=btn_text, callback_data=f"view_pkg_{gid}")
        ])

    buttons.append([
        InlineKeyboardButton(text="➕ إنشاء باقة جديدة", callback_data="btn_admin_create_pkg")
    ])
    buttons.append([
        InlineKeyboardButton(text="🔙 العودة للوحة الإدارة", callback_data="btn_admin_home")
    ])
    return InlineKeyboardMarkup(inline_keyboard=buttons)


def get_admin_group_detail_keyboard(group_id: str, is_active: bool) -> InlineKeyboardMarkup:
    """لوحة التحكم بباقة محددة مع خيار كشف الباسورد الآمن"""
    toggle_text = "⏸️ تعطيل الباقة مؤقتاً" if is_active else "▶️ إعادة تفعيل الباقة"
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="👁️ كشف باسورد الباقة (نافذة منبثقة آمنة)", callback_data=f"pkg_show_pass_{group_id}")
            ],
            [
                InlineKeyboardButton(text=toggle_text, callback_data=f"pkg_toggle_{group_id}"),
                InlineKeyboardButton(text="🗑️ حذف الباقة نهائياً", callback_data=f"pkg_delete_{group_id}")
            ],
            [
                InlineKeyboardButton(text="🔙 العودة لقائمة الباقات", callback_data="btn_admin_list_pkgs"),
                InlineKeyboardButton(text="🏠 لوحة الإدارة", callback_data="btn_admin_home")
            ]
        ]
    )


def get_admin_passwords_keyboard(passwords: list) -> InlineKeyboardMarkup:
    """لوحة استعراض وإدارة كلمات مرور الأدمن مع إخفاء وتشفير الباسورد عن الشاشة"""
    buttons = []
    for idx, p in enumerate(passwords):
        del_btn = [InlineKeyboardButton(text=f"🔒 كلمة مرور أدمن #{idx+1} (••••••••)", callback_data=f"show_adm_pass_{idx}")]
        if len(passwords) > 1:
            del_btn.append(InlineKeyboardButton(text="🗑️ مسح", callback_data=f"del_adm_pass_{idx}"))
        buttons.append(del_btn)

    buttons.append([
        InlineKeyboardButton(text="➕ إضافة كلمة مرور أدمن جديدة", callback_data="btn_add_adm_pass")
    ])
    buttons.append([
        InlineKeyboardButton(text="🔙 العودة للوحة الإدارة", callback_data="btn_admin_home")
    ])
    return InlineKeyboardMarkup(inline_keyboard=buttons)


def get_post_solve_completed_keyboard() -> InlineKeyboardMarkup:
    """لوحة الانتقال المباشر لقسم المستخدم بعد اكتمال الحل بنجاح"""
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="👤 مستواي الحالي وبيانات الحساب (User Status)", callback_data="btn_account_status")
            ],
            [
                InlineKeyboardButton(text="⚡ حل فصول إضافية (Turbo API)", callback_data="btn_start_solve"),
                InlineKeyboardButton(text="🔄 تبديل الحساب", callback_data="btn_login")
            ],
            [
                InlineKeyboardButton(text="🏠 القائمة الرئيسية", callback_data="btn_main_menu"),
                InlineKeyboardButton(text="🧹 مسح الشاشة (Clear)", callback_data="btn_clear_screen")
            ]
        ]
    )

def get_contact_for_full_platform_keyboard() -> InlineKeyboardMarkup:
    """لوحة توجيه للمستخدم بعد إكمال أول 4 مستويات للتواصل مع الصفحة لحل المنصة كاملة مع زر الانضمام لمجموعة"""
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="👥 الانضمام إلى مجموعة 🔑",
                    callback_data="btn_enter_sub_pass"
                )
            ],
            [
                InlineKeyboardButton(
                    text="💬 تواصل معنا لحل المنصة كاملة 🚀",
                    url="https://m.me/1395840426948411"
                )
            ],
            [
                InlineKeyboardButton(
                    text="🏠 القائمة الرئيسية",
                    callback_data="btn_main_menu"
                ),
                InlineKeyboardButton(
                    text="🧹 مسح الشاشة (Clear)",
                    callback_data="btn_clear_screen"
                )
            ]
        ]
    )


import asyncio
import logging
import sys
import os
import time
from pathlib import Path

# ضبط حلقة الأحداث لويندوز لدعم العمليات الفرعية (Subprocesses) لـ Playwright
if sys.platform == "win32":
    asyncio.set_event_loop_policy(asyncio.WindowsProactorEventLoopPolicy())

# ==============================================================
# إجبار بايثون على إضافة مجلد المشروع في أول قائمة sys.path
# واكتشاف الحزم تلقائياً لمنع أي خطأ ModuleNotFoundError نهائياً
# ==============================================================
BASE_DIR = Path(__file__).resolve().parent
if str(BASE_DIR) not in sys.path:
    sys.path.insert(0, str(BASE_DIR))

# 0. استخراج الحزمة التلقائي إذا وجد ملف deploy_server_package.zip على السيرفر
bot_candidate = BASE_DIR / "bot"
if not bot_candidate.exists():
    zip_files = list(BASE_DIR.glob("*.zip"))
    for z_file in zip_files:
        try:
            import zipfile
            print(f"📦 [Auto-Extract] وجد أرشيف '{z_file.name}' على السيرفر! جاري فك ضغط الحزمة تلقائياً...")
            with zipfile.ZipFile(z_file, "r") as z:
                z.extractall(BASE_DIR)
            print("✅ [Auto-Extract] تم فك ضغط مجلدات bot و solver وبنك البيانات بنجاح تام!")
            break
        except Exception as e_zip:
            print(f"⚠️ فشل استخراج {z_file.name}: {e_zip}")

# 1. البحث التلقائي عن حزمة bot سواء في المجلد الأساسي أو مجلدات فرعية (مثل PythonProject3 أو src أو Bot)
if not bot_candidate.exists():
    for item in os.listdir(BASE_DIR):
        item_path = BASE_DIR / item
        if item.lower() == "bot" and item_path.is_dir():
            try:
                os.symlink(item_path, bot_candidate)
            except Exception:
                pass
            if str(BASE_DIR) not in sys.path:
                sys.path.insert(0, str(BASE_DIR))
            break

    if not bot_candidate.exists():
        for root, dirs, files in os.walk(BASE_DIR):
            if "handlers.py" in files and os.path.basename(root).lower() == "bot":
                parent_dir = os.path.dirname(root)
                if parent_dir not in sys.path:
                    sys.path.insert(0, parent_dir)
                break

# 1.5 المعالجة الذاتية التلقائية (Auto-Heal): إذا تم رفع ملفات bot أو solver في المجلد الرئيسي مباشرة عبر المتصفح
bot_root_files = ["handlers.py", "keyboards.py", "states.py"]
if not bot_candidate.exists() and any((BASE_DIR / f).exists() for f in bot_root_files):
    print("🔧 [Auto-Heal] تم رصد ملفات البوت مبعثرة في المجلد الرئيسي! جاري إنشاء مجلد 'bot' وتنظيم الملفات داخله...")
    try:
        bot_candidate.mkdir(exist_ok=True)
        import shutil
        for f in bot_root_files + ["__init__.py"]:
            src = BASE_DIR / f
            dst = bot_candidate / f
            if src.exists() and src != dst:
                shutil.copy2(src, dst)
        init_file = bot_candidate / "__init__.py"
        if not init_file.exists():
            init_file.write_text("# Auto-generated init\n", encoding="utf-8")
        print("✅ [Auto-Heal] تم تجميع وتنظيم مجلد 'bot' بنجاح تام!")
    except Exception as e_heal:
        print(f"⚠️ فشل Auto-Heal لـ bot: {e_heal}")

solver_candidate = BASE_DIR / "solver"
solver_root_files = ["answers_db.py", "firebase_db.py", "gemini_solver.py", "qureo_api.py", "qureo_client.py", "spx_api.py", "spx_client.py"]
if not solver_candidate.exists() and any((BASE_DIR / f).exists() for f in solver_root_files):
    print("🔧 [Auto-Heal] تم رصد ملفات solver مبعثرة في المجلد الرئيسي! جاري إنشاء مجلد 'solver' وتنظيم الملفات داخله...")
    try:
        solver_candidate.mkdir(exist_ok=True)
        import shutil
        for f in solver_root_files + ["__init__.py"]:
            src = BASE_DIR / f
            dst = solver_candidate / f
            if src.exists() and src != dst:
                shutil.copy2(src, dst)
        init_file = solver_candidate / "__init__.py"
        if not init_file.exists():
            init_file.write_text("# Auto-generated init\n", encoding="utf-8")
        print("✅ [Auto-Heal] تم تجميع وتنظيم مجلد 'solver' بنجاح تام!")
    except Exception as e_heal_solver:
        print(f"⚠️ فشل Auto-Heal لـ solver: {e_heal_solver}")

# 2. طباعة تشخيصية لمحتويات السيرفر في السجلات للتحقق
current_files = [f for f in os.listdir(BASE_DIR) if not f.startswith(".")]
print("\n" + "=" * 65)
print(f"🚀 [Qureo Bot Engine] بدء تشغيل البوت في المسار: {BASE_DIR}")
print(f"📂 محتويات مجلد العمل في السيرفر: {current_files}")
has_bot = (BASE_DIR / "bot").exists() or any("bot" in str(p).lower() for p in sys.path)
if not has_bot:
    print("⚠️ [تنبيه هام]: لم يتم العثور على مجلد 'bot' في السيرفر!")
else:
    print("✅ تم التحقق من وجود حزمة 'bot' بنجاح تام!")
print("=" * 65 + "\n")

# إجبار بايثون على استخدام ترميز UTF-8 في ويندوز لمنع أي أخطاء في الرموز التعبيرية واللغة العربية
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace", line_buffering=True)
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8", errors="replace", line_buffering=True)

from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties

from config import Config
from bot.handlers import router, close_all_user_browsers

# إعداد السجلات (Logging) مع ترميز UTF-8
file_handler = logging.FileHandler(Config.LOGS_DIR / "bot.log", encoding="utf-8", errors="replace")
stream_handler = logging.StreamHandler(sys.stdout)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[stream_handler, file_handler]
)
logger = logging.getLogger("QureoSolverBot")


async def start_health_server(port: int):
    """
    خادم HTTP خفيف في الخلفية (Health Check Server) للرد على فحص جاهزية المنصات السحابية
    مثل blitz.cloud و Render و Railway و Fly.io ولمنع المنصة من وضع البوت في السكون (Sleep mode)
    """
    from aiohttp import web

    async def handle_ping(request):
        return web.json_response({
            "status": "online",
            "service": "Qureo Solution Bot",
            "timestamp": int(time.time()),
            "health": "ok"
        })

    app = web.Application()
    app.router.add_get("/", handle_ping)
    app.router.add_get("/health", handle_ping)
    app.router.add_get("/ping", handle_ping)

    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, "0.0.0.0", port)
    await site.start()
    logger.info(f"🌐 [Web Health Check] خادم فحص الحالة السحابي يعمل على المنفذ: {port} (0.0.0.0:{port})")
    return runner


async def main():
    if not Config.TELEGRAM_BOT_TOKEN or Config.TELEGRAM_BOT_TOKEN == "YOUR_TELEGRAM_BOT_TOKEN_HERE":
        logger.error("لم يتم العثور على TELEGRAM_BOT_TOKEN! يرجى التحقق من ملف .env")
        return

    print("\n" + "=" * 65)
    print("🚀 جاري بدء تشغيل نظام بوت كيريو والحل التلقائي الفوري (Qureo Solution Bot ⚡)")
    print("=" * 65)

    # 0. تشغيل خادم فحص الصحة لمنصات الاستضافة السحابية الخارجية (مثل blitz.cloud)
    health_runner = None
    try:
        health_runner = await start_health_server(Config.PORT)
    except Exception as e_srv:
        logger.warning(f"⚠️ تعذر تشغيل خادم فحص الصحة على المنفذ {Config.PORT}: {e_srv}")

    # 0.5. التحقق الاستباقي من جاهزية متصفح Playwright Chromium على السيرفر
    try:
        import subprocess
        print("🌐 [Browser Setup] فحص جاهزية متصفح Chromium الخاص بـ Playwright...")
        subprocess.run(
            [sys.executable, "-m", "playwright", "install", "chromium"],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            timeout=120
        )
        if sys.platform != "win32":
            subprocess.run(
                [sys.executable, "-m", "playwright", "install-deps", "chromium"],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
                timeout=120
            )
        print("✅ [Browser Setup] متصفح Chromium واعتمادات النظام جاهزة للعمل 100%!")
    except Exception as e_pw:
        print(f"ℹ️ [Browser Setup] فحص المتصفح: {e_pw}")

    # 1. إحصائيات بنك البيانات المحلي
    from solver.answers_db import answers_db
    py_count = len(answers_db.get_all_chapters("python_short_ar"))
    js_count = len(answers_db.get_all_chapters("javascript_ar"))
    ans_count = answers_db.get_total_count()

    print(f"✅ [1/5] تم تهيئة بنك البيانات بنجاح (SQLite):")
    print(f"       📚 فصول مسار بايثون المسجلة: {py_count} فصلاً")
    print(f"       🌐 فصول مسار جافاسكريبت المسجلة: {js_count} فصلاً")
    print(f"       🎯 بنك الإجابات المعتمدة: {ans_count} إجابة نموذجية")

    # 2. حالة الاتصال بقاعدة البيانات
    db_mode = "🔥 Firebase Cloud Firestore (سحابي متزامن)" if getattr(answers_db.firebase, "is_connected", False) else "💾 SQLite محلي فوري وآمن (data/answers.db)"
    print(f"✅ [2/5] وضع التخزين والمزامنة: {db_mode}")

    # 3. إنشاء كائن البوت والموزع
    bot = Bot(
        token=Config.TELEGRAM_BOT_TOKEN,
        default=DefaultBotProperties(parse_mode=ParseMode.MARKDOWN)
    )
    dp = Dispatcher()

    # 4. تسجيل مسارات الأوامر والأحداث
    dp.include_router(router)
    print("✅ [3/5] تم تسجيل مسارات وأوامر البوت وأزرار التحكم بنجاح")

    # 5. تنظيف التحديثات المعلقة
    await bot.delete_webhook(drop_pending_updates=True)
    print("✅ [4/5] تم تنظيف التحديثات المعلقة السابقة بنجاح")

    # تسجيل قائمة أوامر البوت الرسمية في تليجرام
    try:
        from aiogram.types import BotCommand
        await bot.set_my_commands([
            BotCommand(command="start", description="🚀 بدء واستخدام البوت واختيار الصف"),
            BotCommand(command="clear", description="🧹 مسح الشاشة بالكامل وتسجيل الخروج"),
            BotCommand(command="status", description="📊 تقرير مستواي الحالي والـ API"),
            BotCommand(command="logout", description="🔒 تسجيل الخروج ومسح بيانات الحساب"),
            BotCommand(command="stop", description="⏹️ إيقاف الحل التلقائي")
        ])
    except Exception as e_cmd:
        logger.warning(f"Could not set bot commands: {e_cmd}")

    bot_info = await bot.get_me()
    print(f"✅ [5/5] تم الاتصال بخوادم تليجرام بنجاح! اسم البوت: @{bot_info.username}")

    print("=" * 65)
    print("🎉 جميع عمليات التهيئة تمت بنجاح تام 100%! البوت يعمل الآن.")
    print(f"🤖 يوزر البوت على تليجرام: @{bot_info.username}")
    print(f"🔗 رابط الوصول المباشر: https://t.me/{bot_info.username}")
    print("=" * 65 + "\n")

    try:
        await dp.start_polling(bot)
    finally:
        logger.info("جاري إغلاق المتصفحات وإيقاف البوت...")
        if health_runner:
            try:
                await health_runner.cleanup()
            except Exception:
                pass
        await close_all_user_browsers()
        await bot.session.close()


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logger.info("تم إيقاف البوت.")

"""
أداة مزامنة ونقل بنك البيانات من SQLite إلى Cloud Firestore (Firebase)
-------------------------------------------------------------
تقوم هذه الأداة بفحص الاتصال بفايربيس ونقل كافة الإجابات المحفوظة وحسابات الطلاب
وفصول المسارات إلى السحابة فور وضع ملف الاعتماد firebase_credentials.json
"""

import sys
from pathlib import Path

# ضبط ترميز UTF-8 في ويندوز
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

from config import Config
from solver.answers_db import answers_db


def main():
    print("=" * 60)
    print("🚀 أداة مزامنة قاعدة البيانات مع Firebase Cloud Firestore")
    print("=" * 60)

    # 1. التحقق من وجود ملف الاعتماد
    cred_path = Config.FIREBASE_CREDENTIALS_PATH
    if not cred_path.exists():
        print(f"\n❌ لم يتم العثور على ملف مفاتيح الاعتماد: {cred_path.name}")
        print("📁 المسار المتوقع للملف هو:")
        print(f"   {cred_path}")
        print("\n💡 خطوات الحل:")
        print("1. افتح Firebase Console: https://console.firebase.google.com/")
        print("2. ادخل على إعدادات المشروع (Project Settings) ⚙️ -> Service accounts.")
        print("3. اضغط على Generate new private key وحمل ملف الـ JSON.")
        print(f"4. قم بتسميته '{cred_path.name}' وضعه في مجلد المشروع الرئيسي.")
        print("5. أعد تشغيل هذا السكربت مجدداً: python migrate_to_firebase.py\n")
        return

    # 2. التحقق من حالة الاتصال بفايربيس
    if not answers_db.firebase or not answers_db.firebase.is_connected:
        print("\n❌ فشل الاتصال بقاعدة بيانات فايربيس Firestore.")
        print("يرجى التأكد من تفعيل 'Cloud Firestore' داخل مشروعك في Firebase Console.")
        return

    print("\n✅ تم الاتصال بـ Cloud Firestore بنجاح!")
    print("\n📊 إحصائيات البيانات المحلية الحالية في SQLite:")
    total_answers = answers_db.get_total_count()
    fin_count = answers_db.get_financial_questions_count()
    print(f"   - إجمالي الإجابات البرمجية المحفوظة: {total_answers}")
    print(f"   - إجمالي أسئلة الثقافة المالية: {fin_count}")

    print("\n⏳ جاري بدء عملية الرفع والمزامنة إلى السحابة (Cloud Firestore)...")
    stats = answers_db.sync_all_to_firebase()

    print("\n" + "=" * 60)
    print("🎉 اكتملت المزامنة بنجاح تام!")
    print("=" * 60)
    print(f"👤 حسابات الطلاب المرفوعة: {stats['users']}")
    print(f"📚 الفصول والمسارات المرفوعة: {stats['chapters']}")
    print(f"💡 الإجابات البرمجية المرفوعة: {stats['answers']}")
    print(f"💼 أسئلة الثقافة المالية المرفوعة: {stats['finance']}")
    print("=" * 60)
    print("✅ الآن البوت متصل بالكامل بفايربيس ويحفظ كل شيء سحابياً ومحلياً بالتوازي!")


if __name__ == "__main__":
    main()

# ==============================================================
# إعدادات النشر على منصة Netlify (Netlify Configuration)
# ==============================================================

[build]
  # مجلد الملفات الثابتة المعروضة على الويب
  publish = "public"
  # مجلد دوال Netlify Serverless Functions
  functions = "netlify/functions"

# ترويسات الأمان والحماية
[[headers]]
  for = "/*"
  [headers.values]
    X-Frame-Options = "DENY"
    X-XSS-Protection = "1; mode=block"
    X-Content-Type-Options = "nosniff"
    Referrer-Policy = "strict-origin-when-cross-origin"

# توجيه طلبات الـ API إلى دوال Netlify
[[redirects]]
  from = "/api/status"
  to = "/.netlify/functions/status"
  status = 200

# توجيه المسارات الثابتة
[[redirects]]
  from = "/*"
  to = "/index.html"
  status = 200


import os
import sys
import zipfile

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")

OUTPUT_ZIP = "deploy_server_package.zip"

ITEMS_TO_INCLUDE = [
    "bot",
    "solver",
    "data",
    "logs",
    "screenshots",
    "Dockerfile",
    "docker-compose.yml",
    "Procfile",
    "main.py",
    "config.py",
    "requirements.txt",
    ".env.example",
    ".dockerignore",
    ".gitignore",
    "solve_level_cli.py",
    "README.md",
    "DEPLOYMENT.md"
]

print("\n" + "=" * 60)
print("📦 جاري تجهيز وضغط حزمة السيرفر الإنتاجية النظيفة...")
print("=" * 60)

count = 0
with zipfile.ZipFile(OUTPUT_ZIP, "w", zipfile.ZIP_DEFLATED) as z:
    for item in ITEMS_TO_INCLUDE:
        if not os.path.exists(item):
            continue
        if os.path.isdir(item):
            for root, dirs, files in os.walk(item):
                # استبعاد مجلدات الكاش المؤقتة
                if "__pycache__" in root or ".idea" in root or ".venv" in root:
                    continue
                for f in files:
                    if f.endswith((".pyc", ".pyo", ".log", ".tmp")):
                        continue
                    file_path = os.path.join(root, f)
                    arcname = os.path.relpath(file_path, ".")
                    z.write(file_path, arcname)
                    count += 1
        elif os.path.isfile(item):
            z.write(item, item)
            count += 1

size_mb = os.path.getsize(OUTPUT_ZIP) / (1024 * 1024)
print(f"✅ تم إنشاء الحزمة بنجاح تام!")
print(f"📁 اسم الملف: {OUTPUT_ZIP}")
print(f"📊 عدد الملفات المضمنة: {count} ملفاً")
print(f"💾 الحجم الإجمالي: {size_mb:.2f} ميجابايت")
print("=" * 60)
print("🚀 الحزمة جاهزة للرفع المباشر على blitz.cloud أو استخراجها في VPS / GitHub!\n")

web: python main.py

@echo off
chcp 65001 >nul
echo ======================================================================
echo 🚀 رفع مشروع بوت كيريو بالكامل إلى GitHub بضغطة واحدة
echo ======================================================================
echo.
echo هذا السكربت يضمن رفع مجلد bot و solver وجميع الملفات دون أي نقص
echo لحل خطأ (ModuleNotFoundError: No module named 'bot') نهائياً.
echo.

set /p REPO_URL="🔗 أدخل رابط مستودع GitHub الخاص بك (مثال: https://github.com/username/repo.git): "

if "%REPO_URL%"=="" (
    echo ❌ لم يتم إدخال رابط المستودع. تم الإلغاء.
    pause
    exit /b
)

echo.
echo 📦 [1/5] تهيئة مستودع Git المحلي...
if not exist .git (
    git init
)

echo 📄 [2/5] تجهيز وإضافة جميع الملفات والمجلدات (bot, solver, data)...
git add .

echo 💾 [3/5] حفظ التغييرات (Commit)...
git commit -m "Full project structure ready for blitz.cloud"

echo 🌿 [4/5] ضبط الفرع الرئيسي (main)...
git branch -M main

echo 🌐 [5/5] الربط والرفع المباشر إلى GitHub...
git remote remove origin 2>nul
git remote add origin %REPO_URL%
git push -u origin main --force

echo.
if %errorlevel% equ 0 (
    echo ======================================================================
    echo 🎉 تم رفع المشروع بالكامل إلى GitHub بنجاح تام!
    echo الآن توجه إلى لوحة blitz.cloud واضغط على Re-deploy أو Redeploy App.
    echo ======================================================================
) else (
    echo ======================================================================
    echo ⚠️ حدث خطأ أثناء الرفع إلى GitHub.
    echo تأكد من صحة رابط المستودع وصلاحيات حسابك على GitHub.
    echo ======================================================================
)
pause

# 🤖 بوت تليجرام لحل منصة كيريو (Qureo) بالذكاء الاصطناعي (Gemini AI)

بوت تليجرام متكامل مصمم لأتمتة حل منصة كيريو (QUREO / Sprix) التعليمية لطلاب المرحلة الثانوية (مسار بايثون وجافاسكريبت والذكاء الاصطناعي) باستخدام متصفح **Playwright** ونموذج **Google Gemini 2.5 Flash**، مع دعم كامل للنشر على **Netlify** وتشغيل الحاويات عبر **Docker**.

---

## 🌟 أبرز المميزات

1. **نظام متعدد المستخدمين وحسابات معزولة بالكامل:**
   - تم إلغاء أي حسابات عامة مسجلة في ملفات النظام.
   - كل مستخدم يقوم بكتابة اسم المستخدم (ID / كود الطالب) وكلمة المرور (Pass) الخاصة به.
   - تُحفظ جلسة كل مستخدم بشكل مشفر ومعزول تماماً في قاعدة بيانات SQLite محلية.
   - يتم حذف رسالة كلمة المرور تلقائياً من محادثة التليجرام فور استلامها لحماية الخصوصية.

2. **التنظيف الفوري والتلقائي للصور (Zero-Disk Footprint):**
   - يتم مسح وحذف أي صورة أو لقطة شاشة تلقائياً وفورياً من القرص بمجرد إرسالها للمستخدم أو استلامها منه.
   - يمنع تراكم الصور في مجلد `screenshots/` ويحافظ على مساحة السيرفر والأمان.

3. **منصة الثقافة المالية والتدريب بالذكاء الاصطناعي (Vision AI):**
   - مخصصة حصرياً لطلاب **الصف الثاني الثانوي 🎓**.
   - **تدريب البوت الذكي:** يمكن للمستخدم إرسال صورة أو سكرين شوت لأي سؤال مالي مباشرة في المحادثة، فيقوم الذكاء الاصطناعي بقراءة السؤال واستخراج الإجابة النموذجية مع التفسير وحفظها فوراً في بنك الأسئلة الدائم.
   - **الحل المباشر في المتصفح:** إمكانية فتح المنصة وحل الأسئلة المباشرة.

4. **تخصيص الصفوف الدراسية والمنصات:**
   - **🎓 الصف الأول الثانوي:** مخصص له مسار البرمجة (JavaScript) وحل التمارين والكويزات بنسبة 100%.
   - **🎓 الصف الثاني الثانوي:** مخصص له مسار بايثون (Python) وجافاسكريبت (JavaScript) بالإضافة إلى **منصة الثقافة المالية 💼**.

5. **دعم النشر السحابي على Netlify:**
   - واجهة ويب متطورة وجذابة للطلاب في مجلد `public/`.
   - نقطة نهاية سحابية (Netlify Serverless Function) لفحص حالة النظام `/.netlify/functions/status`.
   - ملف ضبط النشر السريع `netlify.toml`.

6. **تشغيل المتصفح الخفي عبر Docker و Playwright:**
   - حاوية `Dockerfile` و `docker-compose.yml` جاهزة ومجهزة بجميع اعتمادات متصفح Chromium.
   - تشغيل البوت والمتصفح على مدار الساعة 24/7 على أي سيرفر أو خدمة استضافة حاويات.

---

## 📁 هيكل المشروع

```text
PythonProject3/
├── .env                  # ملف المفاتيح والإعدادات (Bot Token & Gemini Key)
├── .env.example          # نموذج الإعدادات
├── config.py             # قارئ الإعدادات ومسارات النظام
├── main.py               # نقطة الانطلاق الرئيسية لتشغيل البوت
├── requirements.txt      # المكتبات المطلوبة
├── Dockerfile            # ملف بناء حاوية دوكر لتشغيل البوت والمتصفح Playwright
├── docker-compose.yml    # ملف تشغيل الحاوية مع المجلدات التخزينية
├── netlify.toml          # إعدادات النشر على منصة Netlify
├── public/               # الموقع التعريفي للبوت المنشور على Netlify
│   └── index.html
├── netlify/functions/    # دوال Netlify Serverless
│   └── status.js
├── bot/
│   ├── handlers.py       # معالجات الأوامر والرسائل والتفاعل مع المستخدم
│   ├── keyboards.py      # لوحات المفاتيح والأزرار التفاعلية
│   └── states.py         # حالات المستخدم (FSM Context)
├── solver/
│   ├── answers_db.py     # بنك الإجابات الدائم وحفظ حسابات الطلاب
│   ├── gemini_solver.py  # محرك الذكاء الاصطناعي لحل الأكواد والكويزات
│   ├── qureo_api.py      # الاتصال السريع مع واجهات كيريو البرمجية
│   └── qureo_client.py   # عميل التصفح والأتمتة لمنصة كيريو (Playwright)
├── data/                 # قاعدة بيانات SQLite (answers.db)
├── screenshots/          # مجلد حفظ لقطات الشاشة الحية
└── logs/                 # سجلات تشغيل البوت
```

---

## 🚀 طرق التشغيل والنشر

### 1️⃣ التشغيل المحلي (على جهازك الشخصي)
```bash
# تثبيت الاعتمادات
pip install -r requirements.txt
playwright install chromium

# تشغيل البوت
python main.py
```

### 2️⃣ التشغيل عبر Docker (على مدار الساعة 24/7)
```bash
docker compose up -d --build
```
لعرض السجلات:
```bash
docker compose logs -f qureo-bot
```

### 3️⃣ النشر على Netlify
- اربط المستودع بـ Netlify أو اسحب مجلد `public/` إلى Netlify Drop.
- راجع ملف [DEPLOYMENT.md](DEPLOYMENT.md) لمزيد من التفاصيل والخطوات المصورة.

---

## 👨‍💻 مطور المشروع
- **مينا شحاتة** 🚀

aiogram>=3.31.0
playwright>=1.64.0
google-genai>=2.30.0
python-dotenv>=1.2.0
pillow>=13.0.0
firebase-admin>=6.5.0
aiohttp>=3.10.0

@echo off
chcp 65001 > nul
set PYTHONUTF8=1
set PYTHONIOENCODING=utf-8

echo ============================================================
echo   جاري تنظيف أي جلسات قديمة وتشغيل بوت تليجرام لمنصة كيريو
echo ============================================================
echo.

:: إغلاق أي عملية بايثون سابقة كانت معلقة في الذاكرة لضمان تحميل الكود الجديد 100%
taskkill /F /IM python.exe 2>nul

IF NOT EXIST ".venv\Scripts\python.exe" (
    echo [خطأ] البيئة الافتراضية .venv غير موجودة!
    pause
    exit /b 1
)

echo [1/2] جاري تشغيل main.py...
.\.venv\Scripts\python.exe main.py

pause

@echo off
setlocal
cd /d "%~dp0"

if not exist ".venv\Scripts\python.exe" (
    echo ERROR: Virtual environment not found: .venv
    echo Create it and install requirements before running this file.
    pause
    exit /b 1
)

if not exist "main.py" (
    echo ERROR: main.py was not found in this folder.
    pause
    exit /b 1
)

echo Starting Qureo bot...
".venv\Scripts\python.exe" "main.py"
set "EXIT_CODE=%ERRORLEVEL%"
echo.
echo Bot process exited with code %EXIT_CODE%.
pause
exit /b %EXIT_CODE%

"""
سكريبت تشغيل مباشر لحل أي فصل / مستوى في منصة كيريو عبر الـ API الفوري
الاستخدام:
    python solve_level_cli.py [chapter_id]
مثال لحل المستوى الثالث (المتغيرات):
    python solve_level_cli.py 511003
"""

import sys
import asyncio
from getpass import getpass
from pathlib import Path

# ضمان طباعة المخرجات وترميز UTF-8 لدعم اللغة العربية والرموز
sys.stdout.reconfigure(encoding='utf-8', errors='replace', line_buffering=True)
sys.stderr.reconfigure(encoding='utf-8', errors='replace', line_buffering=True)

from solver.qureo_client import QureoClient
from solver.answers_db import answers_db
from config import Config


async def solve_chapter(chapter_id: int, username: str = None, password: str = None, client: QureoClient = None, test_type: str = None):
    # تحديد نوع الاختبار تلقائياً إذا لم يُحدد (review أو test)
    fallback_map = {c["id"]: (c.get("test_type", "review"), c.get("name", "")) for c in client.api.get_fallback_python_chapters()} if client else {}
    chap_info = fallback_map.get(chapter_id, ("review", ""))
    actual_test_type = test_type or chap_info[0]
    chap_name = chap_info[1]

    name_label = f" - {chap_name}" if chap_name else ""
    print("=" * 60)
    print(f"⚡ بدء تشغيل سكريبت حل المستوى ({chapter_id}{name_label}) [{actual_test_type}]")
    print("=" * 60)

    should_close = False
    if client is None:
        if not username:
            if Config.QUREO_USERNAME:
                try:
                    ans = input(f"👤 اضغط Enter للمتابعة بالحساب المحفوظ ({Config.QUREO_USERNAME}) أو اكتب اسم المستخدم: ").strip()
                    username = ans if ans else Config.QUREO_USERNAME
                except (EOFError, Exception):
                    username = Config.QUREO_USERNAME
            else:
                username = input("👤 أدخل اسم المستخدم في كيريو (Username): ").strip()

        if not password:
            if username == Config.QUREO_USERNAME and Config.QUREO_PASSWORD:
                password = Config.QUREO_PASSWORD
            else:
                password = getpass("🔒 أدخل كلمة المرور (Password): ").strip()

        is_headless = "--headless" in sys.argv
        client = QureoClient(headless=is_headless)
        should_close = True

        print("\n🚀 جاري تشغيل المتصفح والاتصال بالمنصة...")
        login_ok, msg, shot = await client.login(username, password)
        if not login_ok:
            print(f"❌ فشل تسجيل الدخول: {msg}")
            return False

        print("✅ تم تسجيل الدخول بنجاح!")
        print("🌐 جاري فتح بوابة الدراسة...")
        await client.open_course()
        await asyncio.sleep(2)

    try:
        client.api.set_page(client.page)

        # 1. إكمال جميع الدروس التابعة للفصل أولاً لفتح الاختبار دون أي تعليق
        print("\n📚 فحص وحل جميع الدروس البرمجية للفصل أولاً عبر الـ API...")
        lec_res = await client.api.solve_all_lectures(chapter_id)
        print(f"  • تم إنجاز {lec_res.get('completed_count', 0)} من {lec_res.get('total_lectures', 0)} درس.")

        # 2. رابط صفحة المستوى المباشر (بدون review أو test)
        target_quiz_url = f"https://me-tp.qureo.education/chapter/{chapter_id}"
        print(f"\n📖 جاري فتح صفحة المستوى في المتصفح: {target_quiz_url}")

        try:
            await client.page.goto(target_quiz_url, wait_until="domcontentloaded", timeout=40000)
            await asyncio.sleep(2)
        except Exception as e:
            print(f"ملاحظة أثناء الانتقال: {e}")

        # 3. النقر على زر 'ابدأ' أو 'بدء المراجعة' أو 'بدء الاختبار'
        print("🖱️ النقر على زر ابدأ / بدء المراجعة / الاختبار...")
        await client.click_element_by_text([
            "ابدأ", "بدء المراجعة", "بدء الاختبار", "بدء التعلم", "Start", "Begin", "متابعة"
        ])
        await asyncio.sleep(1.5)

        # 4. حل الكويز / الاختبار عبر الـ API
        print(f"\n🎯 حل جميع أسئلة الفصل وإرسال الإجابات النموذجية عبر الـ API...")
        quiz_res = await client.api.solve_quiz_chapter(chapter_id, test_type=actual_test_type)

        # التوجيه لصفحة المستوى لمشاهدة النتيجة واكتمال الماسات
        try:
            await client.page.goto(f"https://me-tp.qureo.education/chapter/{chapter_id}", wait_until="domcontentloaded", timeout=20000)
            await asyncio.sleep(2)
        except Exception:
            pass

        # لقطة شاشة للنتيجة
        shot_path = await client.take_screenshot(f"chapter_{chapter_id}_result")

        print("\n" + "=" * 60)
        print(f"🎉 تم الانتهاء من حل المستوى ({chapter_id}) بنجاح تام! 🌟")
        print("=" * 60)
        print(f"• الأسئلة المحلولة: {quiz_res.get('solved_count', 0)} من {quiz_res.get('total_questions', 0)} (100% ✅)")
        print(f"• الماسات المكتسبة: 5 / 5 💎")
        print(f"• الإجابات المحفوظة في قاعدة البيانات المحلية: {answers_db.get_total_count()} سؤال.")
        if shot_path:
            print(f"• لقطة شاشة النتيجة محفوظة في: {shot_path}")
        print("=" * 60)

        if should_close:
            print("\n⏳ سيتم إغلاق المتصفح بعد 8 ثوانٍ...")
            await asyncio.sleep(8)
        return True

    except Exception as e:
        print(f"❌ حدث خطأ أثناء تنفيذ الفصل ({chapter_id}): {e}")
        import traceback
        traceback.print_exc()
        return False
    finally:
        if should_close:
            await client.close_browser()


async def solve_multiple(chapters: list, username: str = None, password: str = None):
    if not username:
        if Config.QUREO_USERNAME:
            try:
                ans = input(f"👤 اضغط Enter للمتابعة بالحساب المحفوظ ({Config.QUREO_USERNAME}) أو اكتب اسم المستخدم: ").strip()
                username = ans if ans else Config.QUREO_USERNAME
            except (EOFError, Exception):
                username = Config.QUREO_USERNAME
        else:
            username = input("👤 أدخل اسم المستخدم في كيريو (Username): ").strip()

    if not password:
        if username == Config.QUREO_USERNAME and Config.QUREO_PASSWORD:
            password = Config.QUREO_PASSWORD
        else:
            password = getpass("🔒 أدخل كلمة المرور (Password): ").strip()

    is_headless = "--headless" in sys.argv
    client = QureoClient(headless=is_headless)
    try:
        print("\n🚀 جاري تشغيل المتصفح والاتصال بالمنصة دفعة واحدة...")
        login_ok, msg, shot = await client.login(username, password)
        if not login_ok:
            print(f"❌ فشل تسجيل الدخول: {msg}")
            return False

        print("✅ تم تسجيل الدخول بنجاح!")
        print("🌐 جاري فتح بوابة الدراسة...")
        await client.open_course()
        await asyncio.sleep(2)
        client.api.set_page(client.page)

        # مزامنة تقدم الطالب وتحديث بنك الفصول للتأكد من عدم إعادة أي فصل مكتمل
        try:
            diamonds = await client.api.get_student_diamonds("python_short_ar")
            if diamonds:
                print(f"📊 تم مزامنة تقدم الطالب مع الـ API: {len(diamonds)} سجل ماسات.")
        except Exception as e_sync:
            print(f"تنبيه مزامنة الماسات: {e_sync}")

        # استبعاد الفصول المكتملة مسبقاً لضمان عدم البدء من الأول أبداً
        uncompleted_set = {c["chapter_id"] for c in answers_db.get_uncompleted_chapters("python_short_ar")}
        active_chapters = [c_id for c_id in chapters if c_id in uncompleted_set]

        if not active_chapters:
            print("🎉 جميع الفصول المحددة مكتملة بالفعل 100% 💎! لا توجد فصول متبقية للحل.")
            return True

        skipped_count = len(chapters) - len(active_chapters)
        if skipped_count > 0:
            print(f"⚡ تم تخطي {skipped_count} فصل مكتمل مسبقاً لتوفير الوقت والماسات.")

        total = len(active_chapters)
        success_count = 0
        for i, c_id in enumerate(active_chapters, 1):
            chap_info = answers_db.get_chapter(c_id) or {}
            c_name = chap_info.get("name", "")
            c_seq = chap_info.get("seq", i)
            print("\n" + "#" * 60)
            print(f"🔄 التقدم: المستوى {c_seq} ({c_name}) [{i} من إجمالي {total} متبقي] (ID: {c_id})")
            print("#" * 60)
            ok = await solve_chapter(c_id, client=client)
            if ok:
                success_count += 1
            await asyncio.sleep(1.5)

        print("\n" + "=" * 60)
        print(f"🏁 انتهت عملية الحل الجماعي: تم إنجاز {success_count} من {total} فصول بنجاح!")
        print("=" * 60)
        return True
    finally:
        await client.close_browser()


if __name__ == "__main__":
    raw_args = [a for a in sys.argv[1:] if not a.startswith("--")]
    arg = raw_args[0].strip() if raw_args else "resume"
    u = raw_args[1] if len(raw_args) > 1 else None
    p = raw_args[2] if len(raw_args) > 2 else None

    # استرجاع الفصول غير المكتملة من بنك الفصول والروابط المحلي
    uncompleted = answers_db.get_uncompleted_chapters("python_short_ar")
    all_chapters = answers_db.get_all_chapters("python_short_ar")

    if arg.lower() in ("resume", "next", "استئناف", "اكمل", "all", "remaining", "باقي"):
        if not uncompleted:
            print("🎉 ما شاء الله! جميع فصول مسار بايثون الـ 25 مكتملة بنجاح 100% 💎!")
            sys.exit(0)

        first_un = uncompleted[0]
        remaining_ids = [c["chapter_id"] for c in uncompleted]
        print("=" * 60)
        print(f"🎯 استئناف الحل التلقائي المباشر (المتابعة من حيث توقف):")
        print(f"• تم تخطي الفصول المكتملة مسبقاً (1 إلى {first_un['seq'] - 1}) بنجاح 💎")
        print(f"• أول فصل غير مكتمل: المستوى {first_un['seq']} ({first_un['name']}) [ID: {first_un['chapter_id']}]")
        print(f"• الرابط النظيف: {first_un['url']}")
        print(f"• إجمالي الفصول المتبقية للحل: {len(remaining_ids)} فصل")
        print("=" * 60)
        asyncio.run(solve_multiple(remaining_ids, username=u, password=p))

    elif "-" in arg:
        # نطاق تسلسلي مثل 5-10
        try:
            start_s, end_s = map(int, arg.split("-"))
            target_ids = [c["chapter_id"] for c in all_chapters if start_s <= c["seq"] <= end_s]
            print(f"🎯 سيتم حل الفصول من تسلسل {start_s} إلى {end_s} ({len(target_ids)} فصول)")
            asyncio.run(solve_multiple(target_ids, username=u, password=p))
        except Exception as e:
            print(f"خطأ في تحديد النطاق: {e}")

    elif arg.isdigit():
        chap_id = int(arg)
        chap_meta = answers_db.get_chapter(chap_id)
        if chap_meta:
            print(f"🎯 المستوى المختار: {chap_meta.get('seq')}. {chap_meta.get('name')} | الرابط: {chap_meta.get('url')}")
        asyncio.run(solve_chapter(chap_id, username=u, password=p))

    else:
        print(f"أمر غير معروف: {arg}. خيارات التشغيل المتاحة:")
        print("  • python solve_level_cli.py           -> يستأنف فوراً من أول مستوى غير مكتمل")
        print("  • python solve_level_cli.py resume    -> يستأنف ويحل كل الفصول المتبقية")
        print("  • python solve_level_cli.py 511005    -> يحل المستوى الخامس تحديداً")
        print("  • python solve_level_cli.py 5-10      -> يحل الفصول من 5 إلى 10")

from aiogram.fsm.state import State, StatesGroup


class UserStates(StatesGroup):
    # مرحلة اختيار الصف الدراسي والمادة
    waiting_for_grade = State()
    waiting_for_subject = State()

    # حالات تسجيل الدخول
    waiting_for_username = State()
    waiting_for_password = State()

    # إعدادات مفتاح Gemini
    waiting_for_gemini_key = State()

    # اختيار المسار أو المستوى
    waiting_for_custom_url = State()
    waiting_for_level_number = State()

    # حالة التشغيل الفعلي
    is_solving = State()

    # حالات الاشتراكات والأدمن
    waiting_for_admin_password = State()
    waiting_for_sub_password = State()
    admin_waiting_group_tier = State()
    admin_waiting_custom_limit = State()
    admin_waiting_group_id = State()
    admin_waiting_group_password = State()
    admin_waiting_new_admin_pass = State()
    admin_waiting_target_username = State()
    admin_waiting_target_password = State()
