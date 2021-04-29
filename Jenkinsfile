pipeline {
 agent { docker { image 'python'} }
 stages {
    stage('Build Environment') {
        steps{
            sh 'pip install -r requirements.txt'
        }
    }
 }
}