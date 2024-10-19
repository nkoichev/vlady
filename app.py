
# python3 -m venv venv
# source venv/bin/activate
# pip install -r requirements.txt


import streamlit as st
def do_stuff_on_page_load():
    st.set_page_config(layout="wide", page_title="Vlady", page_icon="📊")
do_stuff_on_page_load()

import pandas as pd
import numpy as np

from streamlit_option_menu import option_menu
# import plotly.express as px
# import plotly.graph_objects as go
# import requests
# import json


# st.write("Hello, Vlady!")

# show me examples of Конюнкция, дизюнкция, отрицание

import streamlit as st


with st.sidebar:
    choose = option_menu("Hallo, Vlady!", ['Vorlesung 1','Vorlesung 2'],
                        icons=['paperclip', 'paperclip'],
                        menu_icon="calendar3", default_index=0,
                        styles={
        "container": {"padding": "0!important", "background-color": "#F0F2F6"},
        "icon": {"color": "#022fc4", "font-size": "14px"}, 
        "nav-link": {"font-size": "14px", "text-align": "left", "margin":"0px", "--hover-color": "#fff"},
        "nav-link-selected": {"background-color": "#FF4B4B"},
    }
    )

if choose == 'Vorlesung 1':

    # Title of the app
    st.title("Conjunction, Disjunction, Negation, Implication - Logical Operations")


    with st.sidebar:
        st.write("---")
        # User inputs for Boolean values
        a = st.selectbox("Choose a value for A:", [True, False])
        b = st.selectbox("Choose a value for B:", [True, False])


    # Conjunction (AND)
    conjunction = a and b
    if conjunction:
        st.success(f"Conjunction (A AND B): ", {conjunction})
    else:
        st.error(f"Conjunction (A AND B): ", {conjunction})

    # Disjunction (OR)
    disjunction = a or b
    if disjunction:
        st.success(f"Disjunction (A OR B): ", {disjunction})
    else:
        st.error(f"Disjunction (A OR B): ", {disjunction})

    # Negation (NOT)
    negation_a = not a
    negation_b = not b
    if negation_a:
        st.success(f"Negation (NOT A): ", {negation_a})
    else:
        st.error(f"Negation (NOT A): ", {negation_a})
    if negation_b:
        st.success(f"Negation (NOT B): ", {negation_b})
    else:
        st.error(f"Negation (NOT B): ", {negation_b})

    # Implication (IF THEN)
    implication = not a or b
    if implication:
        st.success(f"Implication (IF THEN): ", {implication})
    else:
        st.error(f"Implication (IF THEN): ", {implication})
    

    # Explanation section
    st.write(f"""
    - **Conjunction (AND)**: Returns True if both A and B are True
    """)
    code_conjunction = st.code("A ∧ B")
    st.write(f"""
    - **Disjunction (OR)**: Returns True if either A or B is True.
    """)
    
    code_disjunction = st.code("A ∨ B")
    st.write(f"""
    - **Negation (NOT)**: Inverts the value of A or B.
    """)
    code_negation = st.code("¬A ¬B")
    st.write(f"""
    - **Implication (IF THEN)**: Returns True if A is False or B is True.
    """)
    code_implication = st.code("A → B = ¬A ∨ B")

    st.write(f"""
                :blue[∧] represents Conjunction (AND)   
                :blue[∨] represents Disjunction (OR)  
                :blue[¬] represents Negation (NOT)  
                :blue[→] represents Implication (IF THEN)
                    """)

