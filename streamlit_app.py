import streamlit as st
st.write("## TDS-Graded Assignment 8")
st.write("Name: Shilpa Paul")
st.write("Roll No: 22ds2000014")
st.write("# Find the largest number among three numbers")
n1=st.number_input("Enter the first number: ")
n2=st.number_input("Enter the second number: ")
n3=st.number_input("Enter the third number: ")
if (n1>=n2) and (n1>=n3):
  st.write("# The largest number is",n1)
elif (n2>=n1) and (n2>=n3):
  st.write("# The largest number is",n2)
elif (n3>=n1) and (n3>=n2):
  st.write("# The largest number is",n3)
