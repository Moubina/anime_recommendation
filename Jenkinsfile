pipeline {
    agent any
    stages {
        stage('Build and Test Feature Branch') {
            when { branch 'feature/*' }
            steps {
                bat "echo 'Tests on feature branches'"
                //bat "pip3 install -r requirements.txt"
                //bat "python3 -m pytest tests/"
            }
        }
        stage('Stress Test and Deploy fron dev') {
            when { branch 'dev' }
            steps {
                bat "echo 'Stress Tests on dev branch and deploy'"
                //bat "pip3 install -r requirements.txt --user"
                //bat "python3 stress_test.py"
                bat "docker-compose up -d"
                bat "docker-compose push"
            }
        }
        
        stage('Push to Main') {
            when { branch 'dev' }
            steps {
                bat "echo 'Asking the permission to merge'"

                timeout(time: 5, unit: 'MINUTES') {
                    input message: 'Do you want to merge dev to main?', ok: 'Promote'
                }
                bat "echo 'Merging dev branch into main'"
                bat 'git checkout main'
                bat 'git merge dev'
                bat "git push origin main"
            }
        }
    }
}
