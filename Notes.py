def non_note(a):
    curr = [1000, 500, 100, 50, 10, 5]
    x = 0
    for i in range(6):
        q = curr[i]
        x = a//q
        print("note of {} = {}".format(q, x))
        a = a%q
amount = int(input("Enter a amount : "))
non_note(amount)