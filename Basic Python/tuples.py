my_dict = {
  "Speros": "(555) 555-5555",
  "Michael": "(999) 999-9999",
  "Jay": "(777) 777-7777"
}

def tuples(x):
    newlist = []
    newlist_two = []
    for key in x.keys():
        newlist.append(key)
    for count in x.values():
        newlist_two.append(count)

    newlist_three = zip(newlist, newlist_two)
    print newlist_three
tuples(my_dict)
