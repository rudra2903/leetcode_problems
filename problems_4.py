# Given an integer numRows, return the first numRows of Pascal's triangle.

def pascal(num):

    output = []

    for i in range(num):
        temp_list = []
        for j in range(i+1):
            if j==0 or j==i:
                temp_list.append(1)
            else:
                temp_list.append(output[i-1][j-1] + output[i-1][j])
        output.append(temp_list)

    
    print(output)

pascal(5)