new_list = [2,5,3,6,9,10,8]

search_item = 6

for i in new_list:
    if i == search_item:
        print(f"Found, Index No: {new_list.index(i)}")
        break
    else:
        print("Not Found! Still Searching...")


    

