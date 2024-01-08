pipeline {
    parameters {
        booleanParam(name: 'BUILD_PYTHON_IMAGE', defaultValue: true, description: 'Build the Python image?')
    }

    agent {
        label 'Dev'
    }

    stages {
        stage('DockerBuild') {
            when {
                expression { params.BUILD_PYTHON_IMAGE == true }
            }
            steps {
                script {
                    sh(script: "docker build -t python:v1 .")
                    sh(script: "docker images")
                }
            }
        }

        stage('Docker_Run') {
            steps {
                script {
                    docker.image('postgres').pull()
                    sh(script: "docker network create pythonnetwork")
                    sh(script: "docker volume create pgvol")
                    sh(script: "docker run -itd --name dev-postgres -e POSTGRES_PASSWORD=postgres -e POSTGRES_DB=student --network pythonnetwork -v pgvol:/var/lib/postgresql/data postgres")
                    sh(script: "docker run -itd --name webapp -p 5000:500 --network pythonnetwork python:v1")
                }
            }
        }
    }
}
