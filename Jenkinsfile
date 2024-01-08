pipeline {
    parameters {
        booleanParam(name: 'BUILD_PYTHON_IMAGE', defaultValue: true, description: 'Build the Python image?')
        booleanParam(name: 'BUILD_DOCKER_NETWORK', defaultValue: true, description: 'Build the NETWORK')
        booleanParam(name: 'BUILD_DOCKER_VOLUME', defaultValue: true, description: 'Build the VOLUME?')
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
                    sh "docker build -t python:v1 ."
                    sh "docker images"
                }
            }
        }

        stage('DockerSetup') {
            when {
                expression { params.BUILD_DOCKER_NETWORK == true || params.BUILD_DOCKER_VOLUME == true }
            }
            steps {
                script {
                    if (params.BUILD_DOCKER_NETWORK == true) {
                        sh "docker network create pythonnetwork"
                    }

                    if (params.BUILD_DOCKER_VOLUME == true) {
                        sh "docker volume create pgvol"
                    }
                }
            }
        }

        stage('Docker_Run') {
            steps {
                script {
                    docker.image('postgres').pull()

                    sh "docker run -itd --name dev-postgres -e POSTGRES_PASSWORD=postgres -e POSTGRES_DB=student --network pythonnetwork -v pgvol:/var/lib/postgresql/data postgres"
                    
                    // Check if the Python image needs to be built before running
                    if (params.BUILD_PYTHON_IMAGE == true) {
                        sh "docker run -itd --name webapp -p 5000:500 --network pythonnetwork python:v1"
                    } else {
                        echo "Skipping Python image run since BUILD_PYTHON_IMAGE is set to false."
                    }
                }
            }
        }
    }
}
