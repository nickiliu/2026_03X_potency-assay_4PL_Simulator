import numpy as np
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


# =====================
# 4PL Model
# =====================

def fourpl(x, bottom, top, logEC50, hill):

    return bottom + (
        (top - bottom)
        /
        (1 + 10 ** ((logEC50 - x) * hill))
    )


# =====================
# Fixed X
# =====================

x = np.array([
    0,
    4,
    4.477121255,
    5,
    5.477121255,
    6
])

# =====================
# UI
# =====================

st.title("4PL Interactive Simulator")

y_4477 = st.slider(
    "Y @ Log10=4.4771",
    min_value=5.51,
    max_value=18.13,
    value=11.00,
    step=0.01
)

y_6 = st.slider(
    "Y @ Log10=6",
    min_value=25.12,
    max_value=60.00,
    value=28.00,
    step=0.01
)

# =====================
# Fixed Y
# =====================

y = np.array([
    0.00,
    5.51,
    y_4477,
    18.13,
    25.12,
    y_6
])

# =====================
# Fitting
# =====================

try:

    p0 = [
        min(y),
        max(y),
        4.8,
        1
    ]

    params, _ = curve_fit(
        fourpl,
        x,
        y,
        p0=p0,
        maxfev=100000
    )

    bottom, top, logEC50, hill = params

    EC50 = 10**logEC50

    y_pred = fourpl(x, *params)

    ss_res = np.sum((y - y_pred)**2)

    ss_tot = np.sum(
        (y - np.mean(y))**2
    )

    r2 = 1 - ss_res / ss_tot

    # =====================
    # Parameters
    # =====================

    st.subheader("4PL Parameters")

    st.write(
        f"Bottom = {bottom:.4f}"
    )

    st.write(
        f"Top = {top:.4f}"
    )

    st.write(
        f"LogEC50 = {logEC50:.4f}"
    )

    st.write(
        f"EC50 = {EC50:.2f}"
    )

    st.write(
        f"HillSlope = {hill:.4f}"
    )

    st.write(
        f"R² = {r2:.4f}"
    )

    # =====================
    # Curve
    # =====================

    x_fit = np.linspace(
        0,
        10,
        500
    )

    y_fit = fourpl(
        x_fit,
        *params
    )

    fig, ax = plt.subplots(
        figsize=(8,5)
    )

    ax.plot(
        x_fit,
        y_fit,
        color="blue",
        linewidth=2,
        label="4PL Fit"
    )

    ax.scatter(
        x,
        y,
        color="red",
        s=80,
        label="Data"
    )

    ax.set_xlim(0,10)

    ax.set_xlabel(
        "Log10"
    )

    ax.set_ylabel(
        "Dopamine (pg/uL)"
    )

    ax.legend()

    ax.grid(True)

    st.pyplot(fig)

    # =====================
    # Data Table
    # =====================

    df = pd.DataFrame({
        "Log10": x,
        "Dopamine": y
    })

    st.dataframe(df)

except Exception as e:

    st.error(
        f"Fit failed: {e}"
    )