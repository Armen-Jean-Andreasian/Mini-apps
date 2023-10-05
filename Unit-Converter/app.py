"""
pip install streamlit
"""

import streamlit as st
from script import ConversionTool


class MetricShifter:
    def __init__(self):
        self.options = ["Millimeter (mm)", "Centimeter (cm)", "Decimeter (dm)", "Meter (m)",
                        "Decameter (dam)", "Hectometer (hm)", "Kilometer (km)","Inch (in)",
                        "Foot (ft)", "Yard (yd)", "Mile (mi)"]

    def switcher(self):
        with st.expander("Unit Converter"):
            st.subheader("Convert Different Units of Measurement")
            st.write("")
            st.write("")

            col1, col2, col3, col4 = st.columns(4)

            with col1:
                st.number_input(label="Enter a value", key="num1")

            with col2:
                unit1 = st.selectbox(label="Select Input Unit", options=self.options, key="i_u")

            with col3:
                unit2 = st.selectbox(label="Select Output Unit", options=self.options, key="o_u")

            with col4:
                st.write("")
                st.write("")
                button = st.button(label="Calculate!", key="button")

            if button:
                number1 = st.session_state['num1']

                if unit1 != unit2:
                    oper_instance = ConversionTool()
                    result = oper_instance.calculating(number=number1, local_input_unit=unit1, local_output_unit=unit2)
                    # styling
                    result_text = f"<div style='font-size: 24px; color: white;'>Result: {result}</div>"
                    st.markdown(result_text, unsafe_allow_html=True)
                else:
                    st.error(f"{unit1} is equal to {unit2}. Choose another unit.")
