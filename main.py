import os
import sys
from github import Github

thisPath = os.getcwd() #Script path
yourGitToken = "f1f0b36f63a5942e8b1b7174fe1bd7234fc61fa0" #Insert here your github token
git = Github(yourGitToken).get_user()

def create():
    name = sys.argv[1] #Take the name of the project


    #Check if project exist
    if name not in os.listdir(f"{thisPath}/.."):
        os.chdir(f"{thisPath}/..") #Change directory
        os.mkdir(name) #Create project folder
        os.chdir(name) #Change direcotry to project folder
        repo = git.create_repo(name) #Create repo
        os.system("git init") #Init repo in local
        os.system("touch README.md") #Create README.md file
        os.system("git add .") #Add files
        os.system("git commit -m \"Initial Commit\"") #Commit project
        os.system(f"git remote add origin git@github.com:KyrosDev/{name}.git") #Add files into repo
        os.system("git push -u origin master") #Push everything
    
    #If file already exist print
    else:
        print("Project already exist.")

if __name__ == "__main__":
    create() #Init func