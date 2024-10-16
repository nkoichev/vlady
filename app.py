
# python3 -m venv venv
# source venv/bin/activate
# pip install -r requirements.txt

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


st.write("---")

st.code("∃s⊆S:∀v∈V:D(s,v)")

# Дефинираме множествата S и V
elements = {1, 2, 3, 4, 5}
values = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

S = st.multiselect("Choose some elements of S:", elements)
V = st.multiselect("Choose some values of V:", values)


# Дефинираме предиката D(s, v), който проверява дали v е в s
def D(s, v):
    return v in s


st.code("def D(s, v): return v in s")
st.write("В тази функция сме заложили предиката D(s, v), която проверява дали стойността v е в множеството s")

# Проверяваме дали съществува подмножество s от S, което удовлетворява условията
def find_subset(S, V):
    # Намираме всички подмножества на S
    from itertools import chain, combinations
    
    def all_subsets(S):
        return chain.from_iterable(combinations(S, r) for r in range(len(S)+1))

    for s in all_subsets(S):
        # Проверяваме дали за всяко v от V, D(s, v) е вярно
        if all(D(s, v) for v in V):
            return set(s)
    return None

# Извеждаме резултата
subset = find_subset(S, V)
if subset is not None:
    st.write(f"Резултат: Съществува подмножество s = {subset}, за което ∀v ∈ V: D(s, v) е **:green[вярно]**")
else:
    st.write("Резултат: **:red[Няма такова подмножество]**")
