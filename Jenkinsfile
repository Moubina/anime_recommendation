pipeline {
    agent any
    stages {
        
        stage('Build and Test Feature Branch') {
            bat "echo '------------BUIIIIIIILD FEATURE-------------------'"
            when { branch 'feature/*' }
            steps {
                bat "echo 'Tests on feature branches'"
                //bat "pip3 install -r requirements.txt"
                //bat "python3 -m pytest tests TO DO"
            }
        }
        
        stage('Stress Test and Deploy from dev') {
            bat "echo '------------DEPLOY DEV-------------------'"
            when { branch 'dev' }
            steps {
                bat "echo 'Stress Tests to do on dev branch and deployement'"
                //bat "pip3 install -r requirements.txt --user"
                //bat "python3 stress_test.py"
                bat 'docker-compose up --build'
                
            }
        }
        
        stage('Push to dev') {
            bat "echo '------------PUSH TO DEV FRON FEATUUUURE-------------------'"
            when { branch 'feature/*' }
            steps {
                
                bat "echo 'Merging feature/ branch into dev'"
                bat 'git checkout dev'
                bat 'git merge feature/*'
                bat "git push origin dev"
            }
        }
        
        stage('Push to Main') {
            bat "echo '------------PUSH TO MAIN-------------------'"
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

        stage('Push Image to Docker Hub') {
            bat "echo '------------IMAGE TO DOCKERHUB-------------------'"
            steps {
                bat 'docker login -u moubina -p Pharvine93!'
                bat 'docker-compose build back'
                bat 'docker-compose push back'                
            }
        }
        
    }
}


        

