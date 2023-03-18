pipeline {

  agent any
  environment {
        DOCKERHUB_CREDENTIALS = credentials('dockerhub')
    }

  stages {

    stage('Checkout Source') {
      steps {
        git url:'https://github.com/malamcsc/kubernetes_project.git', branch:'master'
      }
    }
    
      stage("Build image") {
            steps {
                script {
                    myapp = docker.build("malamcsc/kubernetes_project:${env.BUILD_ID}")
                }
            }
        }
    
         
        stage('Login and Dcoker push') {
          steps {
                  
                  withDockerRegistry([ credentialsId: "dockerhub", url: "" ]){
			            myapp.push("${env.BUILD_ID}")
                  echo "Push Docker Image Completed"}
		          }
           }
        

      
    stage('Deploy App') {
      steps {
        echo "Deployment started ..."
        bat "sed -i 's/tagversion/${env.BUILD_ID}/g' deploy.yaml"
        echo "Start deployment of deploy.yaml"
        script {
          kubernetesDeploy(configs: "deploy.yml", kubeconfigId: "mykubeconfig")
        }
      }
    }

  }

}