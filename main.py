import streamlit as st
import language_tool_python

def correct_text(text):
    tool = language_tool_python.LanguageTool('en-US')
    matches = tool.check(text)
    corrected_text = language_tool_python.utils.correct(text, matches)
    return corrected_text

def main():
    st.header("Text Grammer and Spelling Correction")
    text_area = st.text_area("Enter Your Text : ")
    if text_area is not None:
       if st.button("Submit"):
           st.write("Input text is :")
           st.success(text_area)
           out_text = correct_text(text_area)
           st.write("The Updated text is :")
           st.write(out_text)

if __name__ == '__main__':
    main()