if choose == 'Vorlesung 2':

    st.write("Логическа форма на изразяване на зависимости между елементи и множества")
    from itertools import chain, combinations


    tab1, tab2 = st.tabs(["Logical Statement 1", "Logical Statement 2"])

    

    
    with tab1:


        # Display the formula in code form
        st.code("Логическо твърдение 1: ∃s∈S:∀v∈V:Da(s,v)")
        # EXPLAIN THE PREDICATE: ∃s⊆S:∀v∈V:Da(s,v)
        st.write("**Значение**: Съществува подмножество :blue[s] принадлежащо на множеството :blue[S], такова че за всеки елемент от подмножеството :blue[v] принадлежащо на множеството :blue[V], функцията :blue[Da(s, v)] ще бъде вярна.")

        # Define the sets S and V
        elements_s = {1, 2, 3, 4, 5}
        elements_v = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

        with st.sidebar:
            st.write("---")
            S = st.multiselect(f"Choose some elements of :blue[S]:", elements_s)
            V = st.multiselect(f"Choose some elements of :blue[V]:", elements_v)

        # Check if both S and V are selected and non-empty
        if not S or not V:
            st.write("")
        else:

            # Define the predicate D(s, v), which checks if v is in s
            def Da(s, v):
                return v in s

            # Define the second predicate Da2(s, v), which checks if v >= s (this needs to be for each element of s)
            def Da2(s, v):
                return all(v >= el for el in s)  # Ensuring that v is greater than or equal to each element in the subset s

            st.write("---")
            st.write(f"* Примерна функция 1: проверява дали съществуват **s** от множеството **S**, за които да е изпълнена функцията **Da(s, v)**, за всяко **v**. С други думи, всяко :blue[v] трябва да се съдържа в подмножеството :blue[s] и тогава правилото от функцията ще е изпълнено.")
            st.code("def Da(s, v): return v in s")
            st.write("---")
            st.write(f"* Примерна функция 2: проверява дали съществуват **s** от множеството **S**, за които да е изпълнена функцията **Da2(s, v)** за всяко **v**. С други думи, всяко :blue[v] >= всяко :blue[s] и правилото от функцията ще е изпълнено.")
            st.code("def Da2(s, v): return v >= s")
            st.write("---")

            # Function to find all unique subsets of S that satisfy the condition Da(s, v)
            def find_all_subsets(S, V, predicate):
                def all_subsets(S):
                    return chain.from_iterable(combinations(S, r) for r in range(1, len(S) + 1))  # Start from 1, no empty subsets

                valid_subsets = set()  # Use a set to store unique frozen sets (since sets are mutable)
                
                # Check all subsets and collect those that satisfy the predicate for all v in V
                for s in all_subsets(S):
                    if all(predicate(s, v) for v in V):
                        valid_subsets.add(frozenset(s))  # Use frozenset to store the subset in a hashable form
                        
                return [set(s) for s in valid_subsets]  # Convert frozensets back to normal sets for display

            # Function to filter out subsets that are strict subsets of larger valid subsets
            def filter_largest_subsets(subsets):
                largest_subsets = []
                for s in subsets:
                    if not any(s < other for other in subsets):  # Check if 's' is not a strict subset of any other set
                        largest_subsets.append(s)
                return largest_subsets

            # Use the function to find all valid subsets for Da and Da2
            valid_subsets_1 = find_all_subsets(S, V, Da)
            valid_subsets_2 = find_all_subsets(S, V, Da2)

            # Filter out the strict subsets for Da2
            largest_valid_subsets_2 = filter_largest_subsets(valid_subsets_2)

            # Display the results for the first predicate
            if valid_subsets_1:
                # st.write(f"Резултат 1: Съществуват подмножества s = {valid_subsets_1}, за които ∀v ∈ V: Da(s, v) е **:green[вярно]**")
                st.success(f"**Резултат 1**: **:green[Правилото от функцията е изпълнено!]** Съществуват подмножества s = :blue[{V}], за които :blue[∀v ∈ V: Da(s, v)] е **:green[вярно]**. С други думи, всяко :blue[v] се съдържа в съществуващи елементи от подмножеството :blue[s].")
            else:
                st.error("**Резултат 1**: **:red[Правилото от функцията не е изпълнено!]** Някой от елементите :blue[v] не се съдържа в съществуващите елементи от подмножеството :blue[s].")

            st.write("---")

            # Display the results for the second predicate (Da2) after filtering
            if largest_valid_subsets_2:
                st.success(f"**Резултат 2**: **:green[Правилото от функцията е изпълнено!]** Съществуват подмножества s = :blue[{largest_valid_subsets_2}], за които :blue[∀v ∈ V: Da2(s, v)] е **:green[вярно]**. С други думи, всяко :blue[v] e по-голямо или равно на съществуващи елементи от подмножеството :blue[s].")
            else:
                st.error("**Резултат 2**: **:red[Правилото от функцията не е изпълнено!]** Не съществува такъв елемент :blue[s], за който всеки един елемент :blue[v] да e по-голям или равен.")

    with tab2:
        # Display the formula in code form  
        st.code("Логическо твърдение 2: ∃s⊆S:D(s,v) ∧ ∀v∈V:D(s,v)")

        # EXPLAIN THE PREDICATE: ∃s⊆S: D(s, v) ∧ ∀v∈V: D(s, v)
        st.write("Under construction...")






