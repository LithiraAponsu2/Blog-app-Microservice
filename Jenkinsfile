pipeline {
    environment {
        DOCKER_HUB_CREDENTIALS = credentials('docker-hub-credentials')
        DOCKER_IMAGE_NAME_FRONTEND = 'lithira/blogpost-frontend'
        DOCKER_IMAGE_NAME_BACKEND = 'lithira/blogpost-backend'
        DOCKER_IMAGE_NAME_DATABASE = 'lithira/blogpost-database'
    }
    
    stages {
        stage('Lint Frontend Service') {
            agent {
                docker {
                    image 'python:3.9-slim'
                }
            }
            steps {
                dir('frontend') {
                    sh '''
                        echo "Checking current directory..."
                        pwd
                        echo "Listing files in directory..."
                        ls -al
                        echo "Setting up virtual environment..."
                        python -m venv venv
                        . venv/bin/activate
                        pip install flake8
                        echo "Running flake8 on app.py..."
                        flake8 app.py
                    '''
                }
            }
        }

        stage('Lint Backend Service') {
            agent {
                docker {
                    image 'python:3.9-slim'
                }
            }
            steps {
                dir('backend') {
                    sh '''
                        echo "Checking current directory..."
                        pwd
                        echo "Listing files in directory..."
                        ls -al
                        echo "Setting up virtual environment..."
                        python -m venv venv
                        . venv/bin/activate
                        pip install flake8
                        echo "Running flake8 on app.py..."
                        flake8 app.py
                    '''
                }
            }
        }
        
        stage('Build Docker Images') {
            agent any
            steps {
                sh '''
                docker build -t ${DOCKER_IMAGE_NAME_FRONTEND}:${BUILD_NUMBER} ./frontend
                docker build -t ${DOCKER_IMAGE_NAME_BACKEND}:${BUILD_NUMBER} ./backend
                docker build -t ${DOCKER_IMAGE_NAME_DATABASE}:${BUILD_NUMBER} ./database
                '''
            }
        }
        
        stage('Push to Docker Hub') {
            agent any
            steps {
                sh '''
                    echo ${DOCKER_HUB_CREDENTIALS_PSW} | docker login -u ${DOCKER_HUB_CREDENTIALS_USR} --password-stdin
                    docker push ${DOCKER_IMAGE_NAME_FRONTEND}:${BUILD_NUMBER}
                    docker push ${DOCKER_IMAGE_NAME_BACKEND}:${BUILD_NUMBER}
                    docker push ${DOCKER_IMAGE_NAME_DATABASE}:${BUILD_NUMBER}
                    docker logout
                '''
            }
        }
    }
}
