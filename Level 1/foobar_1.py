def solution(x):
    # Your code here
    part = x.split(" ")
    reverseAlphabet = "zyxwvutsrqponmlkjihgfedcba"
    ord_a = ord('a')
    answer = ""
    for i in part:
        for j in range(0,len(i)):
            if (ord(i[j])>=ord('a') and ord(i[j])<=ord('z')):
                answer = (answer + reverseAlphabet[ord(i[j]) - ord_a])
            else:
                answer = answer+i[j]
        answer = answer + ' '

    print(answer)


if __name__ == '__main__':
    solution("Yvzs! I xzm'g yvorvev Lzmxv olhg srh qly zg gsv xlolmb!!")