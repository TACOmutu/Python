import random
ansInt = random.randint(0,100)

count = 0
print("数字当てゲーム")      
        
while True:
    i = input("数字を入力してください:")
    print()
    try:
        inputInt = int(i)
        
        if not(0 <= inputInt <=100):
            print('0〜100の範囲で入力してください\n')
            continue
    except ValueError:
        print('数字を入力してください\n')
        continue
            
    count += 1
    if inputInt == ansInt:
        print(f'正解! {ansInt} です')
        print(f'{count}回で正解しました！')
        break
    elif inputInt < ansInt :
        print(f'もっと大きいです\n')
    else:
        print(f'もっと小さいです\n')
