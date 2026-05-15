import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import random

# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="Experiential TVM Learning Lab",
    page_icon="💰",
    layout="wide"
)

# =========================================================
# HELPER FUNCTIONS
# =========================================================


def currency(x):
    return f"₹{x:,.2f}"


# =========================================================
# TITLE
# =========================================================

st.title("💰 Experiential Learning Lab: Time Value of Money")

st.markdown("""
Welcome to the experiential finance learning platform.

This app teaches:

- Future Value
- Present Value
- Annuities
- Annuity Due
- Perpetuity
- Growing Cash Flows
- Retirement Planning
- APR vs EAR
- NPV and Valuation

through:

✅ Practical financial decisions  
✅ Real-world examples  
✅ Simulations  
✅ Gamification  
✅ AI hints  
✅ Formula selection guidance  
✅ Interactive visualizations
""")

# =========================================================
# SIDEBAR
# =========================================================

menu = st.sidebar.radio(
    "Choose Feature",
    [
        "Introduction",
        "Cash Flow Visualization",
        "Future Value",
        "Present Value",
        "Regular Annuity",
        "Annuity Due",
        "Perpetuity",
        "Growing Perpetuity",
        "Growing Annuity",
        "APR vs EAR",
        "NPV and Uneven Cash Flows",
        "Retirement Planning",
        "Decision Simulator",
        "Formula Selection Assistant",
        "Gamification",
        "AI Hint System",
        "Quiz Engine",
        "Common Student Mistakes"
    ]
)

# =========================================================
# INTRODUCTION
# =========================================================

if menu == "Introduction":

    st.header("📘 Introduction to Time Value of Money")

    st.markdown("""
## Core Idea

A rupee today is worth more than a rupee tomorrow.

Why?

- Money can earn returns
- Inflation reduces purchasing power
- Future cash flows are uncertain
- Individuals prefer immediate consumption

---

## Experiential Question

Would you prefer:

- ₹10,000 today
OR
- ₹12,000 after 2 years?

This introduces:

- compounding
- discounting
- opportunity cost
- delayed gratification
""")

    st.info("""
TVM is the foundation of:

- investing
- retirement planning
- startup valuation
- fintech
- insurance
- loans
- real estate
""")

# =========================================================
# CASH FLOW VISUALIZATION
# =========================================================

elif menu == "Cash Flow Visualization":

    st.header("📊 Cash Flow Visualization")

    st.markdown("""
Visualize:

- inflows
- outflows
- annuities
- uneven cash flows
""")

    years = [0, 1, 2, 3, 4, 5]

    cashflows = []

    for i in years:
        cf = st.number_input(
            f"Cash Flow Year {i}",
            value=0.0,
            key=f"cf_{i}"
        )
        cashflows.append(cf)

    colors = [
        'green' if cf >= 0 else 'red'
        for cf in cashflows
    ]

    fig = go.Figure()

    fig.add_trace(
        go.Bar(
            x=years,
            y=cashflows,
            text=cashflows,
            textposition='outside',
            marker_color=colors
        )
    )

    fig.update_layout(
        title="Cash Flow Timeline",
        xaxis_title="Year",
        yaxis_title="Cash Flow"
    )

    st.plotly_chart(fig, use_container_width=True)

    st.info("""
Green = inflow

Red = outflow
""")

# =========================================================
# FUTURE VALUE
# =========================================================

elif menu == "Future Value":

    st.header("📈 Future Value")

    st.markdown("""
## Formula

FV = PV × (1+r)^n

---

## Real-World Examples

- SIP investments
- Mutual funds
- Fixed deposits
- Retirement investing
- Startup investing
""")

    col1, col2, col3 = st.columns(3)

    with col1:
        pv = st.number_input("Present Value", value=100000.0)

    with col2:
        r = st.number_input("Interest Rate (%)", value=10.0)

    with col3:
        n = st.number_input("Years", value=5)

    fv = pv * ((1 + r/100) ** n)

    st.success(f"Future Value = {currency(fv)}")

    st.subheader("✅ Solved Example")

    st.markdown("""
Investment:

- ₹1,00,000
- 10%
- 5 years

FV = 1,00,000 × (1.10)^5
""")

    st.info(f"Answer = {currency(100000*((1.10)**5))}")

    st.subheader("📝 Practice Problem")

    st.markdown("""
A student invests:

- ₹50,000
- at 12%
- for 8 years

Find Future Value.
""")

    if st.checkbox("Show Practice Solution"):

        ans = 50000 * ((1.12) ** 8)

        st.success(f"Answer = {currency(ans)}")

