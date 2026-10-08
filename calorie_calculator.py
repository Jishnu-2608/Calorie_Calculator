import streamlit as st

# ---------------------------------------------------------
# PAGE CONFIGURATION
# ---------------------------------------------------------

st.set_page_config(
    page_title="Jishnu's Calorie Calculator",
    page_icon="🔥",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# ---------------------------------------------------------
# CUSTOM CSS
# ---------------------------------------------------------

st.markdown(
    """
<style>

/* =========================================================
   REMOVE TOP WHITE SPACE
   ========================================================= */

header[data-testid="stHeader"] {
    background: transparent;
}

[data-testid="stAppViewContainer"] {
    padding-top: 0rem;
}

.main .block-container {
    padding-top: 1rem;
    padding-bottom: 2rem;
}


/* =========================================================
   MAIN BACKGROUND
   ========================================================= */

.stApp {
    background:
        radial-gradient(
            circle at 0% 15%,
            rgba(255, 82, 82, 0.18),
            transparent 28%
        ),
        radial-gradient(
            circle at 100% 18%,
            rgba(0, 188, 212, 0.18),
            transparent 30%
        ),
        radial-gradient(
            circle at 50% 55%,
            rgba(156, 39, 176, 0.10),
            transparent 32%
        ),
        radial-gradient(
            circle at 80% 95%,
            rgba(255, 193, 7, 0.13),
            transparent 28%
        ),
        linear-gradient(
            135deg,
            #fdfbff 0%,
            #f2f7ff 45%,
            #eefcff 100%
        );

    background-attachment: fixed;
}


/* =========================================================
   DECORATIVE BACKGROUND GLOW
   ========================================================= */

.stApp::before {
    content: "";
    position: fixed;

    width: 300px;
    height: 300px;

    border-radius: 50%;

    background:
        radial-gradient(
            circle,
            rgba(255, 64, 129, 0.16),
            transparent 70%
        );

    top: 7%;
    left: -130px;

    animation: backgroundGlowOne 8s ease-in-out infinite;

    pointer-events: none;
    z-index: 0;
}


.stApp::after {
    content: "";
    position: fixed;

    width: 320px;
    height: 320px;

    border-radius: 50%;

    background:
        radial-gradient(
            circle,
            rgba(0, 188, 212, 0.16),
            transparent 70%
        );

    bottom: 5%;
    right: -140px;

    animation: backgroundGlowTwo 10s ease-in-out infinite;

    pointer-events: none;
    z-index: 0;
}


@keyframes backgroundGlowOne {

    0%,
    100% {
        transform: translateY(0px) scale(1);
    }

    50% {
        transform: translateY(-25px) scale(1.12);
    }
}


@keyframes backgroundGlowTwo {

    0%,
    100% {
        transform: translateY(0px) scale(1);
    }

    50% {
        transform: translateY(25px) scale(1.10);
    }
}


/* =========================================================
   BRAND NAME
   ========================================================= */

.brand-name {
    text-align: center;

    font-size: 21px;

    font-weight: 800;

    letter-spacing: 4px;

    margin-top: 5px;
    margin-bottom: 3px;

    background:
        linear-gradient(
            90deg,
            #ff416c,
            #ff4b2b,
            #8e2de2,
            #4facfe
        );

    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;

    animation: brandAnimation 3s ease-in-out infinite;
}


@keyframes brandAnimation {

    0%,
    100% {
        opacity: 0.78;
        transform: scale(1);
    }

    50% {
        opacity: 1;
        transform: scale(1.04);
    }
}


/* =========================================================
   MAIN TITLE
   ========================================================= */

.title {
    text-align: center;

    font-size: 46px;

    font-weight: 900;

    margin-top: 0px;
    margin-bottom: 8px;

    background:
        linear-gradient(
            90deg,
            #ff416c,
            #ff4b2b,
            #9c27b0,
            #2196f3
        );

    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;

    animation: titleAnimation 4s ease-in-out infinite;
}


@keyframes titleAnimation {

    0%,
    100% {
        transform: translateY(0px);
    }

    50% {
        transform: translateY(-5px);
    }
}


/* =========================================================
   SUBTITLE
   ========================================================= */

.subtitle {
    text-align: center;

    color: #596273;

    font-size: 17px;

    margin-bottom: 35px;
}


/* =========================================================
   SECTION HEADINGS
   ========================================================= */

h2,
h3 {
    color: #303746 !important;
}


/* =========================================================
   INPUT AREA
   ========================================================= */

div[data-baseweb="input"],
div[data-baseweb="select"] {

    border-radius: 12px;

    transition:
        transform 0.2s ease,
        box-shadow 0.2s ease;
}


div[data-baseweb="input"]:focus-within,
div[data-baseweb="select"]:focus-within {

    box-shadow:
        0 0 0 2px rgba(132, 94, 247, 0.15),
        0 6px 18px rgba(132, 94, 247, 0.10);
}


/* =========================================================
   CALCULATE BUTTON
   ========================================================= */

div.stButton > button {

    width: 100%;

    height: 55px;

    border-radius: 16px;

    border: none;

    font-size: 18px;

    font-weight: 800;

    color: white;

    background:
        linear-gradient(
            90deg,
            #ff416c,
            #ff4b2b,
            #8e2de2,
            #4facfe
        );

    background-size: 250% 250%;

    box-shadow:
        0 10px 25px rgba(142, 45, 226, 0.25);

    transition:
        transform 0.25s ease,
        box-shadow 0.25s ease;

    animation: buttonGradient 5s ease infinite;
}


@keyframes buttonGradient {

    0% {
        background-position: 0% 50%;
    }

    50% {
        background-position: 100% 50%;
    }

    100% {
        background-position: 0% 50%;
    }
}


div.stButton > button:hover {

    transform:
        translateY(-4px)
        scale(1.01);

    box-shadow:
        0 15px 35px rgba(142, 45, 226, 0.35);
}


div.stButton > button:active {

    transform: scale(0.97);
}


/* =========================================================
   RESULT CARDS
   ========================================================= */

.result-box {

    padding: 25px 18px;

    border-radius: 22px;

    text-align: center;

    margin-top: 20px;
    margin-bottom: 20px;

    background:
        linear-gradient(
            145deg,
            rgba(255,255,255,0.98),
            rgba(255,247,240,0.96)
        );

    border: 1px solid rgba(255, 152, 0, 0.25);

    box-shadow:
        0 12px 35px rgba(67, 56, 202, 0.10);

    animation:
        resultAppear 0.8s ease-out;

    transition:
        transform 0.3s ease,
        box-shadow 0.3s ease;
}


.result-box:hover {

    transform:
        translateY(-8px)
        scale(1.02);

    box-shadow:
        0 20px 40px rgba(67, 56, 202, 0.16);
}


@keyframes resultAppear {

    0% {
        opacity: 0;

        transform:
            translateY(25px)
            scale(0.94);
    }

    100% {
        opacity: 1;

        transform:
            translateY(0)
            scale(1);
    }
}


/* =========================================================
   RESULT LABEL
   ========================================================= */

.result-label {

    font-size: 17px;

    color: #555b66;

    font-weight: 600;
}


/* =========================================================
   RESULT NUMBER
   ========================================================= */

.result-number {

    font-size: 40px;

    font-weight: 900;

    margin: 6px 0;

    background:
        linear-gradient(
            90deg,
            #ff416c,
            #8e2de2,
            #2196f3
        );

    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}


/* =========================================================
   INFORMATION CARD
   ========================================================= */

.info-box {

    padding: 22px;

    border-radius: 18px;

    background:
        linear-gradient(
            135deg,
            rgba(255,255,255,0.96),
            rgba(246,243,255,0.96)
        );

    border-left:
        5px solid #8e2de2;

    box-shadow:
        0 10px 30px rgba(67, 56, 202, 0.08);

    animation:
        fadeUp 0.8s ease-out;
}


@keyframes fadeUp {

    from {
        opacity: 0;
        transform: translateY(15px);
    }

    to {
        opacity: 1;
        transform: translateY(0);
    }
}


/* =========================================================
   SUCCESS MESSAGE
   ========================================================= */

div[data-testid="stAlert"] {

    border-radius: 14px;
}


/* =========================================================
   FOOTER
   ========================================================= */

.footer {

    text-align: center;

    color: #777f8f;

    font-size: 13px;

    margin-top: 35px;

    padding-bottom: 15px;
}

</style>
""",
    unsafe_allow_html=True
)

# ---------------------------------------------------------
# HEADER
# ---------------------------------------------------------

st.markdown(
    '<div class="brand-name">JISHNU\'S</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="title">🔥 Calorie Calculator</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Estimate your daily calorie requirement based on your '
    'personal and activity details.'
    '</div>',
    unsafe_allow_html=True
)

# ---------------------------------------------------------
# PERSONAL DETAILS
# ---------------------------------------------------------

st.subheader("👤 Personal Details")

col1, col2 = st.columns(2)

with col1:

    age = st.number_input(
        "Age",
        min_value=1,
        max_value=120,
        value=21,
        step=1
    )

with col2:

    gender = st.selectbox(
        "Gender",
        ["Male", "Female"]
    )


col3, col4 = st.columns(2)

with col3:

    weight = st.number_input(
        "Weight (kg)",
        min_value=1.0,
        max_value=500.0,
        value=60.0,
        step=0.1
    )

with col4:

    height = st.number_input(
        "Height (cm)",
        min_value=50.0,
        max_value=250.0,
        value=165.0,
        step=0.1
    )

# ---------------------------------------------------------
# ACTIVITY DETAILS
# ---------------------------------------------------------

st.subheader("🏃 Activity Level")

activity_options = {
    "Sedentary — little or no exercise": 1.2,
    "Lightly active — exercise 1–3 days/week": 1.375,
    "Moderately active — exercise 3–5 days/week": 1.55,
    "Very active — exercise 6–7 days/week": 1.725,
    "Extremely active — very hard exercise/physical job": 1.9
}

activity = st.selectbox(
    "Select your typical activity level",
    list(activity_options.keys())
)

# ---------------------------------------------------------
# CALCULATE BUTTON
# ---------------------------------------------------------

st.write("")

calculate = st.button(
    "🔥 Calculate My Calories"
)

# ---------------------------------------------------------
# CALCULATION
# ---------------------------------------------------------

if calculate:

    if age <= 0 or weight <= 0 or height <= 0:

        st.error(
            "Please enter valid values for age, weight, and height."
        )

    else:

        # -------------------------------------------------
        # Mifflin-St Jeor Equation
        # -------------------------------------------------

        if gender == "Male":

            bmr = (
                (10 * weight)
                + (6.25 * height)
                - (5 * age)
                + 5
            )

        else:

            bmr = (
                (10 * weight)
                + (6.25 * height)
                - (5 * age)
                - 161
            )

        # -------------------------------------------------
        # ACTIVITY CALCULATION
        # -------------------------------------------------

        activity_factor = activity_options[activity]

        tdee = bmr * activity_factor

        # -------------------------------------------------
        # DISPLAY VALUES
        # -------------------------------------------------

        bmr_display = round(bmr)

        calorie_display = round(tdee)

        # -------------------------------------------------
        # BALLOON CELEBRATION
        # -------------------------------------------------

        st.balloons()

        # -------------------------------------------------
        # SUCCESS MESSAGE
        # -------------------------------------------------

        st.success(
            "🎉 Your calorie estimate has been calculated!"
        )

        # -------------------------------------------------
        # RESULT CARDS
        # -------------------------------------------------

        col1, col2 = st.columns(2)

        with col1:

            bmr_card = (
                '<div class="result-box">'
                '<div class="result-label">'
                '⚡ Estimated BMR'
                '</div>'
                f'<div class="result-number">'
                f'{bmr_display}'
                '</div>'
                '<div class="result-label">'
                'kcal/day'
                '</div>'
                '</div>'
            )

            st.markdown(
                bmr_card,
                unsafe_allow_html=True
            )

        with col2:

            calorie_card = (
                '<div class="result-box">'
                '<div class="result-label">'
                '🔥 Estimated Daily Calories'
                '</div>'
                f'<div class="result-number">'
                f'{calorie_display}'
                '</div>'
                '<div class="result-label">'
                'kcal/day'
                '</div>'
                '</div>'
            )

            st.markdown(
                calorie_card,
                unsafe_allow_html=True
            )

        # -------------------------------------------------
        # INTERPRETATION
        # -------------------------------------------------

        st.subheader(
            "💡 What does this mean?"
        )

        info_card = (
            '<div class="info-box">'
            '<b>Estimated daily calorie requirement:</b> '
            f'approximately <b>{calorie_display} kcal/day</b>.'
            '<br><br>'
            'This estimate represents the approximate amount of '
            'energy your body may use in a typical day based on '
            'the information you provided and your selected '
            'activity level.'
            '</div>'
        )

        st.markdown(
            info_card,
            unsafe_allow_html=True
        )

        st.info(
            "Your actual calorie needs can vary because of factors "
            "such as body composition, health conditions, exercise "
            "intensity, and other individual differences."
        )

# ---------------------------------------------------------
# FOOTER
# ---------------------------------------------------------

st.markdown(
    '<div class="footer">'
    "Jishnu's Calorie Calculator • Built with Python & Streamlit"
    '<br>'
    'For general informational purposes only.'
    '</div>',
    unsafe_allow_html=True
)
