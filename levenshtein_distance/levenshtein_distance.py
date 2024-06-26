from code_le_di import distance_levenstein
from load_vocab import words
import streamlit as st
def main():
    st.title("Word Correction using Levenshtein Distance")
    input_word = st.text_input("Word: ")
    if st.button("Compute"):
        leven_distance = dict()
        for word in words:
            leven_distance[word] = distance_levenstein(word, input_word)
        sorted_distance = dict ( sorted ( leven_distance.items() , key = lambda item :item[1]) )
        true_word = list(sorted_distance.keys())[0]
        print(true_word)
        st.write("Correct word: ", true_word)
        col1 , col2 = st.columns(2)
        col1.write ("Vocabulary :")
        col1.write (words)
        col2.write ("Distances :")
        col2.write (sorted_distance)

if __name__ == "__main__":
    main()