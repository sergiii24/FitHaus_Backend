pipeline {
 agent { docker { image 'python'} }
 stages {

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
