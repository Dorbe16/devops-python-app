pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'alexdbrrr/webapp'
    }

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/Dorbe16/devops-python-app.git'
            }
        }

        stage('Docker Build & Push') {
            steps {
                sh 'docker build -t $DOCKER_IMAGE .'
                sh 'docker login -u $DOCKER_HUB_USER -p $DOCKER_HUB_PASS'
                sh 'docker push $DOCKER_IMAGE'
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                sh 'kubectl apply -f k8s/deployment.yaml'
                sh 'kubectl apply -f k8s/service.yaml'
            }
        }
    }
}
