import dropbox

class TransferData:
    def __init__(self,accesstoken):
        self.accesstoken = accesstoken
    def uploadfile(self,file_from,file_to):
        dbx = dropbox.Dropbox(self.accesstoken)
        f = open(file_from,'rb')
        dbx.files_upload(f.read(),file_to)
def main():
    accesstoken = 'iD8Xi0tCt4AAAAAAAAAAGKjuGT6Y7w3cJz3vnO9VrlXOGzGNFxHWyMBf4j0AqyO9'
    transferData = TransferData(accesstoken)
    file_from = input("Enter the file to be transfered")
    file_to = input("Enter the full to path to upload to dropbox")
    transferData.uploadfile(file_from,file_to)
    print("file is moved")
main()