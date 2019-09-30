def tokenize(trg, N=1):
    words = trg.split()
    li = []
    
    for i in range(len(words) - N + 1):
        line = ''
        for j in range(N):
            line += words[i+j]
            if N > 1 and not(j == N - 1):
                line += " "
        li.append(line)
    return li
    
def main():
    a="There was a farmer who had a dog ."
    print(tokenize(a))
    print(tokenize(a, 2))

if __name__ == "__main__":
    main()