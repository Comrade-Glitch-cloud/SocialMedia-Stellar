         ___        ______     ____ _                 _  ___  
        / \ \      / / ___|   / ___| | ___  _   _  __| |/ _ \ 
       / _ \ \ /\ / /\___ \  | |   | |/ _ \| | | |/ _` | (_) |
      / ___ \ V  V /  ___) | | |___| | (_) | |_| | (_| |\__, |
     /_/   \_\_/\_/  |____/   \____|_|\___/ \__,_|\__,_|  /_/ 
 ----------------------------------------------------------------- 


Hi there! Welcome to AWS Cloud9!

To get started, create some files, play with the terminal,
or visit https://docs.aws.amazon.com/console/cloud9/ for our documentation.

Happy coding!

cp db.sqlite3 db_backup.sqlite3

rm db.sqlite3

find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
find . -path "*/migrations/*.pyc" -delete

for git hub 
git remote -v
git remote add origin https://github.com/Comrade-Glitch-cloud/SocialMedia-Stellar



git add .

git commit -m "buildspec.yml"
git commit -m "new update"
git branch -m master main

git commit --amend -m "buildspec.yml"
git pull origin main --rebase

git push origin main
git push origin main --force

user name: Comrade-Glitch-cloud

git status

git add buildspec.yml

aws codepipeline delete-pipeline --name x23328231Pipeline
aws codebuild delete-project --name x23328231CodeBuild
eb init -r us-east-1 -p python-3.9 stellar
