# Code below adapted from examples here https://pygithub.readthedocs.io/en/latest/examples/Repository.html and week 4 labs
#import the necessary libraries
from github import Github, Auth
from config import config as cfg
import requests

# get authentifcation token from config.py and connect to GitHub API
apikey = cfg["GITHUB_TOKEN"]
auth = Auth.Token(apikey)
g = Github(auth=auth)

# Connect to the repository - adapted from Andrew's lab.
repo = g.get_repo("EmmaChubbCode/aprivateone")

# test if connection is working by printing the clone URL of the repository
print(repo.clone_url)

# see https://docs.github.com/en/rest/repos/contents?apiVersion=2022-11-28
# get contents from specific file (see: https://pygithub.readthedocs.io/en/latest/examples/Repository.html#get-a-specific-content-file) 
fileInfo = repo.get_contents("assignment4.txt")

# get the download URL for the file so we can read the content of the file (see: https://pygithub.readthedocs.io/en/latest/examples/Repository.html#download-a-file)
urlOfFile = fileInfo.download_url
# print(urlOfFile)

# print the text of the file as per andrew's lab.
response = requests.get(urlOfFile)
contentOfFile = response.text
print (contentOfFile)

# new content is the same as the old content but with "Andrew" replaced with "Emma". see: https://www.w3schools.com/python/ref_string_replace.asp 
new_content = contentOfFile.replace("Andrew", "Emma")

#print(new_content)

# next, update the fule with th new content. see: https://pygithub.readthedocs.io/en/latest/examples/Repository.html#update-a-file-in-the-repository 
gitHubResponse=repo.update_file(fileInfo.path,"updated by prog",
new_content,fileInfo.sha)
print (gitHubResponse)
