def TowerOfHanoi(n,from_rod,to_rod,aux_rod):
    if n==1:
        print("move disk 1 from rod",from_rod,"to_rod",to_rod)
        return
    TowerOfHanoi(n-1,from_rod,aux_rod,to_rod)
    print("move disk",n,"from_rod",from_rod,"to_rod",to_rod)
    TowerOfHanoi(n-1,aux_rod,to_rod,from_rod)
n=4
TowerOfHanoi(n,'A','C','B')