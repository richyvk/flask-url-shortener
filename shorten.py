import cPickle as pickle
import random
import string


def convert_url():
    url_to_shorten = raw_input('Enter URL to shorten: ')

    with open('url_list.p') as f:
        url_list = pickle.load(f)

    for item in url_list:
        if url_to_shorten == item[0]:
            return ("Your URL is shortened to http://shorten.me/%s"
                    % str(item[1]))

    letters = string.ascii_letters + string.digits
    url_hash = ''.join(random.SystemRandom().choice(letters) for n in range(7))
    url_list.append((url_to_shorten, url_hash))

    with open('url_list.p', 'w') as f:
        pickle.dump(url_list, f)

    print url_list

    return ("Your URL is shortened to http://shorten.me/%s"
            % str(url_hash))

print convert_url()
