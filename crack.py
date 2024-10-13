import hashlib
import threading
import time

def crack_password(target_hash, password_list, algorithm, progress_callback):
    total_passwords = len(password_list)
    for i, password in enumerate(password_list):
        if algorithm == 'md5':
            hashed_password = hashlib.md5(password.encode('utf-8')).hexdigest()
        elif algorithm == 'sha256':
            hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()
        elif algorithm == 'sha512':
            hashed_password = hashlib.sha512(password.encode('utf-8')).hexdigest()
        else:
            print(f"Error: Unsupported hashing algorithm '{algorithm}'.")
            return None

        if hashed_password == target_hash:
            return password

        progress_callback(i, total_passwords)

    return None

def progress_tracker(current_index, total_passwords):
    percentage = (current_index / total_passwords) * 100
    print(f"Progress: {percentage:.2f}%")

def multi_threaded_crack(target_hash, password_list, algorithm, num_threads):
    password_per_thread = len(password_list) // num_threads
    threads = []
    cracked_password = None

    for i in range(num_threads):
        start_index = i * password_per_thread
        end_index = (i + 1) * password_per_thread
        thread_password_list = password_list[start_index:end_index]
        thread = threading.Thread(target=crack_password, args=(target_hash, thread_password_list, algorithm, progress_tracker))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()
        if cracked_password:
            break

    return cracked_password

def main():
    target_hash = input("Enter the target hash: ")
    dictionary_file = input("Enter the path to the dictionary file: ")
    algorithm = input("Enter the hashing algorithm (md5, sha256, sha512): ")
    num_threads = int(input("Enter the number of threads: "))

    try:
        with open(dictionary_file, 'r') as file:
            passwords = file.read().splitlines()
    except FileNotFoundError:
        print(f"Error: Dictionary file '{dictionary_file}' not found.")
        exit()

    start_time = time.time()
    cracked_password = multi_threaded_crack(target_hash, passwords, algorithm, num_threads)
    end_time = time.time()

    if cracked_password:
        print(f"Password cracked: {cracked_password}")
    else:
        print("Password not found in the dictionary.")

    print(f"Time taken: {end_time - start_time:.2f} seconds")

if __name__ == '__main__':
    main()