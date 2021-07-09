import requests
import re
from bs4 import BeautifulSoup as bs
import threading

URL_REGEX = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|" \
            r"(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"


class Lock:
    def __init__(self, allow_max_locks=False, max_locks=5):
        self._lock = 0
        self.max_locks = max_locks
        self.max_locks_concept = allow_max_locks

    @property
    def is_locked(self):
        return self._lock == self.max_locks if self.max_locks_concept else self._lock

    @property
    def remaining_locks(self):
        if self.max_locks_concept:
            return self.max_locks - self._lock
        else:
            print("Max lock concept is not on")

    def acquire(self):
        if self.max_locks_concept:
            if self._lock < self.max_locks:
                self._lock += 1
            else:
                raise Exception("Maximum locks acquired")
        else:
            if not self._lock:
                self._lock = 1
            else:
                raise Exception("Lock is already acquired")

    def release(self):
        if self.max_locks_concept:
            self._lock -= 1
        else:
            self._lock = 0


class HrefParserThreadBoosted:
    def __init__(self, threads=5, max_links=1000):
        if threads > 20:
            raise Exception("50 Max threads allowed")
        if max_links > 1000000:
            raise Exception("1M Max links allowed")

        self._max_threads = threads
        self.links = []
        self.edges = []
        self.max_links = max_links
        self._running_threads = 0
        self.lock = Lock(allow_max_locks=True, max_locks=self._max_threads)

    def __parse_links(self, link):
        resp = requests.get(link)

        if resp.status_code == 200:
            html = resp.text
            if html:
                soup = bs(html, 'lxml')

                for anchor in soup.find_all('a', href=True):
                    ugly_data = anchor['href']
                    valid_url = re.search(URL_REGEX, ugly_data)
                    if valid_url:
                        self.links.append(valid_url.group(1))
                        self.edges.append((link, valid_url.group(1)))
            else:
                print('html was none')

        else:
            print(f'status :{resp.status_code}')

        print("Thread should be automatically killed here")
        self.lock.release()
        self._running_threads -= 1

    def driver(self, link):
        self.links.append(link)
        start = 0
        end = self._max_threads

        while 1:
            if len(self.links) > self.max_links:
                break
            # time.sleep(5)
            sublist = self.links[start: end]
            for i in sublist:
                if len(self.links) > self.max_links:
                    break
                if not self.lock.is_locked:
                    self.lock.acquire()
                    print(f"Acquiring lock for thread", flush=True)
                    print(f"running thread...", flush=True)
                    thread = threading.Thread(target=self.__parse_links, args=[i])
                    thread.start()
                    self._running_threads += 1
                    start += 1
                    end += 1

                if self.lock.is_locked:
                    print('[LOCK THREAD BOOST] ----> Max Threads Running...')
                    print(f'\n\n[INFO] : ----> {len(self.links)} Links Parsed!\n\n')

                while len(self.links) <= len(sublist):
                    pass
                    # continue

                while self.lock.is_locked:
                    pass
                    # continue

        while 1:
            if self._running_threads <= 0:
                print(f"[FINISH] : {len(self.links)} links added.")
                print(len(self.links), len(set(self.links)))
                return


if __name__ == '__main__':
    obj = HrefParserThreadBoosted(threads=5, max_links=100)
    obj.driver('https://github.com')
    print(obj.links)
    print(obj.edges)
