def calc_let(st):
    st = st.lower()
    for i in st:
        if i not in a: 
            a[i] = 1
        else:
            a[i] += 1
a = {}
st = input("Input string ")
calc_let(st)
print(a)