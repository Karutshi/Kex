def getOrder(offset):
    latinsquare = [0, 11, 1, 10, 2, 9, 3, 8, 4, 7, 5, 6]
    return [(i + offset - 1) % 12 for i in latinsquare]
	
def getGroupOrder(subject_number):
    return [(i + subject_number - 1) % 4 for i in [0, 3, 1, 2]]
	
l = [
     # Group 1
     [('sparse_11', 1),  ('sparse_32', 11), ('sparse_22_1', 5), ('sparse_00_1', 13), ('sparse_00_5', 33), ('sparse_00_9', 37),  
      ('dense_11', 17),  ('dense_32', 27), ('dense_22_1', 21), ('dense_00_1', 29), ('dense_00_5', 41), ('dense_00_9', 45)],
     # Group 2
     [('sparse_31', 10), ('sparse_12', 2),  ('sparse_22_2', 6), ('sparse_00_2', 14), ('sparse_00_6', 34), ('sparse_00_10', 38),
      ('dense_31', 26), ('dense_12', 18),  ('dense_22_2', 22), ('dense_00_2', 30), ('dense_00_6', 42), ('dense_00_10', 46)],
     # Group 3
     [('sparse_13', 3),  ('sparse_21', 4),  ('sparse_22_3', 7), ('sparse_00_3', 15), ('sparse_00_7', 35), ('sparse_00_11', 39),
      ('dense_13', 19),  ('dense_21', 20),  ('dense_22_3', 23), ('dense_00_3', 31), ('dense_00_7', 43), ('dense_00_11', 47)],
     # Group 4
     [('sparse_33', 12), ('sparse_23', 9),  ('sparse_22_4', 8), ('sparse_00_4', 16), ('sparse_00_8', 36), ('sparse_00_12', 40),
      ('dense_33', 28), ('dense_23', 25),  ('dense_22_4', 24), ('dense_00_4', 32), ('dense_00_8', 44), ('dense_00_12', 48)]
    ]

subject_number = input("Enter the subject number: ")
is_yes_no = bool(input("What question? ") == 2)


data = [""]*48
order = []

for grpnum in getGroupOrder(subject_number):
    videos = l[grpnum]
    for i in getOrder(subject_number + grpnum * 3):
        _, v_id = videos[i]
        order.append(v_id)

with open('Answers.txt', 'r') as f:
    for i in order:
        dat = f.readline()[:-1]
        data[i - 1] = dat
		
print data
print order
print len(order)

with open('Order.txt', 'w') as f:
    for row in data:
        if not is_yes_no:
		    f.write(row + "\n")
        else: 
            f.write(("Yes" if row == "1" else "No") + "\n")
	
print("Wrote answers in order to 'Order.txt'")