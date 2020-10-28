def filter_words(st):
    st.lower()
    st = st.split()
    st = " ".join(st)
    return st.capitalize()
