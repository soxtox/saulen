def solution(set1: str, set2: str) -> List[str]:
    ans = []
    set1 = set1.lower()
    set2 = set2.lower()
    if len(set1) >= 0 and len(set2) <= 200:
        I1 = set1.strip()
        I2 = set2.strip()
        sent1 = I1.split()
        sent2 = I2.split()
        for word in sent1:
            if word in sent2:
                pass
            else:
                ans.append(word)
        for word in sent2:
            if word in sent1:
                pass
            else:
                ans.append(word)
    return ans




if __name__ == '__main__':
    a = input()
    b = input()
    output = solution(a, b)
    output.sort()
    if output == []:
        print('[]')
    else:
        print('["%s"]'% ' ","'.join(map(str, output)))