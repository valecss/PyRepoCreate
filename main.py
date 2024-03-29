import os
import sys
from github import Github

path = os.getcwd() #Script path
user = "" #Insert your username
password = "" #Insert your password
git = Github(user, password).get_user()
username = user

def create():
    name = sys.argv[1] #Take the name of the project


    #Check if project exist
    if name not in os.listdir(f"{path}/.."):
        CHANGEHERE = os.chdir(f"{path}/../") #Change path after '../'
        os.mkdir(name) #Create project folder
        os.chdir(name) #Change direcotry to project folder
        repo = git.create_repo(name) #Create repo
        os.system("git init") #Init repo in local
        os.system("touch README.md") #Create README.md file
        os.system("git add .") #Add files
        os.system("git commit -m \"Initial Commit\"") #Commit project
        os.system(f"git remote add origin git@github.com:{username}/{name}.git") #Add files into repo
        os.system("git push -u origin master") #Push everything
    
    #If file already exist print
    else:
        print("Project already exist.")

if __name__ == "__main__":
    create() #Init func
