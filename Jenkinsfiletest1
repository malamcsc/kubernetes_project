pipeline {

  agent any
  environment {
        DOCKERHUB_CREDENTIALS = credentials('dockerhub')
        BUILD_ID = 25
    }

  stages {

    stage('Checkout Source') {
      steps {
        git url:'https://github.com/malamcsc/kubernetes_project.git', branch:'master'
      }
    }
    
      

      
    stage('Deploy App') {
      steps {
        
        // bat "sed -i 's/tagversion/${env.BUILD_ID}/g' deploy.yaml"
        // bat "(Get-Content deploy.yaml) -replace 'tagversion', ${env.BUILD_ID} | Out-File -encoding ASCII deploy.yaml"
        script {
          kubernetesDeploy(configs: "deploy.yml", kubeconfigId: "mykubeconfig")
        }
        
      }
    }

  }

}