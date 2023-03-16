pipeline {

  agent any

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
				    withCredentials([string(credentialsId: 'dockerhub', variable: 'dockerhub')]) {
            				sh "docker login -u malamcsc -p ${dockerhub}"
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