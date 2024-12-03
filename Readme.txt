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
password: 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

git status

git add buildspec.yml

aws codepipeline delete-pipeline --name x23328231Pipeline
aws codebuild delete-project --name x23328231CodeBuild
eb init -r us-east-1 -p python-3.9 stellar
