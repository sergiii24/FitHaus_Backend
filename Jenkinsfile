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
