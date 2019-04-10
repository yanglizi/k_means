
import math

# Create data
def createdata():
    data = [[0,0],[1,2],[3,1],[8,8],[9,10],[10,7]]
    return data

# Calculate the distance between two points
def distance(a,b):
    dis2 = 0
    for i in range(len(a)):
        dis2 += math.pow(a[i]-b[i],2)
    return math.sqrt(dis2)

# Calculate the distance from the data to the center point, the return value is the distance list corresponding to the number of center points
def dis_center(center,data):
    dis_list = []
    for i in range(len(center)):
        dis_i = []
        for j in range(len(data)):
            dis_i.append(distance(center[i],data[j]))
        dis_list.append(dis_i)
    return dis_list

# 
def n_mean(candidate_i,data):
    data_c = []
    center_i = []
    for i in candidate_i:                                     # Obtain the corresponding points in the data according to candidate_i
        for j in range(len(data)):
            if i==j:
                data_c.append(data[j])

    data_c_t = zip(*data_c)
    for i in data_c_t:                                        # Calculate each feature value of center_i
        sum_i = 0
        for j in i:
            sum_i += j
        center_i.append(sum_i/len(i))
    return center_i

def k_means(data,k):
    center = []
    new_center = []
    ans_max = 1
    for x in range(k):
        center.append([x,x])
    while(ans_max>0.0001):
        ans_max = 0

        new_center.clear()

        dis_list = dis_center(center,data)

        candidate = []                                         # Collection of candidate_i
        candidate_i = []                                       # Index of data belonging to center i

        mincol = [min(col) for col in zip(*dis_list)]          # Get the minimum value of each column in dis_list
        for i in range(len(dis_list)):                         # Get candidate, according to dis_list, data is divided into several parts corresponding to the center point.
            candidate_i = []
            for j in range(len(dis_list[i])):
                if mincol[j]==dis_list[i][j]:
                    candidate_i.append(j)
            candidate.append(candidate_i)

        for i in candidate:                                    # Get new_center
            new_center.append(n_mean(i,data))
        ans_i = 0
        for i in range(len(center)):                           # Maximum iterative difference of center points in center and new_center
            ans_i = distance(center[i],new_center[i])
            ans_max = ans_i if ans_i>ans_max else ans_max
        # ans = distance(center[1],new_center[1])

        center.clear()
        center = new_center.copy()
        

    return new_center



if __name__ == "__main__":
    data = createdata()
    # for i in data:
    #     print(i)

    # print(distance([1,1],[2,2]))
    # print(dis_center([[0, 0], [1, 2]],[[0,0],[1,2],[3,1],[8,8],[9,10],[10,7]]))

    result = k_means(data,2)
    print(result) 
