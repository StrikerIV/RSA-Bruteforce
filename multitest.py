import re
import time
import shutil
import rsa as rsa
import multiprocessing

global solved
solved = False

mod_value = 52891
encrypted = "12789, 12476, 19637, 16114, 43326, 25332, 35366, 16114, 33101, 12476, 52005, 16114, 337, 12476, 30006, 14279, 14830, 16114, 10905, 12476, 337, 43326, 33101"
encrypted = encrypted.split(", ")


def multiprocessing_func(x):
    decrypted_msg = rsa.decrypt(x, mod_value, encrypted)
    decrypted_msg.strip()

    regex = r'[a-zA-Z]+'
    matches = re.findall(regex, decrypted_msg)
    print(x, decrypted_msg, matches)

    if matches:
        if len(matches) > 2:
            matches = matches[0]
            if len(matches) > 2:

                print("POTENTIAL SOLVE")

                with open('potential_solves.txt', 'a') as a_writer:
                    a_writer.write(
                        '\nPotential Solve\n-----------\nThe key is : %s\nThe modulus is : %s\nThe message is : %s\nOriginal encrypted message : %s\n' % (x, mod_value, decrypted_msg, encrypted))


if __name__ == '__main__':
    starttime = time.time()
    processes = []
    for i in range(15000, 30000):

        p = multiprocessing.Process(target=multiprocessing_func, args=(i,))
        processes.append(p)
        p.start()

    for process in processes:
        process.join()

    print('That took {} seconds'.format(time.time() - starttime))
