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
    
      // stage("Push Docker Image") {
		  //   steps {
			//     script {
			// 	    echo "Push Docker Image"
			// 	    withCredentials([usernamePassword(credentialsId: 'dockerhub', passwordVariable: 'DOCKER_REGISTRY_PWD', usernameVariable: 'DOCKER_REGISTRY_USER')]) {
      //       				sh '''docker login -u $DOCKER_REGISTRY_USER  -p $DOCKER_REGISTRY_PSW'''
			// 	    }
			// 	        myapp.push("${env.BUILD_ID}")
				    
			//     }
		  //   }
	    // }
         
        stage('Login and Dcoker push') {
          steps {
				      script{
                  echo "Push Docker Image"
                  sh 'echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'
			            myapp.push("${env.BUILD_ID}")
                  echo "Push Docker Image Completed"
		          }
           }
        }

        // stage('Push') {
        //   steps {
				// sh 'docker push bharathirajatut/nodeapp:latest'}
		    // }    



    
    stage('Deploy App') {
      steps {
        echo "Deployment started ..."
        sh "sed -i 's/tagversion/${env.BUILD_ID}/g' deploy.yaml"
        echo "Start deployment of deploy.yaml"
        script {
          kubernetesDeploy(configs: "deploy.yml", kubeconfigId: "mykubeconfig")
        }
      }
    }

  }

}