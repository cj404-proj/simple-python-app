pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building the Python App...'
                sh 'python --version'
            }
        }
        stage('Test') {
            steps {
                echo 'Running Unit Tests...'
                sh 'pytest test_app.py'
            }
        }
        stage('Run') {
            steps {
                echo 'Running Application...'
                sh 'python app.py'
            }
        }
    }
}