pipeline {
 agent { docker { image 'python'} }
 stages {
    stage('Build Environment') {
        steps{
            sh 'pip install -r requirements-dev.txt'
        }
    }
    stage('Static code metrics') {
        steps {
            echo "Style check"
            sh ''' pylint -d C0301 **/*.py '''
            echo "Code Coverage"
            sh ''' coverage run -m unittest discover '''
            sh ''' python -m coverage xml -o reports/coverage.xml '''
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
    stage('SSH transfer') {
        steps([$class: 'BapSshPromotionPublisherPlugin']) {
            sshPublisher(
                continueOnError: true, failOnError: false,
                publishers: [
                    sshPublisherDesc(
                        configName: "server",
                        verbose: true,
                        transfers: [
                            sshTransfer(execCommand: "cd FitHaus_Backend/; git checkout integration; git pull origin integration"),
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
                            sshTransfer(execCommand: "cd FitHaus_Backend/; docker-compose down -v; docker-compose up -d"),
                        ]
                    )
                ]
            )
        }
    }
  }
}
