import shelve

blt = ["bacon", "lettuce", "tomato"]
beans_on_toast = ["beans", "bread"]
scrambled_eggs = ["eggs", "butter", "milk"]
soup = ["tin of soup"]
pasta = ["pasta", "cheese"]

with shelve.open("recipes", writeback=True) as recipes:
    # recipes["blt"] = blt
    # recipes["beans on toast"] = beans_on_toast
    # recipes["scrambled eggs"] = scrambled_eggs
    # recipes["pasta"] = pasta
    # recipes["blt"].append("butter")
    # tmp_list = recipes["blt"]
    # tmp_list.append("butter")
    # tmp_list.append("bread")
    # recipes["blt"] = tmp_list

    # tmp_list = recipes["pasta"]
    # tmp_list.append("tomato")
    # recipes["pasta"] = tmp_list
    # recipes["soup"].append("croutons")

    for snack in recipes:
        print(snack, recipes[snack])
