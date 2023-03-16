pipeline {

  agent any
  environment {
        DOCKER_REGISTRY = credentials('dockerhub')
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
    
      stage("Push Docker Image") {
		    steps {
			    script {
				    echo "Push Docker Image"
				    withCredentials([usernamePassword(credentialsId: 'dockerhub', passwordVariable: 'DOCKER_REGISTRY_PWD', usernameVariable: 'DOCKER_REGISTRY_USER')]) {
            				sh "docker login -u ${DOCKER_REGISTRY_USER}  -p ${DOCKER_HUB_CRED_PSW}"
				    }
				        myapp.push("${env.BUILD_ID}")
				    
			    }
		    }
	    }

    
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