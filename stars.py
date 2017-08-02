def stars(arr):
    for count in arr:
        if type(count) == str:
            print (count[0].lower()) * len(count)
        else:
            print count * "*"

stars([2, "Tom", 7, "Thej"])
    