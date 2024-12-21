a = input().split() 
b = input().split()
c = input().split()
O = input() #Player_names
X = input() #Players_names

if (a[0]=='O' and a[1] == "O" and a[2]=='O') or (b[0]=='O'and b[1]=='O' and b[2]=='O') or (c[0] == 'O' and c[1]=='O' and c[2]=='O'):
    print('Winner: {}'.format(O))

elif (a[0]=='X' and a[1]=='X' and a[2]=='X') or (b[0]=='X' and b[1]=='X' and b[2]=='X') or (c[0]=='X' and c[1]=='X' and c[2] == 'X'):
    print('Winner: {}'.format(X))

elif (a[0]=='O' and b[0]=='O' and c[0]=='O') or (a[1] == 'O' and b[1] == 'O' and c[1]=='O') or (a[2]=='O' and b[2]=='O' and c[2]=='O'):
    print('Winner: {}'.format(O))

elif (a[0]=='X' and b[0]=='X' and c[0]=='X') or (a[1] == 'X' and b[1] == 'X' and c[1]=='X') or (a[2]=='X' and b[2]=='X' and c[2]=='X'):
    print('Winner: {}'.format(X))

elif (a[0]=='O' and b[1]=='O' and c[2]=='O') or (a[2]=='O' and b[1] == 'O' and c[0] == "O"):
    print('Winner: {}'.format(O))
  
elif  (a[0]=='X' and b[1]=='X' and c[2]=='X') or (a[2]=='X' and b[1] == 'X' and c[0] == "X"):
    print('Winner: {}'.format(X))

else:
    print("Tie")