import streamlit as st

num1  = st.number_input('Enter num1')
num2 = st.number_input('Enter num2')


symbol = st.radio("Click one of the mathematical calculation symbols",
                  ('Addition', 'Subtraction', 'Multiplying', 'Division'))
if symbol == 'Addition':
    st.write('The answer is', num1 + num2)
    
elif symbol == 'Subtraction':
    st.write('The answer is', num1 - num2)
    
elif symbol == 'Multiplying':
    st.write('The answer is', num1 * num2)
    
else:
    st.write('The answer is', num1 / num2)