# =========================================================
# PRESENT VALUE
# =========================================================

elif menu == "Present Value":

    st.header("📉 Present Value")

    st.markdown("""
## Formula

PV = FV / (1+r)^n

---

## Real-World Examples

- salary negotiations
- startup funding
- deferred payments
- bond valuation
""")

    col1, col2, col3 = st.columns(3)

    with col1:
        fv = st.number_input("Future Value", value=500000.0)

    with col2:
        r = st.number_input("Discount Rate (%)", value=12.0)

    with col3:
        n = st.number_input("Years", value=4)

    pv = fv / ((1 + r/100) ** n)

    st.success(f"Present Value = {currency(pv)}")

    st.subheader("🧠 Practical Example")

    st.markdown("""
Company Offer:

Option A:
- ₹8 lakh today

Option B:
- ₹10 lakh after 3 years

Which is better?
""")

# =========================================================
# REGULAR ANNUITY
# =========================================================

elif menu == "Regular Annuity":

    st.header("🏦 Regular Annuity")

    st.markdown("""
## Equal Payments at END of Period

Examples:

- EMI
- pension
- loan repayment
- salary

---

## Formula

PV = C[(1-(1+r)^-n)/r]
""")

    payment = st.number_input("Payment", value=10000.0)

    r = st.number_input("Rate (%)", value=8.0)

    n = st.number_input("Periods", value=10)

    pv = payment * ((1 - (1 + r/100) ** (-n)) / (r/100))

    st.success(f"Present Value = {currency(pv)}")

# =========================================================
# ANNUITY DUE
# =========================================================

elif menu == "Annuity Due":

    st.header("🏠 Annuity Due")

    st.markdown("""
## Payments at BEGINNING of Period

Examples:

- rent
- insurance
- school fees
- subscriptions
- lease rentals

---

## Formula

PV(Annuity Due) = PV(Ordinary Annuity) × (1+r)
""")

    payment = st.number_input("Payment", value=25000.0)

    r = st.number_input("Rate (%)", value=9.0)

    n = st.number_input("Periods", value=5)

    ordinary = payment * ((1 - (1 + r/100) ** (-n)) / (r/100))

    annuity_due = ordinary * (1 + r/100)

    st.success(f"Present Value = {currency(annuity_due)}")

    st.info("Earlier cash flows are more valuable.")

# =========================================================
# PERPETUITY
# =========================================================

elif menu == "Perpetuity":

    st.header("♾️ Perpetuity")

    st.markdown("""
## Formula

PV = C/r

---

## Examples

- rental property
- scholarship fund
- preferred stock
""")

    c = st.number_input("Annual Cash Flow", value=300000.0)

    r = st.number_input("Required Return (%)", value=10.0)

    value = c / (r/100)

    st.success(f"Perpetuity Value = {currency(value)}")

# =========================================================
# GROWING PERPETUITY
# =========================================================

elif menu == "Growing Perpetuity":

    st.header("📊 Growing Perpetuity")

    st.markdown("""
## Formula

PV = C1/(r-g)
""")

    c1 = st.number_input("Next Year's Cash Flow", value=50.0)

    r = st.number_input("Required Return (%)", value=11.0)

    g = st.number_input("Growth Rate (%)", value=5.0)

    if r > g:

        value = c1 / ((r/100) - (g/100))

        st.success(f"Value = {currency(value)}")

    else:

        st.error("Required return must exceed growth rate.")

# =========================================================
# GROWING ANNUITY
# =========================================================

elif menu == "Growing Annuity":

    st.header("📈 Growing Annuity")

    st.markdown("""
## Formula

PV = [C/(r-g)] × [1-((1+g)/(1+r))^n]
""")

    c = st.number_input("First Payment", value=800000.0)

    r = st.number_input("Discount Rate (%)", value=11.0)

    g = st.number_input("Growth Rate (%)", value=7.0)

    n = st.number_input("Years", value=25)

    if r > g:

        pv = (
            (c / ((r/100) - (g/100)))
            *
            (1 - (((1 + g/100)/(1 + r/100)) ** n))
        )

        st.success(f"Present Value = {currency(pv)}")

    else:

        st.error("Discount rate must exceed growth rate.")

# =========================================================
# APR VS EAR
# =========================================================

