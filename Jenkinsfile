pipeline{
    agent{
        label: Dev
    }
    stages {
        stage ('DockerBuild'){
            sh(script: "docker build -t python:v1 .")
            sh(script: "docker images")
        }

    }
}