baby = 2
boy=5
def check_my_rank(rank):
    if rank <= baby:
        print("You're a baby")
    elif rank <= boy:
        print("You're a boy")
    else:
        print("What are you?")

rank=int(input())
check_my_rank(rank)
