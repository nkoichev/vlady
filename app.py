import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import requests
import json


st.write("Hello, Vlady!")

# show me examples of Конюнкция, дизюнкция, отрицание

import streamlit as st

# Title of the app
st.title("Conjunction, Disjunction, Negation - Logical Operations")

# User inputs for Boolean values
a = st.selectbox("Choose a value for A:", [True, False])
b = st.selectbox("Choose a value for B:", [True, False])

# Conjunction (AND)
conjunction = a and b
st.write("Conjunction (A AND B): ", conjunction)

# Disjunction (OR)
disjunction = a or b
st.write("Disjunction (A OR B): ", disjunction)

# Negation (NOT)
negation_a = not a
negation_b = not b
st.write("Negation (NOT A): ", negation_a)
st.write("Negation (NOT B): ", negation_b)

# Explanation section
st.write("""
### Explanation:
- **Conjunction (AND)**: Returns True if both A and B are True.
- **Disjunction (OR)**: Returns True if either A or B is True.
- **Negation (NOT)**: Inverts the value of A or B.
""")