elif menu == "APR vs EAR":

    st.header("🏦 Comparing Loan Rates: APR vs EAR")

    st.markdown("""
## Formula

EAR = (1 + APR/m)^m - 1
""")

    col1, col2 = st.columns(2)

    with col1:
        apr = st.number_input("APR (%)", value=12.0)

    with col2:
        m = st.selectbox(
            "Compounding Frequency",
            {
                "Annual": 1,
                "Semi-Annual": 2,
                "Quarterly": 4,
                "Monthly": 12,
                "Daily": 365
            }
        )

    ear = ((1 + (apr/100)/m) ** m) - 1

    st.success(f"Effective Annual Rate = {round(ear*100,2)}%")

    st.code("=EFFECT(APR,m)", language="excel")

    loanA = ((1 + 0.12/12) ** 12) - 1
    loanB = ((1 + 0.123) ** 1) - 1

    comparison = pd.DataFrame({
        "Loan": ["Loan A", "Loan B"],
        "APR": ["12%", "12.3%"],
        "Compounding": ["Monthly", "Annual"],
        "EAR": [
            f"{round(loanA*100,2)}%",
            f"{round(loanB*100,2)}%"
        ]
    })

    st.table(comparison)

# =========================================================
# NPV
# =========================================================

elif menu == "NPV and Uneven Cash Flows":

    st.header("💼 NPV and Uneven Cash Flows")

    rate = st.number_input("Discount Rate (%)", value=12.0)

    initial = st.number_input("Initial Investment", value=-500000.0)

    cf1 = st.number_input("Year 1 Cash Flow", value=100000.0)
    cf2 = st.number_input("Year 2 Cash Flow", value=200000.0)
    cf3 = st.number_input("Year 3 Cash Flow", value=300000.0)
    cf4 = st.number_input("Year 4 Cash Flow", value=400000.0)

    cashflows = [initial, cf1, cf2, cf3, cf4]

    npv = 0

    for i, cf in enumerate(cashflows):
        npv += cf / ((1 + rate/100) ** i)

    st.success(f"NPV = {currency(npv)}")

# =========================================================
# RETIREMENT PLANNING
# =========================================================

elif menu == "Retirement Planning":

    st.header("👴 Retirement Planning Simulator")

    monthly = st.number_input("Monthly Investment", value=15000.0)

    annual_return = st.number_input(
        "Expected Return (%)",
        value=12.0
    )

    years = st.number_input("Years to Retirement", value=35)

    monthly_rate = annual_return / 100 / 12

    periods = years * 12

    corpus = monthly * (
        (((1 + monthly_rate) ** periods) - 1)
        / monthly_rate
    )

    st.success(f"Estimated Retirement Corpus = {currency(corpus)}")

# =========================================================
# DECISION SIMULATOR
# =========================================================

elif menu == "Decision Simulator":

    st.header("🧠 Financial Decision Simulator")

    scenario = st.selectbox(
        "Choose Scenario",
        [
            "Buy vs Rent",
            "SIP vs FD"
        ]
    )

    if scenario == "Buy vs Rent":

        home_price = st.slider(
            "House Price",
            1000000,
            20000000,
            5000000
        )

        down_payment = st.slider(
            "Down Payment",
            100000,
            5000000,
            1000000
        )

        rate = st.slider(
            "Loan Rate (%)",
            5.0,
            15.0,
            8.5
        )

        years = st.slider(
            "Loan Years",
            5,
            30,
            20
        )

        principal = home_price - down_payment

        r = rate / 100 / 12

        n = years * 12

        emi = principal * r * ((1+r)**n) / (((1+r)**n)-1)

        total_payment = emi * n

        st.success(f"Monthly EMI = ₹{emi:,.2f}")

        st.warning(f"Total Payment = ₹{total_payment:,.2f}")

    elif scenario == "SIP vs FD":

        investment = st.slider(
            "Monthly Investment",
            1000,
            100000,
            10000
        )

        years = st.slider(
            "Years",
            1,
            40,
            20
        )

        sip_return = st.slider(
            "SIP Return (%)",
            5.0,
            20.0,
            12.0
        )

        fd_return = st.slider(
            "FD Return (%)",
            3.0,
            10.0,
            6.5
        )

        sip_r = sip_return / 100 / 12
        fd_r = fd_return / 100 / 12

        n = years * 12

        sip_fv = investment * (((1+sip_r)**n)-1) / sip_r
        fd_fv = investment * (((1+fd_r)**n)-1) / fd_r

        comparison = pd.DataFrame({
            "Investment": ["SIP", "FD"],
            "Corpus": [sip_fv, fd_fv]
        })

        st.table(comparison)

# =========================================================
# FORMULA SELECTION ASSISTANT
# =========================================================

