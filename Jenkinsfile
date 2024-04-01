pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/Dee68/jenkins-ci-cd.git']])
            }
        }
        stage('Setup Environment') {
            steps {
                echo 'Setup and Build ...'
                //get from repo
                //git branch: 'main', url: 'https://github.com/Dee68/jenkins-ci-cd.git'
                // Create and activate virtual environment
                sh 'python3 -m venv myenv'
                sh '. myenv/bin/activate'
               
            }
        }
        stage('Build') {
            steps {
                // Run any build steps here
                echo 'Testing...'
                // Example: Run tests
                sh 'pytest'
            }
        }
    }
}
