
# python3 -m venv venv
# source venv/bin/activate
# pip install -r requirements.txt

import streamlit as st
import pandas as pd
import numpy as np
# import plotly.express as px
# import plotly.graph_objects as go
# import requests
# import json


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


st.write("---")


from itertools import chain, combinations

# Display the formula in code form
st.code("∃s⊆S:∀v∈V:D(s,v)")

# Define the sets S and V
elements = {1, 2, 3, 4, 5}
values = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

S = st.multiselect("Choose some elements of S:", elements)
V = st.multiselect("Choose some values of V:", values)

# Check if both S and V are selected and non-empty
if not S or not V:
    st.write("Изберете множества S и V")
else:

    # Define the predicate D(s, v), which checks if v is in s
    def D(s, v):
        return v in s

    st.code("def D(s, v): return v in s")
    st.write("В тази функция сме заложили предиката D(s, v), която проверява дали стойността v е в множеството s")

    # Function to find a subset of S that satisfies the conditions
    def find_subset(S, V):
        def all_subsets(S):
            return chain.from_iterable(combinations(S, r) for r in range(len(S) + 1))

        # Check if there exists a subset s of S where ∀v ∈ V, D(s, v) is true
        for s in all_subsets(S):
            if all(D(s, v) for v in V):
                return set(s)
        return None

    # Display the result
    subset = find_subset(S, V)
    if subset is not None:
        st.write(f"Резултат: Съществува подмножество s = {subset}, за което ∀v ∈ V: D(s, v) е **:green[вярно]**")
    else:
        st.write("Резултат: **:red[Няма такова подмножество]**")
