import streamlit as st

st.markdown("<h1 style='text-align: center; color: #4CAF50;'>🧮 Arithmetic Calculator</h1>", unsafe_allow_html=True)

if 'display' not in st.session_state:
    st.session_state.display = ""

# Editable display/input box (used for both keyboard and button input)
st.markdown("### Result:")
st.session_state.display = st.text_input(
    label="",
    value=st.session_state.display,
    key="main_input",
    label_visibility="collapsed",
    placeholder="0",
)

# Functions (unchanged)
def update_display(value):
    st.session_state.display += str(value)

def calculate_result():
    try:
        result = eval(st.session_state.display)
        st.session_state.display = str(result)
    except:
        st.session_state.display = "Error"

def clear_display():
    st.session_state.display = ""

st.markdown("---")

# Button layout
col1, col2, col3, col4 = st.columns(4)
col5, col6, col7, col8 = st.columns(4)
col9, col10, col11, col12 = st.columns(4)
col13, col14, col15, col16 = st.columns(4)

with col1:
    st.button("7", on_click=update_display, args=(7,))
with col2:
    st.button("8", on_click=update_display, args=(8,))
with col3:
    st.button("9", on_click=update_display, args=(9,))
with col4:
    st.button("/", on_click=update_display, args=("/",))

with col5:
    st.button("4", on_click=update_display, args=(4,))
with col6:
    st.button("5", on_click=update_display, args=(5,))
with col7:
    st.button("6", on_click=update_display, args=(6,))
with col8:
    st.button("*\u00A0", on_click=update_display, args=("*",))

with col9:
    st.button("1", on_click=update_display, args=(1,))
with col10:
    st.button("2", on_click=update_display, args=(2,))
with col11:
    st.button("3", on_click=update_display, args=(3,))
with col12:
    st.button("-\u00A0", on_click=update_display, args=("-",))

with col13:
    st.button("0", on_click=update_display, args=(0,))
with col14:
    st.button(".", on_click=update_display, args=(".",))
with col15:
    st.button("C", on_click=clear_display)
with col16:
    st.button("+\u00A0", on_click=update_display, args=("+",))

st.markdown("###")
st.button("=  Calculate", on_click=calculate_result)
