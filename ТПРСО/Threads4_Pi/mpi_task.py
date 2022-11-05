from mpi4py import MPI
import random as r
import time

PI = 3.141592653589793
points = 100000

def In_zone(x, y):
    return (x*x+y*y)<1

def main():
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    size = comm.size
    points_to_calculate = points
    in_zone = 0

    if rank == 0:
        arr = [[r.random(), r.random()] for i in range(points)]
    else:
        arr = None
        points_to_calculate = int((points/size)*rank)

    arr = comm.bcast(arr, root=0)
    start = MPI.Wtime()

    for i in range(int(points_to_calculate)):
        in_zone += In_zone(arr[i][0],arr[i][1]);
    pi = 4.0 * in_zone / points_to_calculate;
    end = MPI.Wtime()

    print(f"Rank: {rank}\tPoints_to_calculate: {points_to_calculate}\nTime: {end-start}\tpi: {pi}\t Error: {abs(PI-pi)}" )

main()

#mpiexec -n 4 python C:\Users\nikit\Desktop\University\ТПРСО\Threads4_Pi\mpi_task.py