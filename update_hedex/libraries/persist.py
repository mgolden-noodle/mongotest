import pickle

class Persist(object):

    def save_obj(obj, name, file_path):
        with open("%s/%s.pkl" % (file_path, name), 'wb') as f:
            pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)
            f.close()

    def load_obj(name, file_path):
        try:
            f = open("%s/%s.pkl" % (file_path, name), 'rb')
        except FileNotFoundError:
            return []
        x = pickle.load(f)
        f.close()
        return x
