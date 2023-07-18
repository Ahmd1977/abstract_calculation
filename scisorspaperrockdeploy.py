import random
import streamlit as st
title = st.title("SCISSORS")
choices=["rock","paper","scissors"]
while True:
    computer_choice=random.choice(choices)
    header=st.header("ENTER YOUR CHOICE")
    player=st.text_input("choose one rock paper scissors :  ")
    st.write("computer : ",computer_choice)
    st.write("player : ",player)

    if computer_choice==player:
        st.write("it is tie")
    elif player=="rock":
        if computer_choice=="scissors":
            st.write("you win") 
        elif computer_choice=="paper":
            st.write("you lose")       
    elif player=="scissors":
        if computer_choice=="paper":
            st.write("you win") 
        elif computer_choice=="rock":
            st.write("you lose")             
    elif player=="paper":
        if computer_choice=="rock":
            st.write("you win") 
        elif computer_choice=="scissors":
            st.write("you lose")
    
