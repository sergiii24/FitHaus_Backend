pipeline {
 agent any
 stages {
     stage ('Build') {
          agent {
            docker {
              image 'python'
              reuseNode true
            }
          }
            steps{
                echo "Build environment"
                sh 'pip install -r requirements.txt'
            }
    }

    stage('Static code metrics') {
        agent {
            docker {
                image 'python'
                reuseNode true
            }
        }
        steps {
            echo "Style check"
            sh ''' pylint -d C0301 **/*.py '''
        }
        post{
            always{
                step([$class: 'CoberturaPublisher',
                        autoUpdateHealth: false,
                        autoUpdateStability: false,
                        coberturaReportFile: 'reports/coverage.xml',
                        failNoReports: false,
                        failUnhealthy: false,
                        failUnstable: false,
                        maxNumberOfBuilds: 10,
                        onlyStable: false,
                        sourceEncoding: 'ASCII',
                        zoomCoverageChart: false])
            }
        }

    }

    stage('Sonarqube') {
        environment {
            scannerHome = tool 'SonarQubeScanner'
        }
        steps {
            withSonarQubeEnv('SonarQube') {
                sh "${scannerHome}/bin/sonar-scanner"
            }
        }
    }
    stage('SSH transfer') {
        steps([$class: 'BapSshPromotionPublisherPlugin']) {
            sshPublisher(
                continueOnError: true, failOnError: false,
                publishers: [
                    sshPublisherDesc(
                        configName: "server",
                        verbose: true,
                        transfers: [
                            sshTransfer(execCommand: "cd FitHaus_Backend/; git checkout develop; git pull origin develop"),
                        ]
                    )
                ]
            )
        }
    }
    stage('Deploy FitHaus Backend'){
        steps([$class: 'BapSshPromotionPublisherPlugin']) {
            sshPublisher(
                continueOnError: true, failOnError: false,
                publishers: [
                    sshPublisherDesc(
                        configName: "server",
                        verbose: true,
                        transfers: [
                            sshTransfer(execCommand: "cd FitHaus_Backend/; docker-compose down -v; docker-compose up --build -d"),
                        ]
                    )
                ]
            )
        }
    }
  }
}
