T = int(input())
    
for i in range(T):
    A, B = input().split()
    C = int(A) + int(B)
    print('Case #{}: {} + {} = {}'.format(i+1, A, B, C))
   #print('Case #%s: %s + %s = %s'.%(i+1, A, B, C))
