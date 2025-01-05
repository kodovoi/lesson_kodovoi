import time
from multiprocessing import Pool

def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        while True:
            line = file.readline()
            if not line:
                break
            all_data.append(line)


filenames = [f'file{number}.txt' for number in range(1, 5)]


start_time = time.time()

for filename in filenames:
    read_info(filename)

end_time = time.time()
print(f"Линейный вызов: {time.strftime('%H:%M:%S', time.gmtime(end_time - start_time))}")

if __name__ == '__main__':

    start_time = time.time()

    with Pool() as pool:
        pool.map(read_info, filenames)

    end_time = time.time()
    print(f"Многопроцессный вызов: {time.strftime('%H:%M:%S', time.gmtime(end_time - start_time))}")
