# Audioserver API
A basic structure or interface to an audio server backend.

## Description
	Audioserver API is a web API powered by Django and its accompanying REST framework.
It provides an interactive interface through which the front and back ends may communicate with each other.
As long as the front end meets the data requirements of the supported audio file types, it may create, read, update and/or delete data from the back end without worrying about the underlying architecture of the backend.
By default, the read operation is available to any one; while the create, update and delete operations are available to authenticated users on the admin user database.

## Supported Audio File Types
1. SONG
Data Requirements: title, duration (specified in seconds), upload date (auto generated).
Accessible via .../api/v1/song/
2. PODCAST
Data requirements: title, duration (specified in seconds), host, participants (optional), upload date (auto-generated).
Accessible via .../api/v1/podcast/
3. AUDIOBOOK
Data requirements: title, duration (specified in seconds), author, narrator, upload date (auto-generated).
Accessible via .../api/v1/audiobook/

## Dependencies
	Install the latest versions of the following to interact with the database.
1. django (The Python-based web app framework)
2. djangorestframework (The building-block of the API)
3. django-rest-auth (oversees user authorization with regard to API access)
4. drf-yasg (Presents API documentation. Accessible via .../redoc/)