def main():
    while True:
        print("選択してください：")
        print("1: ひの＠51期")
        print("2: メンバー2の名前")
        print("3: まい@51期")
        print("q: 終了")

        choice = input("> ")

        if choice == "1":
            print("ひのです。")
        elif choice == "2":
            print("メンバー2のコメント")
        elif choice == "3":
            print("まいです。")
        elif choice == "q":
            print("プログラムを終了します。")
            break
        else:
            print("無効な入力です。もう一度選択してください。")

if __name__ == "__main__":
    main()

