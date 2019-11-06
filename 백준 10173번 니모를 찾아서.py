for i in range(80):
    N = input()
    if N == 'EOI':
        break
    N = N.upper()
    
    if 'NEMO' in N:
        print('Found')
    else:
        print('Missing')
