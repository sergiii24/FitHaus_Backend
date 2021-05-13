pipeline {
 agent { docker { image 'python'} }
 stages {
    stage('SSH transfer') {
        steps([$class: 'BapSshPromotionPublisherPlugin']) {
            sshPublisher(
                continueOnError: false, failOnError: true,
                publishers: [
                    sshPublisherDesc(
                        configName: "server",
                        verbose: true,
                        transfers: [
                            sshTransfer(execCommand: "cd /FitHaus_Backend; git git checkout develop; git pull origin develop"),
                        ]
                    )
                ]
            )
        }
    }
    stage('Deploy Helm Scripts'){
        steps([$class: 'BapSshPromotionPublisherPlugin']) {
            sshPublisher(
                continueOnError: false, failOnError: true,
                publishers: [
                    sshPublisherDesc(
                        configName: "server",
                        verbose: true,
                        transfers: [
                            sshTransfer(execCommand: "cd /FitHaus_Backend; docker compose up"),
                        ]
                    )
                ]
            )
        }
    }
  }
}
