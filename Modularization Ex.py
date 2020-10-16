#1
def sample(*args):
    x = print(list(args)) #list
    y = print(args) #tuple
    return x,y

sample(3,5,7,23)

#2
def translate(text):
    trans = ''
    for i in text:
        if i not in('aeiou '):
            trans += i + 'o' + i
        else:
            trans += i
    return trans

x = translate('this is fun')
print(x)

#3
import calendar

def calendar_month(theyear, themonth, w=0, l=0):
    x = calendar.TextCalendar()
    y = x.formatmonth(theyear, themonth, w=0, l=0)
    return y
print(calendar_month(2012, 10, 5, 2))

#4
def is_member(x,a):
    for i in a:
        if i == x:
            return True
        else:
            return False

print( is_member(3,[1,2]))

#5
def overlapping(lst1,lst2):
    for i in lst1:
        for j in lst2:
            if i == j:
                return True
            else:
                return False

#6
def hisotgram(lst):
    star = '*'
    for i in lst:
        x = i * star
        print(x)

hisotgram([4,9,7])

#7
def list_of_word(list):
    length = []
    for i in range(len(list)):
        length.append(len(list[i]))
    return length


#8

def find_longest_word(lwords):
    length = []
    for i in lwords:
        length.append((len(i), i)) #make a tuple of words from list
    length.sort()   #sort the tuple
    return length[-1][1]    #last data has to be the largest

#9
def filter_long_words(lwords, n):
    length = []
    for i in range(len(lwords)):
        if len(lwords[i]) > n:
            length.append(lwords[i])
    return length

#10
def check_if_pangram(word):
    alphabet = 'qwertyuiopasdfghjklzxcvbnm '
    for word in alphabet:
        if word not in alphabet:
            return False
    return True

#11
def char_freq(string):
    freq = {}
    for i in string:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
    return freq

print(char_freq('aaaa'))

#12
def make_forms(verb):
    for i in verb:
        if i.endswith('y'):
            result = i.replace(i[-1], 'ies')
            # return result
        elif i.endswith(('o', 'cs', 's', 'sh', 'z')):
            result = i + 'es'
            # return result
        else:
            result = i + 's'
        print(result)
make_forms(['try', 'brush', 'run', 'fix'])

#13
def make_forming(verb):
    for i in verb:
        if i.endswith('e') and not i.endswith('ie'):
            result = i.replace(i[-1], 'ing')
        elif i.endswith('ie'):
            result = i.replace(i[-2:], 'y') + 'ing'
    print(result)

make_forming(['lie'])