elif menu == "Formula Selection Assistant":

    st.header("🧮 Formula Selection Assistant")

    equal = st.radio(
        "Are cash flows equal?",
        ["Yes", "No"]
    )

    if equal == "No":

        st.success("Recommended Formula: NPV / Uneven Cash Flows")

    else:

        infinite = st.radio(
            "Do cash flows continue forever?",
            ["Yes", "No"]
        )

        if infinite == "Yes":

            growth = st.radio(
                "Do cash flows grow?",
                ["Yes", "No"]
            )

            if growth == "Yes":
                st.success("Recommended Formula: Growing Perpetuity")
            else:
                st.success("Recommended Formula: Perpetuity")

        else:

            growth = st.radio(
                "Do cash flows grow over time?",
                ["Yes", "No"]
            )

            if growth == "Yes":
                st.success("Recommended Formula: Growing Annuity")
            else:

                timing = st.radio(
                    "When do payments occur?",
                    ["Beginning", "End"]
                )

                if timing == "Beginning":
                    st.success("Recommended Formula: Annuity Due")
                else:
                    st.success("Recommended Formula: Ordinary Annuity")

# =========================================================
# GAMIFICATION
# =========================================================

elif menu == "Gamification":

    st.header("🎮 Retirement Challenge")

    score = 0

    q1 = st.radio(
        "You receive ₹1 lakh bonus. What do you do?",
        [
            "Spend Entirely",
            "Invest in SIP",
            "Buy Expensive Gadget"
        ]
    )

    if q1 == "Invest in SIP":
        score += 10
        st.success("Excellent financial decision!")

    q2 = st.radio(
        "Which loan is cheaper?",
        [
            "12% compounded monthly",
            "12.3% compounded annually"
        ]
    )

    if q2 == "12.3% compounded annually":
        score += 10
        st.success("Correct! Compare EAR, not APR.")

    st.progress(score/20)

    st.metric("Financial Literacy Score", score)

    if score == 20:
        st.balloons()

# =========================================================
# AI HINT SYSTEM
# =========================================================

elif menu == "AI Hint System":

    st.header("🤖 AI Finance Hint System")

    st.markdown("""
A student deposits:

- ₹50,000 today
- 10% interest
- 5 years

Find future value.
""")

    answer = st.number_input("Enter Your Answer")

    correct = 50000 * ((1.10) ** 5)

    if st.button("Check Answer"):

        if abs(answer - correct) < 100:
            st.success("Correct Answer!")
        else:
            st.error("Incorrect. Use hints.")

    if st.checkbox("Hint 1"):
        st.info("Is money moving forward or backward in time?")

    if st.checkbox("Hint 2"):
        st.info("Money is growing over time.")

    if st.checkbox("Hint 3"):
        st.info("Use FV = PV × (1+r)^n")

    if st.checkbox("Show Full Solution"):
        st.success(f"Correct Answer = ₹{correct:,.2f}")

# =========================================================
# QUIZ ENGINE
# =========================================================

elif menu == "Quiz Engine":

    st.header("📝 Finance Quiz Engine")

    difficulty = st.selectbox(
        "Choose Difficulty",
        [
            "Beginner",
            "Intermediate"
        ]
    )

    if difficulty == "Beginner":

        pv = random.randint(10000,100000)
        r = random.randint(5,15)
        n = random.randint(1,10)

        correct = pv * ((1+r/100)**n)

        st.markdown(f"""
Calculate Future Value:

Present Value = ₹{pv}
Interest Rate = {r}%
Years = {n}
""")

        ans = st.number_input("Your Answer")

        if st.button("Submit"):

            if abs(ans - correct) < 100:
                st.success("Correct!")
                st.balloons()
            else:
                st.error(
                    f"Correct Answer = ₹{correct:,.2f}"
                )

# =========================================================
# COMMON STUDENT MISTAKES
# =========================================================

elif menu == "Common Student Mistakes":

    st.header("⚠️ Common Student Mistakes")

    mistakes = pd.DataFrame({
        "Mistake": [
            "Using 10 instead of 0.10",
            "Confusing PV and FV",
            "Ignoring payment timing",
            "Using APR instead of EAR",
            "Wrong sign convention",
            "Ignoring inflation"
        ],
        "Explanation": [
            "Convert percentage to decimal",
            "Discounting vs compounding",
            "Beginning vs end matters",
            "EAR gives actual cost",
            "Initial investment usually negative",
            "Real purchasing power changes"
        ]
    })

    st.table(mistakes)

    st.warning("""
Most finance mistakes happen because students fail to identify:

- cash flow structure
- timing
- compounding frequency
""")
