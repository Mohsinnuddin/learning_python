import streamlit as st
import random as r

st.title("Number Guessing Game")

# 1. Initialize persistent session state variables
if "target_number" not in st.session_state:
    st.session_state.target_number = r.randint(1, 100)
    st.session_state.max_chances = 10
    st.session_state.game_over = False

# 2. Display remaining attempts
st.write(f"Remaining attempts: **{st.session_state.max_chances}**")

# 3. Input widget
chosen_number = st.number_input(
    label="Please Enter a number",
    min_value=1,
    max_value=100,
    step=1,
    disabled=st.session_state.game_over
)
st.caption("Number should be between 1 to 100")

# 4. Evaluation logic triggered by the button
if st.button("Submit Guess", disabled=st.session_state.game_over):
    st.session_state.max_chances -= 1

    if chosen_number == st.session_state.target_number:
        st.success(f"🎉 Correct! The number was {st.session_state.target_number}!")
        st.session_state.game_over = True
    elif st.session_state.max_chances <= 0:
        st.error(f"Game Over! You ran out of attempts. The number was {st.session_state.target_number}.")
        st.session_state.game_over = True
    elif chosen_number < st.session_state.target_number:
        st.warning("Go Higher! The number you have chosen is too small.")
    else:
        st.warning("Go Lower! The number you have chosen is too big.")

# 5. Reset button to play again
if st.session_state.game_over:
    if st.button("Play Again"):
        st.session_state.target_number = r.randint(1, 100)
        st.session_state.max_chances = 10
        st.session_state.game_over = False
        st.rerun()