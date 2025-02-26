pipeline {
    agent any

    triggers {
        pollSCM('H/5 * * * *')
    }

    environment {
        DOCKERHUB = credentials('4cf2d8b6-f34e-4ee7-86f3-7166aae7af8d')
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
                sh '''
                python3 -m venv venv
                bash -c "source venv/bin/activate && pip install -r requirements.txt"
                '''
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
                sh 'docker login -u $DOCKERHUB_USR -p $DOCKERHUB_PSW'
                sh 'docker push zivanR/jenkins-pokedex-app:latest'
            }
        }
    }
}