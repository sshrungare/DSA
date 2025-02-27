def show_show_list_by_recusion(i,L,N):
    if i==N:
        return None
    elif  i < N:
        print(i,L[i])
        show_show_list_by_recusion(i+1,L,N)

L = [1,2,3,4,5]

show_show_list_by_recusion(0,L,len(L))
