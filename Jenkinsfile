pipeline {
  agent any
  options {
    buildDiscarder(logRotator(numToKeepStr: '5'))
  }
  environment {
    DOCKERHUB_CREDENTIALS = credentials('dockerhub')
  }

  stages {
    stage('Build') {
      steps {
        bat 'docker build -t malamcsc/kubernetes_project_test .'
      }
    }
    // stage('Login') {
    //   steps {
    //     bat 'echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'
    //   }
    // }

    stage('Push image') {
        withDockerRegistry([ credentialsId: "dockerhub", url: "" ]) {
        bat "docker push malamcsc/kubernetes_project_test"
        }
    }

    // stage('Push') {
    //   steps {
    //     bat 'docker push malamcsc/kubernetes_project_test'
    //   }
    // }
  
  post {
    always {
      bat 'docker logout'
    }
  }
}
}