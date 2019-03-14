import requests
import random
# 获取
def GetRandomGreeting():
    res = requests.get("http://www.xjihe.com/api/life/greetings?festival=新年&page=10", headers = {'apiKey':'sQS2ylErlfm9Ao2oNPqw6TqMYbJjbs4g'})
    results = res.json()['result']
    return results[random.randrange(len(results))]['words']

# 根据开头词获取四字
def GetFourWords(word,n):
    for i in range(n):
        print('获得的字为:' + word)
        try:
            res = requests.get("http://www.xjihe.com/api/edu/chinese/term?term=" + word + "&page=4", headers = {'apiKey':'sQS2ylErlfm9Ao2oNPqw6TqMYbJjbs4g'}, timeout=1)
        except:
            print('超时')
            break
        results = res.json()['result']
        b = 'a'
        l = 0
        while (b[0]!=word) :
            if(len(results)==0):
                break
            b = results[random.randrange(len(results))]['term']
            l += 1
            if (l == len(results)*100):
                print('找不到匹配，下一次\n')
                break
        print(b)
        if(b=='a'):
            break
        word = GetLastWord(b)
        

def GetLastWord(word):
    # print(word + '的最后一个字为' + word[-1])
    return word[-1]

GetFourWords('海',10)