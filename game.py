import random


def rock_cissor_paper(result, selection):

    if result == '가위':
        if selection == '가위':
            print('비겼습니다.')
        if selection == '바위':
            print('이겼습니다.')
        if selection =='보':
            print('졌습니다.')
    elif result == '바위':
        if selection == '가위':
            print('졌습니다.')
        if selection == '바위':
            print('비겼습니다.')
        if selection == '보':
            print('이겼습니다.')
    elif result == '보':
        if selection == '가위':
            print('이겼습니다.')
        if selection == '바위':
            print('졌습니다.')
        if selection == '보':
            print('비겼습니다.')

if __name__ == '__main__':
    option = ['가위', '바위', '보']
    result  = random.choice(option)
    selection = input('가위 바위 보 중 하나를 입력하세요 : ')
    rock_cissor_paper(result, selection)