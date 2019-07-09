# f = open('ssafy.txt', 'r')
# all text 전체를 불러온다 (개행문자 포함!)
# all_text = f.read()
# print(all_text)
 # f.close

# f= open('reversed_ssafy.txt', 'w')

#    # reverse_text = all_text.reverse()
#  #for i in range(4):
#    # f.write(all_text)
# f.close()

with open('ssafy.txt', 'r') as f:
    lines = f.readlines() # 각 라인을 item으로 list의 형태로 변환

lines.reverse() #list를 반대로 뒤집는다.

with open('reversed_ssafy.txt', 'w') as f:
   # rlines = reversed(lines)
    print(lines)
    for line in lines:
        f.write(line)