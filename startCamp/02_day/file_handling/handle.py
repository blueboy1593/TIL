import os

os.chdir(r'C:\Users\student\TIL\startCamp\02_day') #500개의 지원서가 있는 곳으로 이동

filenames = os.listdir('.')
for filename in filenames:
    # 확장자가 .txt인 파일만 이름을 바꾼다.
    extension = os.path.splitext(filename)[-1] # 확장자만 따로 분리
    if extension == '.txt':
        
       # os.rename(filename,f"Samsung_{filename}")
        os.rename(filename, filename.replace("SAFFY_","SSAFY_")) #첫번째 인자로 넘어간 이름을, 두번쨰 인자로 넘어간 이름으로 바꾼다.
