import requests
import hashlib
import sys


def request_api_data(query_char):
    url = 'https://api.pwnedpasswords.com/range/' + query_char
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(f'Error fetching {res.status_code} check the url')
    return res


def get_password_leakes_count(hashes, hash_to_check):  ### seperating the number of count from the responses recieved after function request_api
    hashes = (line.split(':') for line in hashes.text.splitlines())
    for h, count in hashes:
        if h == hash_to_check:
            return count
    return 0


def pwned_api_check(password):
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first_5, tail = sha1password[:5], sha1password[5:]
    response = request_api_data(first_5)
    return get_password_leakes_count(response, tail)


pwned_api_check('hello')


def main(args):
    for password in args:
        count = pwned_api_check(password)
        if count:
            print(f'{password} has been hacked {count} many times...')
        else:
            print(f'{password} is not found hacked anytime')
    return 'done!!'

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
