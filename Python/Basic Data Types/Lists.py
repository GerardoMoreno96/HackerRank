"""Initialize your list and read in the value of  followed by  lines of commands where each
 command will be of the  types listed above. Iterate through each command in order and
  perform the corresponding operation on your list."""

if __name__ == '__main__':
    L = []
    N = int(input())
    for i in range(N):
        cmd = input().split()
        if cmd[0] != 'print':
            if len(cmd) == 3:
                string = 'L.{}({},{})'.format(cmd[0],cmd[1],cmd[2])
            elif len(cmd) ==2:
                string = 'L.{}({})'.format(cmd[0],cmd[1])
            else:
                string = 'L.{}()'.format(cmd[0])
            eval(string)
        else:
            print(L)
