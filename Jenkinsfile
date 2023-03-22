pipeline {

  agent any
  environment {
        DOCKERHUB_CREDENTIALS = credentials('dockerhub')
        BUILD_ID = 4
    }

  stages {

    stage('Checkout Source') {
      steps {
        git url:'https://github.com/malamcsc/kubernetes_project.git', branch:'master', credentialsId: 'github'
      }
    }

      // stage('Checkout') {
      //   steps { git branch: 'master', credentialsId: 'github', url: 'https://github.com/malamcsc/kubernetes_project.git'
      //   }
      // }
      // stage("Build image") {
      //       steps {
      //           script {
      //               myapp = docker.build("malamcsc/kubernetes_project:${env.BUILD_ID}")
      //           }
      //       }
      //   }
    
         
      //   stage('Login and Dcoker push') {
      //     steps {
      //       script{
      //             withDockerRegistry([ credentialsId: "dockerhub", url: "" ]){
      //             myapp.push("${env.BUILD_ID}")}
      //             }
		  //         }
      //      }
      
    // stage('Deploy App') {
    //   steps {
        
    //     sh "sed -i 's/tagversion/${env.BUILD_ID}/g' deploy.yaml"
    //     script {
    //       kubernetesDeploy(configs: "deploy.yml", kubeconfigId: "mykubeconfig")
    //     }
        
    //   }
    // }

    stage('Deploy App') {
      steps {
        
        sh "sed -i 's/tagversion/${env.BUILD_ID}/g' deploy.yaml"
        sh "kubectl apply -f deploy.yml"
        
      }
    }

  }

}