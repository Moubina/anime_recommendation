pipeline {
    agent any
    stages {
        
        stage('Build') {
            steps {
                bat 'git config --global user.email "pharvine.moubina@gmail.com"'
                bat 'git config --global user.name "Moubina"'
                bat 'docker-compose up -d --build'
                
            }
        }

        stage('Push to dev from features') {
            steps {
                bat "echo '--------------PUSH TO DEV FRON FEATUUUURE-------------------'"
                bat "echo 'Merging feature branch into dev'"
                bat 'git checkout feature/*'
                bat 'git checkout dev'
                bat 'git pull origin dev'
                bat 'git merge feature/*'
                bat "git push origin dev"
            }
        }
        
        
        stage('Push to Main') {
            input {
                message 'Do you want to merge dev to main?' 
                ok 'Promote'
                }
            steps {
                bat "echo '------------PUSH TO MAIN------------------'"
                bat "echo 'Asking the permission to merge'"                
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
