# guess_the_number.py
import random

def guess_the_number_game():
    """
    1부터 100 사이의 숫자를 맞추는 게임입니다.
    """
    print("--- 숫자 맞추기 게임 시작! ---")
    print("저는 1부터 100 사이의 숫자를 생각했습니다.")

    # 컴퓨터가 난수 생성
    secret_number = random.randint(1, 100)
    attempts = 0 # 시도 횟수

    while True:
        try:
            user_guess = int(input("숫자를 맞춰보세요: "))
            attempts += 1

            if user_guess < 1 or user_guess > 100:
                print("숫자는 1에서 100 사이여야 합니다. 다시 입력해주세요.")
            elif user_guess < secret_number:
                print("더 높게!")
            elif user_guess > secret_number:
                print("더 낮게!")
            else:
                print(f"축하합니다! {secret_number}를 {attempts}번 만에 맞췄습니다!")
                break # 게임 종료
        except ValueError:
            print("잘못된 입력입니다. 숫자를 입력해주세요.")
        except KeyboardInterrupt: # Ctrl+C 입력 시 프로그램 종료
            print("\n게임이 종료됩니다.")
            break

if __name__ == "__main__":
    guess_the_number_game()
  
