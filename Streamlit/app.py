import streamlit as st
import random as r


st.title("Guess the number")

if "target_number" not in st.session_state:
    st.session_state.target_number =  r.randint(1,100)
    st.session_state.maximum_chances = 10
    st.session_state.gameOver = False
    st.session_state.guesses = []

choosenNumber = st.number_input(label = 'Please enter your Number',
                                max_value= 100,
                                step = 1 ,min_value = 1,
                                disabled = st.session_state.gameOver)


seen = False

for i in range(len(st.session_state.guesses)):
    if st.session_state.guesses[i] == choosenNumber:
        seen = True

if st.button("Submit Guess",disabled=st.session_state.gameOver) and seen == False:
    st.session_state.maximum_chances -= 1
    st.session_state.guesses.append(choosenNumber)


    if choosenNumber == st.session_state.target_number:
        st.success(f"You Guessed it right.You are genius.The number was {choosenNumber}")
        st.session_state.gameOver = True
    elif st.session_state.maximum_chances <= 0:
        st.error(f"Sorry! you lost.Gameover you nooooooob ❌. The number was {st.session_state.target_number}")
        st.session_state.gameOver = True
    elif choosenNumber > st.session_state.target_number:
        st.warning(f"Go lower than {choosenNumber}. You noob 🤙")
        st.warning(f"{st.session_state.maximum_chances} are remaining. Think wisely")
    else:
        st.warning(f"Go Higher than {choosenNumber}. You noob 🤙")
        st.warning(f"{st.session_state.maximum_chances} are remaining. Think wisely")

if seen == True:
    st.warning(f"{choosenNumber} was already guessed."
               "Please try different number and never repeat these silly mistakes."
               f" {st.session_state.maximum_chances} are remaining. Think wisely")
    seen = False

if st.session_state.gameOver == True: 
    if st.button("Play again"):
        st.session_state.target_number =  r.randint(1,100)
        st.session_state.maximum_chances = 10
        st.session_state.gameOver = False
        st.session_state.guesses = []
        st.rerun()