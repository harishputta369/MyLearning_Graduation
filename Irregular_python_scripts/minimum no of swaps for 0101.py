s="GGBBG"#input()
st1=s.replace('B','0')
st1=s.replace('G','1')
st=int(st1)
def countMinSwaps(st):
    min_swaps = 0
    odd_0, even_0 = 0, 0
    odd_1, even_1 = 0, 0
    n = len(st)
    for i in range(0, n):
        if i % 2 == 0:
            if st[i] == "1":
                even_1 += 1
            else:
                even_0 += 1
        else:
            if st[i] == "1":
                odd_1 += 1
            else:
                odd_0 += 1
    cnt_swaps_1 = min(even_0, odd_1)
    cnt_swaps_2 = min(even_1, odd_0)
    return min(cnt_swaps_1, cnt_swaps_2)
print(countMinSwaps(st))
#if __name__ == "__main__":
#    st = "GGBBG"
    # Function call
#    print(countMinSwaps(st))

# This code is contributed by
# ANKITRAI1
