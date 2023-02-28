pipeline {
    agent any
    stages {
        
        stage('Build and Test Feature Branch') {
            steps {
                bat "echo '------------BUIIIIIILD FEATURE------------------'"
                bat "echo 'Tests on feature branches'"
                //bat "pip3 install -r requirements.tt"
                //bat "python3 -m pytest tests TO DO"
            }
        }

        stage('Push to dev from features') {
            steps {
                bat "echo '------------PUSH TO DEV FRON FEATUUUURE-------------------'"
                bat "echo 'Merging feature branch into dev'"
                bat 'git checkout dev'
                bat 'git pull origin dev'
                bat "git merge ${git branch --list 'feature/*' | cut -c3- | tr '\n' ' '}"
                bat "git push origin dev"
            }
        }
        
        stage('Stress Test and Deploy from dev') {
            
            steps {
                bat "echo '------------DEPLOY DEV-------------------'"
                bat "echo 'Stress Tests to do on dev branch and deployement'"
                //bat "pip3 install -r requirements.txt --user"
                //bat "python3 stress_test.py"
                bat 'docker-compose up --build'
                
            }
        }
        
        
        stage('Push to Main') {
            
            steps {
                bat "echo '------------PUSH TO MAIN------------------'"
                bat "echo 'Asking the permission to merge'"

                timeout(time: 1, unit: TimeUnit.HOURS) {
                    input message: 'Do you want to merge dev to main?', ok: 'Promote'
                }
                bat "echo 'Merging dev branch into main'"
                bat 'git checkout main'
                bat 'git merge dev'
                bat "git push origin main"
            }
        }

        stage('Push Image to Docker Hub') {
            steps {
                bat "echo '------------IMAGE TO DOCKERHUB------------------'"
                bat 'docker login -u moubina -p Pharvine93!'
                bat 'docker-compose build back'
                bat 'docker-compose push back'                
            }
        }
        
    }
}