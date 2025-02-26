pipeline {
    agent any

    triggers {
        pollSCM('H/5 * * * *')
    }

    stages {
        stage('Checkout'){
            steps {
                // Récup code depuis github
                checkout scm
            }
        }
        stage('Install dependencies') {
            steps {
                // Installation des dépendances listées dans requirements.txt
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Run Tests') {
            steps {
                // Execution de pytest
                sh 'pytest --maxfail=1 --disable-warnings'
            }
        }
        stage('Build Docker Image') {
            steps {
                // Construire image Docker
                sh 'docker build -t zivanR/jenkins-pokedex-app:latest .'
            }
        }
        stage('Push Docker Image') {
            steps {
                // Connexion à DH et push de l'image
                sh 'docker login -u $DOCKERHUB_USER -p $DOCKERHUB_PASS'
                sh 'docker push zivanR/jenkins-pokedex-app:latest'
            }
        }
    }
}