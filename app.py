
# python3 -m venv venv
# source venv/bin/activate
# pip install -r requirements.txt

import streamlit as st
import pandas as pd
import numpy as np
from streamlit_option_menu import option_menu
# import plotly.express as px
# import plotly.graph_objects as go
# import requests
# import json


st.write("Hello, Vlady!")

# show me examples of Конюнкция, дизюнкция, отрицание

import streamlit as st


with st.sidebar:
    choose = option_menu("", ['Лекция 1','Лекция 2'],
                        icons=['paperclip', 'paperclip'],
                        menu_icon="calendar3", default_index=0,
                        styles={
        "container": {"padding": "0!important", "background-color": "#F0F2F6"},
        "icon": {"color": "#022fc4", "font-size": "14px"}, 
        "nav-link": {"font-size": "14px", "text-align": "left", "margin":"0px", "--hover-color": "#fff"},
        "nav-link-selected": {"background-color": "#FF4B4B"},
    }
    )

if choose == 'Лекция 1':

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

if choose == 'Лекция 2':



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
        st.write("Тази функция 'def D(s, v): return v in s', проверява дали стойността v е в множеството s")

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


    st.write("---")



    # Define the sets S and V
    elements = {1, 2, 3, 4, 5}
    values = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

    # S = st.multiselect("Choose some elements of S:", elements)
    # V = st.multiselect("Choose some values of V:", values)

    # Check if both S and V are selected and non-empty
    if not S or not V:
        st.write("Изберете множества S и V")
    else:

        # Define the predicate D(s, v), which checks if s is greater than or equal to v
        def D(s, v):
            return s >= v

        st.code("def D(s, v): return s >= v")
        st.write("Тази функция 'def D(s, v): return s >= v', проверява дали s е по-голямо или равно на v")

        # Function to check if for every v in V, there exists an s in S where D(s, v) is true
        def find_s_for_all_v(S, V):
            for v in V:
                if not any(D(s, v) for s in S):
                    return False
            return True

        # Display the result
        if find_s_for_all_v(S, V):
            st.write("Резултат: За всяко v ∈ V, съществува s ∈ S, за което D(s, v) е **:green[вярно]**")
        else:
            st.write("Резултат: **:red[Няма такова s за всички v]**")


        st.write("---")


