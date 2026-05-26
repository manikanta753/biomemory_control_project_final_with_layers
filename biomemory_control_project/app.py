
from PIL import Image
import streamlit as st
import matplotlib.pyplot as plt

from dna_storage import package_data, dna_to_text, verify_decoded_text
from cell_simulation import simulate_cell_divisions
from detector import classify_growth, recommended_response

st.set_page_config(
    page_title="BioMemory-Control",
    page_icon="🧬",
    layout="wide"
)

st.title("🧬 BioMemory-Control")
st.subheader("Artificial DNA Data Storage + Cancer-like Growth Detection Simulation")

image = Image.open("architecture.png")
st.image(image, caption="BioMemory-Control Architecture", use_container_width=True)

st.warning(
    "This is a safe software simulation only. It is not a biological protocol, "
    "gene-editing method, or medical tool."
)

with st.sidebar:
    st.header("Simulation Settings")

    input_text = st.text_area(
        "Enter digital data to store in artificial DNA",
        value="BIO MEMORY CONTROL SYSTEM"
    )

    divisions = st.slider("Number of simulated cell divisions", 1, 50, 15)
    mutation_rate = st.slider("Mutation probability per DNA base", 0.0, 0.30, 0.04, 0.01)
    division_rate = st.slider("Simulated division rate", 1.0, 10.0, 4.0, 0.5)
    abnormal_marker = st.checkbox("Abnormal cancer-like marker present", value=False)
    growth_multiplier = st.slider("Growth multiplier", 1.0, 3.0, 1.4, 0.1)

package = package_data(input_text)
dna = package["dna_sequence"]

col1, col2 = st.columns(2)

with col1:
    st.header("1. DNA Data Storage")
    st.write("Original Text:")
    st.code(package["original_text"])

    st.write("Encoded Artificial DNA:")
    st.code(dna[:300] + ("..." if len(dna) > 300 else ""))

    st.metric("DNA Length", package["dna_length"])
    st.metric("Checksum", package["checksum"])

    try:
        decoded_text = dna_to_text(dna)
        verified = verify_decoded_text(decoded_text, package["checksum"])
        st.write("Decoded Text:")
        st.code(decoded_text)
        st.success("Checksum verified" if verified else "Checksum failed")
    except Exception as error:
        st.error(str(error))

with col2:
    st.header("2. Cell Division Simulation")

    df = simulate_cell_divisions(
        initial_dna=dna,
        divisions=divisions,
        mutation_rate=mutation_rate,
        growth_multiplier=growth_multiplier
    )

    st.dataframe(df[[
        "division",
        "cell_count",
        "new_mutations",
        "total_mutations",
        "observed_mutation_rate"
    ]])

latest_mutation_rate = float(df["observed_mutation_rate"].iloc[-1]) if not df.empty else 0.0

status, reason = classify_growth(
    observed_mutation_rate=latest_mutation_rate,
    division_rate=division_rate,
    abnormal_marker=abnormal_marker
)

st.header("3. Growth Risk Detection")

risk_col1, risk_col2, risk_col3 = st.columns(3)

risk_col1.metric("Final Mutation Rate", round(latest_mutation_rate, 4))
risk_col2.metric("Division Rate", division_rate)
risk_col3.metric("Abnormal Marker", "Yes" if abnormal_marker else "No")

if status == "Cancer-like Growth Detected":
    st.error(status)
elif status == "Warning":
    st.warning(status)
else:
    st.success(status)

st.write(reason)
st.info(recommended_response(status))

st.header("4. Graphs")

fig1, ax1 = plt.subplots()
ax1.plot(df["division"], df["observed_mutation_rate"], marker="o")
ax1.set_xlabel("Division")
ax1.set_ylabel("Observed Mutation Rate")
ax1.set_title("Mutation Rate Across Cell Divisions")
st.pyplot(fig1)

fig2, ax2 = plt.subplots()
ax2.plot(df["division"], df["cell_count"], marker="o")
ax2.set_xlabel("Division")
ax2.set_ylabel("Simulated Cell Count")
ax2.set_title("Cell Growth Across Divisions")
st.pyplot(fig2)

st.header("5. System Architecture")

st.code(
'''
Digital Data
   ↓
DNA Encoder
   ↓
Artificial DNA Storage
   ↓
Mutation + Cell Division Simulator
   ↓
Cancer-like Signal Detector
   ↓
Decision Output
'''
)
