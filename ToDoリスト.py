tasks = []


def add_task(task):
    tasks.append(task)
    print(f"タスク[{task}]を追加しました")
    
def show_tasks():
    if not tasks:
        print("タスクはありません")
    else:
        for i ,task in enumerate(tasks,1):
            print(f"{i}.{task}")
            
def removed_task(index):
    if 0 <= index < len(tasks):
        remove_task = tasks.pop(index)
        print(f"タスク[{remove_task}]を削除しました")
    else:
        print("無効な番号です")
        
while True:
    print("ToDoリストです。使用する番号を入力してください")
    print("1.タスク確認 2.タスク追加 3.タスク削除 4.アプリ終了")
    number = input("数字を入力してください　＞＞")
    if "1" == number:
          show_tasks()
    elif "2" == number:
        mission = input("タスクを入力してください　＞＞")
        add_task(mission)
    elif "3" == number:
        if not tasks:
            print("タスクはありません")
        else:
            delete = input("削除するタスクの番号を入力して下さい　＞＞")
            delete = int(delete) - 1
            removed_task(delete)
    elif "4" == number:
        print("アプリを終了します")
        break
    else :
        print(f"{number}は無効な数字です")