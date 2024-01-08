pipeline{
    agent{
        label 'Dev'
    }
    stages {
        stage ('DockerBuild'){
            steps{
                sh(script: "docker build -t python:v1 .")
                sh(script: "docker images")
            }
            
        }

    }
}