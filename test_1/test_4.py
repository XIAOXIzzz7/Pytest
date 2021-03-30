from multiprocessing import Pool
import os



def run(a):

        with open('D:/python1.txt', 'a+t') as a:
            a.write('111111111\n')
            print(os.getpid())



def main():
    po = Pool(maxtasksperchild=3)
    for i in range(10000):
        po.apply_async(run, (i,))
    po.close()
    po.join()


if __name__ == '__main__':
    main()

