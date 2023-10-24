# TOWER OF HANOI

# Pseudocode 
# START
# Procedure Hanoi(disk, source, dest, aux)

#    IF disk == 1, THEN
#       move disk from source to dest             
#    ELSE
#       Hanoi(disk - 1, source, aux, dest)     // Step 1
#       move disk from source to dest          // Step 2
#       Hanoi(disk - 1, aux, dest, source)     // Step 3
#    END IF
   
# END Procedure
# STOP


# Recursive Python function to solve tower of hanoi
def TowerOfHanoi(n, source_rod, dest_rod, aux_rod):
	if n == 0:
		return
	TowerOfHanoi(n-1, source_rod, aux_rod, dest_rod)
	print("Move disk", n, "from rod", source_rod, "to rod", dest_rod)
	TowerOfHanoi(n-1, aux_rod, dest_rod, source_rod)

# Driver code
N = 3

# Source_rod, Aux_rod, Dest_rod are the name of rods
TowerOfHanoi(N, 'Source_rod', 'Aux_rod', 'Dest_rod')

