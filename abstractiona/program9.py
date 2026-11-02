# Q9. Create abstract CloudStorage with upload_file(),
# download_file(), and delete_file().
# Create subclasses for different storage services.

from abc import ABC, abstractmethod


class CloudStorage(ABC):

    @abstractmethod
    def upload_file(self):
        pass

    @abstractmethod
    def download_file(self):
        pass

    @abstractmethod
    def delete_file(self):
        pass


class GoogleDrive(CloudStorage):
    def upload_file(self):
        print("File uploaded to Google Drive")

    def download_file(self):
        print("File downloaded from Google Drive")

    def delete_file(self):
        print("File deleted from Google Drive")


class OneDrive(CloudStorage):
    def upload_file(self):
        print("File uploaded to OneDrive")

    def download_file(self):
        print("File downloaded from OneDrive")

    def delete_file(self):
        print("File deleted from OneDrive")


services = [GoogleDrive(), OneDrive()]

for service in services:
    service.upload_file()
    service.download_file()
    service.delete_file()