import threading
from scripts import frequency_of_str, circular_queue, validity_of_password

def execute_code():
    thread1 = threading.Thread(target=frequency_of_str.frequency_of_string)
    thread2 = threading.Thread(target=circular_queue.circular_queue_dic)
    thread3 = threading.Thread(target=validity_of_password.validate_pwd)

    thread1.start()
    thread2.start()
    thread3.start()

    thread1.join()
    thread2.join()
    thread3.join()

if __name__ == "__main__":
    execute_code()
