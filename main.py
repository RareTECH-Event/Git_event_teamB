def main():
    while True:
        print("選択してください：")
        print("1: ちかこ@53期")
        print("2: ヒロ@53期")
        print("3: 朔太郎＠53期")
        print("q: 終了")

        choice = input("> ")

        if choice == "1":
            print("こんばんは")
        elif choice == "2":
            print("よろしくおねがいします")
        elif choice == "3":
            print("そろそろ寝ようかな")
        elif choice == "q":
            print("プログラムを終了します。")
            break
        else:
            print("無効な入力です。もう一度選択してください。")

if __name__ == "__main__":
    main()
