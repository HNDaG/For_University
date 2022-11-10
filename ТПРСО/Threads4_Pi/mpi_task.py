from mpi4py import MPI
import random as r
import sys
import argparse

PI = 3.141592653589793

points = 0

parser = argparse.ArgumentParser()
parser.add_argument("points", help="display the total number of points",type=int)
args = parser.parse_args()
points = int(sys.argv[1])


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


    ans = dict()
    if rank != 0:
        data = [rank, points_to_calculate, end-start, pi, abs(PI-pi)]
        comm.send(data, dest=0)
    
    else:
        ans[rank] = [points_to_calculate, end-start, pi, abs(PI-pi)]
        for k in range(1, size):
            val = comm.recv(source=k)
            ans[val[0]] = val[1:]

    if rank == 0:
        for j in range(1, size):
            print(f"Rank: {j}\tPoints_to_calculate: {ans[j][0]}\nTime: {ans[j][1]}\tpi: {ans[j][2]}\t Error: {ans[j][3]}\n\n" )
        print(f"Rank: {0}\tPoints_to_calculate: {ans[0][0]}\nTime: {ans[0][1]}\tpi: {ans[0][2]}\t Error: {ans[0][3]}\n\n" )

main()

# Windows
# mpiexec -n 4 python C:\Users\nikit\Desktop\University\ТПРСО\Threads4_Pi\mpi_task.py 100000
# Linux
# mpirun -np 4 python3 mpi_task.py 100000